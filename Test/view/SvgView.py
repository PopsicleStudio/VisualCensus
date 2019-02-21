from PyQt5.QtCore import QRectF, QFile, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPainter, QPen, QPaintEvent, QTransform, QMouseEvent
from PyQt5.QtOpenGL import QGLFormat, QGLWidget, QGL
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QWidget


class SvgView(QGraphicsView):
    Native, OpenGL, Image = range(3)

    def __init__(self, parent=None):
        super(SvgView, self).__init__(parent)

        self.renderer = SvgView.Native
        self.svgItem = None
        self.backgroundItem = None
        self.image = QImage()
        self.default_width = 0
        self.default_height = 0
        self.clicked_event = pyqtSignal(QMouseEvent)

        self.__tf_rotate = QTransform()
        self.__tf_scale = QTransform()

        self.setScene(QGraphicsScene(self))

    def drawBackground(self, p: QPainter, rect: QRectF):
        p.save()
        p.resetTransform()
        p.drawTiledPixmap(self.viewport().rect(), self.backgroundBrush().texture())
        p.restore()

    def openFile(self, svg_file: QFile):
        if not svg_file.exists():
            return

        if self.backgroundItem:
            drawBackground = self.backgroundItem.isVisible()
        else:
            drawBackground = False

        s = self.scene()
        s.clear()
        self.resetTransform()

        self.svgItem = QGraphicsSvgItem(svg_file.fileName())
        self.svgItem.setFlags(QGraphicsItem.ItemClipsToShape)
        self.svgItem.setCacheMode(QGraphicsItem.NoCache)
        self.svgItem.setZValue(0)
        tmp = self.svgItem.renderer().defaultSize()
        self.default_width = tmp.width()
        self.default_height = tmp.height()

        self.backgroundItem = QGraphicsRectItem(self.svgItem.boundingRect())
        self.backgroundItem.setBrush(Qt.white)
        self.backgroundItem.setPen(QPen(Qt.NoPen))
        self.backgroundItem.setVisible(drawBackground)
        self.backgroundItem.setZValue(-1)

        s.addItem(self.backgroundItem)
        s.addItem(self.svgItem)

    def setRenderer(self, renderer):
        self.renderer = renderer

        if self.renderer == SvgView.OpenGL:
            if QGLFormat.hasOpenGL():
                self.setViewport(QGLWidget(QGL.SampleBuffers))
        else:
            self.setViewport(QWidget())

    def setHighQualityAntialiasing(self, highQualityAntialiasing):
        if QGLFormat.hasOpenGL():
            self.setRenderHint(QPainter.HighQualityAntialiasing, highQualityAntialiasing)

    def setViewBackground(self, enable):
        if self.backgroundItem:
            self.backgroundItem.setVisible(enable)

    def paintEvent(self, event: QPaintEvent):
        if self.renderer == SvgView.Image:
            if self.image.size() != self.viewport().size():
                self.image = QImage(self.viewport().size(), QImage.Format_ARGB32_Premultiplied)

            imagePainter = QPainter(self.image)
            QGraphicsView.render(self, imagePainter)
            imagePainter.end()

            p = QPainter(self.viewport())
            p.drawImage(0, 0, self.image)
        else:
            super(SvgView, self).paintEvent(event)

    def _setSize(self, width: float, height: float):
        self.__tf_scale = QTransform.fromScale(width / self.default_width, height / self.default_height)
        self.__tf()

    def _setAngle(self, angle: float):
        self.__tf_rotate = QTransform().rotate(angle)
        self.__tf()

    def __tf(self):
        self.setTransform(self.__tf_rotate * self.__tf_scale)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.clicked_event.emit(event)
