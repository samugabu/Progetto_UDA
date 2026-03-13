# Sistema di Monitoraggio per l'Efficienza Energetica 

Questo progetto è stato sviluppato come **Unità di Apprendimento (UdA) sulla Sostenibilità Ambientale**. L'obiettivo è la realizzazione di un sistema IoT per il monitoraggio oggettivo dei parametri ambientali interni, volto a ottimizzare i consumi energetici e promuovere comportamenti sostenibili.

##  Descrizione del Progetto
Il sistema si basa sul paradigma di sincronizzazione **Produttore-Consumatore**:
1.  **Produttore (Arduino):** Un'unità di acquisizione che traduce i fenomeni fisici in segnali digitali e li invia tramite comunicazione seriale.
2.  **Consumatore (Python):** Un'unità di analisi che riceve i dati, li elabora, gestisce lo storico in formato CSV e visualizza i risultati in tempo reale su un'interfaccia grafica.

##  Hardware Utilizzato
* **Microcontrollore:** Arduino
* **Sensore:** DHT11 (Temperatura e Umidità)
* **Segnalazione Visiva:** LED (rosso, verde e blu) per indicazione dello stato di comfort o allerta.
* **Segnalazione Acustica:** **Buzzer** (aggiunto per segnali acustici in caso di superamento soglie critiche).
* **Comunicazione:** Cavo USB (Protocollo Seriale).

##  Stack Tecnologico
* **Arduino IDE:** Utilizzo della libreria "DHT sensor library" per la gestione del sensore.
* **Python 3.x:** Sviluppo in Visual Studio Code.
    * `Dear PyGui`: Per la creazione dell'interfaccia grafica (GUI).
    * `pyserial`: Per la gestione della comunicazione seriale.
    * `csv`: Per il salvataggio dello storico dei dati.

##  Logica di Controllo e Alert
Il sistema monitora la temperatura e reagisce in base a tre scenari principali:

| Stato | Condizione | LED | Buzzer | Azione Suggerita |
| :--- | :--- | :--- | :--- | :--- |
| **Caldo** | Temperatura > Soglia Max(22) | Rosso | **ON (Beep)** | "Riscaldamento eccessivo / Aprire finestre" |
| **Comfort** | Temperatura Ottimale | Verde | **OFF** | "Ambiente ottimale" |
| **Freddo** | Temperatura < Soglia Min(14) | Blu | **ON (Beep)** | "Temperatura bassa / Controllare isolamento" |

## Team del progetto

**Progetto svolto da:** Matteo Regio, Samuele Gaburri e Daniele Bianolini
