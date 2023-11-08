# Il Primo Programma #




```python
print("Ciao", input("Inserisci il tuo nome: "), "!")
```

    Inserisci il tuo nome: Edoardo
    Ciao Edoardo !
    


```python
nome = "TemplateText"
print(nome)
```

    Edoardo
    


```python
print("hai inserito " + input("scegli nome della via"))
```

    scegli nome della viaciao
    hai inseritociao
    

Ripetere il codice più volte


```python
nome = input("Inserisci il tuo nome: ")
for contatore in range(3):
    print("Ciao", nome, "!")
```

    Inserisci il tuo nome: Ciao
    Ciao Ciao !
    Ciao Ciao !
    Ciao Ciao !
    

# Calcolatrice Python #




```python
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
print("La somma è:",  int(numero1 + numero2))
```

    Inserisci il primo numero: 10
    Inserisci il secondo numero: 20
    La somma è: 30
    




```python
print("La differenza è:", int(numero1 - numero2))
```

    La differenza è: -10
    




```python
print("La moltiplicazione è:", int(numero1 * numero2))
```

    Inserisci il pirmo numero: 2
    Inserisci il secondo numero: 2
    La moltiplicazione è: 4
    




```python
print("La divisione è:", int(numero1 / numero2))
```

    Inserisci il pirmo numero: 2
    Inserisci il secondo numero: 2
    La divisione è: 1.0
    

# Loop e Ripetizione #


```python
for x in range(11):
    print(x)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
for x in range(1,11):
    print(x)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

# Condizioni e Decisioni #


```python
# Calcolatrice Python con decisioni

operazione = input("Inserisci l'operazione (+, -, *, /): ")

numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1 + numero2
elif operazione == "-":
    risultato = numero1 - numero2
elif operazione == "*":
    risultato = numero1 * numero2
elif operazione == "/":
    risultato = numero1 / numero2
else:
    risultato = "Operazione non valida"
    
print("Il risultato è:", risultato)
```

    Inserisci l'operazione (+, -, *, /): *
    Inserisci il primo numero: 5
    Inserisci il secondo numero: 4
    Il risultato è: 20.0
    

# Contare fino a N #


```python
n = int(input("Inserisci un numero intero positivo:"))

for x in range(1,n+1):
    print(numero)
```

    Inserisci un numero intero positivo:6
    1
    2
    3
    4
    5
    6
    

# Calcolare la Somma #


```python
n = int(input("Inserisci un numero intero positivo: "))
somma = 0

for x in range(1, n+1):
    #somma = somma + numero
    somma += numero
print("La somma dei primi", n, "numeri interi è:", somma)
```

    Inserisci un numero intero positivo: 3
    La somma dei primi 3 numeri interi è: 6
    

# Calcolare il Quadrato dei Primi Numeri #


```python
n = int(input("Inserisci un numero intero positivo: "))

print("Quadrati dei primi", n, "numeri:")

for x in range (1, n+1):
    quadrato = numero ** 2
    print("Il quadrato di", numero, "è", quadrato)
```

    Inserisci un numero intero positivo: 5
    Quadrati dei primi 5 numeri:
    Il quadrato di 1 è 1
    Il quadrato di 2 è 4
    Il quadrato di 3 è 9
    Il quadrato di 4 è 16
    Il quadrato di 5 è 25
    

# Verificare la Parità #


```python
numero = int(input("Inserisci un numero: "))

#Se input è DIVISIBILE(%) per 2 e ha resto 0 (== 0)
if numero % 2 == 0:
    print(numero, "é un numero pari.")
else:
    print(numero, "è un numero dispari.")
```

    Inserisci un numero: 23
    23 è un numero dispari.
    

# Calcolare il Fattoriale #


```python
n = int(input("Inserire un numero intero positivo: "))
fattoriale = 1

for x in range(1, n+1):
    #fattoriale = fattoriale * numero
    fattoriale *= numero
print("Il fattoriale di", n, "è:", fattoriale)
```

    Inserire un numero intero positivo: 5
    Il fattoriale di 5 è: 120
    

# Calcolare la media di una Lista di Numeri #


```python
numeri = [] #Lista vuota di nome numeri

