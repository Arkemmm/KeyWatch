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

echo  ,ggg,        gg                                                                               
echo dP""Y8b       dP                                                     I8              ,dPYb,    
echo Yb, `88      d8'                                                     I8              IP'`Yb    
echo  `"  88    ,dP'                                                   88888888           I8  8I    
echo      88aaad8"                                                        I8              I8  8'    
echo      88""""Yb,     ,ggg,   gg     gg  gg    gg    gg     ,gggg,gg    I8      ,gggg,  I8 dPgg,  
echo      88     "8b   i8" "8i  I8     8I  I8    I8    88bg  dP"  "Y8I    I8     dP"  "Yb I8dP" "8I 
echo      88      `8i  I8, ,8I  I8,   ,8I  I8    I8    8I   i8'    ,8I   ,I8,   i8'       I8P    I8 
echo      88       Yb, `YbadP' ,d8b, ,d8I ,d8,  ,d8,  ,8I  ,d8,   ,d8b, ,d88b, ,d8,_    _,d8     I8,
echo      88        Y8888P"Y888P""Y88P"888P""Y88P""Y88P"   P"Y8888P"`Y888P""Y88P""Y8888PP88P     `Y8
echo                                 ,d8I'                                                          
echo                               ,dP'8I                                                           
echo                              ,8"  8I                                                           
echo                              I8   8I                                                           
echo                              `8, ,8I                                                           
echo                               `Y8P"                                                            


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
