"# Projet SAE VCOD 6-01, notebook jupyther python, envoyée sur git. contient l'utilisation de pandas et visualisations avec seaborn" 
application streamlit avec des graphiques interactives.
données
import kagglehub

# Download latest version
path = kagglehub.dataset_download("arnabchaki/data-science-salaries-2023")

print("Path to dataset files:", path)

conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly
