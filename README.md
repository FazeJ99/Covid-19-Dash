# COVID-19 Geographic Distribution Dataset

This repository contains data and scripts for analyzing COVID-19 geographic distribution. The dataset provides detailed information about COVID-19 cases and deaths across different countries and territories.

## Dataset

The dataset is sourced from the file `coviddata.xlsx`, which contains the following columns:

- **dateRep**: Date of the report (YYYY-MM-DD).
- **day, month, year**: Day, month, and year as separate columns.
- **cases**: Number of new COVID-19 cases reported.
- **deaths**: Number of new COVID-19 deaths reported.
- **countriesAndTerritories**: Name of the country or territory.
- **geoId**: Geographical ID for the country/territory.
- **countryterritoryCode**: ISO country code.
- **popData2018**: Population data for the country/territory (as of 2018).

## Project Structure

The repository is organized as follows:


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/covid-data-analysis.git
    cd covid-data-analysis
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Explore the dataset:
    Open the Jupyter notebook in the `notebooks/` folder:
    ```bash
    jupyter notebook notebooks/analysis.ipynb
    ```

## Dependencies

- **pandas**: Used for data manipulation and analysis.
- **Dash**: A framework for building data visualization web applications.
- **plotly**: Used for creating interactive plots in the Dash app.
- **Jupyter**: For running and exploring the dataset in notebooks.

## Usage

- The data preprocessing script (`preprocess_data.py`) can be used to clean and prepare the dataset for analysis.
- Use the Jupyter notebook to explore visualizations, trends, and other insights from the dataset.
- Optionally, you can build an interactive web dashboard using Dash to visualize COVID-19 trends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This dataset contains information about the COVID-19 pandemic and is used for research and educational purposes.

## Dataset

The data for this dashboard is stored in an Excel file (`coviddata.xlsx`) located in the `data` folder. The dataset contains COVID-19 statistics, including cases and deaths for different countries.

## Usage

1. Select countries from the table by clicking on the rows.
2. Use the dropdown menus to switch between 'Deaths' and 'Cases' for both the pie chart and the line chart.
3. The visualizations will update based on the selected countries and metrics.
