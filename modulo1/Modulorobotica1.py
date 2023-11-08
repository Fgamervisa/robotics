#!/usr/bin/env python
# coding: utf-8

# # Il Primo Programma #

# 

# In[4]:


print("Ciao", input("Inserisci il tuo nome: "), "!")


# In[5]:


nome = "TemplateText"
print(nome)


# In[1]:


print("hai inserito " + input("scegli nome della via"))


# Ripetere il codice più volte

# In[12]:


nome = input("Inserisci il tuo nome: ")
for x in range(3):
    print("Ciao", nome, "!")


# # Calcolatrice Python #

# 

# In[5]:


n1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
print("La somma è:",  int(n1 + numero2))


# 

# In[7]:


print("La differenza è:", int(n1 - numero2))


# 

# In[18]:


print("La moltiplicazione è:", int(n1 * numero2))


# 

# In[23]:


print("La divisione è:", int(n1 / numero2))


# # Loop e Ripetizione #

# In[25]:


for x in range(11):
    print(x)


# In[26]:


for x in range(1,11):
    print(x)


# # Condizioni e Decisioni #

# In[8]:


# Calcolatrice Python con decisioni

operazione = input("Inserisci l'operazione (+, -, *, /): ")

n1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    risultato = n1 + numero2
elif operazione == "-":
    risultato = n1 - numero2
elif operazione == "*":
    risultato = n1 * numero2
elif operazione == "/":
    risultato = n1 / numero2
else:
    risultato = "Operazione non valida"
    
print(risultato)


# # Contare fino a N #

# In[14]:


n = int(input("Inserisci un numero intero positivo:"))

for x in range(1,n+1):
    print(x)


# # Calcolare la Somma #

# In[17]:


n = int(input("Inserisci un numero intero positivo: "))
somma = 0

for x in range(1, n+1):
    somma += x
print("La somma dei primi", n, "numeri interi è:", somma)




# In[24]:


n = int(input("Inserisci un numero intero positivo: "))

print("Quadrati dei primi", n, "numeri:")

for x in range (1, n+1):
    quadrato = x ** 2
    print("Il quadrato di", x, "è", quadrato)


# # Verificare la Parità #

# In[29]:


n = int(input("Inserisci un numero: "))

#Se input è DIVISIBILE(%) per 2 e ha resto 0 (== 0)
if n % 2 == 0:
    print(n, "é un numero pari.")
else:
    print(n, "è un numero dispari.")


# # Calcolare il Fattoriale #

# In[55]:


n = int(input("Inserire un numero intero positivo: "))
fattoriale = 1

for numero in range(1, n+1):
    fattoriale *= numero
print("Il fattoriale di", n, "è:", fattoriale)


# # Calcolare la media di una Lista di Numeri #

# In[61]:


numeri = [] #Lista vuota di nome numeri

n = int(input("Quanti numeri vuoi inserire= ")) #Chiede quanti numeri voglio inserire dentro la lista vuota

#chiede un numero per quanto hai detto alla prima domanda
for i in range(n):
    numero = float(input("Inserisci un numero: "))
    numeri.append(numero) #mette il numero inserito dopo quello precedente
    
media = sum(numeri) / len(numeri) #Somma numeri dentro la lista e divide per lunghezza di quanti elementi ci sono

print("La media dei numeri inseriti è:", media, numeri)


# # Gioco dell'Indovinello #

# In[10]:


import random #importa la libreria del random

numero_da_indovinare =random.randint(1, 100) #spara un numero da 1 a 100
tentativi = 0

#chiede un numero
while True:
    tentativo = int(input("Indovina il numero (1-100): "))
    tentativi += 1
    
    if tentativo == numero_da_indovinare:
        print("Bravo! Hai indovinato il numero", numero_da_indovinare, "in", tentativi, "tentativi")
        break
    elif tentativo < numero_da_indovinare:
        print("Il numero è più grande")
    else:
        print("Il numero è più piccolo")


# # MORRA CINESE #

# In[69]:


import random

mosse = ["carta", "forbice", "sasso"]

cpu = random.choice(mosse)

