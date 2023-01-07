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


![image](https://user-images.githubusercontent.com/78708481/211149674-92f1ba8a-136b-47cc-9822-424e31aafda4.png)


### 1.	Préparation des données
Au niveau de cette etape de data processing, on va effectué des modification sur les données.






 

 





