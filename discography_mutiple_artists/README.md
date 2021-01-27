# DESCRIPTION

Image Docker qui permet de télécharger **LES** discographies d'artistes à partir d'un fichier input `artists.txt`


### Distribution du listing d'artists (1 fichier par docker)

On éclate les noms des 24,000 artistes présents dans le fichier artists.json issu du crawling sur le site resident advisory en x fichiers présents dans le dossier data avec une des commandes suivantes : 

 * Top 20% des artistes avec le plus d'abonnés distribués sur 200 fichiers `python distribute_data.py -f artists.json -t 0.2 -n 200 -o data/`
 * Artistes > 5000 abonnées sur R.A. distribués sur 200 fichiers `python distribute_data.py -f artists.json -t 5000 -n 200 -o data/`

### Commandes

* Build de l'image : `sudo docker build -t artists-image .`
* Run classique de l'image avec le fichier exemple : `sudo docker run artists-image`
* Run de l'image avec un des 200 sets d'artistes éclatés : `sudo docker run -v ~/proj/docker_learning/discography_mutiple_artists/data/set_0000.txt:/app/artists.txt artists-image`. **ATTENTION!** Il faut indiquer le chemin absolu pour le fichier host! 

### Problèmes 

Malheureusement, la log ne semble pas s'afficher au fur et à mesure mais cela fonctionne quand même, à garder ça en tête pour l'améliorer

