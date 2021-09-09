# Overview
    # Instructions [Line 20]
    # Imported modules [Line 37]
    # Item scanner [Line 45]
    # Drug class [Line 70]
    # File converter [Line 79]
    # Date transformer [Line 96]
    # Redirection to pharmacy website [Line 106]
    # Automatic reorder request [Line 191]
    # Manual reorder request [Line 210]
    # Request inventory [Line 222]
    # Search inventory [Line 243]
    # Check expiry date [Line 274]
    # Remove drugs from inventory [Line 290]
    # Object converter [Line 302]
    # User interface [Line 313]
    # Activating function [Line 353]


# Instructions

# 1) This code works without any prerequisites. There have to be no existing files, programs, etc.

# 2) Only one condition exists in regard to the scanner. QR- and barcodes must contain the following data structure:

     # name_of_drug
     # purchase_date in format: %Y-%m-%d %H:%M:%S
     # expiry_date in format: %Y-%m-%d %H:%M:%S

     # An example:  Aspirin
     #              2021-09-10 12:00:00
     #              2021-09-20 12:00:00

# 3) If this condition is fulfilled the user can simply run the program. All modified data will be saved when the program is finished the program by pressing 'Done'.    


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
        print("We cannot seem to find your requested item. Please try again.")
        manual_reorder_request()


# Automatic reorder request:
# This function is activated within the function checking the expiry dates to give the user the opportunity to buy new items if they have expired.
# It redirects him to the previous function.

def automatic_reorder_request(drug):
    a = 1
    while a > 0:
        print("Would you like to reorder this product? Please answer 'Yes' or 'No'.")
        answer = input()
        if answer == "Yes":
            website_forward(drug)
            a -= 1
        elif answer == "No":
            print("You can always reorder your drug '" + drug + "' with the manual reordering function.")
            a -= 1
        else:
            print("We did not understand you. Can you try again?")


# Manual reorder request:
# This function lets the user order new items manually.

def manual_reorder_request():
    print("\nWhich drug would you like to reorder? Please enter its name. If you want to cancel the process, please press 'Cancel'.\n")
    drug = input()
    if drug != "Cancel":
        website_forward(drug)
    else:
        print("\nThe process was cancelled.\n")


# Request inventory:
# This function lets the user check the current inventory.

def request_inventory(drug_inventory):
    drug_list = []
    longest_name = ""
    for drug in drug_inventory:
        if len(drug.name) > len(longest_name):
            longest_name = drug.name
    if longest_name != "":
        for drug in drug_inventory:
            add_lines = len(longest_name) - len(drug.name)
            drug_list.append(drug.name + "----" + "-" * add_lines + str(drug.purchase_date) + "----" + str(drug.expiry_date) + "\n")
        drug_list.sort()
        print("\n\n" + "Name           Date of purchase        Date of expiry\n")
        for drug in drug_list:
            print(drug)
    else:
        return print("\nYour inventory is currently empty.\n")


# Search inventory:
# This function lets the user search for specific items in his current inventory.

def search_inventory(drug_inventory):
    print("\nPlease type in the name of a drug to check whether it exists in your inventory.\n")
    drug = input()
    n = 1
    for drug_in_inventory in drug_inventory:
        if drug == drug_in_inventory.name:
            print("\nThis drug exists in your inventory. Would you like to see its information? Please type 'Yes' or 'No'.\n")
            while True:
                answer = input()
                if answer == "Yes":
                    print("\n\nName          Purchase Date          Expiry Date\n")
                    print(drug_in_inventory.name + "----" + str(drug_in_inventory.purchase_date) + "----" + str(drug_in_inventory.expiry_date) + "\n")
                    n -=1
                    break
                if answer == "No":
                    return print("\nYou can always access the information of your medicine cabinet over this function at any other time.\n")
                else:
                    print("\nWe could not understand that. Please type 'Yes' or 'No'.\n")
    while n > 0:
        print("\nThis drug does not exist in your inventory. Would you like to order it? Please type 'Yes' or 'No'.\n")
        while True:
            answer = input()
            if answer == "Yes":
                return website_forward(drug)
            if answer == "No":
                return print("\nYou can always order your drugs over the regular order function at any time.\n")


# Check expiry date:
# This function lets the user check the expiry dates of his items.
       
def check_expiry_date(drug_inventory):
    for drug in drug_inventory:
        day_difference = abs(drug.expiry_date - datetime.today()).days
        if datetime.today() > drug.expiry_date:
            print("\nYou should have disposed of your item '" + drug.name + "' " + str(day_difference) + " days ago. Please go to your local pharmacy and dispose of it there.\n")
            automatic_reorder_request(drug.name)        
        elif  day_difference < 14:
            print("\nYour item '" + drug.name + "' expires in " + str(day_difference) + " days.\n")
            automatic_reorder_request(drug.name)
        else:
            print("\nNone of your items expires in the near future.\n")


# Remove drugs from inventory:
# This function lets the user remove items from his current inventory when he has disposed of them.

def remove_drugs(drug_inventory):
    print("\nWhat drug would you like to remove from your inventory?\n")
    drug = input()
    for drug_in_inventory in drug_inventory:
        if drug == drug_in_inventory.name:
            return drug_inventory.remove(drug_in_inventory)
    return print("\nNo such drug currently exists in your inventory.\n")


# Object converter:
# This function converts the objects back into a file to save them after the program is closed.

def convert_objects_into_file(file, drug_inventory):
    with open(file, "w") as f:
        for drug in drug_inventory:
            f.write(drug.name + "\n")
            f.write(str(drug.purchase_date) + "\n")
            f.write(str(drug.expiry_date) + "\n")


# User interface:
# This function provides the user with different options to choose from that will trigger other functions.

def activated_code():
    print("\n\n-- Welcome to myMEDIBOX! --\n")
    f = open("barcode_file.txt", "a")
    f.close
    drug_inventory = convert_file_into_objects("barcode_file.txt")
    drug_inventory = transform_dates(drug_inventory)
    while True:
        print("\n\n-- Menu --\n\n**********\n\n**********")
        print("\nTo check your inventory, type '1'.\n")
        print("To search through your inventory, type '2'.\n")
        print("To scan new items and add them to your inventory, type '3'.\n")
        print("To remove items from your inventory, type '4'.\n")
        print("To check the expiry dates of your items, type '5'.\n")
        print("To reorder items, type '6'.\n")
        print("When you are done, type 'Done'.\n\n")
        answer = input()
        if answer == "1":
            request_inventory(drug_inventory)
        elif answer == "2":
            search_inventory(drug_inventory)
        elif answer == "3":
            if __name__ == '__main__':
                scan_item()
            drug_inventory = convert_file_into_objects("barcode_file.txt")
            drug_inventory = transform_dates(drug_inventory)
        elif answer == "4":
            remove_drugs(drug_inventory)
        elif answer == "5":
            check_expiry_date(drug_inventory)
        elif answer == "6":
            manual_reorder_request()
        elif answer == "Done":
            return convert_objects_into_file("barcode_file.txt", drug_inventory)
        else:
            print("We did not understand. Please try again.\n")


# Activated code:
# This line activates the previous function and, therefore, the entire code.

activated_code()