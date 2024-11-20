import subprocess
import webbrowser
import pyautogui
import time

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

def search_google(query="Fußball"):
    """
    Öffnet google.de im Browser und sucht nach einem Begriff.
    """
    url = "https://www.google.de"
    if not bring_browser_to_front("Google"):
        # Wenn kein Browser gefunden wird, öffne einen neuen
        webbrowser.open(url)
        time.sleep(3)  # Warte, bis der Browser gestartet ist

    # Fokussiere das Eingabefeld und suche
    time.sleep(1)
    pyautogui.click(400, 400)  # Klicke ungefähr auf die Mitte der Seite (Passe ggf. an)
    pyautogui.typewrite(query)
    pyautogui.press("enter")

if __name__ == "__main__":
    search_google("Fußball")
