from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage,QPainter
from PySide6.QtCore import Qt
import cv2
from src.global_params import camera_config_params

class VideoGraphicsView(QGraphicsView):
    def __init__(self,parent=None):
        super().__init__(parent)

        #add scene 
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)

        #add pixmap to scene
        self.pixmap_item = QGraphicsPixmapItem()
        self._scene.addItem(self.pixmap_item)

        #turn on Antialiasing
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        
        self._zoom = 0
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # Cho phép kéo ảnh

    def cv2_to_qimage(self,cv_img):
        if isinstance(cv_img,str):
            cv_img = cv2.imread(cv_img)
        height, width, channel = cv_img.shape
        bytes_per_line = 3 * width
        return QImage(cv_img.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
    
    def setImage(self, qimage):
        if self._zoom < 0:
            self._zoom = 0
        qimage = self.cv2_to_qimage(qimage)
        pixmap = QPixmap.fromImage(qimage)
        self.pixmap_item.setPixmap(pixmap)
        self.setSceneRect(pixmap.rect())

        if self._zoom == 0:
                self.fitInView(self.pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)


    def wheelEvent(self, event):
        # Zoom theo bánh xe chuột
        zoom_in_factor = camera_config_params.zoom_in_factor
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
            self._zoom += 1
        else:
            zoom_factor = zoom_out_factor
            self._zoom -= 1

        if self._zoom < -10:
            self._zoom = -10
            return
        if self._zoom > 20:
            self._zoom = 20
            return

        self.scale(zoom_factor, zoom_factor)
