import cv2
import numpy as np


def read_unicode_image(path, gray=1):
    """read unicode image"""
    stream = open(path, "rb")
    byte_array = bytearray(stream.read())
    numpy_array = np.asarray(byte_array, dtype=np.uint8)
    image = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    image = np.array(image)
    if gray == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    stream.close()
    return image


def show(img, name="disp", width=1000):
    """
    name: name of window, should be name of img
    img: source of img, should in type ndarray
    """
    cv2.namedWindow(name, cv2.WINDOW_GUI_EXPANDED)
    cv2.resizeWindow(name, width, 1000)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


