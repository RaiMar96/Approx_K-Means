# K-Means Clustering

<!--![simulation result](https://archivio.unict.it/sites/default/files/images/orizzontale-grigio.png)-->

Tesina finale relativa al corso : INTERNET OF THINGS BASED SMART SYSTEMS - UniCT.

Questo Tool implementa il  [K-means clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering) , in versione precisa o approssimata. Il grado di approssimazione viene introdotto tramite i parametri forniti in ingresso allo script ( approx_factor , max_iterations ). Questo permette di implementare la tecnica 'loop perforation' di Approximate Computing.

La struttura della repository è la seguente :

- **dataset** : contiene i file _.csv_ usati come sorgente dati per la computazione ( la struttura di tali file sarà descritta alla sezione apposita ).
- **src** : contine il codice sorgente dell'applicazione _.py_ .
- **output** : contiene il file _cluster.pdf_ rappresentante il plot dei risultati della clusterizzazione, il file _ReadableResults.csv_ rappresentante l'output dell'esecuzione dell'algoritmo in formato leggibile, il file _results.csv_ rappresentante l'output dell'esecuzione dell'algoritmo in formato raw, utilizzabile per la computazione DNN.

Tale tool può essere utilizzato come kernel approssimato nelle **DNN** che si basano su clusterizzazione dei dati per implementazioni in device a risorse limitate.

## Dipendenze

Il Tool è stato implementato in **_python_** ( si pressupone che siano già stati installati **python3** e **pip3**; in caso contrario [download](https://www.python.org/downloads/))

Per una corretta esecuzione è necessario installare i seguenti moduli :

- **pandas**
- **numpy**
- **matplotlib**
- **scipy**

L'installazione delle dipendenze deve essere eseguita tramite i seguenti comandi :

```[shell]
pip3 install pandas
pip3 install numpy
pip3 install matplotlib
pip3 install scipy

```

## Struttura Input File

I dati di input per la computazione devono essere posizionati nella directory _dataset_. Tali dati devono essere forniti come file .csv  ( a scopo di test vengono forniti i file _test1.csv_, _test2.csv_ ). Tale file deve essere fornito come parametro d'ingresso al momento dell'esecuzione dello script.

Nel caso di file con dataset bi-dimensionale, il file deve presentare i seguenti headers per le colonne : **V1** , **V2**.

Nel caso di file con dataset mono-dimensionale, il file deve presentare il seguente header per la colonna : **V1** .

Per i casi descritti precedentemente il tool fornisce il pieno supporto alla stampa dei risultati. Nel caso di dataset  n-dimensionali (con n > 2), la stampa è effettuata solo nelle 2 dimensioni x e y. 

La struttura dei file n-dimensionali deve seguire la convenzione per gli headers descritta in precedenza : **V1**,..,**Vn**

## Struttura Output File

Il file di output in formato raw(_results.csv_), fornisce le informazioni utili alla fine della computazione. Tali informazioni essenziali sono il Codebook e i cluster-index relativi a tutti i punti del dataset. Il Codebook è rappresentato dagli indici relativi ai centroidi che definiscono i cluster e le coordinate stesse dei centroidi. I cluster-index relativi ai punti definiscono a quale cluster essi appartengono. Questo ci garantisce un fattore di compressione di 32/log2(k), cioè rappresentiamo l'informazione relativa ai punti solamente tramite la codifica dell'indice del cluster, piuttosto che un float a 32 bit.
Nel file results.csv, vengono conseguentemente rappresentati prima gli indici e le coordinate dei centroidi e a seguire, per ogni punto del dataset, l'indice del suo cluster. 

## Avvio

Per avviare il tool , lanciare da riga di comando i seguenti comandi (validi sia per bash linux che powershell windows)  all'interno della directory principale :

```[python]
cd ./src
python3 k-means_approx.py

```

A seguito di ciò il programma richiederà l'inserimento dei 3 seguenti valori :

- **Enter cluster size :** richiede di inserire un valore intero che rappresenta la dimensione del cluster.
- **Enter approximation factor 0 < appr_factor < 1 :**richiede di inserire un valore float compreso tra 0 e 1 che rappresenta il fattore di approssimazione.
- **Enter MAX iteration number :** richede il valore massimo delle iterazioni potenzialmente eseguibili dall'algoritmo (potrebbe convergere con un numero minore di iterazioni).
- **Enter input file name ( .csv ) :** richiede il nome del file.csv di input presente in dataset.
- **Do you want to visualize the result? ( yes or no ) :** richiede la digitazione di "yes" per visualizzare il plot dei risultati dinamicamente a fine esecuzione.

## Esempio

Esempio di esecuzione con i seguenti parametri :

- cluster size = **5**
- approximation_factor = **0.002**
- max iter = **50**
- input file = **test2.csv** (dataset a due dimensioni)

il risultato dell'esecuzione è rappresentato dalla seguente immagine :

![simulation result](https://github.com/RaiMar96/IoT_project_2k19-20/blob/master/example/example-bi.png)

Esempio di esecuzione con i seguenti parametri :

- cluster size = **5**
- approximation_factor = **0.002**
- max iter = **50**
- input file = **test1.csv** (dataset a una dimensione)

il risultato dell'esecuzione è rappresentato dalla seguente immagine :

![simulation result](https://github.com/RaiMar96/IoT_project_2k19-20/blob/master/example/example-mono.png)
