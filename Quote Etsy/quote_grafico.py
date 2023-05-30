import Tkinter as tk

def calcola_suddivisione():
    bonifico_etsy = float(entry_etsy.get())
    anticipo_marco = float(entry_marco.get())
    anticipo_danilo = float(entry_danilo.get())

    meta_bonifico = bonifico_etsy / 2

    quota_marco = meta_bonifico - (anticipo_danilo - anticipo_marco) / 2
    quota_danilo = meta_bonifico + (anticipo_danilo - anticipo_marco) / 2

    label_risultato_marco.config(text="Marco: %.2f" % quota_marco)
    label_risultato_danilo.config(text="Danilo: %.2f" % quota_danilo)

# Creazione della finestra principale
window = tk.Tk()
window.title("Calcolatore Suddivisione Etsy")

# Etichette e campi di input
label_etsy = tk.Label(window, text="Importo Bonifico Etsy:")
label_etsy.pack()
entry_etsy = tk.Entry(window)
entry_etsy.pack()

label_marco = tk.Label(window, text="Importo Anticipato da Marco:")
label_marco.pack()
entry_marco = tk.Entry(window)
entry_marco.pack()

label_danilo = tk.Label(window, text="Importo Anticipato da Danilo:")
label_danilo.pack()
entry_danilo = tk.Entry(window)
entry_danilo.pack()

# Bottone per calcolare la suddivisione
button_calcola = tk.Button(window, text="Calcola", command=calcola_suddivisione)
button_calcola.pack()

# Etichette per visualizzare i risultati
label_risultato_marco = tk.Label(window, text="Marco: ")
label_risultato_marco.pack()

label_risultato_danilo = tk.Label(window, text="Danilo: ")
label_risultato_danilo.pack()

# Avvio della finestra principale
window.mainloop()