print("Benvenuti al gioco del Morra Cinese!")
scelta_giocatore = input("Scegli la tua mossa (Carta, forbici, sasso): ")

if scelta_giocatore not in mosse:
    print("Mossa non permessa")
else:
    print("Il computer ha scelto:", cpu)
    if scelta_giocatore == cpu:
        print("Pareggio!")
    elif (scelta_giocatore == "carta" and cpu == "sasso") or \
         (scelta_giocatore == "forbici" and cpu == "carta") or \
         (scelta_giocatore == "sasso" and cpu == "forbici"):
        print("Hai Vinto!")
    else:
        print("Hai Perso!")


# # Calcolo del fattoriale #

# In[74]:


n = int(input("Inserisci un numero intero: "))

fattoriale = 1

if n<0:
    print("Numero Negativo")
elif n == 0:
    print("Il numero di zero è un 1 per definizione")
else:
    for numero in range(1, n+1):
        fattoriale*=numero
print(f"Il fattoriale di {n} è {fattoriale}")


# # somma numeri n #

# In[13]:




N = int(input("Inserisci un numero intero positivo N: "))


somma = 0


for numero in range(2, 2 * N + 1, 2):
    somma += numero
    

print(f"la somma dei primi {N} numeri pari è {somma}")


# # CONTA VOCALI IN UNA FRASE #

# In[14]:


frase  = input("Inserisci una frase o una parola: ").lower() 


conteggio_vocali = 0


vowels = "aeiouy"


for char in frase:

    if char in vowels:
        conteggio_vocali += 1
    

print(f"nella frase ci sono {conteggio_vocali} vocali")


# In[20]:



N = int(input("Inserisci un numero intero positivo N: "))
lista = []



for numero in range(2, 2 * N + 1,2):
    lista.append(numero)
    
print(lista)


# # IDNOVINA IL NUMERO DI DADO CASUALE (1 a 6) #

# In[60]:


import random


die = random.randint(1, 6)

indovina = int(input("Indovina il numero del dado (da 1 a 6): "))


if indovina <1 or indovina <0:
    print("numero non ammesso")
elif indovina == die:
    print(f"Complimenti il numero del dardo era {die}. Hai indovinato!")
else:
    print(f"Mi dispiae, il numero del dado era {die}. Meglio fortuna la prossima volta!")


# # SIMULAZIONE POPOLAZIONE #

# In[66]:



popolazione = int(input("inserisci popolazione iniziale: "))
anni = int(input("Inserisci il numero di anni da simulare: "))

tasso_natalità = float(input("Inserisci tasso natalità: "))
tasso_mortalità = float(input("Inserisci tasso mortalità: "))



for anno in range(anni):
    nascite = (popolazione * tasso_natalità) / 100
    morti = (popolazione * tasso_mortalità) / 100
    popolazione += (nascite - morti)
    
    print(f"Anno {anni}, Popolazione {int(popolazione)}")
    
print("Simulazione completata")




# In[67]:


from datetime import datetime as dt

today = dt.today()
print(f"oggi è il giorno:{today: %d %m %y},  ore:{today: %H %M %S}")


# In[4]:


print("Benvenuto nel convertitore di misura!")
scelta = input("Cosa desideri convertire? (meters/foot/kilos/lbs): ").lower()

if scelta == "meters":
    valore = float(input("Inserisci il valore in meters: "))
    risultato = valore * 3.28034
    print(f"{valore} meters corrispondono = {risultato} foot.")
    
elif scelta == "foot":
    valore = float(input("Inserisci il valore in foot: "))
    risultato = valore * 0.3048
    print(f"{valore} foot corrispondono = {risultato} meters.")
    
elif scelta == "chilogrammi":
    valore = float(input("Inserisci il valore in chilogrammi: "))
    risultato = valore * 2.2046
    print(f"{valore} chilogrammi corrispondono = {risultato} lbs.")
    
elif scelta == "lbs":
    valore = float(input("Inserisci il valore in lbs: "))
    risultato = valore * 3.28034
    print(f"{valore} lbs corrispondono = {risultato} chilogrammi.")




# In[69]:



n = int(input("Inserisci un numero n per calcolare l'n-esimo numero di Fibonacci: "))

