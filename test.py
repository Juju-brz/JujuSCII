from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QPushButton, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de boutons sur une ligne")
        self.setGeometry(100, 100, 400, 200)

        # Widget central et layout principal (vertical)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Ajoute un label pour l'exemple
        main_layout.addWidget(QLabel("Exemple de boutons sur une ligne :"))

        # Crée un layout horizontal pour les boutons
        button_layout = QHBoxLayout()

        # Ajoute 3 boutons au layout horizontal
        button1 = QPushButton("Bouton 1")
        button2 = QPushButton("Bouton 2")
        button3 = QPushButton("Bouton 3")

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        # Ajoute le layout horizontal au layout principal
        main_layout.addLayout(button_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()