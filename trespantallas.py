import requests
import webview
from screeninfo import get_monitors
import keyboard

# Lista para almacenar ventanas abiertas
windows = []


def open_windows(urls):
    global windows
    # Obtener la resolución de la pantalla
    screen_width = sum(m.width for m in get_monitors())
    screen_height = max(m.height for m in get_monitors())

    # Calcular las dimensiones de cada ventana
    window_width = screen_width // 3
    window_height = screen_height

    # Abrir el webview
    for i, url in enumerate(urls):
        window = webview.create_window('Frameless window', url, width=window_width, height=window_height,
                                       x=i * window_width,
                                       y=0, frameless=True)
        windows.append(window)


# Cerrar las primeras tres ventanas
def close_first_three_windows():
    global windows
    for i in range(3):
        if windows:
            window = windows.pop(0)
            window.destroy()


if __name__ == '__main__':
    # Abrir pantallas de inicio
    url = 'http://supranet.ar/muestra/urls.txt'
    response = requests.get(url)

    if response.status_code == 200:
        urls = response.text.splitlines()
        urls = [url.strip() for url in urls if url.strip()]
        open_windows(urls)


        def load_urls_from_file(file_path):
            response = requests.get(file_path)
            if response.status_code == 200:
                urls = response.text.splitlines()
                urls = [url.strip() for url in urls if url.strip()]
                open_windows(urls)
            else:
                print("Error al obtener el archivo de texto:", response.status_code)


        # Botón 1
        def load_urls1():
            load_urls_from_file('http://supranet.ar/muestra/urls1.txt')
            close_first_three_windows()


        # Botón 2
        def load_urls2():
            load_urls_from_file('http://supranet.ar/muestra/urls2.txt')
            close_first_three_windows()


        # Botón 3
        def load_urls3():
            load_urls_from_file('http://supranet.ar/muestra/urls3.txt')
            close_first_three_windows()


        # Asignar las funciones a las teclas correspondientes
        keyboard.add_hotkey('1', load_urls1)
        keyboard.add_hotkey('2', load_urls2)
        keyboard.add_hotkey('3', load_urls3)
        keyboard.add_hotkey('4', close_first_three_windows)  # En caso de emergencia

        webview.start()
    else:
        print("Error al obtener el archivo de texto:", response.status_code)
