--Final Project README--

Hi, I'm Derek. This is my final project for Developers Institute Class, Data_168_PT. For any questions regarding this project, please contact me at:
Email: DEP1919@gmail.com.
GitHub: https://github.com/LuckyHusbando/DI-Bootcamp/tree/main/Final_Project

--Final Project Description--

Project Roadmap: Decadal Video Game Market Analysis (2008–2018)
Objective: To build a data architecture and visualization suite that identifies which genres dominated specific hardware platforms during the industry's transition from the 7th to the 8th generation of consoles both globally and by region.

Phase 1: Data Architecture & SQL Foundation

The objective is to structure a decade's worth of global and regional sales and release metadata into a high-performance relational database.

Database Schema Design: Configure a PostgreSQL database with a star schema, centralizing a "Sales" fact table supported by "Platform," "Genre," and "Publisher" dimensions.

SQL Query Development: Write optimized views to aggregate global sales (NA, EU, JP, Other) specifically filtered for the 2008–2018 timeframe, accounting for the peak of the Wii/PS3/Xbox 360 era and the rise of the PS4/Xbox One.

Data Validation: Implement constraints to handle null values in legacy metadata and ensure consistent naming conventions for cross-platform titles (e.g., ensuring "Call of Duty" records match across different consoles).

Phase 2: Python Processing & Market Modeling

This phase focuses on the "Analytical" layer, using Python to calculate growth metrics and market share shifts.

Pandas Pipeline Construction: Develop a script to ingest SQL data and calculate Year-over-Year (YoY) Growth and Genre Concentration Ratios for each year in the decade.

Trend Identification: Design a logic-based categorization engine to group platforms by "Generation" (e.g., Seventh Gen vs. Eighth Gen).

Apply statistical normalization to compare the longevity of "Evergreen" genres (like Sports) versus "Trend" genres (like the mid-2010s Battle Royale/Shooter surge).

Exploratory Data Analysis (EDA): Use Python libraries (Matplotlib/Seaborn) to perform correlation tests between release volume and total revenue per genre.

Phase 3: Tableau Visualization & Strategic Reporting

The final goal is to translate 10 years of data into an interactive narrative for industry stakeholders.

Data Source Connection: Map the processed Python outputs to Tableau, ensuring that revenue metrics are correctly tiered by region and platform lifecycle.

Dashboard Development: * The Platform Heatmap: A visual matrix showing Genre vs. Platform success to identify "Niche" vs. "Mass Market" pairings.

Market Share Race Chart: An animated or multi-period view of how genre dominance shifted between 2008 and 2018.

Success Metrics & Deliverables

Deliverable 1: A SQL-backed Data Warehouse containing 10 years of validated gaming market records.
Deliverable 2: A Python Analysis Suite that automates the calculation of market share and CAGR (Compound Annual Growth Rate).
Deliverable 3: An Interactive Tableau Dashboard providing a 360-degree view of the 2008–2018 market landscape both globally and by region.
Goal: Identify the top 3 high-growth genres for each major platform and provide a data-backed explanation for how the video game market changed in this era of gaming history.

