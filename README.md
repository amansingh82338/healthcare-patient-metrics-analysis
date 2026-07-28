# Healthcare Analytics Project

## Project Description
This project analyzes a healthcare dataset to uncover operational, financial, and clinical insights — including patient length of stay, billing distributions, demographic patterns, and prevalence of medical conditions. The workflow covers data cleaning, feature engineering, and exploratory data analysis (EDA).

## Project Structure
```
.
├── data/
│   ├── processed/
│   │   └── cleaned_healthcare_dataset.csv
│   └── raw/
│       └── healthcare_dataset.csv
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_exploratory_analysis.ipynb
├── plots/
│   ├── Age distribution.png
│   ├── Average Length of Stay by Admission Type.png
│   ├── Billing amount distribution by medical condition.png
│   └── Prevalence of medical conditions.png
├── src/
│   ├── data_processing.py
│   └── visualizations.py
├── .gitignore
├── LICENSE
└── README.md
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


## Author
*AMAN SINGH CHAUHAN*
