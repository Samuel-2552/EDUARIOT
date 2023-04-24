import easyocr

reader = easyocr.Reader(['en'])
img = 'Castle.jpg'
results = reader.readtext(img)
for result in results:
    print(result[1])
