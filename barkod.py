import csv
import fileinput
import qrcode
from PIL import Image,ImageDraw,ImageFont
import sys
#modeli, macadresi ve urun kodu csvde olanlar icin
logo = Image.open("angoralogo.png")
ce_logo = Image.open("celogo.png")
myFont = ImageFont.truetype('Gotham-Book.otf', 70)
myFont2 = ImageFont.truetype('Gotham-Book.otf', 60)

def barcode_maker(file):
    csv_file = csv.reader(file)
    csv_list = []
    csv_list.extend(csv_file)
    csvlist_iterator = iter(csv_list)
    next(csvlist_iterator)
    sec = raw_input("[K]ucuk etiket mi? [B]uyuk Etiket mi? [I]kiside mi?").lower()
    for line in csvlist_iterator:
    	print("new line")
        temp = []
        for data in line:
            temp.append(data)
        model = temp[0]
        serial = temp[1]
        macaddress = temp[2]
        res = model + '\t' + serial + '\t' + macaddress
        if sec in '':
    		print ("\nBir secim yapin\n")
        	barcode_maker(fileinput.input())
        
        elif sec in 'b':
            image_data = Image.new('RGB', (2000, 1000), color='white')
            ImageDraw.Draw(image_data).text((50, 50), model, font=myFont, fill='black')
            ImageDraw.Draw(image_data).text((50, 150), serial, font=myFont, fill='black')
            ImageDraw.Draw(image_data).text((50, 250), macaddress, font=myFont, fill='black')
            ImageDraw.Draw(image_data).text((1000, 170), 'ANGORA', font=myFont2, fill='black')
            ImageDraw.Draw(image_data).text((1000, 240), 'NETWORKS', font=myFont2, fill='black')
            image_qr = qrcode.make(res)
            imqr = image_qr.resize((600, 600))
            #imqr.paste(logo, (50, 50))
            image_data.paste(ce_logo, (50, 400))
            image_data.paste(logo, (800, 150))
            image_data.paste(imqr, (800, 350))
            image_data.save(str(serial) + 'B' + '.png')
        elif sec in 'k':
            image_data = Image.new('RGB', (1500, 800), color='white')
            ImageDraw.Draw(image_data).text((520, 100), model, font=myFont2, fill='black')
            ImageDraw.Draw(image_data).text((520, 220), serial, font=myFont2, fill='black')
            ImageDraw.Draw(image_data).text((520, 340), macaddress, font=myFont2, fill='black')
            image_qr = qrcode.make(res)
            imqr = image_qr.resize((500, 500))
            #imqr.paste(logo, (550, 350))
            image_data.paste(imqr, (0, 0))
            image_data.save(str(serial) + 'K' + '.png')
        elif sec in 'i':
            image_datab = Image.new('RGB', (2000, 1000), color='white')
            image_datak = Image.new('RGB', (1500, 800), color='white')
            ImageDraw.Draw(image_datab).text((50, 50), model, font=myFont, fill='black')
            ImageDraw.Draw(image_datab).text((50, 150), serial, font=myFont, fill='black')
            ImageDraw.Draw(image_datab).text((50, 250), macaddress, font=myFont, fill='black')
            ImageDraw.Draw(image_datak).text((650, 50), model, font=myFont, fill='black')
            ImageDraw.Draw(image_datak).text((650, 150), serial, font=myFont, fill='black')
            ImageDraw.Draw(image_datak).text((650, 250), macaddress, font=myFont, fill='black')
            image_qrb = qrcode.make(res)
            imqrb = image_qrb.resize((600, 600))
            imqrb.paste(logo, (250, 250))
            image_datab.paste(ce_logo, (50, 400))
            image_datab.paste(imqrb, (800, 350))
            image_qrk = qrcode.make(res)
            imqrk = image_qrk.resize((600, 600))
            imqrk.paste(logo, (250, 250))
            image_datak.paste(imqrk, (0, 0))
            image_datab.save(str(serial) + 'B' + '.png')
            image_datak.save(str(serial) + 'K' + '.png')

        else:
        	print ("\nyanlis secim oldu\n")
        	barcode_maker(fileinput.input())
            #sys.stdout.write("Kucuk etiket / Buyuk etiket / Ikiside secimi yapin")


barcode_maker(fileinput.input())
