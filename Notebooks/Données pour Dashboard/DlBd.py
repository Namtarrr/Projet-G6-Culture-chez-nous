import cx_Oracle
import os
import pandas as pd
from matplotlib import pyplot as plt
import gradio as gr

##### CREATION DES DATASETS ######

# Chemin du répertoire contenant le client Oracle
oracle_client_path : str = r"C:\Program Files\instantclient-basic-windows.x64-23.6.0.24.10"
# Récupérer la valeur actuelle de la variable PATH
current_path : str = os.environ.get("PATH", "")
# Ajouter le chemin du client Oracle à la variable PATH
new_path : str = f"{current_path};{oracle_client_path}"
# Définir la nouvelle valeur de la variable PATH
os.environ["PATH"] = new_path
# Vérifier si le chemin a été ajouté correctement
print("Nouvelle valeur de PATH :", os.environ.get("PATH"))
utilisateur :str = ""
mot_de_passe : str = ""
adresse_IP : str = ""
port : int  = 1521
sid : str = ""
#cx_Oracle.init_oracle_client(lib_dir= r"C:\Program Files\instantclient-basic-windows.x64-23.6.0.24.10")
dsn = cx_Oracle.makedsn(adresse_IP, port, sid)
connection = cx_Oracle.connect(utilisateur, mot_de_passe, dsn)
cursor = connection.cursor()





##### MUSEES #####
cursor.execute('select musee.nom, musee.cp, musee.domaine_sous_type, musee.commune, departement."numdep", departement."nomdept", region."nomReg", region."codeReg",musee.entre_gratuit,musee.entre_payant,musee.entre_total from MUSEE, DEPARTEMENT, REGION where MUSEE.cp = DEPARTEMENT.cp and REGION."numdep" = DEPARTEMENT."numdep"')
# Récupérer les noms des colonnes et données
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_musees = pd.DataFrame(rows, columns=columns)
data_musees.to_csv("data_musees.csv", index=False)


###### FESTIVALS ######
cursor.execute('select festivals.nom, festivals.cp, festivals.latti, festivals.longi, festivals."Site", festivals."Type", departement."numdep", departement."nomdept", region."nomReg", region."codeReg" from FESTIVALS, DEPARTEMENT, REGION where FESTIVALS.cp = DEPARTEMENT.cp and REGION."numdep" = DEPARTEMENT."numdep"')
# Récupérer les noms des colonnes et données
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_festivals = pd.DataFrame(rows, columns=columns)
data_festivals = data_festivals[data_festivals.Type != '8054282.php']
data_festivals.to_csv("data_festivals.csv", index=False)

###### BATIMENTS/MONUMENTS #######
cursor.execute('select batiment_monument.latti, batiment_monument.longi, batiment_monument.titre_denomination, batiment_monument.cp, batiment_monument."TYPE", batiment_monument.commune, departement."numdep", departement."nomdept", region."nomReg", region."codeReg" from batiment_monument, DEPARTEMENT, REGION where batiment_monument.cp = DEPARTEMENT.cp and REGION."numdep" = DEPARTEMENT."numdep"')
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_batmon = pd.DataFrame(rows, columns=columns)
data_batmon.to_csv("data_batmon.csv", index=False)

##### THEATRE ######
cursor.execute('select theatre.nom, theatre.jauge, theatre.cp, theatre.sous_type, theatre.commune, departement."numdep", departement."nomdept", region."nomReg", region."codeReg" from theatre, DEPARTEMENT, REGION where theatre.cp = DEPARTEMENT.cp and REGION."numdep" = DEPARTEMENT."numdep"')
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_theatre = pd.DataFrame(rows, columns=columns)
data_theatre.to_csv("data_theatre.csv", index=False)


#### CINEMA ######
cursor.execute("""select  CINEMA."CP", "Type", "NOM","COMMUNE","FAUTEUIL","Public","ECRAN", "SOUS_TYPE_THEMATIQUE",
"GCD","LATTI","LONGI",REGION."codeReg",REGION."nomReg",DEPARTEMENT."numdep",DEPARTEMENT."nomdept"
from CINEMA, REGION , DEPARTEMENT
where DEPARTEMENT."CP"=CINEMA."CP" and REGION."numdep"=DEPARTEMENT."numdep"  """)
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_cinema = pd.DataFrame(rows, columns=columns)
data_cinema.to_csv('data_cinema.csv', index=False)

#### ARCHIVES ####
cursor.execute("""select  archives."CP", "NOM", "ORGANISME","Type", "Public","SOUS_TYPE_THEMATIQUE","COMMUNE","LATTI",
"LONGI",REGION."codeReg",REGION."nomReg",DEPARTEMENT."numdep",DEPARTEMENT."nomdept", "GCD"
from archives, REGION , DEPARTEMENT
where DEPARTEMENT."CP"=archives."CP" and REGION."numdep"=DEPARTEMENT."numdep" """)
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_archives = pd.DataFrame(rows, columns=columns)
data_archives.to_csv('data_archives.csv', index=False)

#### BIBLIOTHEQUES ####
cursor.execute("""select distinct bibliotheque."CP", "AMPLITUDE_HORAIRE", "NOM", "COMMUNE", "POPULATION",
"SOUS_TYPE_STATUT","Type", "Url","GCD","NB_BENEVOLE", "NB_SALARIE","SURFACE","LATTI","LONGI",REGION."codeReg",
REGION."nomReg",DEPARTEMENT."numdep",DEPARTEMENT."nomdept" from bibliotheque, REGION , DEPARTEMENT where 
DEPARTEMENT."CP"=bibliotheque."CP" and REGION."numdep"=DEPARTEMENT."numdep" """)
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# Charger les données dans un DataFrame Pandas
data_biblio = pd.DataFrame(rows, columns=columns)
data_biblio.to_csv('data_biblio.csv', index=False)


#### REVENUS PAR COMMUNE ####
cursor.execute("""select commune."nomcom", departement."nomdept", commune."revenu_moyene_foyer" 
from commune, departement where commune.cp = departement.cp""")
columns = [description[0] for description in cursor.description]
rows = cursor.fetchall()
# charger les donnees
data_revenus = pd.DataFrame(rows, columns=columns)
data_revenus.to_csv("data_revenus.csv", index=False)
