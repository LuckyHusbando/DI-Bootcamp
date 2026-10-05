--------------------------------------------------------------
-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Uses LAG() to find the previous movie's budget and calculates the growth rate.
--------------------------------------------------------------
WITH RankedMovies AS (
    -- 1. Rank movies for each company by release date and retrieve the previous budget
    SELECT
        pc.company_name,
        m.budget,
        m.release_date,
        -- Get the budget of the immediately preceding movie (within the same company)
        LAG(m.budget, 1, 0) OVER (
            PARTITION BY pc.company_id
            ORDER BY m.release_date, m.movie_id -- Order by date, then ID for tie-breaking
        ) AS previous_budget
    FROM
        movies.movie m
    JOIN
        movies.movie_company mc ON m.movie_id = mc.movie_id -- ASSUMPTION: movie_company join table
    JOIN
        movies.production_company pc ON mc.company_id = pc.company_id
    WHERE
        m.budget IS NOT NULL AND m.budget > 0 AND m.release_date IS NOT NULL
),
BudgetGrowthRates AS (
    -- 2. Calculate the budget growth rate (current_budget - previous_budget) / previous_budget
    SELECT
        company_name,
        (CAST(budget AS DECIMAL) - previous_budget) / NULLIF(previous_budget, 0) AS budget_growth_rate
    FROM
        RankedMovies
    WHERE
        previous_budget > 0 -- Exclude the first movie in the series (where previous_budget is 0)
)
SELECT
    company_name,
    AVG(budget_growth_rate) AS average_budget_growth_rate
FROM
    BudgetGrowthRates
GROUP BY
    company_name
ORDER BY
    average_budget_growth_rate DESC;


--------------------------------------------------------------
-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Uses a CTE to find the global average rating, then filters actors based on movies rated above that average.
--------------------------------------------------------------
WITH OverallAvgRating AS (
    -- 1. Calculate the overall average rating of all movies
    SELECT
        AVG(vote_average) AS global_avg_rating
    FROM
        movies.movie
    WHERE
        vote_average IS NOT NULL AND vote_count >= 10 -- Filter for relevant movies
),
ActorHighRatedMovieCount AS (
    -- 2. Count the number of high-rated movies for each actor
    SELECT
        p.person_name AS actor_name,
        COUNT(m.movie_id) AS high_rated_movie_count
    FROM
        movies.movie m
    JOIN
        movies.movie_crew mc ON m.movie_id = mc.movie_id
    JOIN
        movies.person p ON mc.person_id = p.person_id
    CROSS JOIN -- Use CROSS JOIN to access the single global average value
        OverallAvgRating oar
    WHERE
        mc.job = 'Actor' -- Assumes Actors are identified by job 'Actor'
        AND m.vote_average > oar.global_avg_rating
        AND m.vote_count >= 10
    GROUP BY
        p.person_name
)
SELECT
    actor_name,
    high_rated_movie_count,
    RANK() OVER (ORDER BY high_rated_movie_count DESC) as rating_consistency_rank
FROM
    ActorHighRatedMovieCount
ORDER BY
    rating_consistency_rank, actor_name;


--------------------------------------------------------------
-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Uses AVG() with ROWS frame specification to calculate the average over the current and the two preceding rows.
--------------------------------------------------------------
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.release_date,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_id
        ORDER BY m.release_date, m.movie_id
        -- Calculate average over the current row and the 2 preceding rows (last 3 movies)
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue_last_3
FROM
    movies.movie m
JOIN
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
WHERE
    m.revenue IS NOT NULL AND m.revenue > 0
    AND m.release_date IS NOT NULL
ORDER BY
    g.genre_name, m.release_date DESC;


--------------------------------------------------------------
-- 🌟 Task 4: Identify the Highest-Grossing Movie Series (based on shared keywords)
-- Defines a "series" as a keyword shared by more than one movie.
--------------------------------------------------------------
WITH KeywordSeriesRevenue AS (
    -- 1. Aggregate revenue by keyword, but only for keywords used in multiple movies
    SELECT
        k.keyword_name AS movie_series_keyword,
        SUM(m.revenue) AS total_series_revenue,
        COUNT(DISTINCT m.movie_id) AS movie_count
    FROM
        movies.movie m
    JOIN
        movies.movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN
        movies.keyword k ON mk.keyword_id = k.keyword_id
    WHERE
        m.revenue IS NOT NULL AND m.revenue > 0
    GROUP BY
        k.keyword_name
    HAVING
        COUNT(DISTINCT m.movie_id) > 1 -- Filter to include only keywords that define a "series" (more than one movie)
)
SELECT
    movie_series_keyword,
    total_series_revenue,
    movie_count,
    RANK() OVER (ORDER BY total_series_revenue DESC) AS revenue_rank
FROM
    KeywordSeriesRevenue
ORDER BY
    revenue_rank, total_series_revenue DESC
LIMIT 10;