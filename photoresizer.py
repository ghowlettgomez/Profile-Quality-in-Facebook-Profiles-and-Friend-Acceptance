from PIL import Image
from resizeimage import resizeimage
import urllib.request

def resizeimage(imgurl):
    urllib.request.urlretrieve(imgurl, "imageForResizing.jpg")

    with open('imageForResizing.jpg', 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [100, 100])
            cover.save('resizedImage.jpg', image.format)
