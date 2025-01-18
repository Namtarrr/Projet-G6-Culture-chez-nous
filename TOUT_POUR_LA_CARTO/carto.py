import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import json

# Charger les données
archives = pd.read_csv("ARCHIVES_DATA_TABLE.csv", sep=";")
bat = pd.read_csv("BATIMENT_MONUMENT_DATA_TABLE.csv", sep=",")
biblio = pd.read_csv("BIBLIOTHEQUE_DATA_TABLE.csv", sep=";")
festivals = pd.read_csv("FESTIVALS_DATA_TABLE.csv", sep=";")
cine=pd.read_csv("CINEMA_DATA_TABLE.csv", sep=";")
musee=pd.read_csv("MUSEE_DATA_TABLE.csv", sep=";")
theatre=pd.read_csv("THEATRE_DATA_TABLE.csv", sep=";")
communes = pd.read_csv("COMMUNE_DATA_TABLE.csv", sep=",")
dept= pd.read_csv("DEPARTEMENT_DATA_TABLE.csv", sep=";")
cluster=pd.read_csv("CLUSTERS_COMMUNES.csv")
concentration_dep=pd.read_csv('CONCENTRATION_PAR_DEP.csv', sep=',')

arch_res = archives[['Type', 'NOM', 'LATTI', 'LONGI', 'COMMUNE']]
bat_res = bat[['NOM', 'TYPE', 'LATTI', 'LONGI', 'COMMUNE']]
biblio_res = biblio[['NOM', 'SOUS_TYPE', 'LATTI', 'LONGI', 'COMMUNE']]
fest_res = festivals[['NOM', 'SOUS_TYPE', 'LATTI', 'LONGI']]
cine_res = cine[['NOM', 'SOUS_TYPE', 'LATTI', 'LONGI', 'COMMUNE']]
musee_res = musee[['NOM', 'SOUS_TYPE', 'LATTI', 'LONGI', 'COMMUNE']]
theatre_res = theatre[['NOM', 'SOUS_TYPE', 'LATTI', 'LONGI', 'COMMUNE']]
tt_donnee = pd.concat([arch_res, bat_res, biblio_res, fest_res, cine_res, musee_res, theatre_res], axis=0)

###################################################################################################################
############################################## reprsentation de base ##############################################
###################################################################################################################

#affiche la carte avec les filtrer

def filter_map(selected_categories, sous_categories_dict,dataframes,category_colors, map_center):
    fig = go.Figure()

    for category in selected_categories:
        df = dataframes[category]
        # Filtrer le DataFrame selon les sous-catégories sélectionnées
        if category in sous_categories_dict:
            sous_categories = sous_categories_dict[category]
            df = df[df["SOUS_TYPE"].isin(sous_categories)]
        
        names = df["NOM"].tolist()

        if "COMMUNE" in df.columns:
            communes = df["COMMUNE"].tolist()
            text_list = [(names[i], communes[i]) for i in range(len(names))]
        else:
            text_list = [(names[i], "") for i in range(len(names))]

        fig.add_trace(go.Scattermapbox(
            customdata=text_list,
            lat=df["LATTI"].tolist(),
            lon=df["LONGI"].tolist(),
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color=category_colors[category]
            ),
            name=category,
            hoverinfo="text",
            hovertemplate='<b>Name</b>: %{customdata[0]}<br><b>Commune</b>: %{customdata[1]}'
        ))


    #paramètre pour afficher les frontières
    json_string=map_center["shape"]
    if json_string!="":
        data = json.loads(json_string)
        coordinates = data["coordinates"][0] 
        lons, lats = zip(*coordinates)
        map_center["lat"] = sum(lats) / len(lats)
        map_center["lon"] = sum(lons) / len(lons)

        fig.add_trace(go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode='lines',  
            line=dict(width=2, color='blue'), 
            name="Frontières de la commune"
        ))

    #paramètre général de la carte
    fig.update_layout(
        height=800, 
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=map_center["lat"],
                lon=map_center["lon"]
            ),
            pitch=0,
            zoom=map_center["zoom"]
        )
    )
    
    return fig

