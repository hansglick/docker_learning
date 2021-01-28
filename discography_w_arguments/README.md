# DESCRIPTION

Docker afin de prendre la discographie de l'artiste James Ruskin.

***

### Commandes

 * le build de l'image :
   * `sudo docker build -t ruskin-param-image .`
 * run l'image avec les arguments par défaut :
   * `sudo docker run ruskin-param-image`
 * run l'image avec des arguments spécifiques, ici on prend la discographie de jeff mills :
   * `sudo docker run -e FIRSTNAME=jeff -e LASTNAME=mills ruskin-param-image`


***

### Problèmes résolus

* **Reproduire un environnement conda avec pip** : pour des raisons assez complexes, il est plus difficile d'utiliser les commandes conda dans un docker. On lui préfère donc simplement la commande `pip` pour installer les packages nécessaires à une application python. Afin d'exporter un environnement conda faire les étapes suivantes : 
  * `conda activate music_env`
  * `pip list --format=freeze > requirements.txt`
  * Dans Dockerfile, `RUN pip install -r /tmp/requirements.txt`

 * **Could not find a version that satisfies the requirement** : lors de la commande `RUN pip install -r /tmp/requirements.txt` dans le `dockerfile`, il se peut qu'on rencontre ce type d'erreurs. En fait, cela signifie que la version n'est plus disponible sur les serveurs PyPi. Afin de voir quelles sont les versions disponibles, allez sur le site PyPi qui héberge le package et allez dans history. Par exemple pour avoir les versions de setuptools de disponibles lors de l'installation via `pip` consultez cette [page](https://pypi.org/project/setuptools/#history). Repérez la version la plus proche de celle qui produit une erreur et modifiez le fichier `requirements.txt`

 * **mkl package non installé** : le package mkl a semble-t-il des problèmes de maintenance sur PyPi. Pour cette raison, il n'est pas installé. Ceci ne semble pas faire bugger l'application

