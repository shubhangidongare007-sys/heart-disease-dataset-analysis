import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================
# sep=None automatically detects if the file uses commas or semicolons
df = pd.read_csv('heart.csv', sep=None, engine='python')

# Clean up column names by removing spaces and making them lowercase
df.columns = df.columns.str.strip().str.lower()

# This line prints your available columns in the terminal so we can audit them
print("--- YOUR DATASET COLUMNS ARE: ---")
print(df.columns.tolist())
print("---------------------------------")

# Map 'sex' to numbers (M=1, F=0) if 'sex' exists
if 'sex' in df.columns and df['sex'].dtype == 'object':
    df['sex_encoded'] = df['sex'].map({'M': 1, 'F': 0})

print("Generating high-resolution graphs...")
sns.set_theme(style="whitegrid")

# ==========================================
# STEP 2: GENERATE AND AUTO-SAVE PLOTS
# ==========================================
# Plot 1: Histogram (Age Distribution)
plt.figure(figsize=(8, 4))

# Safely check if 'age' column exists before trying to plot
if 'age' in df.columns:
    sns.histplot(data=df, x='age', kde=True, color='crimson', bins=20)
    plt.title('Distribution of Patients Age', fontsize=12)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('plot1_age_distribution.png', dpi=300)
    print("Success! 'plot1_age_distribution.png' has been saved successfully.")
else:
    print("ERROR: Could not find the 'age' column in your heart.csv file.")
    print("Please double check your dataset file format.")

plt.close()
# ==========================================
# STEP 3: PRINT INSTRUCTOR COMPLIANCE REPORT
# ==========================================
print("\n" + "="*50)
print("         OFFICIAL DATASET SUMMARY REPORT         ")
print("="*50)
print(f"Total Patient Records Analysed: {len(df)}")
print(f"Total Health Features Extracted: {len(df.columns)}")
print("\n--- Statistical Overview of Key Features ---")
print(df.describe().round(2)) # This prints the summary table in English
print("="*50)















