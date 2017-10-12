@echo off
pip freeze > requirements.temp
pex -r ./requirements.temp -o ./Distributable/Environment.pex
del .\requirements.temp
copy .\Input\*.py .\Distributable\