#affiche la carte général
def affichage_carte(archives,bat,biblio):
    # Liste des DataFrames et des catégories correspondantes
    dataframes = {
        "Archives": archives,
        "Bâtiments/Monuments": bat,
        "Bibliothèques": biblio,
        "Festivals": festivals,
        "Cinéma": cine,
        "Musées": musee,
        "Théâtre": theatre
    }

    # Couleurs personnalisées pour chaque catégorie
    category_colors = {
        "Archives": "#E57373",  # Rouge corail
        "Bâtiments/Monuments": "#64B5F6",  # Bleu azur
        "Bibliothèques": "#81C784",  # Vert mousse
        "Festivals": "#BA68C8",  # Violet orchidée
        "Cinéma": "#FFB74D",  # Orange mandarine
        "Musées": "#A1887F",  # Marron taupe
        "Théâtre": "#90A4AE"   # Gris bleuté
    }
    liste_cat=["Archives","Bâtiments/Monuments","Bibliothèques","Festivals","Cinéma","Musées","Théâtre"]


    selected_categories = st.sidebar.multiselect(
        "Choisis les catégories à afficher",
        liste_cat,
        default=liste_cat  
    )
    sous_categories_dict = {}
    for category in selected_categories:
        df = dataframes[category]
        sous_categories = df["SOUS_TYPE"].dropna().unique() 
        selected_sous_categories = st.sidebar.multiselect(
            f"Choisis les sous-catégories pour {category}",
            sous_categories,
            default=sous_categories
        )
        sous_categories_dict[category] = selected_sous_categories

    map_center = chercher_commune()
    if selected_categories:
        fig = filter_map(selected_categories, sous_categories_dict,dataframes,category_colors, map_center)
        st.plotly_chart(fig,use_container_width=True)


#fonction qui cherche une commune et retourne ces coordonnées et sa shape
def chercher_commune():
    search_input = st.sidebar.text_input("Rechercher une ville ou un village")

    if search_input:
        # Filtrage
        suggestions = communes[communes["NOM"].str.contains(search_input, case=False, na=False)]

        # Afficher les suggestions
        if not suggestions.empty:
            selected_commune = st.sidebar.selectbox("Suggestions :", suggestions["NOM"].unique().tolist())
            if selected_commune:
                commune_data = suggestions[suggestions["NOM"] == selected_commune].iloc[0]
                st.sidebar.write(f"Commune sélectionnée : {selected_commune}")
                return {"lat": float(commune_data["LATTI"]), "lon": float(commune_data["LONGI"]),"zoom":12 , "shape": commune_data["geoshape"]}
        else:
            st.sidebar.write("Aucune suggestion trouvée.")
    return {"lat": 46.03, "lon": 2.36 , "zoom":5 ,"shape":""}  # Centre par défaut (France)



###################################################################################################################
############################################## concentration culture ##############################################
###################################################################################################################

#recherche  de departement
def chercher_departement():
    search_input = st.sidebar.text_input("Rechercher un département")

    if search_input:
        # Filtrage
        suggestions = dept[dept["NOM"].str.contains(search_input, case=False, na=False)]

        # Afficher les suggestions
        if not suggestions.empty:
            selected_dept = st.sidebar.selectbox("Suggestions :", suggestions["NOM"].unique().tolist())
            if selected_dept:
                dept_data = suggestions[suggestions["NOM"] == selected_dept].iloc[0]
                st.sidebar.write(f"Département sélectionnée : {selected_dept}")
                return (dept_data["numdep"])
        else:
            st.sidebar.write("Aucune suggestion trouvée.")
    return ("")

#fonction générale qui gere les différents cas d'affichage

def affichage_concentration():
    selection_mode = st.sidebar.selectbox("Choisissez ce que vous voulez afficher",("Departements", "Communes dans un département"),)
    if selection_mode == "Departements":
        st.title("Concentration culturelle par Departements")
        carte_concentration_dep()
        st.title("Population par Departements")
        affichage_population()
    else :
        st.empty()
        num_selected_dept = chercher_departement()
        carte_concentration_communes(num_selected_dept)
    

