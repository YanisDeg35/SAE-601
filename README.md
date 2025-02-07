"# Projet SAE VCOD 6-01, notebook jupyther python, envoyée sur git. contient l'utilisation de pandas et visualisations avec seaborn" 
Application.py utilise streamlit avec des graphiques interactives pour visualiser les différents problème et nos différentes analyses, sur le dataset sur les salaires des métiers de la data.
Le dataset provient de Kaggle avec plusieurs informations, le salaire de plusieurs salariés, leurs expériences, leurs métiers, s'ils sont ou non en télétravail, la taille de leurs entreprises, le pays de l'entreprise et le pays du salarié


import kagglehub

# Download latest version
path = kagglehub.dataset_download("arnabchaki/data-science-salaries-2023")

print("Path to dataset files:", path)

conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly

streamlit run application.py

Lien vers l'application share.streamlit : https://sae-601-pthbojjdky7yrfnmvs5skb.streamlit.app/
