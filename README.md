# DLL-Injections-Techniques-and-Templates
Templates for making .dll's

## How to Use it

#### For dll-template.c

Simply change the code as given in the comments and compile using `x86_64-w64-mingw32-gcc-win32 dll.c -o "OUTPUT".dll -shared` from any linux box having mingw-w64 using `sudo apt install mingw-w64`

#### For dll-proxy.py
Simply run it with python3, `python3 dll-proxy.py "DLL FILE NAME"`

Requirements:- `pip3 install pefile`
