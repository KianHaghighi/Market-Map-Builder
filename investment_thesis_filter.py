import pandas as pd
import re

def load_data(file_path):
    """Load and preprocess the CSV data."""
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Strip spaces from column names
    df.columns = df.columns.str.strip()
    
    # Clean and convert funding column to numeric
    df['funding_total_usd'] = df['funding_total_usd'].replace('[\$,]', '', regex=True).replace(' -   ', '0').astype(float)
    
    return df

def get_investment_thesis():
    """Get investment thesis inputs from the user."""
    thesis = {
        'industry': input("Enter target industry: "),
        'min_funding': float(input("Enter minimum funding (in USD): ")),
        'max_funding': float(input("Enter maximum funding (in USD): ")),
        'location': input("Enter target location: "),
        'market_keywords': input("Enter market keywords (comma-separated): ").split(','),
        'companies_file': input("Enter path to CSV file of companies to look at (leave blank if none): ")
    }
    return thesis

def filter_companies(df, thesis):
    """Filter companies based on the investment thesis."""
    filtered = df[
        (df['category_list'].str.contains(thesis['industry'], case=False, na=False)) &
        (df['funding_total_usd'] >= thesis['min_funding']) &
        (df['funding_total_usd'] <= thesis['max_funding']) &
        (df['country_code'] == thesis['location'])
    ]
    
    # Filter by market keywords
    keyword_filter = filtered['market'].apply(lambda x: any(keyword.lower() in str(x).lower() for keyword in thesis['market_keywords']))
    filtered = filtered[keyword_filter]
    
    # If a specific list of companies is provided, filter further
    if thesis['companies_file']:
        target_companies = pd.read_csv(thesis['companies_file'])['name'].tolist()
        filtered = filtered[filtered['name'].isin(target_companies)]
    
    return filtered

def display_results(filtered_df):
    """Display the filtered results."""
    print(f"\nFound {len(filtered_df)} companies matching the investment thesis:")
    for _, company in filtered_df.iterrows():
        print(f"\nName: {company['name']}")
        print(f"Category: {company['category_list']}")
        print(f"Funding: ${company['funding_total_usd']:,.2f}")
        print(f"Country: {company['country_code']}")
        print(f"Market: {company['market']}")

def main():
    df = load_data('datasets/crunchbase_data/investments_VC.csv')
    thesis = get_investment_thesis()
    filtered_companies = filter_companies(df, thesis)
    display_results(filtered_companies)

if __name__ == "__main__":
    main()