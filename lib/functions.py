
import pandas as pd
import numpy as np
import json, os
from PIL import Image

def ExportToJSON(dictionary, target_file):
    with open(target_file, 'w') as fp:
        json.dump(dictionary, fp, indent=4)

def LoadJSON(target_file):
    with open(target_file, 'r') as file:
        data = json.load(file)
    return data

def VisualEffect(x):
    if x['Parts'] == 1:
        return "VISUAL_EFFECT_ELECTRIC"
    else:
        return "sw_spark_on_" + str(int((x['Panto_Location'])))

def CargoCapacity(x):
    if x['Parts'] == 1:
        return str(x['Cargo_Capacity'])
    else:
        return str(x['Cargo_Capacity']) + " / " + str(x['Parts'])

def ModelLife(x):
    if x['Model_Life'] == 0:
        return 'VEHICLE_NEVER_EXPIRES'
    else:
        return str(x['Model_Life'])

def ArticulatedPart(x):
    if x['Parts'] == 1:
        return '<delete>'
    else:
        return 'sw_' + x['Tram'] + '_articulated_part'

def CreateTramsJSON():
    # Trams

    # convert excel spreadsheet into dataframe
    df_trams = pd.read_excel('docs/jpplustrams.ods','trams', 
        usecols=['Tram', 'ID', 'City', 'Folder', 'Include', 'Name', 'Description', 'Speed', 'Intro', 'Weight', 'Cargo_Capacity', 'Power', 'Model_Life', 'Vehicle_Life', 'Cost_Factor', 'Running_Cost_Factor', 'Cargo_Age_Period', 'Length', 'Parts', 'Panto_Location', 'Loading_Speed'],
        converters={'Tram':str,'Folder':str,'Intro':str, 'Cargo_Capacity':str, 'Vehicle_Life':str, 'Cost_Factor':str, 'Cargo_Age_Period':str, 'Length':str, 'Loading_Speed':str})
    
    # filter out trams not to include
    df_trams = df_trams[(df_trams['Include']==True)]

    # convert stats into nml code
    df_trams['Intro_Date'] = 'date(' + df_trams['Intro'].str[:10].replace('-',',', regex=True) + ')'
    df_trams['Cargo_Capacity'] = '(param_capacity * ' + df_trams.apply(CargoCapacity, axis=1) + ' ) / 2'
    df_trams['Purchase_Cargo_Capacity'] = df_trams['Cargo_Capacity']
    df_trams['Cost_Factor'] = '((param_buycost * ' + df_trams['Cost_Factor'] + ' ) / 4 )'
    df_trams['Name'] = 'string(' + df_trams['Name'] + ')'
    df_trams['Articulated_Part'] = df_trams.apply(ArticulatedPart, axis=1)
    df_trams['Operator'] = df_trams['City'].str.upper()
    df_trams['Additional_Text'] = 'string(STR_CONCAT_4, string(OPERATORS),string(' + df_trams['Operator'] + '),string(LIVERIES),string(' + df_trams['Description'] + '))'
    df_trams[['Running_Cost_Factor_A', 'Running_Cost_Factor_B']] = df_trams['Running_Cost_Factor'].str.split(',', expand=True)
    df_trams['Running_Cost_Factor'] = df_trams['Running_Cost_Factor_A'] + ' + ((param_runcost * ' + df_trams['Running_Cost_Factor_B'] + ' ) / 2 ) * RunningCostFactor()'
    df_trams['Purchase_Running_Cost_Factor'] = df_trams['Running_Cost_Factor_A'] + ' + ((param_runcost * ' + df_trams['Running_Cost_Factor_B'] + ' ) / 2 )'
    df_trams['Default'] = 'sw_' + df_trams['Tram'] + '_stack'
    df_trams['Purchase'] = 'sw_' + df_trams['Tram'] + '_purchase'
    df_trams['Cargo_Age_Period'] = 'sw_cargo_age_period_' + df_trams['Cargo_Age_Period'].str.zfill(2)
    df_trams['Cargo_Subtype_Text'] = 'sw_' + df_trams['Tram'] + '_subtype_text'
    df_trams['Climates_Available'] = 'bitmask(CLIMATE_TEMPERATE, CLIMATE_ARCTIC, CLIMATE_TROPICAL)'
    df_trams['Refittable_Cargo_Classes'] = 'bitmask(CC_PASSENGERS)'
    df_trams['Visual_Effect'] = df_trams.apply(VisualEffect, axis=1)
    df_trams['Sound_Effect'] = 'SOUND_POWER_STATION'
    df_trams['Running_Cost_Base'] = 'RUNNING_COST_ROADVEH'
    df_trams['Reliability_Decay'] = '14'
    df_trams['Refit_Cost'] = '0'
    df_trams['Tram_Type'] = 'ELRL'
    df_trams['Misc_Flags'] = 'bitmask(ROADVEH_FLAG_2CC, ROADVEH_FLAG_AUTOREFIT, ROADVEH_FLAG_TRAM, ROADVEH_FLAG_SPRITE_STACK)'
    df_trams['Sprite_ID'] = 'SPRITE_ID_NEW_ROADVEH'
    df_trams['Model_Life'] = df_trams.apply(ModelLife, axis=1)
    
    df_trams = df_trams.drop(columns=['Include', 'Intro', 'Description', 'Operator', 'Running_Cost_Factor_A', 'Running_Cost_Factor_B'])

    #print(df_trams[['Tram', 'Speed', 'Intro_Date']])
    #print(df_trams.dtypes)
    
    # convert dataframe into dictionary
    trams_dict = df_trams.set_index('Tram').T.to_dict('dict')

    ExportToJSON(trams_dict, 'lib/trams.json')

    with open('lib/trams.json', 'r') as input:
        with open('lib/trams_temp.json', 'w' ) as output:
            for line in input:
                if "<delete>" not in line.strip('\n'):
                    output.write(line)
    os.replace('lib/trams_temp.json', 'lib/trams.json')

    # Pantos

    df_panto = pd.read_excel('docs/jpplustrams.ods','trams', usecols=['Tram', 'City', 'Folder', 'Panto', 'Panto_Location'],converters={'Tram':str,'Folder':str})
    df_panto = df_panto.query('Panto != "user"')
    panto_dict = df_panto.set_index('Panto').T.to_dict('dict')

    ExportToJSON(panto_dict, 'lib/panto.json')

    # Doors

    df_doors = pd.read_excel('docs/jpplustrams.ods','trams', usecols=['Tram', 'City', 'Folder', 'Doors'],converters={'Tram':str,'Folder':str})
    df_doors = df_doors.query('Doors != "user"')
    doors_dict = df_doors.set_index('Doors').T.to_dict('dict')

    ExportToJSON(doors_dict, 'lib/doors.json')

    # Stops

    # convert excel spreadsheet into dataframe
    df_stops = pd.read_excel('docs/jpplustrams.ods','stops', usecols=['Stop', 'City', 'Row'])
    # convert dataframe into dictionary
    stops_dict = df_stops.set_index('Stop').T.to_dict('dict')

    ExportToJSON(stops_dict, 'lib/stops.json')

