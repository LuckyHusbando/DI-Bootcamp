import sqlite3
import pandas as pd

# Connect to the IPL database
conn = sqlite3.connect('database.sqlite')

# --- 1. Load and Explore the Data ---
print("--- Table Structures ---")
# Get all table names
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
table_names = [table[0] for table in tables]

# Load tables and print column names
for table in table_names:
    # Read just the header to get column names efficiently
    df_temp = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 0", conn)
    print(f"Table '{table}': {list(df_temp.columns)}")


# --- 2. Query 1: Select All Columns from Player's Table (Player_Match) ---
print("\n--- Query 1: Player_Match (Head) ---")
query_1 = "SELECT * FROM Player_Match"
df_player_match = pd.read_sql_query(query_1, conn)
print(df_player_match.head())


# --- 3. Query 2: Batsman vs Runs ---
print("\n--- Query 2: Top Batsmen by Runs ---")
query_2 = """
SELECT 
    p.Player_Name, 
    SUM(bs.Runs_Scored) as Total_Runs
FROM Batsman_Scored bs
JOIN Ball_by_Ball b ON bs.Match_Id = b.Match_Id AND bs.Over_Id = b.Over_Id AND bs.Ball_Id = b.Ball_Id AND bs.Innings_No = b.Innings_No
JOIN Player p ON b.Striker = p.Player_Id
GROUP BY p.Player_Name
ORDER BY Total_Runs DESC
"""
df_runs = pd.read_sql_query(query_2, conn)
print(df_runs.head())


# --- 4. Query 3: Fifties and Hundreds ---
print("\n--- Query 3: Fifties and Hundreds ---")
query_3 = """
WITH Match_Runs AS (
    SELECT 
        p.Player_Name, 
        b.Match_Id, 
        SUM(bs.Runs_Scored) as Runs
    FROM Batsman_Scored bs
    JOIN Ball_by_Ball b ON bs.Match_Id = b.Match_Id AND bs.Over_Id = b.Over_Id AND bs.Ball_Id = b.Ball_Id AND bs.Innings_No = b.Innings_No
    JOIN Player p ON b.Striker = p.Player_Id
    GROUP BY p.Player_Name, b.Match_Id
)
SELECT 
    Player_Name,
    SUM(CASE WHEN Runs >= 50 AND Runs < 100 THEN 1 ELSE 0 END) as Fifties,
    SUM(CASE WHEN Runs >= 100 THEN 1 ELSE 0 END) as Hundreds
FROM Match_Runs
GROUP BY Player_Name
ORDER BY Hundreds DESC, Fifties DESC
"""
df_milestones = pd.read_sql_query(query_3, conn)
print(df_milestones.head())


# --- 5. Query 4: Best Bowling Figures ---
print("\n--- Query 4: Best Bowling Figures ---")
query_4 = """
WITH Match_Bowling_Stats AS (
    SELECT 
        b.Match_Id, 
        b.Bowler, 
        -- Calculate Runs Conceded (Runs off bat + Wides + No Balls)
        SUM(bs.Runs_Scored) + IFNULL(SUM(CASE WHEN er.Extra_Type_Id IN (2, 4) THEN er.Extra_Runs ELSE 0 END), 0) as Runs_Conceded,
        -- Calculate Wickets (Excluding run outs etc)
        COUNT(CASE WHEN wt.Kind_Out IN (1, 2, 4, 6, 7, 8) THEN wt.Player_Out END) as Wickets
    FROM Ball_by_Ball b
    JOIN Batsman_Scored bs ON b.Match_Id = bs.Match_Id AND b.Over_Id = bs.Over_Id AND b.Ball_Id = bs.Ball_Id AND b.Innings_No = bs.Innings_No
    LEFT JOIN Extra_Runs er ON b.Match_Id = er.Match_Id AND b.Over_Id = er.Over_Id AND b.Ball_Id = er.Ball_Id AND b.Innings_No = er.Innings_No
    LEFT JOIN Wicket_Taken wt ON b.Match_Id = wt.Match_Id AND b.Over_Id = wt.Over_Id AND b.Ball_Id = wt.Ball_Id AND b.Innings_No = wt.Innings_No
    GROUP BY b.Match_Id, b.Bowler
),
Ranked_Bowling AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY Bowler ORDER BY Wickets DESC, Runs_Conceded ASC) as Rank
    FROM Match_Bowling_Stats
)
SELECT 
    p.Player_Name, 
    r.Wickets as Best_Wickets, 
    r.Runs_Conceded
FROM Ranked_Bowling r
JOIN Player p ON r.Bowler = p.Player_Id
WHERE r.Rank = 1
ORDER BY Best_Wickets DESC
"""
df_bowling = pd.read_sql_query(query_4, conn)
print(df_bowling.head())


