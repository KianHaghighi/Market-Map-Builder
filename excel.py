import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils.dataframe import dataframe_to_rows
import matplotlib.pyplot as plt
import io
import base64
import openpyxl

# Create sample data for Cost Predictions
predictions_data = {
    'Category': ['Development', 'Development', 'Marketing', 'Marketing', 'Operational', 'Operational', 'Miscellaneous', 'Miscellaneous'],
    'Item': ['Developer Salaries', 'Software Licenses', 'Online Advertising', 'Content Creation', 'Cloud Hosting', 'Customer Support', 'Legal Fees', 'Accounting'],
    'Predicted Cost': [10000, 500, 2000, 1000, 1500, 2000, 1000, 500],
    'Time Frame': ['Monthly', 'Monthly', 'Monthly', 'Monthly', 'Monthly', 'Monthly', 'Quarterly', 'Monthly'],
    'Notes': ['For 2 full-time developers', 'Various development tools', 'Google Ads and social media', 'Blog posts and videos', 'AWS or similar', 'Part-time support staff', 'Legal consultations', 'Bookkeeping services']
}

predictions_df = pd.DataFrame(predictions_data)

# Create sample data for Actual Costs (let's assume 3 months of data)
actual_data = {
    'Category': ['Development', 'Development', 'Marketing', 'Marketing', 'Operational', 'Operational', 'Miscellaneous', 'Miscellaneous'] * 3,
    'Item': ['Developer Salaries', 'Software Licenses', 'Online Advertising', 'Content Creation', 'Cloud Hosting', 'Customer Support', 'Legal Fees', 'Accounting'] * 3,
    'Actual Cost': [
        10200, 450, 2100, 950, 1600, 1900, 800, 500,
        10000, 500, 2200, 1100, 1550, 2050, 0, 500,
        10300, 500, 1900, 1050, 1700, 2100, 0, 500
    ],
    'Date': ['2023-01-31', '2023-01-31', '2023-01-31', '2023-01-31', '2023-01-31', '2023-01-31', '2023-01-31', '2023-01-31',
             '2023-02-28', '2023-02-28', '2023-02-28', '2023-02-28', '2023-02-28', '2023-02-28', '2023-02-28', '2023-02-28',
             '2023-03-31', '2023-03-31', '2023-03-31', '2023-03-31', '2023-03-31', '2023-03-31', '2023-03-31', '2023-03-31'],
    'Notes': [''] * 24  # Empty notes for simplicity
}

actual_df = pd.DataFrame(actual_data)

# Create Variance Analysis
variance_df = predictions_df[['Category', 'Item', 'Predicted Cost']].copy()
variance_df['Actual Cost'] = actual_df.groupby('Item')['Actual Cost'].mean().values
variance_df['Variance'] = variance_df['Actual Cost'] - variance_df['Predicted Cost']
variance_df['Notes'] = ''

# Create and save the Excel file
excel_file = 'saas_cost_tracker.xlsx'
excel_file_path = 'C:/Users/kianh/market_map_builder-1/saas_cost_tracker.xlsx'
variance_df.to_excel(excel_file_path, index=False)
print(f"Excel file '{excel_file_path}' created successfully.")