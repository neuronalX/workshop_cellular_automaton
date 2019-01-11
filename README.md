# Workshop IA sur les Automates Cellulaires

Pour les informations concernant l'événement (workshop) passé, voir plus bas dans la page (cf. EVENT).

## MISC

### Activité "débranchée" : Comment coder un automate cellulaire à la main ?
Pour dérouler un automate cellulaire soi-même, il faut imprimer [cette feuille A4](https://github.com/neuronalX/workshop_cellular_automaton/blob/master/grille_a_remplir_Automata1D.pdf)

Puis faire les étapes suivantes :
1) tu choisis ta propre règle : c'est à dire colorier ou non la case centrale pour chaque cas (triplet) possible
2) ensuite tu colores la première ligne comme tu veux (par ex juste la case la plus centrale, comme ça on les gens peuvent rapidement comparer différentes règles
3) tu colores la seconde ligne (et ainsi de suite pour chaque ligne) en appliquant les règles que tu as choisi en 1)

### Comment coder un automate cellulaire en Python ?
Savez vous qu'un tweet suffit pour coder un automate cellulaire 1D en Python ? Comment feriez-vous ?

La [réponse](https://github.com/neuronalX/workshop_cellular_automaton/blob/master/tweetable_1D_cellular_automata.py) et la [démo](https://twitter.com/NPRougier/status/835234915008512000).

### Sources / références
#### Repo github listant une quantité impressionnante de règles d'automates cellulaires !
https://github.com/gollygang/ruletablerepository/wiki/TheRules
#### codes sources (pour la 1D) dans plein de langages différents
http://rosettacode.org/wiki/One-dimensional_cellular_automata
#### variantes des 1D: "totalistic cellular automaton"
http://mathworld.wolfram.com/TotalisticCellularAutomaton.html

### A propos
Ce workshop reprend du code du livre de Nicolas P. Rougier "From Python to Numpy", en particulier du [chapitre 4](http://www.labri.fr/perso/nrougier/from-python-to-numpy/#code-vectorization).


## EVENT: Mercredi 1er Mars à 18h30 au Node, Bordeaux
Animé par Nicolas P. Rougier & Xavier Hinaut, chercheurs à l'Inria Bordeaux dans l'équipe [Mnémosyne](https://team.inria.fr/mnemosyne/).

Co-organisé par le [MindLaBDX](https://mindlabdx.github.io/about/) et [Aquinum](https://aquinum.fr/). (Merci en particulier à Tallulah Gilliard et Pauline Marcon pour l'organisation !)

Lieu : Le Node, 12 rue des Faussets, 33000 Bordeaux

Nombre de places limitées à 60 personnes : [inscrivez-vous ici](https://aquinum.fr/agenda-aquinum-numerique/evenement/1192-workshop-journees-de-l-intelligence-artificielle-2017.html).

Plus de détails sur l'événement sur la [page facebook](https://www.facebook.com/events/173252356508743/).

![Bandeau de l'événement](/images/bandeau_promo_workshop.jpeg)

### Préparer sa machine avant le workshop
Installez sur votre machine :
- Python 3 et/ou 2 (vous pouvez utiliser [pyenv](https://github.com/yyuu/pyenv) pour avoir les deux versions installées en parallèle)
- Numpy (bibliothèque scientifique)
- Matplotlib (bibliothèque pour faire des graphiques)

Le plus simple pour installer Python 3 et le package de bibliothèques courantes (Numpy, Matplotlib) est d'installer [Anaconda](https://www.continuum.io/downloads).

Vous pouvez tester votre installation de Python 3 en téléchargeant le fichier _check_install_python3.py_ et exécutant dans un terminal:
>   python check_install_python3.py

### Pad interactif
Vous pouvez avoir plus d'informations sur le [pad](https://mensuel.framapad.org/p/K2naCQTxjJ-mindlabdx-workshop-IA-I) de l'événement : vous pouvez poser vos questions en avance ou durant le workshop.
