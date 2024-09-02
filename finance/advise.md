Correlato
Qual è il miglior investimento in termini di tempo che uno studente universitario con una mentalità quantitativa può fare se desidera alla fine lavorare in Fondi Speculativi (hedge funds) e prosperare in quegli ambienti?
Apri un conto di trading (questo potrebbe richiedere del tempo, quindi inizia con questo prima)
Scegli un settore di tuo interesse.
Scegli 4 aziende in quel settore, stampa i loro rapporti annuali e leggi tutto dalla A alla Z.
Qualunque cosa tu non capisca, segnalo con una penna colorata e annota in un blocco note.
Dopo aver finito di rivedere tutte e 4 le aziende, vai su Internet e cerca le definizioni di tutti i bit che non hai capito. Dato che hai 4 aziende del settore simili, ci dovrebbero essere sovrapposizioni.
Quindi vai in Microsoft Excel e scrivi un sacco di loro metriche che hai trovato nel loro rapporto annuale. Dato che sono le stesse aziende del settore, ci si aspetta metriche simili. Utile per azione, debito, attività, capitalizzazione di mercato, avviamento, margine di profitto, fatturato. Qualunque sia anche elencato nel rapporto annuale. Niente da internet. Quando hai finito, hai un sacco di parametri finanziari alla tua sinistra e da B a E eccellono nelle tue quattro aziende. Hai fatto un'analisi comparabile dell'azienda (CCA), spesso utilizzata nelle aziende.
Scegli alcune metriche che ti interessano per tutte e 4 le aziende. Ottieni dati storici di queste metriche.
Vai su Yahoo o Bloomberg e scarica i dati storici del prezzo delle azioni delle 4 aziende.
Se hai scelto il settore aereo, ottieni ulteriori variabili correlate a questo, come la quantità di passeggeri volati in Europa o negli Stati Uniti o persino in tutto il mondo. O se si tratta di una società mineraria, aggiungi la storia del prezzo dell'oro.
Scegli uno strumento statistico, MATLAB, R, Anteprima, Excel e imposta una regressione semplicistica. Y è il prezzo delle azioni, la tua X è la metrica fondamentale che hai trovato nel rapporto annuale e le variabili aggiuntive.
Esegui la regressione e studia i risultati. Stai controllando quanto la tua X spiega Y. Probabilmente vedrai un mucchio di definizioni di cui non hai mai sentito parlare, R al quadrato, R al quadrato regolato e così via.
Prendi un libro di econometria e comprendi cosa significano queste cose. R-quadrato, eteroscedasticità, correlazione automatica, aggiustamento per distorsioni nei dati e così via.
Segui le lezioni che hai appreso e fai un'altra analisi di regressione, scoprirai che sarai in grado di aumentare il tuo R-quadrato regolato. Pensi di aver trovato un risultato migliore. Ti sbagli, anche se i risultati indicano un risultato migliore, tutto ciò che hai fatto è stato il dragaggio dei dati. Rendere i dati più adatti. È così che inizia una carriera di "vendite".
Imposta un modello di trading automatico (probabilmente il tuo broker ne ha uno o prova un trader ninja o crea qualcosa tu stesso) che acquista o vende lo stock (uno dei 4 che hai scelto) in base al momento in cui le tue variabili vengono introdotte / pubblicate di nuovo. Questi sono annunci trimestrali o mensili. Esegui una simulazione.
Ti renderai conto che la tua regressione iniziale non includeva né il volume né le commissioni. Ti renderai anche conto quando automatizzi, il tempismo è essenziale perché la tua offerta / domanda cambia costantemente.
Molto probabilmente i tuoi risultati saranno merda.
Presumo che tu voglia segnali più frequenti. I segnali precedenti erano solo mensili o trimestrali. Controlla come viene calcolato RSI (un indicatore tecnico di merda). Aggiungi questa formula nel modello di trading API e imposta un segnale di acquisto su RSI 30 e vendi su RSI 70. Riceverai shitload di segnali di vendita buy e, ancora una volta, i tuoi risultati saranno merda. Con alcune analisi di regressione, scoprirai che 30–70 non sono l'ideale, ma è più simile a 25–80. Tuttavia, l'hai fatto in base alla regressione storica (che racconta solo il passato, quindi non hai basi statistiche per usarlo per il futuro ...).
Quindi prendi un altro libro di Econometria e guarda come puoi creare distribuzioni in modo da poterne campionare i dati. Creare una distribuzione normale e una non normale. Scopri come eseguire un bootstrap (calcola punti dati extra se non hai molti dati storici). Per la distribuzione non normale e normale, si campionano anni di dati. Ora hai dati "futuri" per convalidare il tuo modello.
Finora, hai testato un "modello commerciale con indicatori fondamentali e tecnici", basato su dati storici, ora testalo su dati campionati per una previsione corretta. Ti renderai conto che il risultato della distribuzione normale rispetto a quella non normale sarà significativamente diverso. Pensa .. cosa pensi che vada meglio?
Questi 19 passaggi comprendono la comprensione di BASE dell'analisi finanziaria, analisi comparabili dell'azienda, semplici analisi fondamentali e tecniche, nonché analisi di regressione e come manipolare i dati.

Questi passaggi non superano il livello BSc del primo anno, sfortunatamente molti studenti o laureati che vedo saltare tutto questo e direttamente dal vuoto vogliono mettere insieme algoritmi di apprendimento automatico senza una comprensione di base di economia, finanza ed econometria.

Inizia con le basi, indipendentemente da quanto sia noioso. Non dimenticherai mai la tua fondazione.

Vuoi essere bravo in finanza? Devi essere in grado di comprendere appieno un rapporto annuale di un'azienda, il suo impatto macro e micro, così come la matematica dietro di esso. Essere in grado di sfidare attivamente un commercialista sulle sue figure e quantistica pura sui suoi modelli.

Ecco come ti distingui in mezzo alla folla e come sarai diverso da tutti gli altri.
