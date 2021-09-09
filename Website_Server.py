# Overview
    # Instructions [Line 9]
    # Imported modules [Line 14]
    # Administrative tasks [Line 20]
    # Routes [Line 31]
    # Run application [Line 70]


# Instructions

# You will find the necessary instructions for this file in the Website_Version.py file.


# Imported modules

from flask import Flask, render_template, request
from Website_Version import *


# Administrative tasks:
# These commands will open or create a file if it does not yet exist and convert possible data from within this file into objects.

app = Flask(__name__)

f = open("barcode_file.txt", "a")
f.close
drug_inventory = convert_file_into_objects("barcode_file.txt")
drug_inventory = transform_dates(drug_inventory)


# Routes:
# These routes will activate different functions when triggered by the user on the website.

@app.route("/")
def homepage():
    return render_template("MyMedibox.html")

@app.route("/check-inventory")
def check_inven():
    return request_inventory(drug_inventory)

@app.route("/search-inventory")
def search_inven():
    item = request.values["search_item"]
    return search_inventory(drug_inventory, item)

@app.route("/add-items")
def add_items():
    global drug_inventory
    scan_item()
    drug_inventory = convert_file_into_objects("barcode_file.txt")
    drug_inventory = transform_dates(drug_inventory)
    return """Your item was scanned.<br><a href="/check-inventory">Go to inventory</a>"""

@app.route("/remove-items")
def remove_items():
    item = request.values["remove_item"]
    return remove_drugs(drug_inventory, item)

@app.route("/check-dates")
def check_dates():
    return check_expiry_date(drug_inventory)

@app.route("/reorder-items")
def reorder_products():
    item = request.values["reorder_item"]
    return manual_reorder_request(item)


# Run application:
# This command starts the website.

app.run(debug=True)