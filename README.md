# Healthcare Analytics Project

## Project Description
This project analyzes a healthcare dataset to uncover operational, financial, and clinical insights — including patient length of stay, billing distributions, demographic patterns, and prevalence of medical conditions. The workflow covers data cleaning, feature engineering, and exploratory data analysis (EDA).

## Project Structure
```
healthcare_analytics_project/
├── data/
│   ├── raw/                       # Original, immutable healthcare_dataset.csv
│   └── processed/                 # Cleaned data after preprocessing steps
├── notebooks/
│   ├── 01_data_cleaning.ipynb     # Data exploration and cleaning
│   └── 02_exploratory_analysis.ipynb  # Visual EDA
├── src/
│   ├── data_processing.py         # Functions to clean names and parse dates
│   └── visualizations.py          # Functions to generate standard charts
├── requirements.txt               # Python dependencies
└── README.md                      # Project description, instructions, and summary of findings
```

## Data
- **Source file:** `data/raw/healthcare_dataset.csv` (kept immutable — never edited directly)
- **Processed output:** `data/processed/` — cleaned dataset generated after running the cleaning notebook/script

## Data Cleaning Steps
1. **Text standardization** — `Name` column converted to title case to fix inconsistent capitalization
2. **Date parsing** — `Date of Admission` and `Discharge Date` converted from text strings to datetime objects
3. **Feature engineering** — new `Length of Stay` column calculated as the difference between admission and discharge dates

## Exploratory Analysis
Key metrics explored:
- Average length of stay
- Billing amount distributions
- Patient demographics
- Prevalence of medical conditions

## Source Code
- **`src/data_processing.py`** — Reusable pipeline to load the raw dataset, clean names, parse dates, and calculate length of stay. Import these functions into notebooks to avoid duplicating cleaning logic.
- **`src/visualizations.py`** — Modular plotting functions (histograms, bar charts, boxplots) for visualizing demographics, condition prevalence, and financial metrics.

## Setup & Installation
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## How to Run
1. Place the raw dataset in `data/raw/healthcare_dataset.csv`
2. Run `notebooks/01_data_cleaning.ipynb` to clean the data and generate the processed dataset
3. Run `notebooks/02_exploratory_analysis.ipynb` to generate visualizations and explore key metrics

## Key Findings
*(To be filled in after EDA is complete)*
- Average length of stay: TBD
- Billing distribution insights: TBD
- Most prevalent conditions: TBD

## Author
*AMAN SINGH CHAUHAN*