n = int(input("Quanti numeri vuoi inserire= ")) #Chiede quanti numeri voglio inserire dentro la lista vuota

#chiede un numero per quanto hai detto alla prima domanda
for i in range(n):
    numero = float(input("Inserisci un numero: "))
    numeri.append(numero) #mette il numero inserito dopo quello precedente
    
media = sum(numeri) / len(numeri) #Somma numeri dentro la lista e divide per lunghezza di quanti elementi ci sono

print("La media dei numeri inseriti è:", media, numeri)
```

    Quanti numeri vuoi inserire= 4
    Inserisci un numero: 3
    Inserisci un numero: 3
    Inserisci un numero: 3
    Inserisci un numero: 3
    La media dei numeri inseriti è: 3.0 [3.0, 3.0, 3.0, 3.0]
    

# Gioco dell'Indovinello #


```python
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
```

    Indovina il numero (1-100): 2
    Il numero è più grande
    Indovina il numero (1-100): 17
    Il numero è più grande
    Indovina il numero (1-100): 56
    Il numero è più piccolo
    Indovina il numero (1-100): 3
    Il numero è più grande
    Indovina il numero (1-100): 37
    Il numero è più piccolo
    Indovina il numero (1-100): 33
    Il numero è più grande
    Indovina il numero (1-100): 35
    Il numero è più piccolo
    Indovina il numero (1-100): 34
    Bravo! Hai indovinato il numero 34 in 8 tentativi
    

# MORRA CINESE #


```python
import random

mosse = ["carta", "forbice", "sasso"]

computer_mossa = random.choice(mosse)

print("Benvenuti al gioco del Morra Cinese!")
scelta_giocatore = input("Scegli la tua mossa (Carta, forbici, sasso): ")

if scelta_giocatore not in mosse:
    print("Mossa non permessa")
else:
    print("Il computer ha scelto:", computer_mossa)
    if scelta_giocatore == computer_mossa:
        print("Pareggio!")
    elif (scelta_giocatore == "carta" and computer_mossa == "sasso") or \
         (scelta_giocatore == "forbici" and computer_mossa == "carta") or \
         (scelta_giocatore == "sasso" and computer_mossa == "forbici"):
        print("Hai Vinto!")
    else:
        print("Hai Perso!")
```

    Benvenuti al gioco del Morra Cinese!
    Scegli la tua mossa (Carta, forbici, sasso): carta
    Il computer ha scelto: sasso
    Hai Vinto!
    

# Calcolo del fattoriale #


```python
n = int(input("Inserisci un numero intero: "))

fattoriale = 1

if n<0:
    print("Numero Negativo")
elif n ==0:
    print("Il numero di zero è un 1 per definizione")
else:
    for x in range(1, n+1):
        fattoriale*=numero
print(f"Il fattoriale di {n} è {fattoriale}")
```

    Inserisci un numero intero: 2
    Il fattoriale di 2 è 2
    

# somma numeri n #


```python
# Chiedere all'utente d'inserire un numero imtero positivo N

N = int(input("Inserisci un numero intero positivo N: "))

# Inizializzare la somma a zero
somma = 0

# Calcolare la somma dei primi N numeri pari
for x in range(2, 2 * N + 1, 2):
    somma += numero
    
# Stampare la somma
print(f"la somma dei primi {N} numeri pari è {somma}")
```

    Inserisci un numero intero positivo N: 10
    la somma dei primi 10 numeri pari è 110
    

# CONTA VOCALI IN UNA FRASE #


```python
# Chiedere all'utente d'inserire una frase o una parola

frase  = input("Inserisci una frase o una parola: ").lower() #Converti tutto in minuscolo per semplificare il contaggio

# Inizializzare il contatore delle vocali
conteggio_vocali = 0

# Definisci le vocali da cercare
vocali = "aeiou"

# scansione ogni carattere nella frase
for carattere in frase:
    # Verifica se il carattere è una vocale
    if carattere in vocali:
        conteggio_vocali += 1
    
