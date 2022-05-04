#include <windows.h>
#include <stdio.h>

BOOL WINAPI DllMain(HANDLE hModule, DWORD  fdwReason, LPVOID lpReserved)
{
        // code which should run regardles of what the condition is, should go here
        switch(fdwReason)
        {
                case DLL_PROCESS_ATTACH:
                        // code which runs when a new process attaches this DLL goes here
                        printf("Do process-specific initialization...\n");
                        break;
                case DLL_THREAD_ATTACH:
                        // code which runs when a new thread attaches this DLL goes here
                        printf("Do thread-specific initialization...\n");
                        break;
                case DLL_THREAD_DETACH:
                        // code which runs when a new thread detaches this DLL goes here
                        printf("Do thread-specific cleanup...\n");
                        break;
                case DLL_PROCESS_DETACH:
                         // code which runs when a new process detaches this DLL goes here
                        printf("Perform any necessary cleanup...\n");
                        break;
        }
        return TRUE;

}
