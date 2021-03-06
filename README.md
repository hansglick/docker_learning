# Objectif 

L'objectif de ce repo est l'apprentissage de docker afin de pouvoir déployer le projet [MUSIC PLAYGROUND](https://github.com/hansglick/music_playground)


<img src="img/docker_larger.PNG" width="700">

### Organisation du repository 

 * [Image docker hello world](https://github.com/hansglick/docker_learning/tree/master/image_hello_world) :
   * Installation de `flask`
   * Print d'un message bidon
 * [image docker Grab Discography](https://github.com/hansglick/docker_learning/tree/master/image_grab_discography) :
   * Installation de tout les packages python du projet music_playground
   * Récupération de la discographie d'un artiste via l'API Spotify
   * Passage d'arguments dans le `docker run`
 * [image docker Grab Discographies](https://github.com/hansglick/docker_learning/tree/master/image_grab_discographies)
   * Installation de tout les packages python du projet music_playground
   * Récupération **DES** discographies d'une liste d'artistes représentés par un fichier input `artists.txt`
   * Le fichier `artists.txt` est montée au moment du `docker run` 
 * [image docker Final Application](https://github.com/hansglick/docker_learning/tree/master/image_final_application)
   * Installation de tout les packages python **et linux** du projet music_playground
   * Application finale dockerisée du projet [music_playground](https://github.com/hansglick/music_playground)
   * Récupération des discographies
   * Récupération des urls des tracks sur Youtube
   * Téléchargements des tracks au format mp3
   * Récupération des commentaires YouTube des tracks (NE FONCTIONNE PAS)
   * Récupération de meta data subsidiaires (nombre de vues, likes, dislikes, etc.) (PAS ENCORE)
   * Copie intégrale des fichiers crées dans le container en local
***

### Pourquoi utiliser Docker?

Docker est utile pour déployer une application de **type service**. Un service répond à une question précise. Typiquement, dans le machine learning supervisé, les services possibles sont :  
 * Reconnaissance d'images
 * Examiner si une transaction est frauduleuse ou pas
 * Extraire les features audio d'un artiste
 * etc.

Dans notre cas, i.e. télécharger des millions de fichiers, notre application est de **type task**. On veut executer une tâche. Cependant, docker pourrait nous servir car il permet d'isoler une application et donc de la démultiplier à l'infini sur plusieurs serveurs mais c'est une espèce d'utilisation détourné de docker

***

### Le Dockerfile décortiqué

 * `FROM alias-image` permet de télécharger une image situé sur le [docker hub](https://hub.docker.com/search?q=&type=image). C'est la première commande car il faut d'abord importer python afin de lancer l'installation des packages via `pip`. Le mot clé alias-image représente l'alias d'une image hébergé sur le docker hub. Pour les applications python dockerisés, si le souci de place n'est pas une priorité, il vaut mieux choisir une `buster` image. Il s'agit du mot clé utilisé pour parler d'une version python complète. `FROM python:3.7-buster`  est une bonne valeur par défaut

 * `WORK foldername` permet de désigner le folder par défaut dans le docker. C'est pour ça qu'il est signifié assez haut dans le dockerfile. Par exemple, la suite de commandes `WORKDIR /app` + `COPY fun.py .` signifie *le dossier par défaut dans le docker est /app* + *tu copies le fichier fun.py dans le dossier /app*

 * `COPY files` permet de monter les fichiers en host vers le docker. Typiquement, on monte tout les scripts python et les inputs file via cette commande

 * `RUN commande` permet de run des commandes lors de la construction de l'image. Typiquement, pour installer les packages on utilise cette commande

 * `CMD ou ENTRYPOINTS` permet lancer une commande, une fois l'image construite. Typiquement, on lance l'application python via cette commande. On préfère utiliser la commande CMD plutot que ENTRYPOINTS, bon apparemment c'est une question de subtilité que je ne comprends pas pour le moment

***

### Passer des arguments dans le Docker run

Il y a globalement deux facons de faire:
 1. Monter un fichier dans le container au moment du run. Par exemple, l'image contient une commande qui prend un fichier en input tel que `python app.py inputfile.txt`. On peut donc monter le fichier inputfile.txt au moment du run de cette façon `docker run -v inputfile.txt:/app/inputfile.txt docker-image`
 2. On peut également passer des arguments de manière plus habituelle comme une application python classique ([exemple](https://github.com/hansglick/docker_learning/tree/master/discography_w_arguments)). Pour ce faire :
  * Dans `Dockerfile`, renseignez les variables globales à l'aide du mot clé `ENV`. Par exemple `ENV INPUTFILE=jamesruskin.json`
  * La commande `CMD` ne peut alors plus être défini comme une liste de string comme l'explique le [post stackoverflow](https://stackoverflow.com/questions/40454470/how-can-i-use-a-variable-inside-a-dockerfile-cmd). On pourrait avoir par exemple `CMD python app.py $INPUTFILE`
  * Lors du docker run, signaler simplement la valeur de la variable `INPUTFILE` grâce au flag `-f` de cette manière : `docker run -e INPUTFILE=jeffmills.json docker-image` 

***

### Récupérer en local les files présents dans un container

 1. Récupérer l'id ou bien le name du container en question en faisant : sudo docker ps -all
 2. Rappatrier le fichier en question dans le folder data : `sudo docker cp <NAME or ID>:<CONTAINER_PATH> <HOST_PATH>`
 3. Exemple avec id : `sudo docker cp 04546594ef54:/app/output.json data/output.json`
 4. Exemple en utilisant le name du container : `sudo docker cp gallant_mclaren:/app/output.json data/output.json`


***

### Vocabulaire

 1. On build une image, qui contient une application/service
 2. On run une image, ce qui produit un container
 3. A chaque fois qu'on run une image, ca crée un container de plus. Attention la mémoire peut vite saturée. Raison pour laquelle, une bonne pratique à utiliser lorsqu'on run un docker en test ou bien pour une tâche bien précise on fait `docker run monimage --rm`

***

### Quelques commandes docker

 * `docker build -t monimage .` : permet de build une image docker
 * `docker run monimage` : permet de run une image
 * `docker images` : permet de lister toutes les images docker présentes en local
 * `docker -ps all` : permet de lister tout les containers
 * `docker rmi -f imageid` : permet de remove une image docker

***

### Précisions sur les scripts pythons
 
 * `# -*- coding: utf-8 -*-` : entête à placer dans les scripts python pour prendre en compte la gestion des accents.
 * `#!/usr/bin/python3` : Attention cette commande n'est pas obligatoire, elle sert juste à rendre le script python appelable sans passer par la commande `python` si le script a été rendu executable par la commande `chmod +x myscript.py`





