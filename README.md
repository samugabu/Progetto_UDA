# Sistema di Monitoraggio per l'Efficienza Energetica 🌡️🌱

Questo progetto nasce come **Unità di Apprendimento (Uda) sulla Sostenibilità Ambientale**. L'obiettivo è realizzare un sistema IoT completo per il monitoraggio dei parametri ambientali interni, al fine di ottimizzare i consumi energetici e promuovere comportamenti consapevoli.

## 📌 Descrizione del Progetto
Il sistema adotta il paradigma **Produttore-Consumatore** per gestire il flusso di dati:
1.  **Produttore (Arduino):** Acquisisce dati di temperatura e umidità e li invia tramite seriale.
2.  **Consumatore (Python):** Riceve i dati, li elabora, li salva su file CSV e li visualizza in tempo reale su una GUI.

## 🛠️ Hardware Utilizzato
* **Microcontrollore:** Arduino
* **Sensore:** DHT11 (Temperatura e Umidità)
* **Segnalazione Visiva:** LED (Rosso e Verde) per indicazione stato comfort/alert
* **Segnalazione Acustica:** Buzzer (Attivato in caso di temperature critiche - Alte/Bassee)
* **Comunicazione:** Cavo USB per protocollo Seriale

## 💻 Software e Librerie
* **Arduino IDE:** Libreria `DHT sensor library`
* **Python 3.x:**
    * `Dear PyGui`: Per l'interfaccia grafica
    * `pyserial`: Per la comunicazione con Arduino
    * `threading`: Per la gestione dei processi paralleli
    * `pandas` / `csv`: Per il salvataggio dei dati

## ⚙️ Strategie di Sincronizzazione e Implementazione
Il progetto implementa diverse strategie per garantire l'efficienza e la stabilità del sistema:

* **Delay-less Coding (Arduino):** L'acquisizione dei dati avviene ogni 10-20 secondi utilizzando la funzione `millis()` al posto di `delay()`, evitando il blocco del microcontrollore.
* **Protocollo a Pacchetti:** I dati vengono inviati come stringhe terminate dal
* 
