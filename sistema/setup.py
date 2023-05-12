import webview

def open_window():
    webview.create_window("Webview by Supranet", "http://www.supranet.ar")

if __name__ == '__main__':
    open_window()
    webview.start()