import qrcode
import qrcode.constants
import qrcode.image.svg
import os

class Generator:
    def __init__(self, name:str, data:str, boxSize:str = '20', border:str = '2', fill_color:str = 'black', back_color:str = 'white', png = True, svg = False):
        self.format =  '.png' if ( png and not(svg) ) else '.svg'         
        self.name = name + self.format
        self.data = data

        self.boxSize = boxSize
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color
        
        self.qr = self.__config()

    def verificate_nameFormat(self):
        pass

    def __config(self):

        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.boxSize,
            border = self.border
        )
        qr.add_data(self.data)
        qr.make(fit = True)
        
        return qr

    def generate(self):
        if(self.format == '.png'):
            img = self.qr.make_image(fill_color = self.fill_color, back_color = self.back_color)

        elif(self.format == '.svg'):
            img = self.qr.make_image(image_factory=qrcode.image.svg.SvgPathImage, fill_color=self.fill_color, back_color=self.back_color)
        
        else:
            raise ValueError("Unsupported format. Use 'png' or 'svg'.")

        img.save(self.name)

    def delete(self):
        try:
            if os.path.exists(self.name):
                os.remove(self.name)
                print(f"File {self.name} deleted successfully")
            else:
                print(f"File {self.name} does not exist")
        except Exception as e:
            print(f"Error deleting file {self.name}: {e}")
        finally:
            del self

a = Generator("wikiSteamR", "https://es.wikipedia.org/wiki/Steam" , fill_color="#FF00FF")
a.generate()