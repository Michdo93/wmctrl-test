import subprocess
import webbrowser

def bring_browser_to_front(window_title="Google"):
    """
    Bringt ein Browserfenster mit einem bestimmten Titel in den Vordergrund.
    """
    try:
        subprocess.run(["wmctrl", "-a", window_title], check=True)
    except subprocess.CalledProcessError:
        print(f"Kein Fenster mit Titel '{window_title}' gefunden. Browser wird gestartet.")
        return False
    return True

def open_google():
    """
    Öffnet google.de im Browser und bringt den Browser in den Vordergrund.
    """
    url = "https://www.google.de"
    if not bring_browser_to_front("Google"):
        # Wenn kein Browser gefunden wird, öffne einen neuen
        webbrowser.open(url)

if __name__ == "__main__":
    open_google()
