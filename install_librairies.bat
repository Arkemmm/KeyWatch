@echo off

REM Mettre à jour pip
py -m pip install --upgrade pip

REM Installation des bibliotheques...
py -m pip install pywin32
py -m pip install keyboard

REM Verification...
if %errorlevel% neq 0 (
    color 0a
    echo Une erreur est survenue.
) else (
    color 0f
    echo Installation des bibliotheques Python reussi !
)

pause
