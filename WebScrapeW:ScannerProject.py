from requests_html import HTMLSession
import os
import cv2
from pyzbar.pyzbar import decode
from googlesearch import search


os.system('clear')

def webcamScan():
    print("Opening webcam...")
    cap = cv2.VideoCapture(0)

    finish = None
    while finish == None:
        success, img = cap.read()
        if not success:
            print("There seems to be an issue with the camera")
            break
        for barcode in decode(img):
            codes = barcode.data.decode('utf-8')
            print(codes)
            googleSearch(codes)
            finish = input("Finish scanning?(Y/N): ").lower().strip()
            if finish == 'y':
                break
            elif finish == 'n':
                finish = None
            else: 
                print("Sorry, what was that?")
                finish = None
        cv2.imshow('Result', img)
        cv2.waitKey(1)
              
   

# This can only scan images saved in the computer
def fileScan(image):
    os.chdir('/Users/jaliljusay/Documents')
    
    img = cv2.imread(f'{image}')
    code = decode(img)
    for barcode in code:
        upc = barcode.data.decode('utf-8')
    print(upc)
    googleSearch(upc)



def googleSearch(upc):
    
    links = []
    for link in search(upc, tld='co.in', num = 10, stop = 10, pause = 2):
        if 'openfoodfacts' in link:
            links.append(link)
    try:   
        finalLink = links[0]
    except IndexError:
        print("It seems there was an issue. Let's try scanning the item again")
        webcamScan()
    else:
        webScrape(finalLink)


def webScrape(url):

    s = HTMLSession()

    r = s.get(url)

    # Note to self: There's a huge difference btwn xpath and full xpath. The one in green is the FULL Xpath one.

    #servingSize = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/thead/tr/th[3]/text()[2]', first=True)
    #energyPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[1]/td[3]/text()[2]', first=True)
    #fatPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[2]/td[3]', first=True)
    #saturatedfatPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[3]/td[3]', first=True)
    #cholesterolPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[4]/td[3]', first=True)
    #carbsPerServing = r.html.xpath('//*[@id="nutriment_carbohydrates_tr"]/td[3]', first=True)
    #sugarsPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[6]/td[3]', first=True)
    #fibersPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[6]/td[3]', first=True)
    #proteinPerServing = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/tbody/tr[8]/td[3]', first=True)

    servingSize = r.html.xpath('/html/body/div/div/div/div[2]/div[4]/div[8]/div[2]/table/thead/tr/th[3]/text()[2]', first=True)
    energyPerServing = r.html.xpath('//*[@id="nutriment_energy_tr"]/td[3]/text()[2]', first=True)
    fatPerServing = r.html.xpath('//*[@id="nutriment_fat_tr"]/td[3]', first=True)
    saturatedfatPerServing = r.html.xpath('//*[@id="nutriment_saturated-fat_tr"]/td[3]', first=True)
    cholesterolPerServing = r.html.xpath('//*[@id="nutriment_cholesterol_tr"]/td[3]', first=True)
    carbsPerServing = r.html.xpath('//*[@id="nutriment_carbohydrates_tr"]/td[3]', first=True)
    sugarsPerServing = r.html.xpath('//*[@id="nutriment_sugars_tr"]/td[3]', first=True)
    fibersPerServing = r.html.xpath('//*[@id="nutriment_fiber_tr"]/td[3]', first=True)
    proteinPerServing = r.html.xpath('//*[@id="nutriment_proteins_tr"]/td[3]', first=True)

    
    try:
        if saturatedfatPerServing == None:
            saturatedfatPerServing = 'N/A'
        else:
            saturatedfatPerServing = saturatedfatPerServing.text

        if cholesterolPerServing == None:
            cholesterolPerServing = 'N/A'
        else:
            cholesterolPerServing = cholesterolPerServing.text

        if sugarsPerServing == None:
            sugarsPerServing = 'N/A'
        else:
            sugarsPerServing = sugarsPerServing.text

        fatPerServing = fatPerServing.text
        carbsPerServing = carbsPerServing.text
        fibersPerServing = fibersPerServing.text
        proteinPerServing = proteinPerServing.text
    except AttributeError:
        print("It seems you've scanned a nonfood/beverage item. Please try again with a food or beverage")
        webcamScan()
    else:
        d = {
            "Serving Size: ": servingSize,
            "Energy Per Serving: ": energyPerServing, # Idk why but it prints out the html version instead of the string version. Tried doing '.text' but it keeps giving errors unless i print()
            "Fat per Serving: ": fatPerServing,
            "Saturated Fat per serving: ": saturatedfatPerServing,
            "Cholesterol per serving: " : cholesterolPerServing,
            "Carbs per serving: ": carbsPerServing,
            "Sugars per serving: ": sugarsPerServing,
            "Fibers per serving: ": fibersPerServing,
            "Protein per serving: ": proteinPerServing
        }
    print(d)

def initiation():
    camOrNoCam = None
    while camOrNoCam == None:
        camOrNoCam = input('Would you like to use the webcam (type webcam) to scan or go from the files (must be in the Documents directory) in your computer? (type file): ').lower().strip()
        if camOrNoCam == 'webcam':
            webcamScan()
        elif camOrNoCam == 'file':
            file = input("Please enter file name: ").strip()
            fileScan(file)
        else:
            print('Sorry what was that?')
            camOrNoCam = None

# For good practice
if __name__ == '__main__':
    initiation()








