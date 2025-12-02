import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go



def create_plots(df):

# konwersja timestamp na datetime
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S %d-%m-%Y")
# sortowanie po timestamp
    df = df.sort_values(["timestamp_dt"])

    fig = make_subplots(rows = 2, cols= 2,
                    subplot_titles = ["Temperatura","wilgotnosc","cissnienie","wiatr"]
                    )

    fig.add_trace(
    go.Scatter(y= df["temp"], name = "temp" ),
    row = 1, col = 1
    )
    fig.add_trace(
    go.Scatter(y= df["humidity"], name = "humidity" ),
    row = 1, col = 2
    )
    fig.add_trace(
    go.Scatter(y= df["pressure"], name = "pressure" ),
    row = 2, col = 1
    )
    fig.add_trace(
    go.Scatter(y= df["wind"], name = "wind" ),
    row = 2, col = 2
    )
    fig.update_layout(height = 700, width = 900, title = "Wiele wykresow")
    fig.show()


# def line_chart(df, city):
#     # konwersja timestamp na datetime
#     df["timestamp_dt"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S %d-%m-%Y")
#     # sortowanie po timestamp
#     df = df.sort_values(["timestamp_dt"])
#
#     sub = df[df["place"] == city].sort_values("timestamp_dt")
#     fig = px.line(
#         sub,
#         x="timestamp_dt",
#         y="temp"
#     )
#     fig.show()

