import matplotlib.pyplot as plt
import seaborn as sns

def setup_theme():
    """Sets the default seaborn theme for uniform plotting."""
    sns.set_theme(style="whitegrid")

def plot_age_distribution(df):
    """Plots a histogram of patient ages."""
    setup_theme()
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
    plt.title('Patient Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

def plot_condition_prevalence(df):
    """Plots a horizontal bar chart of medical conditions by frequency."""
    setup_theme()
    plt.figure(figsize=(10, 5))
    sns.countplot(
        y='Medical Condition', 
        data=df, 
        order=df['Medical Condition'].value_counts().index, 
        palette='pastel'
    )
    plt.title('Prevalence of Medical Conditions')
    plt.xlabel('Number of Patients')
    plt.ylabel('Medical Condition')
    plt.show()

def plot_billing_by_condition(df):
    """Plots a boxplot to show the distribution of billing amounts per medical condition."""
    setup_theme()
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Medical Condition', y='Billing Amount', data=df, palette='Set2')
    plt.title('Billing Amount Distribution by Medical Condition')
    plt.xlabel('Medical Condition')
    plt.ylabel('Billing Amount ($)')
    plt.show()

def plot_los_by_admission(df):
    """Plots the average length of stay categorized by admission type."""
    setup_theme()
    plt.figure(figsize=(10, 5))
    sns.barplot(
        x='Admission Type', 
        y='Length of Stay', 
        data=df, 
        palette='muted', 
        errorbar=None
    )
    plt.title('Average Length of Stay by Admission Type')
    plt.xlabel('Admission Type')
    plt.ylabel('Average Length of Stay (Days)')
    plt.show()

if __name__ == "__main__":
    # Visualizations can be called directly by passing the DataFrame
    # plot_age_distribution(df)
    pass