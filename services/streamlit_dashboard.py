import pandas as pd
import matplotlib.pyplot as plt
import random

from fontTools.misc.testTools import parseXML

import plotly.express as px

df = pd.read_excel("pogoda_rozszerzona.xlsx")
# konwersja timestamp na datetime
df["timestamp_dt"] = pd.to_datetime(df["timestamp"], format = "%H:%M:%S %d-%m-%Y")
# sortowanie po timestamp
df=df.sort_values(["timestamp_dt"])
# print(df.info())


#plotly

# wykres kolowy - w porownaniu do matplotlib jest szybszy bo jest deklaratywny, wiecej rzeczy w matplotlib trzeba zdefiniowac

# fig = px.pie(
#     data_frame = df,
#     names= "description",
#     title = "udzial typow pogody"
# )
# fig.show()

#wykres slupkowy

# fig = px.bar(data_frame = df,
#              x = "place",
#              title = "liczba obserwacji w miastach")
# fig.update_layout(xaxis_title = "Miasta",
#                   yaxis_title = "liczba rekorsow")
# fig.show()

# # podstawowy wykres - zmiany w layout
# fig = px.bar(
#     data_frame=df,
#     x="place",
#     title="Liczba obserwacji w miastach",
#     color="place",  # różne kolory dla miast
#     color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#1A535C", "#FFBE0B", "#8338EC"]
# )
#
# # styl słupków
# fig.update_traces(
#     marker=dict(
#         line=dict(width=2, color="black"),  # obramowanie
#         opacity=0.9
#     ),
#     texttemplate='%{y}',        # wyświetlanie wartości nad słupkami
#     textposition='outside'
# )
#
# # styl layoutu
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczba rekordów",
#     template="simple_white",     # jasny elegancki motyw
#     font=dict(
#         family="Arial",
#         size=14,
#         color="black"
#     ),
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     margin=dict(l=40, r=40, t=60, b=40)
# )
#
# # styl osi
# fig.update_xaxes(
#     tickangle=45,
#     showgrid=True,
#     gridcolor="#E0E0E0"
# )
#
# fig.update_yaxes(
#     showgrid=True,
#     gridcolor="#E0E0E0",
#     rangemode="tozero"
# )
#
# fig.show()




# fig= px.scatter(
#     df,
#     x = "temp",
#     y = "humidity",
#     title = "temp vs Humidity",
#     labels = {"temp": "Temp. C", "humidity": "Humidity %"}
# )
# fig.show()

# wykres liniowy

city = "Toronto"
sub = df[df["place"] == city].sort_values("timestamp_dt")
fig = px.line(
    sub,
    x = "timestamp_dt",
    y = "temp"

)
fig.show()










# wszystko ponizej dotyczylo matplotlib
# wykres puntowy: temo vs humidity

# plt.figure()
# plt.scatter(df["temp"], df["humidity"])
# plt.xlabel("Temperature C")
# plt.ylabel("Humidity %")
# plt.title("Temperature vs. Humidity")
# plt.grid(True)
# plt.xlim(-20,50)
# plt.ylim(0,100)
# plt.show()

# #histogram rozklady temp
# plt.figure()
# # wyciaganie wartosci xi y i informacji o slupkach
# y, x, patches = plt.hist(df["temp"])
# plt.xlabel("Temperature C")
# plt.ylabel("Frequency")
# plt.title("Temperature histogram")
# plt.grid()
#
# print(y,x,patches)
#
# for p in patches:
#     p.set_color((random.random(),random.random(),random.random()))
#
# plt.show()

# # boxplot temp wedlug miasta
# #wybieramy 5 miast ktore miaja najwiecej pomiarow
# top_cities = df["place"].value_counts().head(5).index
# print(top_cities)
# # wybor wierszy ktore maja jedno z pieciu miast
# subset = df [df["place"].isin(top_cities) ]
# # wypis wszystkich wierszy (:) i tylko lokumny place
# # print(sunset.loc[:,["Place"]])
#
# data_for_box = [
#     subset[subset["place"] == city]["temp"]
#                 for city in top_cities
# ]
#
# plt.figure()
# plt.boxplot(data_for_box, tick_labels = top_cities)
#
# plt.show()

# # wykres liniowy temp dla jednego miasta w czasie
#
# city = "Lisbon"
#
# city_df = df[df["place"] == city]
# print(city_df)
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["temp"], label = "Temp" )
# plt.legend()
# plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label ="odczuwalna")
#
# plt.title(f" temepratura w czasie - {city}")
# plt.show()

# # srednia temp w miastach- wykres slupkowy
# mean_temp= df.groupby("place")["temp"].mean().sort_values()
# print(mean_temp)
#
# plt.figure()
# plt.ylim(-10,30)
# plt.grid()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.show()

# #zadanka
# #1Utwórz wykres słupkowy, gdzie pokażesz średnią wilgotność w miastach
# mean_hum= df.groupby("place")["humidity"].mean().sort_values()
# print(mean_hum)
#
# plt.figure()
# plt.ylim(-0,100)
# plt.xlabel("Czas")
# plt.ylabel("Wilgotność")
# plt.grid()
# plt.bar(mean_hum.index, mean_hum.values)
# plt.show()
#
# #2Utwórz wykres liniowy, gdzie pokazujesz prędkość wiatru w Toronto na przestrzeni czasu
# city = "Toronto"
# print(df)
# city_df = df[df["place"] == city]
# print(city_df)
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["wind"], label = "Wind speed" )
# plt.title(f" Prędkość wiatru w czasie - {city}")
# plt.show()

#3 Opcjonalnie - spróbuj wprowadzić wyglądy do wykresów


#4 Policz, ile występuje każdego rodzaju pogody (description).
# Narysuj wykres kołowy, który pokazuje udział procentowy typów pogody.Dodaj etykiety z wartościami procentowymi.

# weather_count= df["description"].value_counts()
# weather_name = df["description"].value_counts().index
# # print(weather)
# plt.legend()
# plt.figure()
# plt.pie(weather_count, labels = weather_name, autopct='%1.1f%%')
# plt.show()