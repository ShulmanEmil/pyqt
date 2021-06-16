import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    colorChanged = pyqtSignal()

    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600
        # Window size

        self.setWindowTitle('Paint Application')
        self.setGeometry(top, left, width, height)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        # Set a picture

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self._color = None
        # Settings

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        brushMenu = mainMenu.addMenu('Brush Size')
        # Set menu

        colorAction = QAction(QIcon('color.png'), 'Color', self)
        colorAction.triggered.connect(self.onColorPicker)
        # Color selection

        eraserAction = QAction(QIcon('eraser.png'), 'Eraser', self)
        eraserAction.triggered.connect(self.onEraserPicker)
        # Set eraser

        self.toolbar = self.addToolBar('Eraser')
        self.toolbar.addAction(eraserAction)
        self.toolbar = self.addToolBar('Color')
        self.toolbar.addAction(colorAction)
        # Set toolbar

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        # Save

        clearAction = QAction('Clear', self)
        clearAction.setShortcut('Ctrl+C')
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        # Clear

        threepxAction = QAction('3px', self)
        threepxAction.setShortcut('Ctrl+T')
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction('5px', self)
        fivepxAction.setShortcut('Ctrl+F')
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction('7px', self)
        sevenpxAction.setShortcut('Ctrl+S')
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction('9px', self)
        ninepxAction.setShortcut('Ctrl+N')
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)
        # Size selection

    def onColorPicker(self):
        """Color change function"""

        dlg = QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QColor(self._color))

        if dlg.exec_():
            color = QColor(0, 0, 0)
            color.setNamedColor(dlg.currentColor().name())
            self.brushColor = color

    def onEraserPicker(self):
        """Eraser Function"""

        self.brushColor = Qt.white

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize,
             Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "PNG Image file (*.png)")
        if path == '':
            return
        self.image.save(path)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
