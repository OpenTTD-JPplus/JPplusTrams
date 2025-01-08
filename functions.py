
from PIL import Image

# Pantos

pantos = {
    "panto04" :  {"company" : "toyama", "folder" : "t100", "tram" : "t100", "row" : 2,},
    "panto05" :  {"company" : "toyama", "folder" : "8000", "tram" : "toyama8000", "row" : 1,},
}

for p in pantos:
    r = pantos[p]["row"]
    area = (0, 0 + (r-1) * 24, 248, 0 + r * 24 +1)
    #print("src/trams/" + pantos[p]["company"] + "/" + pantos[p]["tram"] + "/" + pantos[p]["tram"] + "_panto.png")
    img = Image.open("src/trams/" + pantos[p]["company"] + "/" + pantos[p]["folder"] + "/" + pantos[p]["tram"] + "_panto.png")
    sprite = img.crop(area)
    sprite.save("src/parts/pantos/" + p + ".png")

# Doors

doors = {
    "door07" :  {"company" : "toyama", "folder" : "t100", "tram" : "t100",},
    "door08" :  {"company" : "toyama", "folder" : "8000", "tram" : "toyama8000",},
    "door09" :  {"company" : "toyama", "folder" : "7000", "tram" : "toyama7000",},
}

for d in doors:
    sprite = Image.open("src/trams/" + doors[d]["company"] + "/" + doors[d]["folder"] + "/" + doors[d]["tram"] + "_doors.png")
    sprite.save("src/parts/doors/" + d + ".png")
    