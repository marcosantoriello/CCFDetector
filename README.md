# CCFDetector: Using ML Against Credit Card Frauds
Progetto conclusivo relativo al corso di Fondamenti di Intelligenza Artificiale.
### Obiettivo
L'obiettivo del progetto è la realizzazione di un sistema di Machine Learning
(più nello specifico di un classificatore) in grado di determinare se una 
transazione effettuata con carta di credito sia fraudolenta, oppure lecita.

### Struttura della Repository
- Nella directory root, è presente il notebook che attraversa e dettaglia tutto
  il processo di progettazione, costruzione e valutazione del modello.
- In *Application* è presente un'app demo, purtroppo non terminata per motivi
  puramente legati al tempo.
- In *Deliverables* sono presenti documentazione e presentazione finali del progetto.
- In *Documentation* è presente il file in formato .tex della documentazione, oltre
  che le varie immagini presenti in essa.
- In *Presentation* sono presenti gli assets utilizzati per la presentazione.

### Replicazione del contenuto del repo
**Requisiti**<br>
- Python 3
- PyCharm IDE (consigliato)
- Dataset (vedi *Caricamento Dataset*)

Per replicare il contenuto di questo repo, basta effettuare una *clone* da GitHub
ed aprirla con un IDE come PyCharm, che consiglio. Per l'esecuzione del notebook
è sufficiente utilizzare in sequenza il comando *Run* presente nell'IDE oppure,
 se presente, il comando *Run All*. L'importante è eseguire le varie celle nell'ordine
in cui sono disposte nel notebook.<br>

**Caricamento Dataset**<br>
Il **dataset** è disponibile al seguente link: https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions <br>
A causa delle sue enormi dimensioni, nemmeno una volta compresso può essere caricato.<br>
Una volta scaricato, importare nella directory principale del repo scaricato solo
il file *credit_card_transactions-ibm_v2.csv*.

**Ulteriori informazioni**<br>
Nella cartella *Application*, come accennato prima, è presente il modello esportato,
insieme allo scaler e al LabelEncoder addestrati. Questi servono per la demo chiamata
 *app.py* che, purtroppo, non è terminata e, dunque, attualmente non funzionante.