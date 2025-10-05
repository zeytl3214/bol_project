from flask import Flask, send_file
from deal_scraper import top_deals_csv
import os


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/get_top_deals")
def top_deals():
    top_deals_csv()

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "topdeals.csv")
    #send_file(file_path, as_attachment=True) #to download

    if os.path.exists(file_path):
        return "Topdeals CSV ready! (data/topdeals.csv)"
    else:
        return "Error: CSV couldn't be formed"

if __name__ == '__main__':
    app.run(debug=True)

    
