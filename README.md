# HR Analytics Dashboard

An end-to-end HR analytics project built with **Power BI, Python, Pandas, and Jupyter Notebook** to turn employee data into practical insights for workforce and retention decisions.

## Business Problem

Employee attrition can increase recruitment costs, create skill gaps, reduce team stability, and affect productivity. HR teams need a clear way to understand **where attrition is occurring, which employee groups show higher attrition, and what workforce factors are associated with employee turnover**.

The main business questions addressed in this project were:

- Which departments and job roles have higher attrition?
- How does overtime relate to employee attrition?
- Does job level or monthly income show differences in attrition?
- Are business travel requirements associated with different attrition patterns?
- How do age, tenure, distance from home, and other employee characteristics relate to attrition?
- How can HR teams monitor performance, training, compensation, and workforce demographics alongside attrition?

## Challenges / Problems Faced

### 1. Raw HR data needed preparation
The original dataset required inspection for data types, missing values, distributions, and consistency before analysis.

**Solution:**  
Performed data inspection and cleaning using Python/Pandas and prepared a cleaned CSV for Power BI analysis.

### 2. Attrition is not explained by one variable
Looking only at overall attrition does not provide enough information for HR decision-making.

**Solution:**  
Analyzed attrition across multiple dimensions including **department, job role, overtime, business travel, job level, income, stock options, demographics, and employee experience**.

### 3. Outliers in compensation and workforce variables
Variables such as Monthly Income, Distance From Home, and Total Working Years contain observations that can appear as statistical outliers.

**Solution:**  
Used the **IQR method** to identify potential outliers and investigated them instead of automatically deleting them. This keeps the analysis representative of the workforce while allowing unusual observations to be considered separately.

### 4. Some standard HR metrics were not available
The dataset does not contain the information required to calculate metrics such as **time-to-hire, absenteeism rate, manager span of control, or compa-ratio**.

**Solution:**  
Documented these limitations rather than creating unsupported assumptions or artificial metrics. The dashboard focuses on measures that can be calculated reliably from the available data.

### 5. Turning analysis into a usable dashboard
A large number of HR variables can easily make a dashboard difficult to interpret.

**Solution:**  
Organized the analysis into focused pages for **Overview, Attrition, Demographics, Compensation & Tenure, and Details**, allowing users to move from high-level KPIs to more detailed analysis.

## Business Impact

The dashboard is designed to help HR and management:

- **Identify attrition hotspots** by department and job role.
- **Investigate workforce factors associated with turnover**, such as overtime, job level, income, and business travel.
- **Segment employees** using demographic and workforce characteristics.
- **Monitor employee development** through performance and training information.
- **Support data-driven HR discussions** instead of relying only on overall employee counts.
- **Prioritize further investigation** into employee groups showing notable attrition patterns.

> The dashboard identifies patterns and relationships in the dataset; it does not establish that a particular factor directly causes employee attrition.

## Key Analysis

- Employee count and attrition rate
- Attrition by department and job role
- Attrition by overtime and business travel
- Attrition by job level
- Monthly income and compensation patterns
- Employee tenure and experience
- Demographic distribution
- Performance rating distribution
- Training activity
- Stock option analysis
- Correlation analysis
- IQR-based outlier analysis

## Dashboard Structure

- **Overview** — overall workforce KPIs and HR trends
- **Attrition** — detailed employee turnover analysis
- **Demographics** — workforce composition and demographic patterns
- **Compensation & Tenure** — income, tenure, performance, and training analysis
- **Details** — detailed employee-level information

## Tools & Technologies

- **Power BI** — interactive dashboard, DAX, Power Query, data modeling
- **Python** — exploratory data analysis
- **Pandas** — data cleaning and analysis
- **Jupyter Notebook** — analysis workflow
- **CSV** — cleaned analytical dataset

## Project Workflow

**Raw Data → Data Cleaning → Exploratory Data Analysis → HR Metrics → Power BI Data Model → Interactive Dashboard → Business Insights**

## Dataset Limitations

The IBM HR Analytics Employee Attrition dataset does not contain fields required for some common HR metrics such as time-to-hire, absenteeism rate, manager span of control, or compa-ratio. These metrics are therefore not presented as calculated measures in this project.

## Project Outcome

This project demonstrates practical skills in **data cleaning, exploratory data analysis, HR analytics, Power BI dashboard development, data visualization, statistical outlier analysis, and translating data into business-focused insights**.

## Author

**Syed Mohammed Ghouse**

GitHub: https://github.com/s4184271-sys
