@echo off

REM Define colors and styles
set "color_normal=0f"
set "color_error=0c"
set "color_success=0a"
set "style_separator=----------------------------------------"

REM Clear the screen
cls

REM Turn off command echoing
echo off

echo ██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗
echo ██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║
echo ██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║
echo ██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
echo ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

REM Update pip
echo Updating pip...
py -m pip install --upgrade pip > nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo %style_separator%
    echo An error occurred during pip update.
    echo %style_separator%
    color %color_error%
    goto :exit
)

REM Install libraries
echo Installing libraries...
py -m pip install pywin32 keyboard > nul 2>&1

REM Check installation status
if %errorlevel% neq 0 (
    echo.
    echo %style_separator%
    echo An error occurred during library installation.
    echo %style_separator%
    color %color_error%
) else (
    echo.
    echo %style_separator%
    echo Libraries installed successfully!
    echo %style_separator%
    color %color_success%
)

:exit
REM Display completion message
echo.
echo Press any key to exit...
pause > nul

REM Reset color and exit
color %color_normal%
exit
