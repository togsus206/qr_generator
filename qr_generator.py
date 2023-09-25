import qrcode 
from PIL import Image

while True:
    try:
        info = input("De el texto a covertir en qr o elija salir: ")
        
        if info.lower() == "salir":
            break
            
        #Generador del codigo
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(info)
        qr.make(fit=True)


        #Crear la imagen desde el qr
        qr_code = qr.make_image(fill = "black", back_color="white")

        #Guardar y abrir
        qr_code.save("mi_codigo.png")
        qr_code.show()
        
    except Exception as e:
        print("Hubo un problema con el link/links pasado:", str(e))          
