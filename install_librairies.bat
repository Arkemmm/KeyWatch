@echo off
setlocal EnableDelayedExpansion

REM Define colors and styles
set "color_normal=0f"
set "color_error=0c"
set "color_success=0a"
set "style_separator=----------------------------------------"

REM Clear the screen
cls

REM Update pip
echo Updating pip...
py -m pip install --upgrade pip > nul 2>&1

REM Install libraries
echo Installing libraries...
py -m pip install pywin32 > nul 2>&1
py -m pip install keyboard > nul 2>&1
py -m pip install discord_webhook > nul 2>&1

REM Check installation status
if %errorlevel% neq 0 (
    echo.
    echo %style_separator%
    echo An error occurred during installation.
    echo %style_separator%
    color %color_error%
) else (
    echo.
    echo %style_separator%
    echo Libraries installed successfully!
    echo %style_separator%
    color %color_success%
)

REM Display completion message
echo.
echo Press any key to exit...
pause > nul

REM Reset color and exit
color %color_normal%
exit

