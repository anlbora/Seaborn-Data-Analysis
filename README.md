# Data Analysis Program

The Data Analysis Program is a desktop application developed with PyQt5, Pandas, Seaborn, and Matplotlib to facilitate data exploration, analysis, and visualization. This program provides a user-friendly interface for loading datasets, exploring their structures, generating descriptive statistics, conducting correlation analysis, and more.

![1](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/a262f10d-076b-4520-8622-378bd4672830)

## Features

### Data Loading and Exploration

- **Load Datasets**: 
  - **Seaborn Datasets**: Choose a sample dataset from the Seaborn datasets library.
    ![2](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/bb8caf04-adb4-4949-b41d-8250144641d8)
    ![3](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/38f7a15e-bc1f-4f51-8a49-ba917f5d6e3e)
  - **Local Datasets**: Load a local dataset from your device by leaving the combo box as "None".
    ![4](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/2a91bdd4-8d6f-4a28-9ddb-2698d3af72a3)

- **Inspect Dataset**: 
  - View the head and tail of the dataset.
    ![5](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/c1240d97-2367-4181-887b-419a4da99756)
  - Display data types of each column.
    ![6](https://github.com/anlbora/Seaborn-Data-Analysis/assets/a100442507/b7b2908c-f5dc-439a-84bb-9da555c51e1c)
  - Show the sum of null values for each column and fill NA values. Options to ignore "0" values and encode boolean values.
    ![7](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/50887ab7-2151-4703-b9e4-a60a3acf1381)
  - View dataset's statistical values.
    ![8](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/2f050bfc-6673-4bee-8b76-4cb8932d51d1)
  - Get information for each column.
    ![9](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/261121f2-bc77-4307-b32f-3d0c681cb5df)

### Data Editing for Machine Learning

- **Prepare Data**: 
  - Fill null values and encode non-numeric data types to make the dataset machine learning-ready.

- **Basic Machine Learning Model**: 
  - Create a basic RandomForest model and save it for future predictions.
    ![10](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/70eec8fc-7f93-4398-baba-1dda8f9e3d14)
  - Predict outcomes by typing in data or getting random data. Edit random data and predict.
    ![17](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/4ec0ae76-51c5-4814-ab4e-5e71b4d0b82d)
    ![18](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/e4faed0c-a3aa-4e23-a71c-cf630c79c9ea)
    ![19](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/6c268ad8-a6be-448e-867f-55a2287ee0af)

### Column Categorization

- **Categorize Columns**: 
  - Identify categorical and numerical columns, distinguishing between high-cardinality categorical columns and numerical columns treated as categorical.

### Data Analysis

- **Target Variable Summary**: 
  - Generate summaries of the target variable grouped by other columns, with visualization options.
    ![14](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/ade1e06a-51b1-408b-91b3-bfb71d5e7fd5)
    ![15](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/274b7e81-8cc9-4779-b0ab-92e5acb78f01)

- **Correlation Analysis**: 
  - Perform correlation analysis on numerical columns and visualize the correlation matrix as a heatmap.
    ![16](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/84997c1f-af25-4883-93db-dd39a28d31b9)

- **Column Summary**: 
  - Provide insights into categorical and numerical columns with count plots, histograms, and percentage summaries.
    ![12](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/01d2d012-9dba-43e3-b492-f43579b9b894)
    ![13](https://github.com/anlbora/Seaborn-Data-Analysis/assets/100442507/47be63d9-3d85-4bff-8149-2f5842a97a82)
