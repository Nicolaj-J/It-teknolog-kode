import cv2
from pyzbar.pyzbar import decode
from gpiozero import Buzzer

buzzer = Buzzer(20) #instance af buzzer klassen

def barcode_read():
    cam = cv2.VideoCapture(0) #instance af videocapture klassen
    cam.set(3,640) # width is 3 (plads, pixel størrelse) definere størrelsen af billedet den tager
    cam.set(4,480) # Height is 4 (plads, pixel størrelse) definere størrelsen af billedet den tager
    while True:
        success, img = cam.read()
        if not decode(img):
            print("No barcode detected")
            pass
        else:
            buzzer.on()
            for barcode in decode(img):
                barcode_data = barcode.data.decode('utf-8')
                cam.release()
                #cv2.destroyAllWindows()
                buzzer.off()
                return barcode_data
                #break
                
        
    
        #cv2.imshow('Result',img)
        #cv2.waitKey(1)