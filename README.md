# Blenderenv

This is a Blender version and env manager.

## BETA - Fonctionnement

Cet outil permet de gérer en mode ligne de commande des versions de Blender, avec le choix de la version à utiliser. Il permet aussi de gérer des environnement virtuel python pour les add-ons.

*Il sera prévu de faire une interface GUI pour les utilisateurs non avancés par la suite.*

En détails :

- Gestion des versions de blender au niveau système.
- Gestion des versions de blender au niveau d'un projet d'Add-On. Permet de facilité le développement et les tests unitaires
-  sans pour autant altérer l'installation de blender.
- Les environnements virtuels permettent de gerer des version de packages durant le dev mais aussi en tant que dépendances pour des add-ons toujours sans altération de l'installation.
- Il permet aussi de simplifier le processus de build car installation depuis les sources, cela permet aussi de faire ses propres builds du module `bpy`.
