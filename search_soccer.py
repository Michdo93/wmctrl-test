import subprocess
import webbrowser
import pyautogui
import time

def find_window_with_title(partial_title):
    """
    Überprüft, ob ein Fenster mit dem angegebenen Titel existiert.
    Gibt True zurück, wenn das Fenster gefunden wurde.
    """
    try:
        output = subprocess.check_output(["wmctrl", "-l"]).decode("utf-8")
        for line in output.splitlines():
            if partial_title.lower() in line.lower():
                return True
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Überprüfen von Fenstertiteln: {e}")
    return False

def bring_window_to_front(partial_title):
    """
    Bringt das Fenster mit dem angegebenen Titel in den Vordergrund.
    """
    try:
        subprocess.run(["wmctrl", "-a", partial_title], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Kein Fenster mit Titel '{partial_title}' gefunden.")
        return False

def open_or_switch_to_google():
    """
    Wechselt zu einem bestehenden Google-Tab oder öffnet einen neuen.
    """
    google_url = "https://www.google.de"
    if find_window_with_title("Google"):
        print("Google-Tab gefunden, wechsle zu diesem.")
        bring_window_to_front("Google")
    else:
        print("Kein Google-Tab gefunden, öffne neuen Tab.")
        webbrowser.open(google_url)
        time.sleep(3)  # Warte, bis der Browser geladen ist

def search_google(query="Fußball"):
    """
    Führt eine Suche auf Google durch.
    """
    open_or_switch_to_google()

    # Warte kurz, falls die Seite noch lädt
    time.sleep(2)

    # Fokussiere das Suchfeld und gib den Suchbegriff ein
    pyautogui.typewrite(query)
    pyautogui.press("enter")

if __name__ == "__main__":
    search_google("Fußball")
