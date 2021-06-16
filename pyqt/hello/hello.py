import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    # Initialization

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110, 85)
    # Label and text

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("Hello World App")
    widget.show()
    sys.exit(app.exec_())
    # Show window


if __name__ == '__main__':
    window()
