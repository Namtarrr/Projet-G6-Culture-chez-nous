# Projet-G6-Culture-chez-nous
Repo concernant le projet réalisé par le G6 en SID à l'université Paul Sabatier année 2025 sur le thème culture chez nous

Dossier Notebook 

	CALCUL_CONCENTRATION.ipynb : Contient les calculs de concentration (de culture) pour les départements et les communes.Viens récupérer les latitude et longitude manquantes et geoshape. 
 
	Clustering.ipynb : Fait des tests et réalise le clustering, envoie également le fichier.
	
 	DashBord.ipynb : Permet de générer le dashboard à l'aide de gradio. Attention avoir une version de python supérieur ou égale a 3.10
	
 	insertinOracleTotal.ipynb : Permet de faire les insertions des CSV nettoyés dans la base de données Oracle.
	
 	Nettoyage des donnees.ipynb : Permet de générer les données nettoyées.

	Dans le dossier Données pour Dashboard, on retrouve les données nécessaires au lancement du Dashboard. Il y a également le fichier DlBd.py qui permet de régénérer ces données.


Dans le dossier exportBD  on trouve, comme le nom l'indique, l'export de la base de données qui peut être exécuté afin de recréer celle-ci.


Dans le dossier TOUT_POUR_LA_CARTO, on trouve carto.py qui, une fois exécuté, permet de générer des cartes dynamiques.
utiliser dans ce dossier la commande python -m streamlit run .\carto.py pour lancer la carte.

Dans le dossier Video, on retrouve une vidéo de démonstration de la carte et une vidéo de démonstration du notebook.
