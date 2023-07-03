@echo off

rem 这个自动编译ui文件的程序是chatgpt生成的，写法比较奇怪，我自己也没看懂。但是能用

setlocal enabledelayedexpansion

rem 一定要把python的Scripts目录加入环境变量，否则无法识别pyside6-uic.exe！！！

rem 如果没有加环境变量，也可以将下面的pyside6-uic.exe改为完整的目录，比如D:/Python/Python311/Scripts/pyside6-uic.exe

set PYUIC6_COMMAND=pyside6-uic.exe

set WIDGETS_FOLDER=./widget/

echo Searching for .ui files in %WIDGETS_FOLDER%...

for /r %WIDGETS_FOLDER% %%f in (*.ui) do (
    set OUTPUT_FILE=%%~nf.ui
    set OUTPUT_FILE=ui_!OUTPUT_FILE!
    set OUTPUT_FILE=!OUTPUT_FILE:.ui=.py!

    echo Converting %%~nxf to !OUTPUT_FILE!...
    call "%PYUIC6_COMMAND%" "%%f" -> "%WIDGETS_FOLDER%!OUTPUT_FILE!"
)

echo All .ui files have been converted to .py.