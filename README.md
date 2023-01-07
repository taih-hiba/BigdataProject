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





