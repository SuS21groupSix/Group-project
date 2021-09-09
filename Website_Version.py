# Overview
    # Instructions [Line 17]
    # Imported modules [Line 36]
    # Item scanner [Line 44]
    # Drug class [Line 79]
    # File converter [Line 78]
    # Date transformer [Line 95]
    # Redirection to pharmacy website [Line 105]
    # Manual reorder request [Line 190]
    # Request inventory [Line 197]
    # Search inventory [Line 207]
    # Check expiry date [Line 219]
    # Remove drugs from inventory [Line 233]
    # Object converter [Line 244]


# Instructions

# 1) This code requires to be in the same folder as the corresponding Website_Server.py file.
#    Furthermore, it requires the MyMedibox.html file to be in another 'templates' folder.
#    Furthermore, it requires the cc_style.css file to be in another 'static' folder.

# 2) Another condition exists in regard to the scanner. QR- and barcodes must contain the following data structure:

     # name_of_drug
     # purchase_date in format: %Y-%m-%d %H:%M:%S
     # expiry_date in format: %Y-%m-%d %H:%M:%S

     # An example:  Adrenalin
     #              2021-09-10 12:00:00
     #              2021-09-20 12:00:00  
  
# 3) If these conditions are fulfilled the user can simply run the Website_Server.py file to get to the website.


# Imported modules

from datetime import datetime
from pyzbar import pyzbar
import webbrowser
import cv2


# Item scanner:
# This function scans the QR- or barcode and writes its contents into a file.

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        with open("barcode_file.txt", mode ='a') as file:
            file.write(barcode_info + "\n" )
    return len(barcodes)

    
def scan_item():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        cv2.imshow('Barcode/QR code reader', frame)
        number_barcodes = read_barcodes(frame)
        if cv2.waitKey(1) & 0xFF == 27 or number_barcodes > 0:
            break
    camera.release()
    cv2.destroyAllWindows()


# Drug class

class Drug:
    def __init__(self, name, purchase_date, expiry_date):
        self.name = name
        self.purchase_date = purchase_date
        self.expiry_date = expiry_date


# File converter:
# This function converts the contents of the file into objects.

def convert_file_into_objects(file):
    drug_inventory = []
    with open(file, "r") as f:                             
        while True:
            line1 = f.readline().rstrip()
            if line1 == "":
                break
            line2 = f.readline().rstrip()
            line3 = f.readline().rstrip()
            drug_name = Drug(line1, line2, line3)
            drug_inventory.append(drug_name)                        
    return drug_inventory
            

# Date transformer:
# This function transforms the dates of type string into the datetime format.

def transform_dates(drug_inventory):
    for drug in drug_inventory:
        drug.purchase_date = datetime.strptime(drug.purchase_date, "%Y-%m-%d %H:%M:%S")
        drug.expiry_date = datetime.strptime(drug.expiry_date, "%Y-%m-%d %H:%M:%S")
    return drug_inventory


# Redirection to pharmacy website:
# This function redirects the user to the website of a pharmacy to buy new items.

