""""
Signed Juju
This Code convert your image to ASCII image
/Example/Example.png

ok good
"""
from PIL import Image
import PySide6.QtWidgets
from PySide6.QtWidgets import QLabel, QDialog, QPushButton, QVBoxLayout, QLineEdit, QTextEdit, QWidget


####    ASCII   ####
def convert_image_to_ASCII(path):
    myImage = Image.open(path)
    #myImage.show()
    myCharacter = ""
    myImg_in_grscal = myImage.convert("L")
    LittlemyImg_in_grscal = myImg_in_grscal.resize([100, 100])
    #myImg_in_grscal.show()

    Weight = LittlemyImg_in_grscal.size[0]
    Height = LittlemyImg_in_grscal.size[1]


    #### LOOP   ####
    for y in range(Height):
        for x in range(Weight):
            pixel_intensity = LittlemyImg_in_grscal.getpixel([x, y])

            if pixel_intensity >= 0 and pixel_intensity <51:
                character = " "
            elif pixel_intensity >= 51 and pixel_intensity <102:
                character = "."
            elif pixel_intensity >= 102 and pixel_intensity <153:
                character = "o"
            elif pixel_intensity >= 153 and pixel_intensity <204:
                character = "0"
            elif pixel_intensity >= 204 and pixel_intensity <255:
                character = "@"

            myCharacter += character
        myCharacter += "\n"

    return myCharacter
    
    

#####    GUI    #####

app = PySide6.QtWidgets.QApplication()
#app = QApplication()

layoutWindow = QVBoxLayout()

mainWindow = QDialog()
mainWindow.setLayout(layoutWindow)
mainWindow.show()
mainWindow.resize(1200, 1000)

label = QLabel(text=" Enter path of image to convert")
champ_text = QLineEdit()


button_convert = QPushButton(text="CONVERT")
result_ascii = QTextEdit()

input = QLineEdit()
input.returnPressed.connect(button_convert.click)

ASCII_button = QPushButton(text="ASCII")

mainWindow.setWindowTitle("JujuSCII")
layoutWindow.addWidget(label)
layoutWindow.addWidget(champ_text)
layoutWindow.addWidget(ASCII_button)
layoutWindow.addWidget(button_convert)
layoutWindow.addWidget(result_ascii)

def clickConvert():
    file_Path = champ_text.text()
    imageASCII = convert_image_to_ASCII(file_Path)
    result_ascii.setText(imageASCII)

button_convert.clicked.connect(clickConvert)


#### Tool Window #####

def ToolASCII():
    toolWindow = QDialog()
    toolWindow.show()
    return 0

ASCII_button.clicked.connect(ToolASCII)

result_ascii.setFontFamily("Liberation Mono")
app.exec()

