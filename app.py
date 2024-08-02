from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('builder.html')

@app.route('/users', methods=['POST'])
def add_user():
    user = User(username=request.form['username'], email=request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect('/')

def generate_checkboxes_html(df):
    checkboxes_html = ""
    for index, row in df.iterrows():
        checkboxes_html += f'<div class="form-check">'
        checkboxes_html += f'<input class="form-check-input" type="checkbox" name="selected_rows" value="{index}" id="row_{index}">'
        checkboxes_html += f'<label class="form-check-label" for="row_{index}">{row["Topic"]}</label>'
        checkboxes_html += '</div>'
    return checkboxes_html

@app.route('/market_map', methods=['GET', 'POST'])
def market_map():
    # Product Hunt data set
    df_ph = pd.read_csv("datasets/product_hunt_data/2020.csv")  # Adjust path as needed
    df_pf_2021 = pd.read_csv("datasets/product_hunt_data/2021.csv")  # Adjust path as needed
    df_ph_2022 = pd.read_csv("datasets/product_hunt_data/2022.csv")  # Adjust path as needed
    df_ph = pd.concat([df_ph, df_pf_2021, df_ph_2022], ignore_index=True)

    markets_html = ""
    checkboxes_html = generate_checkboxes_html(df_ph)

    if request.method == 'POST':
        print(request.form)
        market = request.form['market']
        selected_rows = request.form.getlist('selected_rows')
        # Filter the DataFrame based on the market keyword.
        filtered_df = df_ph[df_ph['Topic'].str.contains(market, case=False, na=False)]
        # Alter the links so that the user can be directed
        df_ph['ShortUrl'] = df_ph['ShortUrl'].apply(lambda x: f'<a href="{x}">{x}</a>')
        markets_html = filtered_df.to_html(escape=False, classes='table table-striped', index=False)
    else:
        # Optionally, display the entire dataset or a subset when the page first loads
        markets_html = df_ph.to_html(escape=False, classes='table table-striped', index=False)

    return render_template('market_map.html', markets_html=markets_html, checkboxes_html=checkboxes_html)


@app.route('/crunchbase_data')
def crunchbase_data():
    data = fetch_crunchbase_data()
    return render_template('crunchbase_data.html', data=data)

@app.route('/select_companies', methods=['POST'])
def select_companies():
    selected_companies = request.form.getlist('company')
    # Process the selected companies
    return f"Selected companies: {', '.join(selected_companies)}"

def generate_companies_html(market):
    # Example function to generate HTML for companies
    companies = ['Company A', 'Company B', 'Company C']
    companies_html = '<div class="form-check">'
    for company in companies:
        companies_html += f'<input class="form-check-input" type="checkbox" name="company" value="{company}">'
        companies_html += f'<label class="form-check-label">{company}</label><br>'
    companies_html += '</div>'
    return companies_html

def fetch_producthunt_data():
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {
        "Authorization": "Bearer WOvgoSDNLBtwGJ_iWZYUV6HOOMB_Mg0v__XS_MTAblQ",
        "Content-Type": "application/json"
    }
    query = """
    {
      posts {
        edges {
          node {
            name
            tagline
            votesCount
            website
          }
        }
      }
    }
    """
    response = requests.post(url, headers=headers, json={"query": query})
    if response.status_code == 200:
        return response.json()["data"]["posts"]["edges"]
    else:
        return None

def fetch_crunchbase_data():
    url = "https://api.crunchbase.com/api/v3.1/your_endpoint"
    params = {
        "user_key": "e3941765dfeec33977f94b57cba729ba",
        "other_params": "value"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Or process the response as needed
    else:
        return "Error fetching data"

def generate_companies_html(market):
    # Example function to generate HTML for companies
    companies = ['Company A', 'Company B', 'Company C']
    companies_html = '<div class="form-check">'
    for company in companies:
        companies_html += f'<input class="form-check-input" type="checkbox" name="company" value="{company}">'
        companies_html += f'<label class="form-check-label">{company}</label><br>'
    companies_html += '</div>'
    return companies_html


@app.route('/producthunt_data')
def producthunt_data():
    data = fetch_producthunt_data()
    if data:
        return render_template('producthunt_data.html', data=data)
    else:
        return "Error fetching data from Product Hunt"

def fetch_producthunt_data():
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {
        "Authorization": "Bearer WOvgoSDNLBtwGJ_iWZYUV6HOOMB_Mg0v__XS_MTAblQ",
        "Content-Type": "application/json"
    }
    query = """
    {
      posts {
        edges {
          node {
            name
            tagline
            votesCount
            website
          }
        }
      }
    }
    """
    response = requests.post(url, headers=headers, json={"query": query})
    if response.status_code == 200:
        return response.json()["data"]["posts"]["edges"]
    else:
        return None

@app.route('/create_from_scratch', methods=['GET', 'POST'])
def create_from_scratch():
    return render_template('create_from_scratch.html')

if __name__ == '__main__':
    app.run(debug=True)