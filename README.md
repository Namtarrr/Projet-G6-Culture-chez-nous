# Projet G6 - Culture chez nous

Ce dépôt contient le projet réalisé par le groupe G6 en SID à l'Université Paul Sabatier (année 2025) sur le thème **Culture chez nous**.

---

## Structure du projet

### Dossier `Notebook`
Ce dossier contient les notebooks principaux pour l'analyse et le traitement des données :

- **`CALCUL_CONCENTRATION.ipynb`**  
  Contient les calculs de concentration (de culture) pour les départements et les communes. Récupère également les latitudes, longitudes manquantes et les géoshapes.

- **`Clustering.ipynb`**  
  Réalise des tests de clustering et génère les fichiers nécessaires.

- **`DashBord.ipynb`**  
  Permet de générer le dashboard à l'aide de Gradio. **Attention :** nécessite une version de Python supérieure ou égale à 3.10.

- **`insertinOracleTotal.ipynb`**  
  Permet l'insertion des fichiers CSV nettoyés dans la base de données Oracle.

- **`Nettoyage des donnees.ipynb`**  
  Génère les données nettoyées prêtes pour l'utilisation.

Dans le sous-dossier **`Données pour Dashboard`**, vous trouverez :
- Les données nécessaires pour lancer le Dashboard.
- Le script **`DlBd.py`** permettant de régénérer ces données.

---

### Dossier `exportBD`
Contient l'export de la base de données. Ce fichier peut être utilisé pour recréer la base.

---

### Dossier `TOUT_POUR_LA_CARTO`
Ce dossier contient :
- **`carto.py`** : Script pour générer des cartes dynamiques.  
  **Commande pour lancer la carte :**
  ```bash
  python -m streamlit run .\carto.py

---
### Dossier `Video`
Contient une vidéo de démonstration de la carte et du dashboard
