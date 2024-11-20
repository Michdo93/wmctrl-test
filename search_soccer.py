import subprocess
import webbrowser
import pyautogui
import time

def find_window_with_title(partial_title):
    """
    Überprüft, ob ein Fenster mit dem angegebenen Titel existiert.
    Gibt die Fenster-ID zurück, wenn das Fenster gefunden wurde.
    """
    try:
        output = subprocess.check_output(["wmctrl", "-l"]).decode("utf-8")
        for line in output.splitlines():
            if partial_title.lower() in line.lower():
                return line.split()[0]  # Rückgabe der Fenster-ID
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Überprüfen von Fenstertiteln: {e}")
    return None

def bring_window_to_front(window_id):
    """
    Bringt das Fenster mit der angegebenen Fenster-ID in den Vordergrund.
    """
    try:
        subprocess.run(["wmctrl", "-i", "-a", window_id], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Kein Fenster mit ID '{window_id}' gefunden.")
        return False

def open_or_switch_to_google():
    """
    Wechselt zu einem bestehenden Google-Tab oder öffnet einen neuen.
    """
    google_url = "https://www.google.de"
    window_id = find_window_with_title("Google")
    if window_id:
        print("Google-Tab gefunden, wechsle zu diesem.")
        bring_window_to_front(window_id)
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
