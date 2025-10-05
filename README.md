# Top-deals Scraper

A Flask-based web service that scrapes *Topdeals* products from [Bol.com](https://www.bol.com/nl/nl/deals) using **Selenium**.  
The service extracts product **titles, prices, and links**, saves them as a CSV file, and returns the file via a downloadable response.

## Project Structure

bol_project/

├── deal_scraper.py
├── flask_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
└── topdeals.csv

## Installation

1. Clone the Repository

Clone the project to your local machine
cd topdeals-scraper


2. Create and Activate a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate      #macOS / Linux
venv\Scripts\activate         #Windows

3. Install Dependencies
Install all required Python libraries using pip:

   pip install -r requirements.txt

Usage

Run the Flask Application: Start the Flask service from your terminal (with the virtual environment activated):

python flask_app.py

Trigger the Scraper: Open your web browser and navigate to the following URL to start the scraping process

http://127.0.0.1:5000/get_top_deals

The scraper will:

Launch Chrome using Selenium.

Scroll to load all available Topdeals on the Bol.com page.

Save the extracted data to data/topdeals.csv.




