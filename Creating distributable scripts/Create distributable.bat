@echo off
pex -r ./Input/requirements.txt -o ./Distributable/Environment.pex
copy .\Input\*.py .\Distributable\