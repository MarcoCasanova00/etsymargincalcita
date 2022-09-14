#roba grafica
import pyfiglet

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    RESULT = '\033[92m'


logo = pyfiglet.figlet_format("Margin Calculator for my Etsy Shop", font = "digital" )
print(logo)


# creo lista inputs
inputs = []

#funzione 1 o enterdata
def enterdata():
	
	data = float(input(f"{bcolors.WARNING}Inserisci ammontare USD : "))
	if type(data) != float:
		print (f"{bcolors.WARNING}Hai inserito un valore non valido. Inserisci un float")
		
	else: inputs.append(data)

#funzione 2 o spese
def spese():
	
	fees = float(input(f"{bcolors.WARNING}Ora inserisci l'ammontare delle fees di Etsy in USD: \n{bcolors.ENDC}"))
	if type(fees) != float:
		print (f"{bcolors.WARNING}Hai inserito un valore non valido. Inserisci un float \n")
	else: 
		global totalespese
		totalespese = sum(inputs)+fees
		print (f"{bcolors.RESULT}Le tue spese totali tra Etsy e Fornitore ammontano a USD: \n", totalespese)
		print (f"{bcolors.ENDC}Ok. Passiamo al prossimo step")
		definitivo()
		
		
#funzione 3 o definitivo
def definitivo():
	
	sales = float(input(f"{bcolors.WARNING}Ora inserisci l'ammontare lordo delle vendite su Etsy in USD: \n{bcolors.ENDC}"))
	if type(sales) != float:
		print (f"{bcolors.WARNING}Hai inserito un valore non valido. Inserisci un float \n")
	else: 
		totalenetto = sales-totalespese
		print (f"{bcolors.RESULT}Il tuo guadagno netto e' di USD: \n", totalenetto)
		percentuale = 100 * totalenetto/sales
		print (f"{bcolors.RESULT}Ovvero il " + str(percentuale) + "% di " + str(sales))
		quit()
		

#loop principale
choice = ""

while choice != "//":
	choice = input(f"{bcolors.ENDC}Che vuoi fare? \n 1.Aggiungi pagamento al fornitore \n 2.Termina l'aggiunta di pagamenti al fornitore. \n")
	if choice == '1':
		enterdata()
	elif choice == '2':
		print (f"{bcolors.RESULT}Le spese del fornitore ammontano a USD :", sum(inputs))
		print (f"{bcolors.ENDC}Ok. Passiamo al prossimo step")
		spese()
	else:
		print(f"{bcolors.WARNING}La tua scelta non e' valida. Riprova.")
        






