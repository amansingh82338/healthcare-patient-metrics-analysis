import pandas as pd

def load_data(filepath):
    """Loads the dataset from a given filepath."""
    return pd.read_csv(filepath)

def standardize_text(df, columns):
    """Converts specified string columns to title case."""
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.title()
    return df

def convert_to_datetime(df, columns):
    """Converts specified columns to datetime objects."""
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df

def calculate_length_of_stay(df, start_col='Date of Admission', end_col='Discharge Date'):
    """Calculates the length of stay in days and adds it as a new column."""
    if start_col in df.columns and end_col in df.columns:
        df['Length of Stay'] = (df[end_col] - df[start_col]).dt.days
    return df

def process_healthcare_data(filepath):
    """
    Executes the full preprocessing pipeline on the raw data.
    Returns the cleaned pandas DataFrame.
    """
    df = load_data(filepath)
    df = standardize_text(df, ['Name'])
    df = convert_to_datetime(df, ['Date of Admission', 'Discharge Date'])
    df = calculate_length_of_stay(df)
    print("Data processing pipeline executed successfully.")
    return df

if __name__ == "__main__":
    # Load directly using the file path in quotes
    # df = process_healthcare_data('../data/raw/healthcare_dataset.csv')
    pass