# Stampare la somma
print(f"nella frase ci sono {conteggio_vocali} vocali")
```

    Inserisci una frase o una parola: CIAO
    nella frase ci sono 3 vocali
    


```python
# Chiedere all'utente di inserire un nuerp intero positivo N
N = int(input("Inserisci un numero intero positivo N: "))
lista = []


# Calcolare la somma dei primi n numeri pari
for x in range(2, 2 * N + 1,2):
    lista.append(numero)
    
print(lista)
```

    Inserisci un numero intero positivo N: 10
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    

# IDNOVINA IL NUMERO DI DADO CASUALE (1 a 6) #


```python
import random

# Genera un numero casuale da 1 a 6(simulando un lanco di un dado)
numero_dado = random.randint(1, 6)

# Chiedi all'utente d'indovinare il numero
indovina = int(input("Indovina il numero del dado (da 1 a 6): "))

# Verifica se l'utente ha indovinato correttamente
if indovina <1 or indovina <0:
    print("numero non ammesso")
elif indovina == numero_dado:
    print(f"Complimenti il numero del dardo era {numero_dado}. Hai indovinato!")
else:
    print(f"Mi dispiae, il numero del dado era {numero_dado}. Meglio fortuna la prossima volta!")
```

    Indovina il numero del dado (da 1 a 6): 6
    Complimenti il numero del dardo era 6. Hai indovinato!
    

# SIMULAZIONE POPOLAZIONE #


```python
# Inizializza la popolazione e gli anni
popolazione = int(input("inserisci popolazione iniziale: "))
anni = int(input("Inserisci il numero di anni da simulare: "))
# Tasso di natalità e tasso di mortalità (% annuale)
tasso_natalità = float(input("Inserisci tasso natalità: "))
tasso_mortalità = float(input("Inserisci tasso mortalità: "))


# Simulazione della crescita della popolazione
for anno in range(anni):
    nascite = (popolazione * tasso_natalità) / 100
    morti = (popolazione * tasso_mortalità) / 100
    popolazione += (nascite - morti)
    
    print(f"Anno {anni}, Popolazione {int(popolazione)}")
    
print("Simulazione completata")
```

    inserisci popolazione iniziale: 10
    Inserisci il numero di anni da simulare: 10
    Inserisci tasso natalità: 10
    Inserisci tasso mortalità: 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Anno 10, Popolazione 10
    Simulazione completata
    

# dire giorno ed ora con datetime #


```python
import datetime

