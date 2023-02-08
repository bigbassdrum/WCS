import streamlit as st
import pandas as pd

# afficher un titre
st.title('Hello Wilders, welcome to my application!')

# afficher du texte
st.write("I enjoy to discover stremalit possibilities")

# afficher un dataframe
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather) # ou utiliser "magic commands": df_weather

# afficher des graphiques
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# graphique seaborn
import seaborn as sns
viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

# pour afficher : remplacer plt.show() par st.pyplot()
st.pyplot(viz_correlation.figure)

pd.show_versions()