def SortTrams():

    trams = LoadJSON('lib/trams.json')

    with open('src/vehicleid.pnml', 'w') as f:
        f.write('\n// Tram ID Allocation\n')
        for t in trams:
            name_length = len(t)
            if name_length <= 1:
                padding = '\t\t\t\t'
            elif 2 <= name_length <= 5:
                padding = '\t\t\t'          
            elif 6 <= name_length <= 8:
                padding = '\t\t'
            else:
                padding = '\t'
            id_length = len(str(trams[t]['ID']))
            if id_length == 1:
                padding2 = '  ) {}\n'
            else:
                padding2 = ' ) {}\n'
            f.write('item(FEAT_ROADVEHS, item_' + t + ','+ padding + str(trams[t]['ID']) + padding2)
        f.write('\n// Sort Order in Menu\nsort(FEAT_ROADVEHS, [\n')
        
        # write IDs to sort
        cities = []
        for t in trams:
            city = trams[t]["City"].capitalize()
            cities.append(city)
            x = cities.count(city)
            if x == 1:
                f.write('\n// ' + city + '\n')
            f.write(str(trams[t]['ID']) + ',\t// ' + trams[t]["Intro_Date"][5:9] + ' ' + t + '\n')

        f.write(']);\n')
        f.close()

def TransferPantos():
    pantos = LoadJSON('lib/panto.json')
    for p in pantos:
        r = int(pantos[p]["Panto_Location"])
        area = (0, 0 + (r-1) * 24, 248, 0 + r * 24 +1)
        #print("src/trams/" + pantos[p]["company"] + "/" + pantos[p]["tram"] + "/" + pantos[p]["tram"] + "_panto.png")
        img = Image.open("src/trams/" + pantos[p]["City"] + "/" + pantos[p]["Folder"] + "/" + pantos[p]["Tram"] + "_panto.png")
        sprite = img.crop(area)
        sprite.save("src/parts/pantos/" + p + ".png")

def TransferDoors():
    doors = LoadJSON('lib/doors.json')
    for d in doors:
        sprite = Image.open("src/trams/" + doors[d]["City"] + "/" + doors[d]["Folder"] + "/" + doors[d]["Tram"] + "_doors.png")
        sprite.save("src/parts/doors/" + d + ".png")

def CropStops():
    stops = LoadJSON('lib/stops.json')
    for s in stops:
        r = stops[s]["Row"]
        area = (0, 0 + (r-1) * 65, 261, 0 + r * 65 +1)
        img = Image.open("src/stops/" + stops[s]["City"] + "/" + s + ".png")
        sprite = img.crop(area)
        sprite.save("src/stops/" + stops[s]["City"] + "/" + s + ".png")

def UpdateStats():
    trams = LoadJSON('lib/trams.json')
    schema = LoadJSON('lib/schema.json')

    for t in trams:
        for s in schema:
            new_lines = []

            with open('src/trams/' + trams[t]["City"] + '/' + trams[t]["Folder"] + '/' + t + '.pnml', 'r') as file:
                lines = file.readlines()
            keys = list(schema[s].keys())

            # Ignore string exists for this stat
            if 'ignore_string' in keys:
                for line in lines:
                    if schema[s]["search_string"] in line and schema[s]['ignore_string'] not in line:
                        new_lines.append(schema[s]['return_string'].replace("<stat>",trams[t][s]))
                        new_lines.append(';')
                        if 'comment' in keys:
                            new_lines.append(schema[s]["comment"])
                        new_lines.append('\n')
                    else:
                        new_lines.append(line)

            # No ignore string for this stat
            else:
                for line in lines:
                    if schema[s]['search_string'] in line:
                        new_lines.append(schema[s]['return_string'].replace("<stat>",trams[t][s]))
                        new_lines.append(';')
                        if 'comment' in keys:
                            new_lines.append(schema[s]["comment"])
                        new_lines.append('\n')
                    else:
                        new_lines.append(line)

    
            with open('src/trams/' + trams[t]["City"] + '/' + trams[t]["Folder"] + '/' + t + '.pnml', 'w') as file:
                file.writelines(new_lines)
                file.close()
