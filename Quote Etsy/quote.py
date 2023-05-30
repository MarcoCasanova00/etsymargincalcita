bonifico_etsy = float(input("Inserisci l'importo del bonifico di Etsy: "))
anticipo_marco = float(input("Inserisci l'importo anticipato da Marco: "))
anticipo_danilo = float(input("Inserisci l'importo anticipato da Danilo: "))

metà_bonifico = bonifico_etsy / 2

quota_marco = metà_bonifico - (anticipo_danilo - anticipo_marco) / 2
quota_danilo = metà_bonifico + (anticipo_danilo - anticipo_marco) / 2

print("La suddivisione del bonifico di Etsy sarà:")
print("Marco: ", quota_marco)
print("Danilo: ", quota_danilo)