today = datetime.datetime.today()
print(f"oggi è il giorno:{today: %d %m %y},  ore:{today: %H %M %S}")
```

    oggi è il giorno: 04 10 23,  ore: 09 09 04
    


```python

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
```

    Benvenuto nel convertitore di misura!
    Cosa desideri convertire? (metri/piedi/chilograbbi/libbre): metri
    Inserisci il valore in metri: 2
    2.0 metri corrispondono = 6.56068 piedi.
    

# FIBONACCI #


```python
# Chiedere all'utente d'inserire un numero n
n = int(input("Inserisci un numeor n per calcolare l'n-esimo numero di Fibonacci: "))
#inizializzare le variabili per i primi due numeri di fibonacci
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
```

    Inserisci un numeor n per calcolare l'n-esimo numero di Fibonacci: 20
    l'n-esimo numero di fibonacci è: 4181
    

# FUNZIONI CUSTOM #


```python
def fibonacci(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
        
    return fib_series
```


```python
fibonacci(9)
```




    [0, 1, 1, 2, 3, 5, 8, 13, 21]




```python
import math

def calcola_area_cerchio(raggio):
    return math.pi * (raggio ** 2)

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
```

    Benvenuro nella calcolatrice di aree
    Vuoi calcolare l'area di un cerchio (c), rettangolo (r), triangolo (t): c
    Inserisci il raggio del cerchio: 10
    L'area del cerchio è  314.16
    

# calcolo interessi #


```python
def calcola_interessi(importo_iniziale, tasso_interesse, periodi_investimento):
    importo_finale = importo_iniziale * (1 + tasso_interesse / 100) ** periodi_investimento
    return importo_finale
```


```python
print("Benvetuo nel Calolatore d'interessi!")

importo = float(input("Inserisci l'importo iniziale: "))
tasso = float(input("Inserisci il tasso d'interesse annuale (%): "))
periodo = int(input("Inserisci il periodo d'investimento (anni): "))

importo_finale = calcola_interessi(importo, tasso, periodo)

print(f"l'importo finale dopo {periodo} anni è di {importo_finale:.2f} euro.")
```

    Benvetuo nel Calolatore d'interessi!
    Inserisci l'importo iniziale: 200000
    Inserisci il tasso d'interesse annuale (%): 32
    Inserisci il periodo d'investimento (anni): 20
    l'importo finale dopo 20 anni è di 51583240.31 euro.
    

# Calcolo forza gravitazionale 2 pianeti #


```python
def forza_gravitazionale(m1, m2, r):
    #costante gravitazioamel
    G = 6.67430e-11 #N(m/gk)^2
    
    #Calcola dela forza gravitazionale
    F = (G * m1 * m2) / (r ** 2)
    
    return F
```


```python
#esempio di utilizzo
massa_terra = 5.972e24 #kg
massa_luna = 7.342e22 #kg
distanza_terra_luna = 384400000 #metri

forza = forza_gravitazionale(massa_terra, massa_luna, distanza_terra_luna)
print(f"forza gravitazionale tra la terra e la luna: {forza} Newton")
```

    forza gravitazionale tra la terra e la luna: 1.9804922390990566e+20 Newton
    

# calcola anagrammi #


```python
from itertools import permutations
k=0

def trova_anagrammi(parola):
    anagrammi = ["".join(p) for p in permutations(parola)]
                #unisce elementi in permutations di parola
                #for p in permutations(parola):
                #   anagrammi = ["".join(p)]
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
```

    Benvenuto nel risolutore di anagrammi!
    Inserisci una parola: edo
    gi anagrammi di 'edo' sono: '0'
    eod
    gi anagrammi di 'edo' sono: '1'
    deo
    gi anagrammi di 'edo' sono: '2'
    doe
    gi anagrammi di 'edo' sono: '3'
    oed
    gi anagrammi di 'edo' sono: '4'
    ode
    gi anagrammi di 'edo' sono: '5'
    

# dizionario #


```python
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
    
```

    Inserisci l'importo da convertire: 8329
    Inserisci la valuta di partenza: dollari
    Inserisci la valuta di destinazione: euro
    8329.0 dollari sono equivalenti a 7079.65 euro
    


```python
tassi_di_cambio["euro"]
```




    0.85




```python
# Chiedi all'utente di inserire una frase
frase = input("Inserisci una frase: ")

# Converti la frase in minuscolo per evitare proemi di maiuscole/minuscole
frase = frase.lower()

# Inizializza una lista di lettere dell'alfabeto
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Inizializza un dizionare per tenere traccia del conteggio delle lettere
conteggio_lettere = {}

# Itera attraverso ciascuna lettera dell'alfabeto
for lettera in alfabeto:
    #Conta quante volte apare a lettere dell'alfabeto
    conteggio = frase.count(lettera)
    
    #Aggiungi la lettera e il conteggio al dizionare se la lettera appare almeno una volta
    if conteggio > 0:
        conteggio_lettere[lettera] = conteggio
        
#stampa il conteggio delle lettere in un formato leggibile
for lettera, conteggio in conteggio_lettere.items():
    print(f"{lettera}: {conteggio}")
```

    Inserisci una frase: caiolamadonnadelsignore
    a: 4
    c: 1
    d: 2
    e: 2
    g: 1
    i: 2
    l: 2
    m: 1
    n: 3
    o: 3
    r: 1
    s: 1
    


```python
conteggio_lettere.items()
```




    dict_items([('a', 4), ('c', 1), ('d', 2), ('e', 2), ('g', 1), ('i', 2), ('l', 2), ('m', 1), ('n', 3), ('o', 3), ('r', 1), ('s', 1)])




```python
prodotti = {}
prodotti["pan bauletto"] = 2
prodotti["coca cola"] = 3
```


```python
prodotti
```




    {'pan bauletto': 2, 'coca cola': 3}




```python
from datetime import datetime
import pytz

print("Benvetuo nell'orologio mondiale")

# Definisci le città e i relativi fusi orari
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
```

    Benvetuo nell'orologio mondiale
    
    Città disponibili:
    New York
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): New York
    Londra
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): esci
    citta non valid. Riprova
    Tokyo
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): clear
    Sydney
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): f
    Rio de Janeiro
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): f
    
    Città disponibili:
    New York
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): f
    Londra
    Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): f
    Tokyo
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[1], line 20
         17 for citta in citta_fusi_orari.keys():
         18     print(citta)
    ---> 20     scelta_citta = input("Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): ").strip()
         21     if scelta_citta.lower() == 'esci':
         23         if scelta_citta in citta_fusi_orari.keys():
    

    File ~/anaconda3/lib/python3.11/site-packages/ipykernel/kernelbase.py:1175, in Kernel.raw_input(self, prompt)
       1171 if not self._allow_stdin:
       1172     raise StdinNotImplementedError(
       1173         "raw_input was called, but this frontend does not support input requests."
       1174     )
    -> 1175 return self._input_request(
       1176     str(prompt),
       1177     self._parent_ident["shell"],
       1178     self.get_parent("shell"),
       1179     password=False,
       1180 )
    

    File ~/anaconda3/lib/python3.11/site-packages/ipykernel/kernelbase.py:1217, in Kernel._input_request(self, prompt, ident, parent, password)
       1214             break
       1215 except KeyboardInterrupt:
       1216     # re-raise KeyboardInterrupt, to truncate traceback
    -> 1217     raise KeyboardInterrupt("Interrupted by user") from None
       1218 except Exception:
       1219     self.log.warning("Invalid Message:", exc_info=True)
    

    KeyboardInterrupt: Interrupted by user


# Dizionari e main #


```python
# Funzione principale può avere qualsiasi nome
def paolo():
    print("Mi chiamo Paolo")
    
if __name__ == "__main__" : #è una condizione logica che "si verifica sempre" e pertanto tutto ciò
                           #che risulta indentato a questa ocondizione viene eseguita
    paolo()
```

    Mi chiamo Paolo
    


```python
#Funzione principale puà avere uqalsiasi nome
def main():
    print("la funzione principale del codice è stata eseguita, in questa ufnzione possono essere presenti funzioni s")
    
if __name__ == "__main__": 
    main()
```

    la funzione principale del codice è stata eseguita, in questa ufnzione possono essere presenti funzioni s
    


```python
#main
# funzoone per il calcolo del BMI
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
```

    Benvenuto nella calcolatri bmi!
    Inserisci i tuo peso in chilogrammi: 62
    Inserisci la tua altezza in metri: 190
    il tuo BMI è 0.00, sei classificato come 'Sottopeso.'
    


```python
cibo_calorie = {
    "pizza": 285,
    "hamburger": 250,
    "insalata": 100,
    "panino del mc": 335,
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
    
#Funzione principale
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
```

    menù:
    
     1. aggiungi cibo consmato
    
     2. calcola calorie totali
    
     3 esci
    scegli un opzione: 3
    ok
    

Personaggi satorie e romanzi


```python
import random

# Liste di speci, classi, armi e abilità
speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

#Gebera un personaggio casuale
specie = random.choice(speci)
classe = random.choice(classi)
arma = random.choice(armi)
abilità_scelte = random.sample(abilità, random.randint(1,3))

#stampa il personaggio generato
print(f"Personaggio Fantasy Generato: ")
print(f"Specie: {specie}")
print(f"Classe: {classe}")
print(f"Arma: {arma}")
print(f"Abilità: {', '.join(abilità_scelte)}")
```

    Personaggio Fantasy Generato: 
    Specie: Elfo
    Classe: Mago
    Arma: Arco
    Abilità: Camuffamento, Incantesimi di guarigione, Estrazione mineraria
    


```python
import random 
# Liste di speci, classi, armi e abilità
speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

#ufnzone per creare un personaggio causale
def crea_personaggio():
    return {
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1,3))
    }

