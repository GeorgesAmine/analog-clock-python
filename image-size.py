from PIL import Image
filename="./assets/watch-bg2.jpg"
with Image.open(filename) as img:
    w = img.size[0]
    h = img.size[1]

print(w)
print(h)
print(str(w)+"x"+str(h))