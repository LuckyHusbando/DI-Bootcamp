### 🎮 Video Game Genre Success By Platform: An Analysis of Market Dynamics from 2008-2018

Created by: Derek Pursell -- Email: DEP1919@gmail.com

---

> **A Comprehensive Data Engineering & Analytics Project**

![Project Status: Active](https://img.shields.io/badge/Project_Status-Active-brightgreen)
![Data Stack: SQL | Python | Tableau](https://img.shields.io/badge/Stack-SQL_%7C_Python_%7C_Tableau-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Objective
To build a robust data architecture and visualization suite that identifies which genres dominated specific hardware platforms during the industry's critical transition from the **7th generation** (PS3, Xbox 360, Wii) to the **8th generation** (PS4, Xbox One, Switch).

---

## 🏗 Phase 1: Data Architecture & SQL Foundation
*Transforming raw metadata into a high-performance analytical engine.*

### Database Schema Design
We implement a **Star Schema** to optimize for complex analytical queries across 10+ years of sales records.

* **Fact Table:** `Sales` (Global, NA, EU, JP, Other)
* **Dimensions:** `Platform`, `Genre`, `Publisher`, `Release_Date`

### SQL Query Development & Validation
* **Performance:** Optimized views aggregate sales data for the 2008–2018 window.
* **Data Integrity:** Implemented `COALESCE` and strict `FOREIGN KEY` constraints to handle legacy null values and ensure cross-platform title consistency.

---

## 🐍 Phase 2: Python Processing & Market Modeling
*The "Analytical Layer" utilizing statistical normalization and trend detection.*

### Trend Identification Logic
* **Generation Clustering:** Automating the grouping of platforms into generational cohorts.
* **Normalization:** Comparing "Evergreen" genres (e.g., Sports, which maintained a consistent ~27% market share) against "Trend" surges (e.g., Shooters peaking in 2015-2018).

---

## 🎨 Phase 3: Tableau Visualization & Strategic Reporting
*Translating 10 years of data into interactive narratives for stakeholders.*

### Dashboard Deliverables
**The Platform Heatmap:** A visual matrix identifying "Niche" vs. "Mass Market" pairings (e.g., the dominance of RPGs on Nintendo handhelds vs. Shooters on Xbox).

---

## 📦 Success Metrics & Deliverables

| Deliverable | Description | Key Tech |
| :--- | :--- | :--- |
| **Data Warehouse** | 10 years of validated, structured market records. | PostgreSQL |
| **Analysis Suite** | Automated pipeline for YoY Growth & CAGR. | Pandas / NumPy |
| **360° Dashboard** | Interactive global/regional market landscape. | Tableau |

### Final Goal
Identify major market trends over the period and provide a data-backed explanation for how the global market shifted over the period 2008-2018.

---

## 🚀 About Me

- 📊 I have a deep interest in **Game Economics and Reward Systems**
- 💬 Ask me about **Game Mechanics, Dungeons & Dragons, & Data Science**
- ⚡ Fun fact: **I love animals and our family has been working with animal rescue organizations for years.**

---

## 🛠 Tech, Tools, & Data
### 💻 Languages & Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/sql-%2307405e.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

---

## 📫 Let's Connect!
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/derek-pursell/)
[![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=white)](https://public.tableau.com/app/profile/derek.pursell/viz/TheVideoGameIndustry-2008-2018-KeyInsights/Dashboard?publish=yes)

---
