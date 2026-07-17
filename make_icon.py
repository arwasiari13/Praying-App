from PIL import Image, ImageDraw

S = 256
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# rounded-square background, deep green
d.rounded_rectangle([8, 8, S - 8, S - 8], radius=56, fill=(15, 42, 33, 255))

# gold crescent: big circle minus offset circle
gold = (212, 175, 106, 255)
d.ellipse([52, 52, 204, 204], fill=gold)
d.ellipse([84, 44, 220, 180], fill=(15, 42, 33, 255))

# small star
star_cx, star_cy, r = 170, 150, 16
import math
pts = []
for i in range(10):
    ang = math.pi / 2 + i * math.pi / 5
    rad = r if i % 2 == 0 else r * 0.45
    pts.append((star_cx + rad * math.cos(ang), star_cy - rad * math.sin(ang)))
d.polygon(pts, fill=gold)

img.save("build/icon.png")
img.save("build/icon.ico",
         sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("icon written")
