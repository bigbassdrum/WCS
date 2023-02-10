import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# graphique seaborn
correl = sns.heatmap(df_cars.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))

# pour afficher : remplacer plt.show() par st.pyplot()
# st.pyplot(correl.figure)

# Pairplot
pairp = sns.pairplot(df_cars.sample(frac=0.2))

# pour afficher : remplacer plt.show() par st.pyplot()
# st.pyplot(pairp.figure)

# Evolution de la puissance à travers les années
ax1 = sns.set_style(style=None, rc=None )
fig, ax1 = plt.subplots(figsize=(12,7))
graph_1 = sns.lineplot(data = df_cars['year'], color = "purple", marker='o', sort = False, ax=ax1, label = "mpg")
plt.ylabel("mpg")
plt.xlabel("year")
graph_1.set_title("Evolution de la puissance à travers les années")
ax2 = ax1.twinx()
graph_2 = sns.barplot(data = df_cars, x='year', y='time-to-60', color = "royalblue", alpha=0.5, ax=ax2)
plt.ylabel("time-to-60")
# st.pyplot(ax1.figure)

# Menu
st.sidebar.title("Navigation")
options = st.sidebar.radio("Menu", options=["1. Correlation", 
"2. Pairplot", 
"3. Evolution de la puissance à travers les années",
"4. US",
"5. Europe",
"6. Japan"
])

# Navigation avec boutons radios
if options == "1. Correlation":
    st.title("1. Correlation", anchor=None)
    st.pyplot(correl.figure)    
elif options == "2. Pairplot":
    st.title("2. Pairplot", anchor=None)
    st.pyplot(pairp)
elif options == "3. Evolution de la puissance à travers les années":
    st.title("3. Evolution de la puissance à travers les années", anchor=None)
    st.pyplot(fig, ax2)
elif options == "4. US":
    df_cars[df_cars['continent'].str.contains('US')]
elif options == "5. Europe":
    df_cars[df_cars['continent'].str.contains('Europe')]
elif options == "6. Japan":
    df_cars[df_cars['continent'].str.contains('Japan')]