#funzione principale
def main():
    personaggio_generato = crea_personaggio()
    
    print("Personaggi Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")
        
#eseguire la funzione main quando il programma viene eseguito
if __name__ == "__main__":
    main()
```

    Personaggi Fantasy Generato:
    Specie: Orco
    Classe: Ladro
    Arma: Ascia
    Abilità: Magia dell'acqua, Incantesimi di guarigione
    


```python
import random 
# Liste di speci, classi, armi e abilità
speci = ["Elfo", "Umano" "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

#ufnzone per creare un personaggio causale
def crea_personaggio():
    personaggio={
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1,3))
    }
    return personaggio

#funzione principale
def main():
    personaggio_generato = crea_personaggio()
    
    print("Personaggi Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")
        
#eseguire la funzione main quando il programma viene eseguito
if __name__ == "__main__":
    main()
```

    Personaggi Fantasy Generato:
    Specie: UmanoNano
    Classe: Guerriero
    Arma: Arco
    Abilità: Camuffamento
    

# La letteratura combinatoria #


```python
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
```

    Generatore di personaggi per romanzi
    Inserisci il nome del personaggio: edoardo
    Nome: edoardo
    Aspetto Fisico: occhi cazzurri
    Aspetto Personale: ottimista
    Sfondo: commerciale
    Motivazione: vendetta
    

# citazione del giorno #


```python
#database di citazioni
citazioni = [
    "lao",
    "A",
    "B",
    "C",
]

