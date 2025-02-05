"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
df = pd.read_csv(r"H:\IUT\SAE 601\ds_salaries.csv")


import kagglehub

# Download latest version
path = kagglehub.dataset_download("arnabchaki/data-science-salaries-2023")

print("Path to dataset files:", path)

### 2. Exploration visuelle des données
#votre code 

st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

if st.checkbox("Afficher un aperçu des données"):
    st.write(df)
    


#Statistique générales avec describe pandas 
#votre code 
st.subheader("📌 Statistiques générales")
st.write(df.describe())  #  Résumé statistique des colonnes numériques du DataFrame.

fig = px.box(df, x='job_title', y='salary_in_usd', color='experience_level')  # Créer un boxplot interactif
st.plotly_chart(fig)
fig = px.bar(df, x='job_title', y='salary_in_usd', color='company_size')  # Créer un graphique à barres interactif
st.plotly_chart(fig)
fig, ax = plt.subplots()  #  Crée une figure et un axe pour le graphique


### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 
st.subheader("📈 Distribution des salaires en France")
df_fr = df[df['company_location'] == 'FR']
df_fr
fig1 = px.box(df_fr, x='job_title', y='salary_in_usd', color='experience_level')  # Créer un boxplot interactif
st.plotly_chart(fig1)

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
selected_option = st.selectbox('Choisir une option', options=['experience_level', 'employment_type', 'job_title', 'company_location'])
df_cat = df.groupby(selected_option)[ 'salary_in_usd'].mean().reset_index()

fig = px.bar(df_cat, title='Graphique moyen par catégorie', x=selected_option, y='salary_in_usd',color=selected_option)
st.plotly_chart(fig)

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
numeric_df = df.select_dtypes(include=[np.number])  # Sélectionner uniquement les colonnes numériques
st.write(numeric_df)

# Calcul de la matrice de corrélation
#votre code
#sns.heatmap() : Créer des cartes thermique
correlation_matrix = pd.DataFrame(numeric_df).corr()



# Affichage du heatmap avec sns.heatmap
#votre code 
st.subheader("🔗 Corrélations entre variables numériques")
fig3, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig3)



### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code 
top = df['job_title'].value_counts().nlargest(10).index
df_top = df[df['job_title'].isin(top)]
salaire_an = df_top.groupby(['job_title', 'work_year'])['salary_in_usd'].mean().reset_index()

st.subheader("📈 Évolution des salaires pour les 10 postes les plus courants")

fig4 = px.line(salaire_an,x='work_year',y='salary_in_usd', color='job_title', title='Évolution des salaires pour les 10 postes les plus courants',labels={'salary_in_usd': 'Salaire moyen (USD)', 'work_year': 'Année'},template="plotly_white")
st.plotly_chart(fig4)


### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 

st.subheader("Salaire médian par expérience et taille d'entreprise")
df2 = df.groupby(['company_size', 'experience_level'])['salary_in_usd'].median().reset_index()

fig = px.bar(df2, title='somme des salaires médianes par expérience et taille d entreprise', x='company_size', y='salary_in_usd',color='experience_level')
st.plotly_chart(fig)


### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 




### 9.  Impact du télétravail sur le salaire selon le pays




### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

