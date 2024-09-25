import os
import sys
import webview

def open_window():
    # El script JavaScript que inyectará el CSS en la página web
    css_injection_script = """
    var style = document.createElement('style');
    style.innerHTML = `
    p.info_text__OQfN6 {
      display: none;
    }
    
    div a img {
      display: none;
    }
    `;
    document.head.appendChild(style);
    """
    
    # Crea la ventana con la URL deseada
    window = webview.create_window(
        "Webview by Supranet", 
        "https://lumalabs.ai/embed/2fe14849-ffc9-4a9f-a205-340ceb032a80?mode=sparkles&background=%23ffffff&color=%23000000&showTitle=true&loadBg=true&logoPosition=bottom-left&infoPosition=bottom-right&cinematicVideo=undefined&showMenu=false", 
        fullscreen=True
    )
    
    # Inyecta el CSS a través de JavaScript
    webview.start(lambda: window.evaluate_js(css_injection_script))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    open_window()
