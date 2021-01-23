# Description

Ce projet à pour but de montrer comment mettre en place un système de cache reposant sur Redis dans une app django. Redis apporte ici un gain de performance car les recherches dans la base effectuées récemment sont stockées en mémoire RAM pour une durée que j'ai fixé à 15min.

# Note

pour apprécier la différence : 
> sudo npm install -g loadtest

Pour lancer le test en utilisant la db 
> loadtest -n 100 -k  http://localhost:8000/store/


Pour lancer le test en utilisant le cache 
> loadtest -n 100 -k  http://localhost:8000/store/cache/