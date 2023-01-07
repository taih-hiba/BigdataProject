# BIG DATA Project

## I.	Architecture de la solution

![image](https://user-images.githubusercontent.com/78708481/211147804-2ba829ca-59e2-4344-aacd-478ccc25e8d1.png)

Au cours de ce projet on travaillera avec apache Kafka spark streaming et ML et le stockage sur HBase. On travaillera avec Twitter API afin d’avoir un flux de données en temps réel.
Comme vous pouvez le voir sur le graphique ici, le flux Twitter est ingéré par Kafka et envoyé sous forme de signaux par les producteurs de Kafka, puis Spark Streaming peut choisir de recevoir les signaux Kafka en fonction des sujets et sous forme de flux distribués. 
Nous présentons une architecture de bout en bout sur la façon de diffuser des données à partir de Twitter, de les nettoyer et d'appliquer un modèle simple d'analyse des sentiments pour détecter la polarité et la subjectivité de chaque tweet.

## II. Préparation de l’environnement
On commence par télécharger Docker Desktop à partir du site suivant : Docker Desktop

![image](https://user-images.githubusercontent.com/78708481/211148970-0aaba6ac-c681-4ee2-a1ad-e32a9c93876f.png)

Par la suite, on crée un nouveau dossier dans lequel on va créer un nouveau fichier docker-compose.yml, il est composé de 7 images, « Kafka », « zookeeper », « zeppelin », « Hbase », « Spark-master ».

![image](https://user-images.githubusercontent.com/78708481/211149025-f62217de-0998-44ea-9bae-ceafd03010ed.png)

![image](https://user-images.githubusercontent.com/78708481/211149032-61911dea-9e02-4d01-b4ae-8b3d8813fbd2.png)

Pour lancer le container, on tape la commande « docker-compose up » 

![image](https://user-images.githubusercontent.com/78708481/211149054-81ce4f9a-147e-496f-af24-abdafa3e7aa0.png)

Voici les différents services sont en mode « running »

![image](https://user-images.githubusercontent.com/78708481/211149066-c2704ced-fae8-48c0-820c-1d7cda6c1a98.png)

On peut aussi visualiser leurs états dans docker desktop

![image](https://user-images.githubusercontent.com/78708481/211149085-7778b5cd-8bbb-49a2-90a2-dc602c62b8b0.png)

## III.	Ingérer des données à l'aide de Kafka
Cette partie concerne l'envoi de tweets depuis l'API Twitter. Pour ce faire, suivez les instructions illustrées dans cette partie.
L'avantage d'utiliser Kafka avec Twitter Stream est la tolérance aux pannes. Nous avons un premier module The Producer qui collecte les données de Twitter, puis les enregistre, et un autre module The Consumer qui lit les logs puis traite les Data. Le producteur vient d'enregistrer les données sous forme de journaux dans la file d'attente et le consommateur est responsable de la lecture de ces journaux et de leur traitement.
Comme vous le savez, pour diffuser des données depuis Twitter, vous avez besoin d'un compte de développeur Twitter. Vous aurez besoin d’un compte de développeur Twitter et vos informations d'identification
Avant de pouvoir écrire vos premiers événements, vous devez créer un topic Kafka. Ouvrez une session de terminal de kafka et exécutez : 
#### kafka-topics.sh --create –topic twitter-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4

![image](https://user-images.githubusercontent.com/78708481/211149234-7366047b-3162-4a54-b521-e800478e0dc3.png)

twitter-topic: c'est le nom du topic 

localhost:9092: l'adresse du brocker kafka

Pour vérifier la création du topic ou bien afficher la liste des topics existants sur kafka on utilise la commande suivante
#### kafka-topics.sh --list --bootstrap-server localhost:9092

![image](https://user-images.githubusercontent.com/78708481/211149276-aa78fdfb-b1c5-4997-8a5a-be337f311188.png)

### 1.	Kafka Producer

Créer un producteur Kafka. L'objectif est de se connecter à l'API Twitter et d'obtenir les tweets et les publier dans le topic qu'on a créé.

 Ouvrez le kafka-producer.py.
 
 ![image](https://user-images.githubusercontent.com/78708481/211149402-9383ed1b-4acc-48b0-b086-68b6d26bc7bf.png)

Ici on spécifie les paramètres de l’api twitter

![image](https://user-images.githubusercontent.com/78708481/211149418-332ad1c3-bbd6-42c7-8318-818306c53b6f.png)

On s’authentifie à l’API à l’aide de la bibliothèque tweepy et on crée le producer en spécifiant l’adresse et le port du broker. « localhost :9092 ».

![image](https://user-images.githubusercontent.com/78708481/211149438-da22e10b-5c4b-4fb9-aa36-44dfdc250c06.png)

On envoie les données au Producer en spécifiant le nom du topic.

![image](https://user-images.githubusercontent.com/78708481/211149454-d65e9be4-dd42-4667-888f-0cfa9ab1f82f.png)


### 2.	Kafka Consumer
Pour vérifier que les données sont présentes dans le topic on exécute le kafka-consummer .
#### kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic twitter-topic — group my-first-app --from-beginning

![image](https://user-images.githubusercontent.com/78708481/211149519-e6cf72c4-99d1-4eed-8294-2f3db6e86ea4.png)

## IV.	Entrainement du modèle avec Spark ML

Il peut y avoir de nombreuses façons différentes d'effectuer l'analyse des sentiments, certaines bibliothèques fournissent une fonction d'analyse des sentiments prête à l'emploi. On a donc décider d’entrainer plusieurs modèles, qu’on pourrait appliquer aux tweets qu’on a rassemblés. Le modèle avec des performances décentes, sera utilisé sur les données de l’API. 
Pour utiliser PySpark dans Jupyter Notebook, on doit configurer le pilote PySpark contenant des libraries ml qui introduit des modeles de classification et de featuring.

![image](https://user-images.githubusercontent.com/78708481/211149646-ded038cb-ed67-4cc8-954c-1aba4b074420.png)


La première étape est la création de SparkContext. SparkContext est nécessaire lorsque nous voulons exécuter des opérations dans un cluster. SparkContext indique à Spark comment et où accéder à un cluster. 

![image](https://user-images.githubusercontent.com/78708481/211149656-cdb19bb1-2fe4-422d-83ad-78155bb5dc81.png)

![image](https://user-images.githubusercontent.com/78708481/211149661-c761bca7-0311-4d53-8467-c0cc2a511cc2.png)

On va charger les données dans notre spark dataframe. On va travailler avec une twitter dataset, vous trouverez le lien ci-dessous.

https://mega.nz/file/ApdlDSqR#63xhv-uX3dDNFyePcBnarQD9HWpHGDQ61CNwatfTdEM

![image](https://user-images.githubusercontent.com/78708481/211149674-92f1ba8a-136b-47cc-9822-424e31aafda4.png)

les negatifs tweets sont indiqué par "0"
les positifs tweets sont indiqué par "4"

On peut visualiser combien on a de donnée à caractère positif et negatif.

<img width="758" alt="image" src="https://user-images.githubusercontent.com/78708481/211150217-abfb5e6f-5669-4152-a8f1-5c4d4841a303.png">

### 1.	Préparation des données
Au niveau de cette etape de data processing, on va effectué des modification sur les données.

On selectionne d'abord les colonnes utile pour le trainig à savoir text and label (sentiment).

![image](https://user-images.githubusercontent.com/78708481/211150280-5f53553a-e24a-4ee6-9a8a-b1ad1c393abd.png)

On split les données en traning and testing.

![image](https://user-images.githubusercontent.com/78708481/211150303-c62055a4-9c4e-48b7-bda2-03dbfed16f94.png)

On commence d'abord par la separation des mots au niveau du text en utilisant tokenizer.

![image](https://user-images.githubusercontent.com/78708481/211150348-1e2b215e-4752-4aae-aae9-e0ea66d2744e.png)

on supprime les stops words.

![image](https://user-images.githubusercontent.com/78708481/211150399-b539aa0c-7c67-4a96-902c-bb9f4ddbb641.png)

on convertit les mots en numeric features.

![image](https://user-images.githubusercontent.com/78708481/211150411-754e751e-98ae-4d2a-aded-33a5ae2c9eaa.png)

### 2.	Logistic Regression
Maintenant c'est le tour des modelzs pour l'entrainement et la classification.

On utilise d'abord logistic regression.

On entraine le modèle:

![image](https://user-images.githubusercontent.com/78708481/211150496-08493c23-27ed-4887-9c33-509d0a50b78f.png)

On prépare le testing data:

![image](https://user-images.githubusercontent.com/78708481/211150509-28ffdbdb-a509-412c-b4e7-51dfcc040448.png)

On passe à la prédiction en evaluant le modèle (accuracy):

![image](https://user-images.githubusercontent.com/78708481/211150516-5ba352c6-1c8d-4497-99bd-94d647ae9996.png)

### 3.	Naive Bayes

On passe au deuxième model Naive Bayes.
On entraine le modèle:

![image](https://user-images.githubusercontent.com/78708481/211150613-a4522fc1-6644-4e4c-8cc2-cbec64831420.png)

On passe à la prédiction en evaluant le modèle (accuracy):

![image](https://user-images.githubusercontent.com/78708481/211150630-8850c955-8bf3-4c51-8e1a-678d1c388764.png)

## V.	Prédiction avec le modèle choisi (Logistic Regression)
 
Dans cette etape on va utiliser le modèle entrainé "logistic Regression" pour prédire les données en streaming en utilisant le kafka topic qu'on a créé. ainsi qu'on va stocker ces données dans la base de données HBase.
 
 ### 1.	Import libraries.
 
 ![image](https://user-images.githubusercontent.com/78708481/211150782-929fbec0-a596-4f72-be70-9ba395121354.png)

### 2.	Connexion à Hbase 

![image](https://user-images.githubusercontent.com/78708481/211150797-2894ff77-f22d-4ce7-9317-5d71f83f4861.png)

On va créer une fonction insert rows pour insérer les données en streaming.ainsi qu'on va tester la connexion avec Hbase.

![image](https://user-images.githubusercontent.com/78708481/211150825-ac05690b-1ab3-40f8-a7d9-001100e5feda.png)

### 3. Streaming process

![image](https://user-images.githubusercontent.com/78708481/211150883-c969aad0-866d-4c96-b589-9459d83cb801.png)

![image](https://user-images.githubusercontent.com/78708481/211150893-5575c088-192e-47c0-aa52-d0cdb29bda58.png)

Au niveau de cette etape on récupère les tweets en streaming en effectue le processing sur ces tweets et on prédit les sentiments en utilisant le modèle entrainé, on stocke ainsi les données sur HBase. ainsi qu'on effectue une visualisation des données en indiquant le nombre de tweets negatif et positifs.

le resultat est comme suit.

<img width="749" alt="image" src="https://user-images.githubusercontent.com/78708481/211151047-59bb2190-a9a7-419d-bd3b-b7763710d662.png">

<img width="699" alt="image" src="https://user-images.githubusercontent.com/78708481/211151085-50c08652-c866-486e-8703-b6c2889c2bf2.png">

### 4.	Verification des données dans hbase
On peut vérifié le stockage des données dans hbase .

On scan "twitter_tabl" dans hbase shell.

![image](https://user-images.githubusercontent.com/78708481/211151186-a9c64671-1a4b-4c6b-97a1-1ffd4a51cb51.png)


## 	Contributors

#### TAIH HIBA
#### MAOUID NOUHAILA
#### BAYD IMANE












 

 





