--Task 1 - Average Age of Medal Winners (Correlated Subquery)

SELECT
    m.medal_name,
    (
        -- Correlated Subquery: Calculates the average age for the medal ID from the outer query (m.id)
        SELECT
            AVG(gc.age)
        FROM
            competitor_event AS ce
        JOIN
            games_competitor AS gc ON ce.competitor_id = gc.id
        WHERE
            ce.medal_id = m.id -- This is the correlation link
    ) AS average_age
FROM
    medal AS m
WHERE
    m.medal_name <> 'NA'
ORDER BY
    average_age DESC;

--Task 2 - Top 5 Regions (Nested Subqueries)

SELECT
    results.region_name,
    results.unique_competitors_count
FROM (
    -- Outer Subquery (S2): Groups by region and counts unique competitors who meet the event criteria
    SELECT
        nr.region_name,
        COUNT(DISTINCT gc.person_id) AS unique_competitors_count
    FROM
        noc_region AS nr
    JOIN
        person_region AS pr ON nr.id = pr.region_id
    JOIN
        games_competitor AS gc ON pr.person_id = gc.person_id
    WHERE
        gc.id IN (
            -- Innermost Subquery (S1): Finds competitor IDs who participated in > 3 distinct events
            SELECT
                competitor_id
            FROM
                competitor_event
            GROUP BY
                competitor_id
            HAVING
                COUNT(DISTINCT event_id) > 3
        )
    GROUP BY
        nr.region_name
) AS results
ORDER BY
    results.unique_competitors_count DESC
LIMIT 5;

--Task 3 - Temporary Table for Medal Counts

-- Step 1: Create a temporary table to store the total number of medals won by each competitor.
-- The schema prefix has been removed from the table name and the table creation statement.
CREATE TEMPORARY TABLE IF NOT EXISTS CompetitorMedalCounts AS
SELECT
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM
    competitor_event AS ce
WHERE
    ce.medal_id IN (1, 2, 3) -- Filter to include only Gold (1), Silver (2), and Bronze (3)
GROUP BY
    ce.competitor_id;

-- Step 2: Select from the temporary table, filtering for competitors with more than 2 medals.
SELECT
    p.full_name,
    t.total_medals
FROM
    CompetitorMedalCounts AS t
JOIN
    games_competitor AS gc ON t.competitor_id = gc.id
JOIN
    person AS p ON gc.person_id = p.id
WHERE
    t.total_medals > 2
ORDER BY
    t.total_medals DESC;

--Task 4 - DELETE Statement with Subquery

-- Prerequisite: Create a temporary table containing all competitors for analysis/deletion.
CREATE TEMPORARY TABLE IF NOT EXISTS CompetitorAnalysis AS
SELECT
    id AS competitor_id,
    person_id,
    age
FROM
    games_competitor;

-- DELETE Statement with Subquery:
-- Remove records from the temporary table where the competitor_id is NOT found
-- in the list of medal winners returned by the subquery.
DELETE FROM
    CompetitorAnalysis
WHERE
    competitor_id NOT IN (
        -- Subquery: Select all DISTINCT competitor_ids that have won at least one medal.
        SELECT DISTINCT
            competitor_id
        FROM
            competitor_event
        WHERE
            medal_id IN (1, 2, 3) -- Gold, Silver, or Bronze
    );

-- Optional: Verify the remaining records (only medal winners)
SELECT * FROM CompetitorAnalysis LIMIT 5;

--Exercise 2--

--Task 1: Update Heights using a Correlated Subquery

UPDATE Competitor AS C1
SET Height = (
    -- Correlated Subquery: Calculates the average height for the region of the outer query's competitor.
    SELECT AVG(C2.Height)
    FROM Competitor AS C2
    WHERE C2.Region = C1.Region -- Correlates the inner query (C2) to the outer query (C1) by Region.
)
WHERE C1.Height IS NULL;

--Task 2: Insert into a Temporary Table using Nested Subqueries

-- Create a temporary table to store the results
CREATE TEMPORARY TABLE MultiEventCompetitors (
    Competitor_ID INT,
    Games TEXT,
    Total_Events INT
);

-- Insert records using a nested subquery structure
INSERT INTO MultiEventCompetitors (Competitor_ID, Games, Total_Events)
SELECT
    P.Competitor_ID,
    P.Games,
    COUNT(P.Event_ID) AS Total_Events
FROM Participations AS P
WHERE P.Competitor_ID IN (
    -- Outer Subquery: Finds Competitor_IDs that appear more than once for the same Games.
    SELECT Competitor_ID
    FROM Participations
    GROUP BY Competitor_ID, Games
    HAVING COUNT(Event_ID) > 1
)
GROUP BY P.Competitor_ID, P.Games;

-- Display the results
SELECT * FROM MultiEventCompetitors;

--Task 3 - Compare Regional Average Medals to Overall Average

SELECT
    C.Region,
    AVG(M.Medal_Count) AS Avg_Medals_Per_Competitor
FROM Competitor AS C
JOIN Medal AS M
    ON C.Competitor_ID = M.Competitor_ID
GROUP BY
    C.Region
HAVING
    AVG(M.Medal_Count) > (
        -- Subquery 1 (Overall Average): Calculates the average medal count across ALL competitors.
        SELECT AVG(Medal_Count)
        FROM Medal
    )
ORDER BY
    Avg_Medals_Per_Competitor DESC;

--Task 4 - Identify Summer and Winter Participants

-- 1. Create a temporary table to store the distinct participation seasons for each competitor.
CREATE TEMPORARY TABLE CompetitorSeasons AS
SELECT
    Competitor_ID,
    Games,
    CASE
        WHEN Games LIKE '%Summer' THEN 'Summer'
        WHEN Games LIKE '%Winter' THEN 'Winter'
        ELSE 'Other' -- Catches non-specific game names if they exist
    END AS Season
FROM Participations
GROUP BY Competitor_ID, Season;

-- 2. Identify and list the Competitor_IDs that appear in both seasons.
SELECT
    C.Competitor_ID,
    GROUP_CONCAT(C.Season) AS Participated_Seasons
FROM CompetitorSeasons AS C
GROUP BY
    C.Competitor_ID
HAVING
    -- Check if the distinct seasons include both Summer AND Winter
    COUNT(DISTINCT C.Season) = 2
    AND Participated_Seasons LIKE '%Summer%'
    AND Participated_Seasons LIKE '%Winter%';