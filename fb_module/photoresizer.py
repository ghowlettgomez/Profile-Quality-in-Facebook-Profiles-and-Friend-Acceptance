from PIL import Image
from resizeimage import resizeimage
import urllib.request

class Photo_Resizer(object):

    def resizeimage(imgurl, path):
        urllib.request.urlretrieve(imgurl, path + "/imageForResizing.jpg")

        with open(path + '/imageForResizing.jpg', 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [100, 100])
                cover.save(path + '/resizedImage.jpg', image.format)
