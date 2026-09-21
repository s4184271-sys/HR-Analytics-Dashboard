import pandas as pd

# HR Analytics EDA
# Keep HR_Analytics_Cleaned.csv in the same folder as this script.

df = pd.read_csv("HR_Analytics_Cleaned.csv")

print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal Employees:", len(df))

print("\nDepartment distribution:")
print(df["Department"].value_counts())

print("\nJob Role distribution:")
print(df["JobRole"].value_counts())

print("\nGender distribution:")
print(df["Gender"].value_counts())

print("\nAge statistics:")
print(df["Age"].describe())

print("\nMarital Status:")
print(df["MaritalStatus"].value_counts())

attrition_rate = (df["Attrition"] == "Yes").mean()
print(f"\nOverall Attrition Rate: {attrition_rate:.2%}")

print("\nAttrition Rate by Department:")
print(df.groupby("Department")["Attrition"].apply(lambda x: (x == "Yes").mean()).sort_values(ascending=False))

print("\nAttrition Rate by Job Role:")
print(df.groupby("JobRole")["Attrition"].apply(lambda x: (x == "Yes").mean()).sort_values(ascending=False))

print("\nAttrition Rate by OverTime:")
print(df.groupby("OverTime")["Attrition"].apply(lambda x: (x == "Yes").mean()))

print("\nAttrition Rate by Business Travel:")
print(df.groupby("BusinessTravel")["Attrition"].apply(lambda x: (x == "Yes").mean()).sort_values(ascending=False))

print("\nAverage Age by Attrition:")
print(df.groupby("Attrition")["Age"].mean())

print("\nAverage Distance From Home by Attrition:")
print(df.groupby("Attrition")["DistanceFromHome"].mean())

print("\nAverage Monthly Income by Attrition:")
print(df.groupby("Attrition")["MonthlyIncome"].mean())

print("\nAverage Monthly Income by Job Level:")
print(df.groupby("JobLevel")["MonthlyIncome"].mean())

print("\nAttrition Rate by Job Level:")
print(df.groupby("JobLevel")["Attrition"].apply(lambda x: (x == "Yes").mean()))

print("\nSalary Hike by Attrition:")
print(df.groupby("Attrition")["PercentSalaryHike"].mean())

print("\nAttrition Rate by Stock Option Level:")
print(df.groupby("StockOptionLevel")["Attrition"].apply(lambda x: (x == "Yes").mean()))

df["AttritionFlag"] = df["Attrition"].map({"Yes": 1, "No": 0})

print("\nNumeric correlations with AttritionFlag:")
print(df.select_dtypes(include="number").corr()["AttritionFlag"].sort_values(ascending=False))

for col in ["MonthlyIncome", "DistanceFromHome", "TotalWorkingYears"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"\n{col} outliers: {len(outliers)}")
