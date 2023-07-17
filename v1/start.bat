@echo off
title Fluxus Key Bypass
color d
echo To get your HWID, click on the "Get Key" button in the app, and copy the data from the HWID query &echo.
echo Keep in mind, each HWID has it's own Key &echo.
echo Example: https://flux.li/windows/start.php?HWID=XXXX (Copy all XXXX) &echo. &echo.
set /p hwid=Enter Your HWID: 
cls
color C
node index.js %hwid%
pause