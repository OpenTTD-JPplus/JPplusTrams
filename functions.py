
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
    "door10" :  {"company" : "toyama", "folder" : "de5000", "tram" : "toyamade5000",},
}

for d in doors:
    sprite = Image.open("src/trams/" + doors[d]["company"] + "/" + doors[d]["folder"] + "/" + doors[d]["tram"] + "_doors.png")
    sprite.save("src/parts/doors/" + d + ".png")
    
# Stops

stops = {
    "kumamoto01" : {"city" : "kumamoto", "row" : 1, },
    "kumamoto02_both" : {"city" : "kumamoto", "row" : 1, },
    "kumamoto02_bttm" : {"city" : "kumamoto", "row" : 1, },
    "kumamoto02_solo" : {"city" : "kumamoto", "row" : 1, },
    "kumamoto02_topp" : {"city" : "kumamoto", "row" : 1, },
    "toyama01" : {"city" : "toyama", "row" : 1, },
    "overpass_1side_btm_both_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_1side_btm_both_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_1side_btm_north_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_1side_btm_north_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_1side_top_north_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_1side_top_north_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_both_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_both_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_north_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_north_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_south_noplatform" : {"city" : "overpass", "row" : 1, },
    "overpass_2sides_south_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_nontrack" : {"city" : "overpass", "row" : 1, },
    "overpass_nostairs_platform" : {"city" : "overpass", "row" : 1, },
    "overpass_nostairs_noplatform" : {"city" : "overpass", "row" : 1, },
}

for s in stops:
    r = stops[s]["row"]
    area = (0, 0 + (r-1) * 65, 261, 0 + r * 65 +1)
    img = Image.open("src/stops/" + stops[s]["city"] + "/" + s + ".png")
    sprite = img.crop(area)
    sprite.save("src/stops/" + stops[s]["city"] + "/" + s + ".png")