# Sistema di Monitoraggio per l'Efficienza Energetica 🌡️🌱

[cite_start]Questo progetto nasce come **Unità di Apprendimento (Uda) sulla Sostenibilità Ambientale**[cite: 2]. [cite_start]L'obiettivo è realizzare un sistema IoT completo per il monitoraggio dei parametri ambientali interni, al fine di ottimizzare i consumi energetici e promuovere comportamenti consapevoli[cite: 3, 5].

## 📌 Descrizione del Progetto
[cite_start]Il sistema adotta il paradigma **Produttore-Consumatore** per gestire il flusso di dati[cite: 7]:
1.  [cite_start]**Produttore (Arduino):** Acquisisce dati di temperatura e umidità e li invia tramite seriale[cite: 8, 14].
2.  [cite_start]**Consumatore (Python):** Riceve i dati, li elabora, li salva su file CSV e li visualizza in tempo reale su una GUI[cite: 21, 32, 38].

## 🛠️ Hardware Utilizzato
* [cite_start]**Microcontrollore:** Arduino [cite: 10]
* [cite_start]**Sensore:** DHT11 (Temperatura e Umidità) [cite: 10]
* [cite_start]**Segnalazione Visiva:** LED (Rosso e Verde) per indicazione stato comfort/alert [cite: 25]
* **Segnalazione Acustica:** Buzzer (Attivato in caso di temperature critiche - Alte/Bassee)
* [cite_start]**Comunicazione:** Cavo USB per protocollo Seriale [cite: 11]

## 💻 Software e Librerie
* [cite_start]**Arduino IDE:** Libreria `DHT sensor library` [cite: 17]
* **Python 3.x:**
    * [cite_start]`Dear PyGui`: Per l'interfaccia grafica [cite: 13]
    * `pyserial`: Per la comunicazione con Arduino
    * [cite_start]`threading`: Per la gestione dei processi paralleli [cite: 23]
    * [cite_start]`pandas` / `csv`: Per il salvataggio dei dati [cite: 32]

## ⚙️ Strategie di Sincronizzazione e Implementazione
[cite_start]Il progetto implementa diverse strategie per garantire l'efficienza e la stabilità del sistema:

* [cite_start]**Delay-less Coding (Arduino):** L'acquisizione dei dati avviene ogni 10-20 secondi utilizzando la funzione `millis()` al posto di `delay()`, evitando il blocco del microcontrollore[cite: 19, 31].
* [cite_start]**Protocollo a Pacchetti:** I dati vengono inviati come stringhe terminate dal carattere newline (`\n`), facilitando la sincronizzazione della lettura lato PC[cite: 12, 19].
* **Multithreading (Python):** La lettura della porta seriale avviene su un thread separato rispetto alla GUI. [cite_start]Questo evita che l'interfaccia si blocchi durante l'attesa dei dati[cite: 23, 37].
* [cite_start]**Gestione Buffer:** Viene utilizzata una coda (`queue`) per trasferire in modo sicuro i dati tra il thread di lettura e quello di visualizzazione[cite: 23].

## 🚨 Logica di Alert
| Stato | Condizione | LED | Buzzer | [cite_start]Suggerimento GUI [cite: 29] |
| :--- | :--- | :--- | :--- | :--- |
| **Critico (Caldo)** | Temp > Soglia Max | [cite_start]Rosso [cite: 26] | ON | "Riscaldamento eccessivo - Aprire finestre" |
| **Comfort / Eco** | Temp Ottimale | [cite_start]Verde [cite: 27] | OFF | "Ambiente Ottimale" |
| **Stand-by / Freddo**| Temp < Soglia Min | [cite_start]Spenti [cite: 28] | ON | "Temperatura bassa - Accendere riscaldamento" |

## 📂 Struttura del Repository
```text
├── Arduino/
│   └── monitoraggio_temperatura.ino  # Codice sorgente Arduino [cite: 43]
├── Python/
│   ├── main_gui.py                   # Applicazione Dear PyGui [cite: 44]
│   └── data_logger.py                # Gestione salvataggio CSV
├── Data/
│   └── storico_misure.csv            # Esempio di file dati salvato [cite: 45]
└── README.md                         # Relazione tecnica del progetto
