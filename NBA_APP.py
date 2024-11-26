import streamlit as st
from PIL import Image
import pandas as pd
import pickle

# Titre et image
st.title("From Draft to Legacy: Predict NBA Career Duration")

# Chargement de l'image
nba_image = Image.open('2910758.jpg')
st.image(nba_image, use_container_width=True)

# User inputs directly as a single form
st.header("Player Information")
name = st.text_input("Name (Player Name):", value="")
st.header("Player Statistics")
gp = st.text_input("Games Played (GP):", value="")
min_played = st.text_input("Minutes Played (MIN):", value="")
pts = st.text_input("Points Per Game (PTS):", value="")
fgm = st.text_input("Field Goals(FGM):", value="")
fga = st.text_input("Field Goal Attempts (FGA):", value="")
fg_percent = st.text_input("Field Goal Percent (FG%):", value="")
three_pm = st.text_input("3-Point Made (3P Made):", value="")
three_pa = st.text_input("3-Point Attempts (3PA):", value="")
three_percent = st.text_input("3-Point Percent (3P%):", value="")
ftm = st.text_input("Free Throws Made (FTM):", value="")
fta = st.text_input("Free Throw Attempts (FTA):", value="")
ft_percent = st.text_input("Free Throw Percent (FT%):", value="")
oreb = st.text_input("Offensive Rebounds (OREB):", value="")
dreb = st.text_input("Defensive Rebounds (DREB):", value="")
reb = st.text_input("Rebounds (REB):", value="")
ast = st.text_input("Assists (AST):", value="")
stl = st.text_input("Steals (STL):", value="")
blk = st.text_input("Blocks (BLK):", value="")
tov = st.text_input("Turnovers (TOV):", value="")

# Prétraitement des données utilisateur
def preprocess_user_data(data):
    """
    Prépare les données utilisateur pour les rendre compatibles avec le modèle entraîné.
    """
    # Calcul des colonnes dérivées
    data['Efficiency'] = data['PTS'] / ((data['FGA'] + data['3PA'] + data['FTA']).replace(0, 1))
    data['Efficiency_per_Minute'] = data['Efficiency'] / data['MIN']
    
    # Supprimer les colonnes inutiles
    columns_to_drop = ['Name', 'FGA', 'FGM', 'FTM', '3PA', 'DREB', 'OREB', 'Efficiency_per_Minute', '3P Made']
    data = data.drop(columns=columns_to_drop, errors='ignore')
    
    return data

# Charger le modèle SVM sauvegardé
with open('best_svm_model.pkl', 'rb') as file:
    svm_model = pickle.load(file)

# Bouton pour effectuer la prédiction
if st.button("Predict NBA Career Length"):
    try:
        # Convertir les entrées utilisateur en valeurs numériques
        user_data = pd.DataFrame({
            'Name': [name],
            'GP': [float(gp) if gp else 0],
            'MIN': [float(min_played) if min_played else 0],
            'PTS': [float(pts) if pts else 0],
            'FGM': [float(fgm) if fgm else 0],
            'FGA': [float(fga) if fga else 0],
            'FG%': [float(fg_percent) if fg_percent else 0],
            '3P Made': [float(three_pm) if three_pm else 0],
            '3PA': [float(three_pa) if three_pa else 0],
            '3P%': [float(three_percent) if three_percent else 0],
            'FTM': [float(ftm) if ftm else 0],
            'FTA': [float(fta) if fta else 0],
            'FT%': [float(ft_percent) if ft_percent else 0],
            'OREB': [float(oreb) if oreb else 0],
            'DREB': [float(dreb) if dreb else 0],
            'REB': [float(reb) if reb else 0],
            'AST': [float(ast) if ast else 0],
            'STL': [float(stl) if stl else 0],
            'BLK': [float(blk) if blk else 0],
            'TOV': [float(tov) if tov else 0]
        })
        
        # Prétraiter les données utilisateur
        preprocessed_data = preprocess_user_data(user_data)
        
        # Appliquer la prédiction
        prediction = svm_model.predict(preprocessed_data)
        prediction_text = "has an NBA career length of 5+ years" if prediction[0] == 1 else "has an NBA career length less than 5 years"
        
        # Afficher le résultat
        st.success(f"Player {name} {prediction_text}.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