def website_forward(drug): 
    if drug == "Aspirin":
        webbrowser.open("https://www.amavita.ch/de/aspirin-s-tabl-500-mg-20-stk.html")
    elif drug == "Ibuprofen":
        webbrowser.open("https://www.amavita.ch/de/amavita-ibuprofen-filmtabl-400-mg-10-stk.html")
    elif drug == "Eye drops":
        webbrowser.open("https://www.amavita.ch/de/bepanthenr-augentropfen-fur-trockene-und-irritierte-augen-10-ml.html")
    elif drug == "Ear drops":
        webbrowser.open("https://www.amavita.ch/de/similasan-ohrentropfen-10-ml.html")
    elif drug == "Nasal spray":
        webbrowser.open("https://www.amavita.ch/de/rinosedin-nasenspray-0-1-10-ml.html")
    elif drug == "Paracetamol":
        webbrowser.open("https://www.amavita.ch/de/amavita-paracetamol-tabl-500-mg-20-stk.html")
    elif drug == "Voltaren":
        webbrowser.open("https://www.amavita.ch/de/voltaren-dolo-forte-drag-25-mg-10-stk.html")
    elif drug == "Imodium":
        webbrowser.open("https://www.amavita.ch/de/imodium-lingual-schmelztabl-2-mg-20-stk.html")
    elif drug == "Bepanthen":
        webbrowser.open("https://www.amavita.ch/de/bepanthen-plus-creme-5-tb-30-g.html")
    elif drug == "Adrenalin":
        webbrowser.open("https://www.amavita.ch/de/rubimed-adrenalin-comp-glob-45-g.html")
    elif drug == "Effervescent tablets":
        webbrowser.open("https://www.amavita.ch/de/nasobol-inhalo-brausetabl-30-stk.html")
    elif drug == "Bandage":
        webbrowser.open("https://www.amavita.ch/de/emosan-medi-ellbogen-bandage-l.html")
    elif drug == "Syrup":
        webbrowser.open("https://www.amavita.ch/de/supradynr-junior-sirup-325-ml.html")
    elif drug == "Magnesium":
        webbrowser.open("https://www.amavita.ch/de/magnesium-vital-complex-kaps-1-25-mmol-100-stk.html")
    elif drug == "NeoCitran":
        webbrowser.open("https://www.amavita.ch/de/neocitran-schnupfen-erkaltung-filmtabl-12-stk.html")
    elif drug == "Cough Syrup":
        webbrowser.open("https://www.amavita.ch/de/prospanex-hustensaft-fl-200-ml.html")
    elif drug == "Nasal ointment":
         webbrowser.open("https://www.amavita.ch/de/amavita-panthoben-nasensalbe-10-g.html")
    elif drug == "Eukalyptus":
         webbrowser.open("https://www.amavita.ch/de/otrivin-natural-plus-mit-eukalyptus-spray-20-ml.html")
    elif drug == "Lozenges":
         webbrowser.open("https://www.amavita.ch/de/solmucol-erkaltungshusten-lutschtabl-100-mg-24-stk.html")
    elif drug == "Dextromethorphan":
         webbrowser.open("https://www.amavita.ch/de/bisolvon-dextromethorphan-pastillen-10-5-mg-20-stk.html")
    elif drug == "Effervescent salt":
         webbrowser.open("https://www.amavita.ch/de/siesta-1-brausesalz-150-g.html")
    elif drug == "Lactease":
         webbrowser.open("https://www.amavita.ch/de/lactease-4500-fcc-kautabl-40-stk.html")
    elif drug == "Glycerin":
        webbrowser.open("https://www.amavita.ch/de/glycerin-elk-pharma-supp-18-stk.html")
    elif drug == "Normolytoral":
        webbrowser.open("https://www.amavita.ch/de/normolytoral-plv-btl-10-stk.html")
    elif drug == "Riopan Gel":
        webbrowser.open("https://www.amavita.ch/de/riopan-gel-800-mg-fl-250-ml.html")
    elif drug == "Itinerol":
        webbrowser.open("https://www.amavita.ch/de/itinerol-b6-supp-erw-10-stk.html")
    elif drug == "Disflatyl drops":
        webbrowser.open("https://www.amavita.ch/de/disflatyl-tropfen-fl-30-ml.html")
    elif drug == "Vitamin C + zinc":
        webbrowser.open("https://www.amavita.ch/de/redoxon-zinc-brausetabl-30-stk.html")
    elif drug == "Vitamin D3":
        webbrowser.open("https://www.amavita.ch/de/vita-d3-protect-losung-zum-einnehmen-fl-20-ml.html")
    elif drug == "Supradyn Gummies":
        webbrowser.open("https://www.amavita.ch/de/supradyn-junior-gummies-ds-60-stk.html")
    elif drug == "Power essence":
        webbrowser.open("https://www.amavita.ch/de/wonnensteiner-kraftessenz-liq-fl-750-ml.html")
    elif drug == "Dibase solution":
        webbrowser.open("https://www.amavita.ch/de/dibase-los-25000-ie-fl-2-5-ml.html")
    elif drug == "Vitamin B6 tablets":
        webbrowser.open("https://www.amavita.ch/de/vitamin-b6-streuli-tabl-300-mg-ds-20-stk.html")
    elif drug == "Mint Spray":
        webbrowser.open("https://www.amavita.ch/de/nicorette-mint-spray-zur-anwendung-in-der-mundhohle-150-dos.html")
    elif drug == "Nail polish":
        webbrowser.open("https://www.amavita.ch/de/kloril-p-nagellack-fl-3-3-ml.html")
    elif drug == "Nicotinell Gum":
        webbrowser.open("https://www.amavita.ch/de/nicotinell-gum-4-mg-fruit-96-stk.html")
    elif drug == "Biotin Merz":
        webbrowser.open("https://www.amavita.ch/de/biotin-merz-tabl-5-mg-25-stk.html")
    elif drug == "Nasal rinsing salt":
        webbrowser.open("https://www.amavita.ch/de/emser-r-nasenspulsalz-2-5-g-50-beutel.html")
    else:
        return "We cannot seem to find your requested item. Please try again."
    return "We opened the website for you."


