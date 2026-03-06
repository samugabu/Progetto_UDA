# Sistema di Monitoraggio per l'Efficienza Energetica 🌡️🌱

Questo progetto è stato sviluppato come **Unità di Apprendimento (UdA) sulla Sostenibilità Ambientale**. L'obiettivo è la realizzazione di un sistema IoT per il monitoraggio oggettivo dei parametri ambientali interni, volto a ottimizzare i consumi energetici e promuovere comportamenti sostenibili.

## 📌 Descrizione del Progetto
Il sistema si basa sul paradigma di sincronizzazione **Produttore-Consumatore**:
1.  **Produttore (Arduino):** Un'unità di acquisizione che traduce i fenomeni fisici in segnali digitali e li invia tramite comunicazione seriale.
2.  **Consumatore (Python):** Un'unità di analisi che riceve i dati, li elabora, gestisce lo storico in formato CSV e visualizza i risultati in tempo reale su un'interfaccia grafica.

## 🛠️ Hardware Utilizzato
* **Microcontrollore:** Arduino
* **Sensore:** DHT11 (Temperatura e Umidità)
* **Segnalazione Visiva:** LED (Rosso e Verde) per indicazione dello stato di comfort o allerta.
* **Segnalazione Acustica:** **Buzzer** (aggiunto per segnali acustici in caso di superamento soglie critiche).
* **Comunicazione:** Cavo USB (Protocollo Seriale).

## 💻 Stack Tecnologico
* **Arduino IDE:** Utilizzo della libreria "DHT sensor library" per la gestione del sensore.
* **Python 3.x:** Sviluppo in Visual Studio Code.
    * `Dear PyGui`: Per la creazione dell'interfaccia grafica (GUI).
    * `pyserial`: Per la gestione della comunicazione seriale.
    * `threading` & `queue`: Per implementare il paradigma consumatore su thread separati.
    * `csv`: Per il salvataggio del log storico dei dati.

## ⚙️ Strategie di Sincronizzazione
Per garantire un sistema fluido e reattivo, sono state adottate le seguenti tecniche:
* **Delay-less Coding:** Su Arduino, la funzione `millis()` gestisce il campionamento (ogni 10-20 secondi) senza bloccare l'esecuzione del codice.
* **Protocollo a Pacchetti:** I dati vengono inviati come stringhe terminate da newline (`\n`) per sincronizzare correttamente la lettura lato PC.
* **Multithreading:** La lettura della seriale e l'aggiornamento della GUI viaggiano su thread distinti per evitare rallentamenti o freeze dell'interfaccia.

## 🚨 Logica di Controllo e Alert
Il sistema monitora la temperatura e reagisce in base a tre scenari principali:

| Stato | Condizione | LED | Buzzer | Azione Suggerita |
| :--- | :--- | :--- | :--- | :--- |
| **Alert Critico** | Temperatura > Soglia Max | Rosso | **ON (Beep)** | "Riscaldamento eccessivo / Aprire finestre" |
| **Comfort / Eco** | Temperatura Ottimale | Verde | OFF | "Ambiente ottimale" |
| **Stand-by / Freddo** | Temperatura < Soglia Min | Spenti | **ON (Beep)** | "Temperatura bassa / Controllare isolamento" |

## 📂 Struttura del Repository
* `/arduino`: Contiene lo sketch `.ino` per la lettura del sensore e la gestione di LED e Buzzer.
* `/python`: Contiene lo script per la GUI in Dear PyGui e la gestione del thread consumatore.
* `/data`: Esempio di file `storico.csv` con timestamp, temperatura e umidità.
* `README.md`: Relazione tecnica e documentazione del progetto.

---
*Progetto realizzato per sensibilizzare sull'uso consapevole dell'energia attraverso la tecnologia.*
