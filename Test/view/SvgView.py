from PyQt5.QtCore import QRectF, QFile, Qt, QSize
from PyQt5.QtGui import QImage, QPainter, QPen, QPaintEvent, QWheelEvent, QTransform
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

    def wheelEvent(self, event):
        self.__zoomBy(pow(1.2, event.angleDelta().y() / 240.0))

    def zoomFactor(self):
        return self.transform().m11()

    def __zoomBy(self, factor):
        currentZoom = self.zoomFactor()
        if factor < 1 and currentZoom < 0.1 or factor > 1 and currentZoom > 50:
            return
        self.scale(factor, factor)

    def zoomIn(self):
        self.__zoomBy(2)

    def zoomOut(self):
        self.__zoomBy(0.5)

    def resetZoom(self):
        if not self.zoomFactor() == 1.0:
            self.resetTransform()
            self._zoomChanged.emit()

    def setSize(self, width: float, height: float):
        self.setTransform(QTransform.fromScale(width / self.default_width, height / self.default_height))

    def setAngle(self, angle: float):
        self.rotate(angle)
