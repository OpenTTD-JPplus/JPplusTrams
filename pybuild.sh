#!/bin/bash
python nml_patcher.py -f "JPplusTrams.pnml" -o "JPplusTrams.nml" -b 0 -v 1
nmlc JPplusTrams.nml -o JPplusTrams.grf -c -t src/custom_tags.txt -l src/lang
python move_grf.py
