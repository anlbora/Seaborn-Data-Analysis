from PyQt5 import uic

with open("MainWindow.py", "w", encoding= "utf-8") as fout:
    uic.compileUi("mainWindow.ui", fout)