# Manual reorder request:
# This function lets the user order new items manually.

def manual_reorder_request(drug):
    return website_forward(drug)


# Request inventory:
# This function lets the user check the current inventory.

def request_inventory(drug_inventory):
    html_return = "<table border='1'><thead><tr><th>Name</th><th>Purchase Date</th><th>Expiry Date</th></tr></thead>"
    for drug in drug_inventory:
        html_return += "<tr><td>" + drug.name + "</td><td>" + str(drug.purchase_date) + "</td><td>" + str(drug.expiry_date) + "</td></tr>"
    return html_return + """</table><br><a href="/">Return to homepage</a>"""


# Search inventory:
# This function lets the user search for specific items in his current inventory.

def search_inventory(drug_inventory, drug):
    html_return = "<table border='1'><thead><tr><th>Name</th><th>Purchase Date</th><th>Expiry Date</th></tr></thead>"
    for drug_in_inventory in drug_inventory:
        if drug == drug_in_inventory.name:
            html_return += "<tr><td>" + drug_in_inventory.name + "</td><td>" + str(drug_in_inventory.purchase_date) + "</td><td>" + str(drug_in_inventory.expiry_date) + "</td></tr>"
            return html_return + """</table><br><a href="/">Return to homepage</a>"""
    return """This drug does not exist in your inventory.<br><a href="/">Return to homepage</a>"""


# Check expiry date:
# This function lets the user check the expiry dates of his items.
       
def check_expiry_date(drug_inventory):
    html_return = ""
    for drug in drug_inventory:
        day_difference = abs(drug.expiry_date - datetime.today()).days
        if datetime.today() > drug.expiry_date:
            html_return += "You should have disposed of your item '" + drug.name + "' " + str(day_difference) + " days ago. Please go to your local pharmacy and dispose of it there.<br>"       
        elif  day_difference < 14:
            html_return += "Your item '" + drug.name + "' expires in " + str(day_difference) + " days.<br>"
    return html_return + """<br><a href="/">Return to homepage</a>"""


# Remove drugs from inventory:
# This function lets the user remove items from his current inventory when he has disposed of them.

def remove_drugs(drug_inventory, drug):
    for drug_in_inventory in drug_inventory:
        if drug == drug_in_inventory.name:
            drug_inventory.remove(drug_in_inventory)
            return """The item was removed from your inventary.<br><a href="/check-inventory">Go to inventory</a>"""
    return """No such drug currently exists in your inventory.<br><a href="/check-inventory">Go to inventory</a>"""


# Object converter:
# This function converts the objects back into a file to save them after the program is closed.

def convert_objects_into_file(file, drug_inventory):
    with open(file, "w") as f:
        for drug in drug_inventory:
            f.write(drug.name + "\n")
            f.seek
            f.write(str(drug.purchase_date) + "\n")
            f.write(str(drug.expiry_date) + "\n")