"""
Restaurant Management System ,
    App is made to facilitate restaurant management processes.

Developed by Md raihan in mar 2024
    
"""

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from mainwindow import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