a=0
b=1
c=1

# Calcolare l'n-esimo numero di fibonacci
if n <= 0:
    print("il numero deve essere maggiore di 0")
elif n == 1:
    risultato = a
else:
    for iterazione in range(n-3):
        a = b
        b = c
        c = a + b
    risultato = c
# Stampare l'n-esio numero di fibonacci
print("l'n-esimo numero di fibonacci è:", risultato)




# In[79]:


def fibonacci(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
        
    return fib_series


# In[80]:


fibonacci(9)


# In[5]:


from math import pi

def calcola_area_cerchio(raggio):
    return pi * (raggio ** 2)

def calcola_area_rettangolo(base, altezza):
    return base * altezza

def calcola_area_triangolo(base, altezza):
    return (base * altezza) / 2

print("Benvenuro nella calcolatrice di aree")

scelta = input("Vuoi calcolare l'area di un cerchio (c), rettangolo (r), triangolo (t): ").lower()

if scelta == 'c':
    raggio = float(input("Inserisci il raggio del cerchio: "))
    area = calcola_area_cerchio(raggio)
    print(f"L'area del cerchio è {area: .2f}")
elif scelta == 'r':
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = calcola_area_rettangolo(base, altezza)
    print(f"L'area del rettangolo è {area:.2f}")
elif scelta == 't':
    base = float(input("inserisci la base del triangolo: "))
    altezza = float(input("Inserisci l'altezza del triangolo: "))
    area = calcola_area_triangolo(base, altezza)
    print(f"l'area del triangolo è {area:-2f}") #{area:-2f} significa di stampare il valore AREA ma massimo 2 numeri dopo virgola
else:
    print("Scelta non valida, riprova")


# # calcolo interessi #

# In[6]:


def calcola_interessi(importo, interest, investing):
    importo_finale = importo * (1 + interest / 100) ** investing
    return importo_finale


# In[8]:


print("Benvetuo nel Calolatore d'interessi!")

importo = float(input("Inserisci l'importo iniziale: "))
tasso = float(input("Inserisci il tasso d'interesse annuale (%): "))
periodo = int(input("Inserisci il periodo d'investimento (anni): "))

importo_finale = calcola_interessi(importo, tasso, periodo)

print(f"l'importo finale dopo {periodo} anni è di {importo_finale:.2f} euro.")



# # calcola anagrammi #

# In[30]:


from itertools import permutations
k=0

def trova_anagrammi(parola):
    anagrammi = ["".join(p) for p in permutations(parola)]
    return anagrammi

print("Benvenuto nel risolutore di anagrammi!")

parola_input = input("Inserisci una parola: ").strip().lower()

if len(parola_input) < 2:
    print("Inserisci una parola con almeno 2 caratteri: ")
else:
    anagrammi = trova_anagrammi(parola_input)
    
    for anagramma in anagrammi:
        if anagramma != parola_input:
            k+=1
            print(anagramma)
        print(f"gli anagrammi di '{parola_input}' sono: '{k}'")


# # dizionario #

# In[5]:


# Definizione dei tassi di cambio

tassi_di_cambio= {
    "dollari": 1.0,
    "euro": 0.85,
    "yen": 110.41,
    # aggiungi altre valute e tassi di cambio se necessario
}

# Chiedi all'utente d'inserire l'importo, la valuta di partenza e la valuta di destinazione
importo = float(input("Inserisci l'importo da convertire: "))
valuta_di_partenza = input("Inserisci la valuta di partenza: ").lower()
valuta_destinazione = input("Inserisci la valuta di destinazione: ").lower()

#Verifica se le valute sono nel dizionari dei tassi di cambio
if valuta_di_partenza in tassi_di_cambio and valuta_destinazione in tassi_di_cambio:
    #Calcola il tasso di cambio e l'importo converitto
    tasso_di_cambio = tassi_di_cambio[valuta_destinazione] / tassi_di_cambio[valuta_di_partenza]
    importo_convertito = importo * tasso_di_cambio

#stampa il risultato
    print(f"{importo} {valuta_di_partenza} sono equivalenti a {importo_convertito:.2f} {valuta_destinazione}")
else:
    print("Valute non supportate. Assicurati di inserire valute valide.")
    


# In[6]:


tassi_di_cambio["euro"]


# In[10]:


frase = input("Inserisci una frase: ")


frase = frase.lower()


alfabeto = 'abcdefghijklmnopqrstuvwxyz'


conteggio_lettere = {}


for lettera in alfabeto:
    
    conteggio = frase.count(lettera)
    
    
    if conteggio > 0:
        conteggio_lettere[lettera] = conteggio
        

for lettera, conteggio in conteggio_lettere.items():
    print(f"{lettera}: {conteggio}")


# In[12]:


conteggio_lettere.items()


# In[13]:


prodotti = {}
prodotti["pan bauletto"] = 2
prodotti["coca cola"] = 3


# In[14]:


prodotti


# In[1]:


from datetime import datetime
import pytz

print("Benvetuo nell'orologio mondiale")


citta_fusi_orari = {
    "New York": "America/New York",
    "Londra": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sidney",
    "Rio de Janeiro": "America/Sao_Paulo",
}

while True:
    print("\nCittà disponibili:")
    for citta in citta_fusi_orari.keys():
        print(citta)
        
        scelta_citta = input("Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): ").strip()
        if scelta_citta.lower() == 'esci':
            
            if scelta_citta in citta_fusi_orari.keys():
                fuso_orario = pytz.timezone(citta_fusi_orari[scelta_citta])
                ora_corrente = datetime.now(fuso_orario)
                print(f"L'ora corrente a {scelta_citta} è: {ora_corrente.strftime('%H:%M:%S')}")
            else:
                print("citta non valid. Riprova")




# In[5]:



def paolo():
    print("Mi chiamo Paolo")
    
if __name__ == "__main__" : 
                           
    paolo()


# In[8]:



def main():
    print("la funzione principale del codice è stata eseguita, in questa ufnzione possono essere presenti funzioni s")
    
if __name__ == "__main__": 
    main()


# In[2]:


#main

def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)

