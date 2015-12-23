from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 500 * 1
height = 500
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 画圆:
for x in range(width):
    for y in range(height):
        if (x-250)**2 + (y-250)**2 <= 200**2:
            draw.point((x, y), fill=(255,255,0))
        if (x-250)**2 + (y-250)**2 <= 100**2:
            draw.point((x, y), fill=(255,255,255))


# 储存：
image.save('code1.jpg', 'jpeg')