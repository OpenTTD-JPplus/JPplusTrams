[2022-08-30]
Bumped version to 0.9.3 in custom_tags.txt
Bumped version to 93 in moprv.nml

Fixed (item_hf2_box) 1957 Bufo Piece Goods Road Train not available, was missing climates_available.
    +    climates_available:             bitmask(CLIMATE_TEMPERATE, CLIMATE_ARCTIC, CLIMATE_TROPICAL);

Fixed the following six vehicles so they don't expire anymore.
    item_ie3_box (year 1970 "Kaimuki 6M Electric Boxcar Train") model_life and vehicle_life was swapped.
    item_ic3_box (year 2000 "Yarra 'Wharfie' Hybrid Boxcar Train") model_life and vehicle_life was swapped.
    item_ie3_flat (year 1970 "Yarra 'Magpie' Electric Flatbed Train") model_life and vehicle_life was swapped.
    item_ic3_flat (year 2000 "Kaimuki 4H Hybrid Flatbed Train") model_life and vehicle_life was swapped.
    item_ie3_open (year 1970 "KD E600 Electric Open Train") model_life and vehicle_life was swapped.
    item_ic3_open (year 2000 "Adelbrecht 500 Hybrid Open Train") model_life and vehicle_life was swapped.

    Same change on all six vehicles:
        - model_life:                     40;
        - vehicle_life:                   VEHICLE_NEVER_EXPIRES;
        + model_life:                     VEHICLE_NEVER_EXPIRES;
        + vehicle_life:                   40;

[2022-08-13]
Bumped version to 0.9.2 in custom_tags.txt
Bumped version to 92 in moprv.nml

Reverted CC change.
Reverted name change of Lupo Carelli t.1.
Fixed missing electricity icon on 1990 duNord 'Ox' Livestock Trolley Truck:
    - purchase:                   spriteset_mt3_stock;
    + purchase:                   switch_purchase_mt3_stock;

[2022-08-10]
Bumped version to 0.9.1 in custom_tags.txt
Bumped version to 91 in moprv.nml

Introduced optional earlier introduction year choice via parameter:
    // This new parameter is set to original values by default.
    Added new parameter (param 14) in moprv.nml for changing introduction year:
        // Used to change Steam Gen1 and Gen2 introduction years for earlier start.
        param 14 {
            param_fgei {
                name: string(STR_PARAM_NAME_FGEI);
                desc: string(STR_PARAM_DESC_FGEI);
                min_value: 0;
                max_value: 2;
                def_value: 0;
                names: {
                    0: string(STR_PARAM_FGEI_VALUE_ORIG);
                    1: string(STR_PARAM_FGEI_VALUE_1830);
                    2: string(STR_PARAM_FGEI_VALUE_1800);
                };
            }
        }
    Added new checks on Gen1 and Gen2 steam vehicles:
        Gen1 has both, Gen2 only has the second (year might differ due to some units having different intro date):
            + if (param_fgei == 1) {
            +     property {
            +     introduction_date:              date(1830,01,01);
            +     model_life:                     70;
            +     }
            + }
            + if (param_fgei == 2) {
            +     property {
            +     introduction_date:              date(1800,01,01);
            +     model_life:                     50;
            +     }
            + }
    Added new strings in english.lng for use with this parameter:
        + STR_PARAM_NAME_FGEI:Steam Vehicle Introduction Year
        + STR_PARAM_DESC_FGEI:This changes the introduction year of the Steam Vehicles.
        + STR_PARAM_FGEI_VALUE_ORIG: Use default introduction year 1860.
        + STR_PARAM_FGEI_VALUE_1830: Use alternative introduction year 1830.
        + STR_PARAM_FGEI_VALUE_1800: Use alternative introduction year 1800. Also changes 2nd Gen Steam to 1850.

[2022-08-10]
Bumped version to 0.9.0 in custom_tags.txt
Bumped version to 90 in moprv.nml

Fixed Dual-Mode vehicles not getting changed properties when running on electricity:
    This was changed by Brickblock1 in his upload. Kept intact in this version.

Added def_value:1 to all vehicle selection parameters so they are enabled by default when adding GRF to loadout.

Added CCTT_FUNC to tramtypetable to allow Cable Cars to fallback to RAIL if FUNC not available:
    - tramtypetable { RAIL, ELRL, FUNC }
    + tramtypetable { RAIL, ELRL, CCTT_FUNC: [FUNC, RAIL] }

Cable Cars:
    Changed item_f0_tram and item_f1_tram from tram_type FUNC to CCTT_FUNC.
    Added STR_CABLECAR_01 and STR_CABLECAR_02 in english.lng to give unique names to the cable cars.
    Modified statistics of both cable cars to try and balance them a bit.

Fixed names that assumedly lacked spacing in english.lng:
    - STR_SMOD_TMC:Bufo Motive Works'GP'
    + STR_SMOD_TMC:Bufo Motive Works 'GP'
    - STR_FMOD_BWB:Bufo Motive Works'B'
    + STR_FMOD_BWB:Bufo Motive Works 'B'
    - STR_FMOD_BWA:Bufo Motive Works'GP'
    + STR_FMOD_BWA:Bufo Motive Works 'GP'
    - STR_FMOD_BW1:Bufo Motive Works'GPII'
    + STR_FMOD_BW1:Bufo Motive Works 'GPII'
    - STR_CFMOD_BWB:Bufo Motive Works'C'
    + STR_CFMOD_BWB:Bufo Motive Works 'C'
    - STR_CFMOD_BWA:Bufo Motive Works'HP'
    + STR_CFMOD_BWA:Bufo Motive Works 'HP'
    - STR_CFMOD_BW1:Bufo Motive Works'GPII'
    + STR_CFMOD_BW1:Bufo Motive Works 'GPII'

Fixed assumed typo for STR_TMOD_LC1 in english.lng:
    - Lupo Carelli t.1
    + Lupo Carelli t.10

Fixed typo for STR_TMOD_LC2 in english.lng:
    - STR_TMOD_LC2:LUpo t.20
    + STR_TMOD_LC2:Lupo t.20

Changed speedratings of y2015, y2020 and y2025 busses:
    Earlier generations Normal/Articulated have been in sync, but these three generations were not.
    2015: Bufo Bus changed from 140km/h to 120km/h
    2020: duNord Trolley Bus changed from 120km/h to 140km/h
    2025: Both busses changed from 140km/h to 160km/h for a slight boost in the last generation.

Changed speedratings of y2030 and y2040 passenger trams:
    To keep these at same max speed as the last generation of busses, they are also changed from 140km/h to 160km/h.
