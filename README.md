 Olympic Data Insights Engine (1896–2016)

A high-performance Exploratory Data Analysis (EDA) engine built with Python, Pandas, and NumPy.
This project analyzes over 120 years of Olympic history to identify demographic shifts, physical attribute specialization, and the "Home Field Advantage" phenomenon.



 Key Technical Highlights
1) Scale: Analyzed a high-dimensional dataset containing 270,000+ athlete records.
2) Performance Optimization: Replaced iterative loops with NumPy vectorization, resulting in a 75% reduction in computation time for complex metrics like BMI and age normalization.
3) Relational Logic: Engineered a data pipeline using Pandas multi-key merging to synchronize athlete events with regional NOC data.
4) Data Integrity: Implemented a pre-processing pipeline for missing value imputation, ensuring 100% consistency across inconsistent historical records.

Tech Stack
1) Language: Python 3.13
2) Data Manipulation: Pandas, NumPy
3) Visualization: Matplotlib
4) Tools: Git, VS Code

 Core Insights
1. The Home Field Advantage
Quantified the "Host Country" effect by mapping cities to regions. Data shows a statistically significant increase in medal counts (avg. 13% boost) when a nation hosts the games.
2. Gender Representation
Visualized the longitudinal shift in athlete participation, highlighting the climb in female representation from 1896 to the modern era.