#funzione per la valtazione del BMI
def valuta_bmi(bmi):
    if bmi < 10.5:
        return "Sottopeso"
    elif 10.5 <= bmi < 24.9:
        return "Normopeso"
    elif 25 <= bmi < 29.9:
        return "Sovrappeso"
    else: 
        return "Obeso"
    
# Funzione principale
def main():
    print("Benvenuto nella calcolatri bmi!")
    peso = float(input("Inserisci i tuo peso in chilogrammi: "))
    altezza = float(input("Inserisci la tua altezza in metri: "))
    
    bmi = calcola_bmi(peso, altezza)
    valutazione = valuta_bmi(bmi)
    
    print(f"il tuo BMI è {bmi:.2f}, sei classificato come '{valutazione}.'")
    
if __name__ == "__main__":
    main()

# In[3]:


cibo_calorie = {
    "pizza": 285,
    "hamburger": 250,
    "insalata": 100,
    "pollo arrosto": 335,
    "yogurt": 150
}

#Funzione per calcolare le calorie cosnumate
def calorie_consumate(cibo, quantita):
    if cibo not in cibo_calorie.keys():
        print("Cibo non presente")
    elif cibo in cibo_calorie:
        calorie_per_100g = cibo_calorie[cibo]
        calorie_totali = (calorie_per_100g / 100) * quantita
        return calorie_totali
    else:
        return 0
    

def main():
    cibo_consumato = []
    
    while True:
        print("menù:")
        print("\n 1. aggiungi cibo consmato")
        print("\n 2. calcola calorie totali")
        print("\n 3 esci")
        
        scelta = input("scegli un opzione: ")
        
        if scelta == "1":
            print("\n")
            for key, value in cibo_calorie.items():
                print(key,value)
                
            cibo = input("inserisci il cibo consumto: ").lower()
            quantita = float(input("Inserisci la quantita in grammi: "))
            cibo_consumato.append((cibo,quantita))
        elif scelta == "2":
            calorie_totali = sum(calorie_consumate(c,q) for c, q in cibo_consumato)
            print(f"\ncalore totali consumate: {calorie_totali} calorie")
        elif scelta == "3":
            print("ok")
            break
        else:
            print("\nscelta non valida. riprova")
