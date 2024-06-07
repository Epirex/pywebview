import os
import sys
import time
import webview

def destroy(window):
    time.sleep(900)
    window.destroy()

def open_window():
    return webview.create_window("Supranet", "index.html", fullscreen=True, easy_drag=False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    window = open_window()
    webview.start(destroy, window)
