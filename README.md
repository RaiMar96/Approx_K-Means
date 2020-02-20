# K-Means Clustering
Tesina finale per relativa al corso : INTERNET OF THINGS BASED SMART SYSTEMS - UniCT. <br>
Questo Tool implementa il  [K-means clustering alogrith](https://en.wikipedia.org/wiki/K-means_clustering) , in versione precisa o approssimata. Il grado di approssimazione viene introdotta tramite i parametri forniti in ingresso allo script ( approx_factor , max_itartions ). Questo permette di implementare la tecnica di Approximate Computing di loop perforation.

La struttura della repository è la seguente :
- **dataset** : contiene i file _.csv_ usati come sorgente dati per la computazione ( la struttura di tali file sarà descrtitta alla sezione apposita ).
- **src** : contine il codice sorgente dellìapplicazione _.py_ .
- **output** : contiene il file _cluster.png_ rappresentante il plot dei risultati della clusterizzazione.

Tale tool può essere utilizzato come kernel approssimato in **DNN** che si basano su clusterizzazione dei dati.

## Dipendenze
Il Tool è stato implementato in _python_ ( si pressupone che siano già installati **python3** e **pip3** in caso contrario [download](https://www.python.org/downloads/)). 
Per una corretta eseczuione è necessario installare i seguenti moduli :
- **pandas**
- **numpy**
- **matplotlib**

L'installazione delle dipendenze deve essere eseguita tramite i seguenti comandi :
```
pip3 install pandas
pip3 install numpy
pip3 install matplotlib

```
## Struttura Input File
I dati di input per la computazione come detto in alto devono essere posizionati nella directory _dataset_ , tali dati devono essere forniti come file .csv  ( a scopo di test vengono fotniti i file _test1.csv_, _test2.csv_ ). Tale file verrà fornito come parametro d'ingresso al momento dell'esecuzione dello script.

Nel caso di file bi-dimensionale (come il file di test proposto), il file deve presentare i seguenti header per le colonne : **V1** , **V2**
Nel caso di file mono-dimensionale (come il file di test proposto), il file deve presentare i seguenti header per le colonne : **V1** 

## Avvio
Per avviare il tool , lanciare da riga di comando i seguenti (valide sia per bash linux che poweshell windows) comandi all'interno della directory principale :

```
cd ./src
python3 k-means_approx.py

```
A seguito di ciò il programma richiederà l'inserimento dei 3 seguenti valori :
- **Enter cluster size :** richiede di inserire un valore intero che rappresenta la dimensione del cluster.
- **Enter approximation factor 0 < appr_factor < 1 :**richiede di inserire un valore compreso tra 0 e 1 che rappresenta il fattore di approssimazione.
- **Enter max iteration number :** richede il valore massimo di iterazioni eseguite dall'algoritmo.
- **Enter input file name ( .csv ) :** richiede il nome del file.csv di input presente in dataset.

## Esempio
Esempio di Esecuzione con i seguenti parametri :
- cluster size = **5**
- approximation factor = **0.002**
- max iter = **50**
- input file = **test2.csv**

il risultato dell'esecuzione è rappresentato dalla seguente immagine :

![simulation result](https://github.com/RaiMar96/IoT_project_2k19-20/blob/master/example/example.png)
