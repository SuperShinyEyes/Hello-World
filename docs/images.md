#### Crop images by pixels

```python
from PIL import Image

def crop_img(img):
  X = 200
  Y = 60
  WIDTH = 240
  HEIGHT = 320
  img = Image.open(img)
  # img2 = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  # img2.save("image_cropped.jpg")
  img_cropped = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  img_cropped.save('image_cropped.jpg')
  print img_cropped.size, '\n'
```

#### example
```python
```
