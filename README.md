# BIG DATA Project

I.	Architecture de la solution

![image](https://user-images.githubusercontent.com/78708481/211147804-2ba829ca-59e2-4344-aacd-478ccc25e8d1.png)

Au cours de ce projet on travaillera avec apache Kafka spark streaming et ML et le stockage sur HBase. On travaillera avec Twitter API afin d’avoir un flux de données en temps réel.
Comme vous pouvez le voir sur le graphique ici, le flux Twitter est ingéré par Kafka et envoyé sous forme de signaux par les producteurs de Kafka, puis Spark Streaming peut choisir de recevoir les signaux Kafka en fonction des sujets et sous forme de flux distribués. 
Nous présentons une architecture de bout en bout sur la façon de diffuser des données à partir de Twitter, de les nettoyer et d'appliquer un modèle simple d'analyse des sentiments pour détecter la polarité et la subjectivité de chaque tweet.




