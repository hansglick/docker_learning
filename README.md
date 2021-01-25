# Objectif 

L'objectif de ce repo est l'apprentissage de docker afin de pouvoir déployer le projet [MUSIC PLAYGROUND](https://github.com/hansglick/music_playground)


# Quelques commandes docker

 * `docker build -t monimage .` : permet de build une image docker
 * `docker run monimage` : permet de run une image
 * `docker images` : permet de lister toutes les images docker présentes en local
 * `docker rmi -f imageid` : permet de remove une image docker


# La spécificité CONDA

Pour une raison que je n'ai pas comprise, la commande `conda activate` ne **fonctionne pas** dans un Dockerfile. Pour parer à ça, on utilise la commande `conda run -n moncondaenv macommandepython`. Cette commande permet de run *macommandepyhton* au sein de l'environnement *moncondaenv*

# Attention aux accents

Les scripts python utilisés doivent contenir les entêtes suivantes afin que Docker puisse fonctionner :
 * `#!/usr/bin/python3`
 * `# -*- coding: utf-8 -*-`

### **toyexample**

Ce folder contient un dockerfile qui utilise un environnement **conda**

### **discography**

Ce folder contient un dockerfile qui lance un scipt récupérant la discography de Jeff Mills à l'intérieur d'un environnement conda

