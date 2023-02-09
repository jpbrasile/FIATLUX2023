# FIATLUX2023
FIATLUX est un projet d'optimisation "end to end" basé sur l'association de plusieurs avancées technologiques, dont:
- Le déploiement possible sur internet via des microservices susceptible d'inclure des objets 3D complexes.
- Un assistant virtuel venant aide aux utilisateurs de FIATLUX.
- L'adaptation des techniques de "ray tracing" au calcul scientifique avec l'algorithme de la marche de sphères.
- Son adaptation aux cartes GPU de nouvelle génération (réalisant **210 000 milliards d'opérations par seconde !** pour le ray tracing).
- L'intégration des capacités symboliques-numériques de Julia a un modèle de simulation traditionnel disposant d'une très large bibliothèque.
- Le remplacement de modèles complexes par leurs équivalents plus rapides (jumeaux numériques). 

1- **Microservices:** 

Un microservice est une fonction, exécutable à partir d'un navigateur, qui s'occupe d'une tâche spécifique dans une application plus grande. C'est comme une pièce d'un puzzle qui s'emboîte avec d'autres pièces pour former une application complète. Les microservices peuvent être développés, déployés et gérés indépendamment les uns des autres, ce qui permet une plus grande flexibilité et une meilleure maintenance de l'application dans son ensemble.

Nous intègrerons des outils permettant de créer de tels microservices à partir
- du langage Julia avec [PlutoSliderServer.jl](https://github.com/JuliaPluto/PlutoSliderServer.jl)
- du langage Python avec [SpecklePy](https://github.com/specklesystems/specklepy)
- du langage Rhino/Grasshopper avec un [connecteur Speckle](https://speckle.systems/tag/grasshopper/)

Le déploiement sur le Net est facilité grâce à [Streamlit](https://streamlit.io/)

*Nous avons d'ores et déjà réalisé un [maquettage](https://fiatluxweb.herokuapp.com/) utilisant ces ressources, que nous avons déployées sur le net.*

2- **Assistant virtuel:**

L'arrivée fracassante de ChatGPT a démocratisé l'usage des "large language models" pour la création d'assistants virtuels. Il est probable que des améliorations significatives sont encore à venir. Pour ce qui nous concerne, nous souhaitons que notre assistant virtuel puisse "apprendre" tout le contenu de FIATLUX pour le restituer de façon appropriée en réponse à une demande. Nous intégrerons donc un assistant virtuel, tel que [RAVEN](https://github.com/daveshap/raven) qui est en cours de développement "open source".
Les assistants virtuels sont aussi précieux pour l'aide qu'ils peuvent apporter pour le codage ([Github Copilot](https://github.com/features/copilot) par exemple) et pour la transcription de codes d'un langage en un autre. Notre assistant permettra, par exemple, de transcrire les lois de pilotage d'un convertisseur en un code exécutable sur micro-contrôleur.

3- **La marche des sphères**

Nous intégrerons les percées récentes de cet algorithme stockastique pour modéliser une très large gamme de problèmes physiques.
Sans nécessiter de maillage préalable et fournissant facilement l'information de gradient, il est particulièrement bien adapté à l'optimisation de géométries complexes représentées sous forme paramétrique. A titre de comparaison une pièce complexe nécessitant 14 heures de maillage peut être traitée en moins d'une minute avec l'algorithme de la marche des sphères (accélération d'un rapport 5000 !

Nous intégreons ainsi Grasshopper, le logiciel paramétrique des architectes, car c'est l'outil idéal pour produire de telles géométries même dans les cas les plus complexes. 

Pour plus de détail sur l'algorithme, son domaine d'application et ses avantages par rapport aux méthodes éléments finis, je vous invite à visionner l'[excellente présentation](https://cs.dartmouth.edu/wjarosz/publications/sawhneyseyb22gridfree.html) de Keenan Crane.

4- **[Cartes GPU de nouvelle génération](https://wccftech.com/nvidia-rtx-6000-ada-graphics-card-benchmarked-3dmark-72-percent-faster-vs-a6000-ampere/ ):**

Fin 2018 une carte GPU de 10 000 $ exécutait 10 milliards d'opérations de ray tracing par seconde, aujourd'hui une carte coûtant 35% moins cher est 21 000 fois plus rapide faisant passer un calcul de 6 heures à une seconde! Nous utiliserons ce type de carte pour réaliser nos calculs scientifiques, car tous nos microservices sont compatibles d'un portage sur GPU . 

5- **Modélisation end to end:**

Le package [ModelingToolKit.jl](https://github.com/SciML/ModelingToolkit.jl) de Julia permet le traitement symbolique d'un problème avant sa résolution par l'écosystème [SciML](https://sciml.ai/) de Julia. Cela permet de transformer un problème initialement mal posé en un problème optimisé (les gains peuvent être d'un rapport 10 avec le simple ajout d'une ligne de code !). Il permet par  exemple de calculer symboliquement les gradients, jacobiens et hessiens afin de simplifier le travail de l'algorithme de résolution mis en jeu par la suite. 

Il permet aussi le traitement de milliers d'équations différentielles fournies "en vrac" pour les ordonner, supprimer les redondances et ne conserver que celles utiles à la résolution du problème principal.

Une [thèse](https://ecp.ep.liu.se/index.php/modelica/article/view/186) est en cours pour intégrer ce backend, avec toutes les performances qui en découlent, à OpenModelica, un outil de modélisation acausal déjà mature et disposant d'une très large bibliothèque. [Un gain de 7](https://global.discourse-cdn.com/business5/uploads/julialang/original/3X/8/2/826e8936737aad3a6f105d3cd194e80f27816599.png) en performance a été obtenu. Mais ce nouvel outil sera également compatible de l'emploi de jumeaux numériques, tels que ceux décrits ci-après, pour accélérer encore les performances.

6- **Jumeaux numériques**
L’emploi de jumeaux numériques différentiables permet 
- d’accélérer la mise en œuvre d’un modèle bien plus rapidement ([JuliaSim](https://juliahub.com/products/juliasim/ ) indique ainsi une accélération de 80) 
- d’opérer son optimisation grâce à la connaissance du gradient. 

Plusieurs pistes très prometteuses seront explorées et donneront lieu à la création de microservices FIATLUX :

-	Dans les cas simples le jumeau numérique peut être réalisé à partir de [surrogates.jl](https://github.com/SciML/Surrogates.jl)  et [SimpleChain.jl](https://github.com/PumasAI/SimpleChains.jl). La phase d’optimisation utilise alors ce modèle au lieu du modèle initial bien plus lourd dans sa mise en œuvre. 
-	Les [DEQ](https://julialang.org/blog/2021/10/DEQ/ )   : Réseau de neurones avec une couche implicite qui remplace un nombre infini de couches d’un réseau de neurones traditionnel.
-	Le [CPINN](https://paperswithcode.com/paper/competitive-physics-informed-networks )) : Il s’agit d’un réseau de neurones inspiré par la physique (les lois physiques sont dans la fonction de coût) mais qui converge bien mieux et bien plus vite grâce à l’emploi d’un GAN.
-	Le [calcul avec réservoir](https://docs.sciml.ai/ReservoirComputing/dev/ ) : réseau de neurones aux paramètres figés (réservoir), suivi d’une seule couche neuronale paramétrée). Cette architecture est bien adaptée à l’extrapolation des séries temporelles. 


