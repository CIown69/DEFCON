import numpy as np
import plotly.graph_objects as go
import geocoder

def get_city_coordinates(city_name):
    location = geocoder.arcgis(city_name)
    return location.latlng if location.ok else None

city_name = input("Enter the city name: ")
coordinates = get_city_coordinates(city_name)

if coordinates is None:
    print(f"Coordinates for '{city_name}' not found.")
else:
    epicenter_lat, epicenter_lon = coordinates

    blast_radii = [0.97, 6.53, 11.1, 18.2]  # in km
    blast_zone_colors = ['orange', 'red', 'yellow', 'black']
    blast_zone_names = ['Fireball', 'Blast', 'Thermal Pulse', 'Pressure Wave']

    # The grid for each circular radius
    traces = []
    for i, radius in enumerate(blast_radii):
        theta = np.linspace(0, 2*np.pi, 100)
        x = epicenter_lon + radius / (111.32 * np.cos(np.radians(epicenter_lat))) * np.cos(theta)
        y = epicenter_lat + radius / 111.32 * np.sin(theta)

        # The trace for each circular radius
        trace = go.Scattermapbox(
            lat=y,
            lon=x,
            mode='lines',
            line=dict(color=blast_zone_colors[i], width=2),
            hoverinfo='none',
            name=blast_zone_names[i]
        )
        traces.append(trace)

    layout = go.Layout(
        title=f"{city_name} Nuclear Detonation",
        mapbox=dict(
            center=dict(lat=epicenter_lat, lon=epicenter_lon),
            zoom=10,
            style="carto-positron",
        ),
        annotations=[
            dict(
                x=0.9,
                y=0.9,
                xref="paper",
                yref="paper",
                text="Key Note: Instant Fatalities",
                showarrow=False,
            ),
            dict(
                x=0.9,
                y=0.85,
                xref="paper",
                yref="paper",
                text="<b>Fireball:</b> Fatality Rate: 100%",
                showarrow=False,
            ),
            dict(
                x=0.9,
                y=0.80,
                xref="paper",
                yref="paper",
                text="<b>Blast:</b> Fatality Rate: 70%",
                showarrow=False,
            ),
            dict(
                x=0.9,
                y=0.75,
                xref="paper",
                yref="paper",
                text="<b>Thermal Pulse:</b> Fatality Rate: 50%",
                showarrow=False,
            ),
            dict(
                x=0.9,
                y=0.70,
                xref="paper",
                yref="paper",
                text="<b>Pressure Wave:</b> Fatality Rate: 20%",
                showarrow=False,
            ),
        ]
    )

    fig = go.Figure(data=traces, layout=layout)

    fig.show()