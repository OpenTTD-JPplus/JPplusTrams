
from PIL import Image

# Pantos

pantos = {
    "panto04" :  {"company" : "toyama", "tram" : "t100", "row" : 2,},
}

for p in pantos:
    r = pantos[p]["row"]
    area = (0, 0 + (r-1) * 24, 248, 0 + r * 24 +1)
    #print("src/trams/" + pantos[p]["company"] + "/" + pantos[p]["tram"] + "/" + pantos[p]["tram"] + "_panto.png")
    img = Image.open("src/trams/" + pantos[p]["company"] + "/" + pantos[p]["tram"] + "/" + pantos[p]["tram"] + "_panto.png")
    sprite = img.crop(area)
    sprite.save("src/parts/pantos/" + p + ".png")

# Doors

doors = {
    "door07" :  {"company" : "toyama", "tram" : "t100",},
}

for d in doors:
    sprite = Image.open("src/trams/" + doors[d]["company"] + "/" + doors[d]["tram"] + "/" + doors[d]["tram"] + "_doors.png")
    sprite.save("src/parts/doors/" + d + ".png")
    