#Funzione per generare una citazione casuale
def genera_citazione():
    return random.choice(citazioni)

#funzione principale
def main():
    print("Benvevuto nel generatore di citazioni")
    input("Premi invio per ottenere una citazione causale...")
    
    citazione = genera_citazione()
    print(f"citazione del giorno: {citazione}")
    
if __name__ == "__main__":
    main()
```

    Benvevuto nel generatore di citazioni
    Premi invio per ottenere una citazione causale...
    citazione del giorno: Non sforzare troppo qualcosa.. perché forse è shit - Edoardo
    

# GENERATORE FRASI DA INFLUENCER #


```python
import random
#lista di frammenti di citazioni famose (più brevi)
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
#funzione per crare nuove citazioni rimenscolando i frammenti
def crea_citazione():
    num_frammenti = random.randint(5,7) #scegli un numero casuale di frammenti da utilizzare
    citazione_rimescolata = random.sample(frammenti, num_frammenti)
    nuova_citazione = " ".join(citazione_rimescolata)
    return nuova_citazione

#genera una nuova nuova citazione
nuova_citazione = crea_citazione()
print("Nuova citazione generata:")
print(nuova_citazione)
```

    Nuova citazione generata:
    dio come va? blabla madonna lalalal blululullulu
    


```python
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
#funzione per crrare nuove citazioni mescolando i frammenti
def crea_citazione():
    num_frammenti = random.randint(4,7) #scegli un umero casuale di frammenti da utilizzare
    citazione_rimescolata = random.sample(frammenti, num_frammenti)
    nuova_citazione = " ".join(citazione_rimescolata)
    return nuova_citazione
    
#genera una nuova citazione
def main():
    nuova_citazione = crea_citazione()
    print("Nuova citazione generata:")
    print(nuova_citazione)
    
if __name__ == "__main__":
    main()
```

    Nuova citazione generata:
    dio blululullulu madonna blabla pipipipip come va? ciao
    


```python
import random

#liste di parole predefinite per la generazione dlela poesia
aggettivi = ["dolce", "serena", "profondo", "luminoso", "gentile"]
sostantivi = ["amore", "mare", "cielo", "vento", "sogno"]
verbi = ["danza", "splende", "abbraccia", "canta", "sorride"]

#genera una poesia casuale
def genera_poesia():
    verso1 = f"Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}."
    verso2 = f"Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}."
    verso3 = f"Nel {random.choice(aggettivi)} {random.choice(sostantivi)}"
```