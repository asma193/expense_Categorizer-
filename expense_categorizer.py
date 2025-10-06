import pandas as pd 

df = pd.read_csv("expense_data.csv")

# categorize expenses
categories = {
    "Food": ["mcdonald", "kfc", "restaurant", "grocery", "food"],
    "Travel": ["uber", "train", "flight", "bus", "taxi"],
    "Subscriptions": ["netflix", "youtube", "spotify", "amazon", "subscription"],
    "Shopping": ["mall", "store", "clothes", "shopping"],
    "Others": []
}

# Function to categorize expenses
def categorize(description):
    desc = description.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in desc:
                return category
    return "Others"

# categorization
df["Category"] = df["Description"].apply(categorize)

#  column
df["Month"] = pd.to_datetime(df["Date"]).dt.strftime("%B %Y")

# Generate summary
summary = df.groupby(["Month", "Category"])["Amount"].sum().reset_index()

# Save output
df.to_csv("categorized_report.csv", index=False)
summary.to_csv("monthly_summary.csv", index=False)

# Display output
print("✅ Expense categorization completed!")
print("\n📊 Monthly Summary:")
print(summary)
