# Market Map Builder

This project is a web application that allows users to analyze and visualize data from Product Hunt and Crunchbase. The application is built using Flask and Pandas, and it provides functionalities to filter and display data based on user input.

![Market Map Builder Homepage](![Screenshot 2024-08-12 113159](https://github.com/user-attachments/assets/7927ca1a-3d6c-4485-a7bc-f54a053be0fe)

This screenshot shows the homepage of the Market Map Builder application, where users can upload or select CSV files for analysis.

![Filtering Data](![image](https://github.com/user-attachments/assets/d54c4c5b-0ec3-45aa-afbc-c4a32e89adfe)


This screenshot demonstrates the functionality of filtering data based on market keywords. Users can enter keywords to narrow down the displayed results.


## Features

- **Product Hunt Data Analysis**: Load and concatenate data from multiple CSV files, filter data based on market keywords, and display the results in an HTML table.
- **Crunchbase Data Integration**: Fetch and display data from Crunchbase.
- **Company Selection**: Allow users to select companies and process the selected data.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/KianHaghighi/market_map_builder.git
    cd market_map_builder
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    flask run
    ```

2. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files (CSS, JavaScript).
- `datasets/`: Directory containing CSV files for Product Hunt data.

## Endpoints

- `/`: Main page for Product Hunt data analysis.
- `/crunchbase_data`: Page to display Crunchbase data.
- `/select_companies`: Endpoint to process selected companies.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```sh
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**:
    ```sh
    git push origin feature/your-feature-name
    ```
6. **Create a new Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [Product Hunt](https://www.producthunt.com/)
- [Crunchbase](https://www.crunchbase.com/)
