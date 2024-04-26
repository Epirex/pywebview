import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView
import socket
import threading

class Communicate(QObject):
    url_received = pyqtSignal(str)

class WebViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl("http://google.com"))

        self.communicator = Communicate()
        self.communicator.url_received.connect(self.load_url_in_browser)

        self.browser.loadFinished.connect(self.url_loaded)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('192.168.100.111', 12345))
        self.server_socket.listen(5)
        threading.Thread(target=self.listen_for_urls, daemon=True).start()

    def listen_for_urls(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            url = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Recibida URL: {url}")
            self.communicator.url_received.emit(url)
            client_socket.close()

    def load_url_in_browser(self, url):
        try:
            if self.browser:
                self.browser.load(QUrl(url))
                print(f"Cargando URL: {url}")
        except Exception as e:
            print(f"Error al cargar la URL: {e}")

    def url_loaded(self):
        url = self.browser.url().toString()
        print(f"URL Cargada: {url}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebViewWindow()
    window.show()
    sys.exit(app.exec_())
