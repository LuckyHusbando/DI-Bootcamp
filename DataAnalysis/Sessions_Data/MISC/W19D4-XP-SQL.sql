--------------------------------------------------------------
-- 🎬 Exercise 1: Movie Analysis with Window Functions
--------------------------------------------------------------

-- Task 1: Rank Movies by Popularity within Each Genre
-- Uses the RANK() function to rank movies by popularity within each genre.
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.popularity,
    RANK() OVER (
        PARTITION BY g.genre_name
        ORDER BY m.popularity DESC
    ) AS popularity_rank_in_genre
FROM
    movies.movie m
JOIN
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
ORDER BY
    g.genre_name, popularity_rank_in_genre;

--------------------------------------------------------------

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Uses the NTILE(4) function to divide movies by revenue into quartiles (1st quartile is the top 25%).
-- Note: NTILE is used for distribution, not for selecting a specific Top N (like Top 3).
-- The result will show which quartile each movie falls into.
SELECT
    pc.company_name,
    m.title AS movie_title,
    m.revenue,
    NTILE(4) OVER (
        PARTITION BY pc.company_name
        ORDER BY m.revenue DESC
    ) AS revenue_quartile
FROM
    movies.movie m
JOIN
    movies.movie_company mc ON m.movie_id = mc.movie_id -- Assumes movie_company join table
JOIN
    movies.production_company pc ON mc.company_id = pc.company_id
WHERE
    m.revenue IS NOT NULL AND m.revenue > 0 -- Filter out movies with no or zero revenue
ORDER BY
    pc.company_name, revenue_quartile, m.revenue DESC;

--------------------------------------------------------------

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Uses SUM() with the ROWS frame specification (UNBOUNDED PRECEDING) to calculate the running total budget.
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.release_date, -- Included for ORDER BY context
    m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date, m.movie_id -- Order by date and then ID for stable ordering
        ROWS UNBOUNDED PRECEDING
    ) AS running_total_budget
FROM
    movies.movie m
JOIN
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
WHERE
    m.budget IS NOT NULL AND m.budget > 0
ORDER BY
    g.genre_name, m.release_date, m.movie_id;

--------------------------------------------------------------

-- Task 4: Identify the Most Recent Movie for Each Genre
-- Uses the FIRST_VALUE() function to find the movie with the latest release date within each genre.
SELECT DISTINCT
    g.genre_name,
    FIRST_VALUE(m.title) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC, m.movie_id
    ) AS most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC, m.movie_id
    ) AS release_date_of_most_recent
FROM
    movies.movie m
JOIN
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
WHERE
    m.release_date IS NOT NULL
ORDER BY
    g.genre_name;

--------------------------------------------------------------
--------------------------------------------------------------
-- 🌟 Exercise 2: Cast and Crew Performance Analysis
--------------------------------------------------------------

-- Task 1: Rank Actors by Their Appearance in Movies
-- Uses DENSE_RANK() to rank actors based on the number of movies they appeared in.
WITH ActorMovieCount AS (
    SELECT
        p.person_id,
        p.person_name AS actor_name,
        COUNT(mc.movie_id) AS movie_count
    FROM
        movies.person p
    JOIN
        movies.movie_crew mc ON p.person_id = mc.person_id
    WHERE
        mc.job = 'Actor' -- Assumes Actors are identified by job 'Actor' in movie_crew
    GROUP BY
        p.person_id, p.person_name
)
SELECT
    actor_name,
    movie_count,
    DENSE_RANK() OVER (
        ORDER BY movie_count DESC
    ) AS actor_rank
FROM
    ActorMovieCount
ORDER BY
    actor_rank, actor_name;

--------------------------------------------------------------

-- Task 2: Identify the Top Director by Average Movie Rating
-- Uses a CTE to calculate the average rating and then RANK() to find the top director.
WITH DirectorAvgRating AS (
    SELECT
        p.person_name AS director_name,
        AVG(m.vote_average) AS average_rating
    FROM
        movies.person p
    JOIN
        movies.movie_crew mc ON p.person_id = mc.person_id
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE
        mc.job = 'Director' -- Assumes Directors are identified by job 'Director' in movie_crew
        AND m.vote_average IS NOT NULL
        AND m.vote_count > 0
    GROUP BY
        p.person_name
)
SELECT
    director_name,
    average_rating,
    RANK() OVER (
        ORDER BY average_rating DESC
    ) AS director_rating_rank
FROM
    DirectorAvgRating
ORDER BY
    director_rating_rank, director_name
LIMIT 1; -- Limit to the top director(s)

--------------------------------------------------------------

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Uses SUM() to calculate the running total revenue of movies for each actor, ordered by release date.
SELECT
    p.person_name AS actor_name,
    m.title AS movie_title,
    m.release_date, -- Included for ORDER BY context
    m.revenue,
    SUM(m.revenue) OVER (
        PARTITION BY p.person_name
        ORDER BY m.release_date, m.movie_id -- Order by date and then ID for stable ordering
        ROWS UNBOUNDED PRECEDING
    ) AS cumulative_revenue
FROM
    movies.person p
JOIN
    movies.movie_crew mc ON p.person_id = mc.person_id
JOIN
    movies.movie m ON mc.movie_id = m.movie_id
WHERE
    mc.job = 'Actor' -- Assumes Actors are identified by job 'Actor' in movie_crew
    AND m.revenue IS NOT NULL
    AND m.revenue > 0
ORDER BY
    actor_name, m.release_date, m.movie_id;

--------------------------------------------------------------

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Uses a CTE to calculate the total budget and then a window function (RANK) to find the top director.
WITH DirectorTotalBudget AS (
    SELECT
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM
        movies.person p
    JOIN
        movies.movie_crew mc ON p.person_id = mc.person_id
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE
        mc.job = 'Director' -- Assumes Directors are identified by job 'Director' in movie_crew
        AND m.budget IS NOT NULL
        AND m.budget > 0
    GROUP BY
        p.person_name
)
SELECT
    director_name,
    total_budget,
    RANK() OVER (
        ORDER BY total_budget DESC
    ) AS budget_rank
FROM
    DirectorTotalBudget
ORDER BY
    budget_rank, director_name
LIMIT 1; -- Limit to the top director(s)