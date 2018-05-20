from PIL import Image
from resizeimage import resizeimage
import urllib

urllib.urlretrieve("https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/p320x320/20292856_1642847895760348_8618985146905580226_n.jpg?_nc_cat=0&oh=b5e33ae0ff7fbe5d9794fc44431a7b5b&oe=5B7F4099", "imageForResizing.jpg")

with open('imageForResizing.jpeg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [100, 100])
        cover.save('resizedImage.jpg', image.format)