if __name__ == "__main__":
    main()




# In[3]:


import random


speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]


specie = random.choice(speci)
classe = random.choice(classi)
arma = random.choice(armi)
abilità_scelte = random.sample(abilità, random.randint(1,3))


print(f"Personaggio Fantasy Generato: ")
print(f"Specie: {specie}")
print(f"Classe: {classe}")
print(f"Arma: {arma}")
print(f"Abilità: {', '.join(abilità_scelte)}")


# In[8]:


import random 

speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]


def crea_personaggio():
    return {
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1,3))
    }


def main():
    personaggio_generato = crea_personaggio()
    
    print("Personaggi Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")
        

if __name__ == "__main__":
    main()


# In[10]:


import random 

speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]


def crea_personaggio():
    personaggio={
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1,3))
    }
    return personaggio


def main():
    personaggio_generato = crea_personaggio()
    
    print("Personaggi Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")
        

if __name__ == "__main__":
    main()




# In[12]:


import random

physical_traits = ["capelli nero", "capelli biondi", "occhi cazzurri", "occhi verdi"]
personality_traits = ["gentile", "introverso", "estroverso", "ottimista"]
backgrounds = ["contadino", "nobile", "artigiano", "commerciale"]
motivations = ["vendetta", "ricchezza", "amore", "vita esterna"]

def genera_personaggio():
    nome = input("Inserisci il nome del personaggio: ")
    aspetto_fisico = random.choice(physical_traits)
    aspetto_personale = random.choice(personality_traits)
    sfondo = random.choice(backgrounds)
    motivazione = random.choice(motivations)
    
    descrizione =f"Nome: {nome}\nAspetto Fisico: {aspetto_fisico}\nAspetto Personale: {aspetto_personale}\nSfondo: {sfondo}\nMotivazione: {motivazione}"
    
    return descrizione
print("Generatore di personaggi per romanzi")
print(genera_personaggio())




# In[14]:



citazioni = [
    "Non sforzare troppo qualcosa.. perché forse è shit - Edoardo",
    "A",
    "B",
    "C",
]


def genera_citazione():
    return random.choice(citazioni)


def main():
    print("Benvevuto nel generatore di citazioni")
    input("Premi invio per ottenere una citazione causale...")
    
    citazione = genera_citazione()
    print(f"citazione del giorno: {citazione}")
    
if __name__ == "__main__":
    main()




# In[17]:


import random

frammenti = [
    "ciao",
    "come va?",
    "dio",
    "grazioso",
    "madonna",
    "blabla",
    "lalalal",
    "pipipipip",
    "blululullulu"
]

def crea_citazione():
    num_frammenti = random.randint(5,7) 
    citazione_rimescolata = random.sample(frammenti, num_frammenti)
    nuova_citazione = " ".join(citazione_rimescolata)
    return nuova_citazione


nuova_citazione = crea_citazione()
print("Nuova citazione generata:")
print(nuova_citazione)


# In[4]:


import random

frammenti = [
    "Il mattino",
    "il mare",
    "#donna",
    "#perte",
    "Asdd",
    "blabla",
    "lalalal",
    "pipipipip",
    "blululullulu"
]

def crea_citazione():
    num_frammenti = random.randint(4,7) 
    citazione_rimescolata = random.sample(frammenti, num_frammenti)
    nuova_citazione = " ".join(citazione_rimescolata)
    return nuova_citazione
    

def main():
    nuova_citazione = crea_citazione()
    print("Nuova citazione generata:")
    print(nuova_citazione)
    
if __name__ == "__main__":
    main()


# In[ ]:


import random


aggettivi = ["dolce", "serena", "profondo", "luminoso", "gentile"]
sostantivi = ["amore", "mare", "cielo", "vento", "sogno"]
verbi = ["danza", "splende", "abbraccia", "canta", "sorride"]


def genera_poesia():
    poesia = f"""Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}.\n
      Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}.\n
      Nel {random.choice(aggettivi)} {random.choice(sostantivi)}"""

