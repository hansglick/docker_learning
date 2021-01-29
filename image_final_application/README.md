# DESCRIPTION

Image Docker de l'application finale, i.e., récupérer les discographies des artistes, trouvez les liens des tracks sur youtube, téléchargez les tracks au format mp3, et prendre les commentaires. Ici on récupère tout les fichiers crées dans le container dans le dossier `container_files`. Les mp3s et les discographies + metadata (`final.json`) sont situés dans le dossier `/app/songs` du container


### Commandes

* Build de l'image :
  * `sudo docker build -t yttracks .`
* Run classique de l'image avec le fichier exemple :
  * `sudo docker run yttracks`


### A modifier

 * Dans le fichier `dwlsongs.sh`, à la ligne 5, modifiez `jq '.[0:6]'` par `jq '.[]'` une fois qu'on passe en production. `[0:6]` signifie qu'on ne télécharge que les 7 premiers tracks uniquement (phase de test)

 * Dans le ficher `dwlsongs.sh`, à la ligne 19, pour télécharger une qualité de son maximale, remplacez 
   * `youtube-dl -x --audio-format mp3 -o "songs/%(id)s.%(ext)s" --audio-quality 9 $myurl`
   * par
   * `youtube-dl -x --audio-format mp3 -o "songs/%(id)s.%(ext)s" --audio-quality 1 $myurl`


### Trucs à savoir & astuces

* Pour ne pas rebuild from scratch une image si on ne modifie que des scripts :
  * `sudo docker run -v ~/proj/app.py:/app/app.py yttracks`
* Copier l'ensemble du container en local :
  * `sudo docker cp sleepy_driscoll:/app container_files/`
* Remove un folder (hors docker) :
  * `sudo rm -rf folder_path`
* Printer les logs d'un script python lancé dans docker :
  * `print(malog,flush=True)`
* Installation de packages linux :
  * `RUN apt-get -y update`
  * `RUN apt-get -y upgrade`
  * `RUN apt-get install -y ffmpeg`





### Problèmes 

#### **Application de récupération des commentaires ne fonctionne plus**

Pour télécharger les commentaires d'une vidéo YouTube, j'utilisais le package de [Egbert Bouman](https://github.com/egbertbouman/youtube-comment-downloader). Cependant, son application semble ne plus fonctionner même en local. Je lui ai envoyé un email pour le prévenir à l'adresse e.bouman@tudelft.nl

#### **Package Youtube-search a parfois des ratés**
Pour récupérer l'url de la première vidéo issue d'une requête sur Youtube, j'utilise le package [Youtube-search](https://pypi.org/project/youtube-search/). Celle-ci pour une raison inconnue n'arrive parfois pas à retourner de résultats. Cela ne dépend pas de la requête puisqu'en relancant le script une seconde fois, le problème survient pour une autre requête. 

#### **bash non disponible sur docker** 
`bash` n'est, par défaut, pas installé sur les images docker car on veut garder le plus de place possible. Seul `sh` est disponible