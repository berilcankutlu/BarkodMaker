import csv
import fileinput
import qrcode
from PIL import Image,ImageDraw,ImageFont
#modeli, macadresi ve urun kodu csvde olanlar icin
#kucuk barkod
logo = Image.open("angoralogo.png")
def barcode_maker(file):
    csv_file = csv.reader(file)
    csv_list = []
    csv_list.extend(csv_file)
    csvlist_iterator = iter(csv_list)
    next(csvlist_iterator)
    myFont =  ImageFont.truetype('Gotham-Book.otf', 20)
    for line in csvlist_iterator:
        temp = []
        for data in line:
            temp.append(data)
        model = temp[0]
        serial = temp[1]
        macaddress = temp[2]
        res = model + '\t' + serial + '\t' + macaddress
        image_data = Image.new('RGB', (700,200), color='white')
        ImageDraw.Draw(image_data).text((150,20), model, font=myFont, fill='black')
        ImageDraw.Draw(image_data).text((150, 50), serial, font=myFont, fill='black')
        ImageDraw.Draw(image_data).text((150, 80), macaddress, font=myFont, fill='black')
        image_qr = qrcode.make(res)
        imqr = image_qr.resize((150,150))
        imqr.paste(logo,(50,50))
        image_data.paste(imqr, (0, 0))
        image_data.save(str(serial) + '.png')

    del temp

barcode_maker(fileinput.input())