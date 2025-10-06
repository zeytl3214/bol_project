# Bol.com Top Deals Scraper

This project scrapes product data (name, price, and link) from the “Top Deals” page on Bol.com using Selenium and saves it to a CSV file. Additionally, it provides a Flask API to trigger the scraping and access the CSV file.

---

## Features

- Web scraping with Selenium
- Handles lazy loading and infinite scroll
- Saves product data to CSV
- Flask API to generate and access CSV

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/zeytl3214/bol_project.git
    cd bol_project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Run the scraper directly
```bash
python deal_scraper.py  # generates data/topdeals.csv with latest deals
```

### Run the Flask API
```bash
python app.py  # starts Flask API at http://127.0.0.1:5000/
```

Open your browser and go to http://127.0.0.1:5000/

Access the scraper via http://127.0.0.1:5000/get_top_deals

The CSV will be created in data/topdeals.csv


### Notes

Make sure ChromeDriver is installed and compatible with your Chrome version.

The scraper runs in headless mode by default.