# --- 6. Query 5: Comprehensive Career Metrics ---
print("\n--- Query 5: Comprehensive Career Metrics ---")
# Combining logic using CTEs for a single query result
query_5 = """
WITH Total_Runs_CTE AS (
    SELECT b.Striker as Player_Id, SUM(bs.Runs_Scored) as Total_Runs
    FROM Batsman_Scored bs
    JOIN Ball_by_Ball b ON bs.Match_Id = b.Match_Id AND bs.Over_Id = b.Over_Id AND bs.Ball_Id = b.Ball_Id AND bs.Innings_No = b.Innings_No
    GROUP BY b.Striker
),
Match_Runs AS (
    SELECT b.Striker as Player_Id, b.Match_Id, SUM(bs.Runs_Scored) as Runs
    FROM Batsman_Scored bs
    JOIN Ball_by_Ball b ON bs.Match_Id = b.Match_Id AND bs.Over_Id = b.Over_Id AND bs.Ball_Id = b.Ball_Id AND bs.Innings_No = b.Innings_No
    GROUP BY b.Striker, b.Match_Id
),
Milestones_CTE AS (
    SELECT Player_Id,
           SUM(CASE WHEN Runs >= 50 AND Runs < 100 THEN 1 ELSE 0 END) as Fifties,
           SUM(CASE WHEN Runs >= 100 THEN 1 ELSE 0 END) as Hundreds
    FROM Match_Runs
    GROUP BY Player_Id
),
Bowling_Stats AS (
    SELECT 
        b.Match_Id, 
        b.Bowler, 
        SUM(bs.Runs_Scored) + IFNULL(SUM(CASE WHEN er.Extra_Type_Id IN (2, 4) THEN er.Extra_Runs ELSE 0 END), 0) as Runs_Conceded,
        COUNT(CASE WHEN wt.Kind_Out IN (1, 2, 4, 6, 7, 8) THEN wt.Player_Out END) as Wickets
    FROM Ball_by_Ball b
    JOIN Batsman_Scored bs ON b.Match_Id = bs.Match_Id AND b.Over_Id = bs.Over_Id AND b.Ball_Id = bs.Ball_Id AND b.Innings_No = bs.Innings_No
    LEFT JOIN Extra_Runs er ON b.Match_Id = er.Match_Id AND b.Over_Id = er.Over_Id AND b.Ball_Id = er.Ball_Id AND b.Innings_No = er.Innings_No
    LEFT JOIN Wicket_Taken wt ON b.Match_Id = wt.Match_Id AND b.Over_Id = wt.Over_Id AND b.Ball_Id = wt.Ball_Id AND b.Innings_No = wt.Innings_No
    GROUP BY b.Match_Id, b.Bowler
),
Best_Bowling_CTE AS (
    SELECT 
        Bowler as Player_Id, Wickets as Best_Wickets, Runs_Conceded as Best_Bowling_Runs
    FROM (
        SELECT *, ROW_NUMBER() OVER(PARTITION BY Bowler ORDER BY Wickets DESC, Runs_Conceded ASC) as Rank
        FROM Bowling_Stats
    ) 
    WHERE Rank = 1
)
SELECT 
    p.Player_Name,
    tr.Total_Runs,
    m.Fifties,
    m.Hundreds,
    bb.Best_Wickets,
    bb.Best_Bowling_Runs
FROM Player p
LEFT JOIN Total_Runs_CTE tr ON p.Player_Id = tr.Player_Id
LEFT JOIN Milestones_CTE m ON p.Player_Id = m.Player_Id
LEFT JOIN Best_Bowling_CTE bb ON p.Player_Id = bb.Player_Id
WHERE tr.Total_Runs IS NOT NULL OR bb.Best_Wickets IS NOT NULL
ORDER BY tr.Total_Runs DESC
"""
df_comprehensive = pd.read_sql_query(query_5, conn)
print(df_comprehensive.head())

conn.close()