
# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from tkinter import messagebox

GEHEIM_CODE = "1337"
FENSTER_GROESSE = "320x450"

def button_aktion(taste, anzeige_feld):
    """
    Diese Funktion verarbeitet die Tasteneingabe.
    """

    # Wenn die C  ancel Taste gedrückt wird
    if taste == "C":
        anzeige_feld.delete(0, tk.END) # Display leeren
        anzeige_feld.config(bg="white") # Hintergrundfarbe zurücksetzen

    # Wenn die Bestätigungstaste gedrückt wird
    elif taste == "OK":
        eingabe = anzeige_feld.get() # Eingabe auslesen

        if eingabe == GEHEIM_CODE: # Überprüfen, ob mit geheimcode übereinstimmt
            anzeige_feld.config(bg="#90ee90") # Grün
            messagebox.showinfo("Status", "Zugriff gewährt!")

        else: # Wenn Eingabe nicht mit Geheimcode übereinstimmt
            anzeige_feld.config(bg="#ffcccc") # Rosa/Pink
            messagebox.showerror("Status", "Zugriff verweigert!")
            anzeige_feld.delete(0, tk.END) # Text/Eingabe löschen

    else:
        # Zahl wurde gedrückt -> Anhängen
        # Prüfen, ob wir einen farbigen Hintergrund haben
        if anzeige_feld.cget('bg') != 'white':
             anzeige_feld.config(bg='white')
             anzeige_feld.delete(0, tk.END) # Reset bei neuer Eingabe

        aktueller_inhalt = anzeige_feld.get()
        anzeige_feld.delete(0, tk.END)
        anzeige_feld.insert(0, aktueller_inhalt + taste)


def gui_erstellen(main_window):
    """
    Baut die grafische Oberfläche auf.
    """
    # Display/Eingabefenster erstellen
    anzeige = tk.Entry(main_window, font=("Consolas", 24), justify="right", bd=10)
    anzeige.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=20)

    # Layout der Tasten
    tasten_layout = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['C', '0', 'OK']
    ]

    # Buttons erstellen
    for zeile_index, zeile in enumerate(tasten_layout, start=1):
        for spalte_index, tasten_text in enumerate(zeile):
            # Button erstellen
            btn = tk.Button(
                main_window, 
                text=tasten_text, 
                font=("Arial", 18),
                command=lambda x=tasten_text: button_aktion(x, anzeige) # Funktion den einzelnen Buttons zuweisen
            )
            
            # Button ins Grid legen
            btn.grid(
                row=zeile_index, 
                column=spalte_index, 
                sticky="nsew", 
                padx=2, 
                pady=2
            )
    
    # Responsivität (Grid anpassen, wenn Fenstergröße sich ändert)
    main_window.columnconfigure((0, 1, 2), weight=1) # Alle 3 Spalten wachsen gleichmäßig
    # Zeilen 1 bis 4 (Buttons) sollen wachsen
    for i in range(1, 5):
        main_window.rowconfigure(i, weight=1)


if __name__ == "__main__":
    # Hauptfenster initialisieren
    main_window = tk.Tk()
    main_window.title("Safe-System")
    main_window.geometry(FENSTER_GROESSE)

    # GUI aufbauen/ Funktion aufrufen
    gui_erstellen(main_window)

    # Event-Loop starten
    main_window.mainloop()