#affiche les concentration de culture par communnes
def carte_concentration_communes(num_selected_dept):
    st.title("Concentration culturelle par Commune au sein d'un departements")
    num_selected_dept=str(num_selected_dept)
    if len(num_selected_dept)==1:
        num_selected_dept="0"+num_selected_dept
    df= pd.read_csv("COMMUNE_DATA_TABLE.csv", sep=",")

    min_valeur = df["Concentration"].min()
    max_valeur = df["Concentration"].max()


    fig = go.Figure()
    
    df["CP"]=df["CP"].astype("str")
    df["CP"]= df["CP"].apply(lambda x: x.zfill(5) if len(x) == 4 else x)
    df["DEP"]=df["CP"].str[:2]
    df=df[df["DEP"]==num_selected_dept]

    

    # Parcourir chaque ligne du DataFrame pour extraire les frontières et les afficher
    for _, row in df.iterrows():
            commune_name = row["NOM"]
            geoshape = row["geoshape"]
            concentration_com=row["Concentration"]
            normalized_valeur = (concentration_com - min_valeur) / (max_valeur  - min_valeur) * 255

            # Vérifier si la valeur de geoshape est une chaîne de caractères avant d'utiliser json.loads
            if isinstance(geoshape, str):
                try:
                    geoshape = json.loads(geoshape)  
                    geom_type = geoshape.get("type")
                    coordinates = geoshape.get("coordinates")
                    
                    # Ajouter les frontières de la commune
                    if geom_type == "Polygon":
                        for polygon in coordinates:
                            lon, lat = zip(*polygon)
                            fig.add_trace(go.Scattermapbox(
                                lon=lon,
                                lat=lat,
                                mode="lines",
                                line=dict(width=1, color="black"),
                                fill="toself",
                                fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                                text=f"{commune_name}- Valeur: {concentration_com}",
                                hoverinfo="text",
                                showlegend=False 
                            ))
                    elif geom_type == "MultiPolygon":
                        for multipolygon in coordinates:
                            for polygon in multipolygon:
                                lon, lat = zip(*polygon)
                                fig.add_trace(go.Scattermapbox(
                                    lon=lon,
                                    lat=lat,
                                    mode="lines",
                                    line=dict(width=1, color="black"),
                                    fill="toself",
                                    fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                                    text=f"{commune_name}- Valeur: {concentration_com}",
                                    hoverinfo="text",
                                    showlegend=False 
                                ))
                except json.JSONDecodeError:
                    print(f"Erreur de décodage JSON pour {commune_name}, geoshape ignoré.")
            else:
                print(f"Valeur géométrique invalide pour {commune_name}, geoshape ignoré.")

    # Centrer la carte sur une position moyenne
    fig.update_layout(
        height=800,
        mapbox=dict( 
            style="open-street-map",
            center=dict(lat=df["LATTI"].mean(), lon=df["LONGI"].mean()),
            zoom=8,
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    # Afficher la carte
    st.plotly_chart(fig, use_container_width=True)

#de manière identique par departement
def carte_concentration_dep():
    # Charger les données GeoJSON des départements
    with open("departements.geojson", "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    for feature in geojson_data["features"]:
        feature["properties"]["code"] = str(feature["properties"]["code"])
    concentration_dep["DEP"]=concentration_dep["DEP"].astype("str")
    valeurs_dict = dict(zip(concentration_dep["DEP"], concentration_dep["Concentration"]))
    data = {
        "DEP": [feature["properties"]["code"] for feature in geojson_data["features"]],
        "Concentration": [
            valeurs_dict.get(feature["properties"]["code"], None)  # Met la valeur ou None si non trouvé
            for feature in geojson_data["features"]
        ],
    }
    df = pd.DataFrame(data)

    min_valeur = df["Concentration"].min()
    max_valeur = df["Concentration"].max()

    fig = go.Figure()

    # Parcourir chaque département dans le GeoJSON
    for feature in geojson_data["features"]:
        code = feature["properties"].get("code", "N/A")  
        nom = feature["properties"].get("nom", "Inconnu")  
        geom = feature["geometry"]
        
        # Récupérer la concentration associée au département
        valeur = df.loc[df["DEP"] == code, "Concentration"].values[0]

        if pd.isna(valeur):
            valeur=0
            normalized_valeur=0
        else:
            normalized_valeur = (valeur - min_valeur) / (max_valeur - min_valeur) * 255
        
        # Ajouter la géométrie à la carte
        if geom["type"] == "Polygon":
            for coords in geom["coordinates"]:
                x, y = zip(*coords)
                fig.add_trace(go.Scattermapbox(
                    lon=x,
                    lat=y,
                    mode="lines",
                    line=dict(width=0.5, color="black"),
                    fill="toself",
                    fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                    text=f"{nom} - Valeur: {valeur}",
                    hoverinfo="text",
                    showlegend=False 
                ))
        elif geom["type"] == "MultiPolygon":
            for polygon in geom["coordinates"]:
                for coords in polygon:
                    x, y = zip(*coords)
                    fig.add_trace(go.Scattermapbox(
                        lon=x,
                        lat=y,
                        mode="lines",
                        line=dict(width=0.5, color="black"),
                        fill="toself",
                        fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                        text=f"{nom} - Valeur: {valeur}",
                        hoverinfo="text",
                        showlegend=False 
                    ))

    # Paramètre général de la carte
    fig.update_layout(
        height=800, 
        mapbox=dict(
            style="open-street-map", 
            center=dict(lat=46.5, lon=2.5), 
            zoom=5,  # Niveau de zoom
        ),
        margin=dict(l=0, r=0, t=0, b=0)  
    )

    st.plotly_chart(fig)

#affiche la population par departements
def affichage_population():
    with open("departements.geojson", "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    
    for feature in geojson_data["features"]:
        feature["properties"]["code"] = str(feature["properties"]["code"])

    concentration_dep["DEP"]=concentration_dep["DEP"].astype("str")
    valeurs_dict = dict(zip(concentration_dep["DEP"], concentration_dep["Population"]))
    data = {
        "DEP": [feature["properties"]["code"] for feature in geojson_data["features"]],
        "Population": [
            valeurs_dict.get(feature["properties"]["code"], None)  # Met la valeur ou None si non trouvé
            for feature in geojson_data["features"]
        ],
    }
    df = pd.DataFrame(data)
    min_valeur = df["Population"].min()
    max_valeur = df["Population"].max()

    fig = go.Figure()

    # Parcourir chaque département dans le GeoJSON
    for feature in geojson_data["features"]:
        code = feature["properties"].get("code", "N/A")  
        nom = feature["properties"].get("nom", "Inconnu")  
        geom = feature["geometry"]
        
        # Récupérer la concentration associée au département
        valeur = df.loc[df["DEP"] == code, "Population"].values[0]

        if pd.isna(valeur):
            valeur=0
            normalized_valeur=0
        else:
            normalized_valeur = (valeur - min_valeur) / (max_valeur - min_valeur) * 255
        
        # Ajouter la géométrie à la carte
        if geom["type"] == "Polygon":
            for coords in geom["coordinates"]:
                x, y = zip(*coords)
                fig.add_trace(go.Scattermapbox(
                    lon=x,
                    lat=y,
                    mode="lines",
                    line=dict(width=0.5, color="black"),
                    fill="toself",
                    fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                    text=f"{nom} - Valeur: {valeur}",
                    hoverinfo="text",
                    showlegend=False 
                ))
        elif geom["type"] == "MultiPolygon":
            for polygon in geom["coordinates"]:
                for coords in polygon:
                    x, y = zip(*coords)
                    fig.add_trace(go.Scattermapbox(
                        lon=x,
                        lat=y,
                        mode="lines",
                        line=dict(width=0.5, color="black"),
                        fill="toself",
                        fillcolor=f"rgba({normalized_valeur}, 0, {255-normalized_valeur}, 0.6)",
                        text=f"{nom} - Valeur: {valeur}",
                        hoverinfo="text",
                        showlegend=False 
                    ))

    # Paramètre général de la carte
    fig.update_layout(
        height=800, 
        mapbox=dict(
            style="open-street-map",  
            center=dict(lat=46.5, lon=2.5),  
            zoom=5,
        ),
        margin=dict(l=0, r=0, t=0, b=0)  
    )

    st.plotly_chart(fig)


###################################################################################################################
############################################## carte avec les bulles ##############################################
###################################################################################################################

#affiche une carte avec toutes les offres
def simple_map(df):
    fig = go.Figure()

    names = df["NOM"].tolist()
    communes = df["COMMUNE"].tolist()
    text_list = [(names[i], communes[i]) for i in range(len(names))]
        
    fig.add_trace(go.Scattermapbox(
        customdata=text_list,
        lat=df["LATTI"].tolist(),
        lon=df["LONGI"].tolist(),
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            color="greenyellow"
        ),
        hoverinfo="text",
        hovertemplate='<b>Name</b>: %{customdata[0]}<br><b>Commune</b>: %{customdata[1]}'
    ))

    fig.update_layout(
        height=800, 
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=46.03,
                lon=2.36
            ),
            pitch=0,
            zoom=5
        )
    )
    
    return fig

#viens regrouper les offres de la fonction précédente
def affichage_carte_bulle(archives,bat,biblio):
        # Liste des DataFrames et des catégories correspondantes
    dataframes = {
        "Archives": archives,
        "Bâtiments/Monuments": bat,
        "Bibliothèques": biblio,
        "Festivals": festivals,
        "Cinéma": cine,
        "Musées": musee,
        "Théâtre": theatre
    }

    # Couleurs personnalisées pour chaque catégorie
    category_colors = {
        "Archives": "red",
        "Bâtiments/Monuments": "blue",
        "Bibliothèques": "green",
        "Festivals": "purple",
        "Cinéma": "orange",
        "Musées": "brown",
        "Théâtre": "yellow"
    }

    default_fig = simple_map(tt_donnee)
    default_fig.update_traces(cluster=dict(enabled=True))
    st.plotly_chart(default_fig,use_container_width=True)


    liste_cat=["Archives","Bâtiments/Monuments","Bibliothèques","Festivals","Cinéma","Musées","Théâtre"]
    selected_categories = st.sidebar.multiselect(
        "Choisis les catégories à afficher",
        liste_cat,
        default=liste_cat  
    )

    sous_categories_dict = {}

    for category in selected_categories:
        df = dataframes[category]
        sous_categories = df["SOUS_TYPE"].dropna().unique() 

        selected_sous_categories = st.sidebar.multiselect(
            f"Choisis les sous-catégories pour {category}",
            sous_categories,
            default=sous_categories
        )
        sous_categories_dict[category] = selected_sous_categories



    # affichage 
    if selected_categories:
        fig = filter_map(selected_categories, sous_categories_dict,dataframes,category_colors,{"lat": 46.03, "lon": 2.36 , "zoom":5 ,"shape":""})
        fig.update_traces(cluster=dict(enabled=True))
        st.plotly_chart(fig,use_container_width=True)


###################################################################################################################
############################################## cluster ##############################################
###################################################################################################################

def afficher_cluster(communes):
    st.title("Ville et Commune colorés par clusters")
    fig = go.Figure()

   
    communes["CP"] = communes["CP"].astype(str).apply(lambda x: x.zfill(5))
    cluster["CP"] = cluster["CP"].astype(str).apply(lambda x: x.zfill(5))
    
 
    comm = communes.merge(cluster, on=["CP", "NOM"], how="left")

   
    liste_categ_couleurs = {
        'Seulement monuments et bibliothèques': '#6CA6CD',  # Bleu clair
        'Beaucoup de cinémas': '#98FB98',  # Vert menthe
        'Musée Cinémas': '#FFD700',  # Jaune doré
        'Peu de monuments': '#F4A7B9',  # Rose poudré
        'Peu de bibliothèques': '#C6A4E5',  # Lavande
        'Beaucoup d\'archives': '#FFA07A',  # Orange saumon
        'Musée': 'red'       # Rouge
    }


    for cluster_id, color in liste_categ_couleurs.items():
        cluster_data = comm[comm["Cluster_renommés"] == cluster_id] 
        
        if not cluster_data.empty:  
            fig.add_trace(go.Scattermapbox(
                lat=cluster_data["LATTI"],
                lon=cluster_data["LONGI"],
                mode='markers',
                hovertext=cluster_data["NOM"],  
                marker=go.scattermapbox.Marker(
                    size=5,
                    color=color
                ),
                name=f"{cluster_id}"  
            ))

   
    fig.update_layout(
        height=800,
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=46.03,
                lon=2.36
            ),
            pitch=0,
            zoom=5
        )
    )

 
    st.plotly_chart(fig, use_container_width=True)

###################################################################################################################
############################################## CHOIX ##############################################
###################################################################################################################


#permet le choix général des graphiques

st.set_page_config(layout="wide")

choix_carte = st.sidebar.selectbox(
    "Choix de la carte",
    ("Representation culture", "Concentration de culture", "Representation bulle","Cluster"),
)


if choix_carte=="Representation culture":
    st.title("Offre culturelle en France")
    affichage_carte(archives,bat,biblio)
elif choix_carte=="Representation bulle":
    st.title("Offre culturelle en France")
    affichage_carte_bulle(archives,bat,biblio)
elif choix_carte=="Cluster":
    afficher_cluster(communes)
else:
    affichage_concentration()
    



