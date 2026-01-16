import easyocr

reader = easyocr.Reader(['en'],gpu=True)

def read_plate(img):
    result = reader.readtext(img)
    if len(result)==0:
        return ""
    return result[0][1]