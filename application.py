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

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Question 2 Distribution Salaire", "Question 3 Distribution salaire par niveau d'expérience et rôle", "Question 4 Analyse des tendances de salaires", "Question 5 Corrélation entre variables", "Question 5 Analyse interactive des variations de salaire", "Question 7 Salaire médian par expérience et taille d'entreprise", "Question 8 Ajout de filtres dynamiques", "Question 9 Impact du teletravail sur le salaire selon le pays", "Question 10 Filtrage avancé des données"])
#import kagglehub

# Download latest version
#path = kagglehub.dataset_download("arnabchaki/data-science-salaries-2023")

#print("Path to dataset files:", path)

### 2. Exploration visuelle des données
#votre code 
if page == "Question 2 Distribution Salaire":
    st.header('Question 2 Distribution Salaire')
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
if page == "Question 3 Distribution salaire par niveau d'expérience et rôle":
    st.header("Question 3 Distribution salaire par niveau d'expérience et rôle")
    st.subheader("📈 Distribution des salaires en France")
    df_fr = df[df['company_location'] == 'FR']
    df_fr
    fig1 = px.box(df_fr, x='job_title', y='salary_in_usd', color='experience_level')  # Créer un boxplot interactif
    st.plotly_chart(fig1)

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
if page == "Question 4 Analyse des tendances de salaires":
    st.header('Question 4 Analyse des tendances de salaires')
    selected_option = st.selectbox('Choisir une option', options=['experience_level', 'employment_type', 'job_title', 'company_location'])
    df_cat = df.groupby(selected_option)[ 'salary_in_usd'].mean().reset_index()
    
    fig = px.bar(df_cat, title='Graphique moyen par catégorie', x=selected_option, y='salary_in_usd',color=selected_option)
    st.plotly_chart(fig)

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
if page == "Question 5 Corrélation entre variables":
    st.header('Question 5 Corrélation entre variables')
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
if page == "Question 6 Analyse interactive des variations de salaire":
    st.header('Question 6 Analyse interactive des variations de salaire')
    st.subheader("📈 Évolution des salaires pour les 10 postes les plus courants")
    
    top = df['job_title'].value_counts().nlargest(10).index
    df_top = df[df['job_title'].isin(top)]
    salaire_an = df_top.groupby(['job_title', 'work_year'])['salary_in_usd'].mean().reset_index()
    
    fig4 = px.line(salaire_an,x='work_year',y='salary_in_usd', color='job_title', title='Évolution des salaires pour les 10 postes les plus courants',labels={'salary_in_usd': 'Salaire moyen (USD)', 'work_year': 'Année'},template="plotly_white")
    st.plotly_chart(fig4)
    st.write('on observe une chute generale des salaires en 2021, probablement a cause de developpement des IA, soit a cause du confinement, mais ils se retablissent rapidements.' )

### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 
if page == "Question 7 Salaire médian par expérience et taille d'entreprise":
    st.header("Question 7 Salaire médian par expérience et taille d'entreprise")
    st.subheader("Salaire médian par expérience et taille d'entreprise")
    df2 = df.groupby(['company_size', 'experience_level'])['salary_in_usd'].median().reset_index()
    
    fig = px.bar(df2, title='somme des salaires médianes par expérience et taille d entreprise', x='company_size', y='salary_in_usd',color='experience_level')
    st.plotly_chart(fig)
    st.write('la lecture de ce graphique n est pas evidante, il faut comprendre que chaque barre est une somme mediannes des types de salaries (leurs experience), et il faut utiliser le fait que graphque est interactif pour observer les mediannes exactes pour tel ou tel classe.' )

### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 
if page == "Question 8 Ajout de filtres dynamiques":
    st.header('Question 8 Ajout de filtres dynamiques')
    st.subheader("Filtres salaire")
    
    min_salary = 0
    max_salary = 500000
    selection_salaire = st.slider('Sélectionnez une plage de salaires (en USD)', min_value= min_salary, max_value=max_salary, value=(min_salary,max_salary))
    
    Salaire = df[(df['salary_in_usd'] >= selection_salaire[0]) & (df['salary_in_usd'] <= selection_salaire[1])]
    st.write(Salaire)



### 9.  Impact du télétravail sur le salaire selon le pays
if page == "Question 9 Impact du teletravail sur le salaire selon le pays":
    st.header('Question 9 Impact du teletravail sur le salaire selon le pays')
    st.subheader("Impact du télétravail sur le salaire selon le pays")
    
    df_remote = df[df['remote_ratio'] == 100]
    df_sansremote = df[df['remote_ratio'] == 0]
    
    pays = df_remote['company_location'].unique()
    selection_pays = st.selectbox('Sélectionnez un pays', pays)
    df_pays = df_remote[df_remote['company_location'] == selection_pays]
    df_pays2 = df_sansremote[df_sansremote['company_location'] == selection_pays]
    
    salaire_stat = df_pays['salary_in_usd'].describe()
    salaire_stat2 = df_pays2['salary_in_usd'].describe()
    stats = pd.DataFrame({ 'Télétravail 100%': salaire_stat,'Sans télétravail': salaire_stat2 })
    
    
    st.write(f"Statistiques des salaires pour {selection_pays}  :")
    st.write(stats)
    st.write('on observe que generalement, entre les pays, le salaire est plus haute pour ceux qui sont en presentielle.' )
    
    fig, ax = plt.subplots()
    ax.hist(df_pays['salary_in_usd'], bins=20, edgecolor='black')
    ax.set_title(f"Distribution des salaires en télétravail pour {selection_pays}")
    ax.set_xlabel('Salaire en USD')
    ax.set_ylabel('Nombre d\'employés')
    st.pyplot(fig)
    st.write('Si on choisi un pays avec beaucoup de données, on peut observer quelquechose qui s approche a une distribution normale, en teletravail, il y a autant de plus de salariées, que leurs salaire s approche de la moyenne .' )
### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 
if page == "Question 10 Filtrage avancé des données":
    st.header('Question 10 Filtrage avancé des données')
    st.subheader(" Filtrage avancé des données sur le niveau d'experience et la taille de l'entreprise")
    
    niv_experience = df['experience_level'].unique()
    taille_company = df['company_size'].unique()
    
    selection_experience = st.multiselect( 'Sélectionnez le niveau d\'expérience', options=niv_experience)
    selection_taille = st.multiselect('Sélectionnez la taille d\'entreprise',options=taille_company )
    
    
    if selection_experience:
        df_filtre = df[df['experience_level'].isin(selection_experience)]
    else:
        df_filtre = df.copy()
    if selection_taille:
        df_filtre = df_filtre[df_filtre['company_size'].isin(selection_taille)]
    
    st.dataframe(df_filtre)
    st.write(f'Voici les données filtrées, selon le niveau d\'expérience et la taille d\'entreprise, ici les filtres apliquées sont :  {selection_experience}, {selection_taille}')