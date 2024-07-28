import pandas as pd

# from py_crunchbase import PyCrunchbase
# from py_crunchbase.apis.search.predicates import Currency

# pycb = PyCrunchbase()
# api = pycb.search_funding_rounds_api()

# api.select(
#     'identifier', 'announced_on', 'funded_organization_identifier', 'money_raised', 'investment_type'
# ).where(
#     announced_on__gte=2012, num_investors__lte=4, money_raised__gte=Currency(10000000)
# ).order_by(
#     'announced_on'
# )

# for page in api.iterate():
#     for funding_round in page:
#         print(funding_round.permalink)

#search for companies in the market
companies = []

#search through the industries data set; find the most successful ones
industries = []

#segment the specific companies into categories defined by the user or AI
categories = []


df = pd.read_csv('datasets\\funding_rounds.csv')
df_ph = pd.read_csv("datasets\product_hunt_data\\2020.csv")

def clean_data():
    df['funding_amount'] = df['funding_amount'].str.replace(',', '')
    df['funding_amount'] = df['funding_amount'].str.replace('$', '')
    df['funding_amount'] = df['funding_amount'].astype(float)
    df['date_column'] = pd.to_datetime(df['date_column'])
    return df

def fill_missing_data():
    df['funding_amount'] = df['funding_amount'].fillna(df['funding_amount'].mean())
    return df


def get_data(market=None, company=None, category=None):
    #look in product hunt data for companies in the market
    if market:
        companies.append(df_ph[df_ph['Topic'].str.lower() == market.lower()])
    return

# #data cleaning and preprocessing
# clean_data()
# fill_missing_data()
# get_data()

#display markets that the user can choose from
print('Markets to choose from:')
print(df_ph['Topic'].unique())

#prompt user for input about market
market = input('Enter the market you want to analyze: ')
keywords = market.split(' ')


#build the market map and display it
get_data(market=market)
print(companies)
