import plotly.graph_objects as go

north_dakota_coord = {"lat": 46.7296, "lon": -94.6859}
russian_cities = [
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
    {"name": "Saint Petersburg", "lat": 59.9343, "lon": 30.3351},
    {"name": "Novosibirsk", "lat": 55.0084, "lon": 82.9357},
    {"name": "Yekaterinburg", "lat": 56.8389, "lon": 60.6057},
    {"name": "Nizhny Novgorod", "lat": 56.2965, "lon": 43.9361},
    {"name": "Kazan", "lat": 55.8304, "lon": 49.0661},
    {"name": "Chelyabinsk", "lat": 55.1644, "lon": 61.4368},
    {"name": "Omsk", "lat": 54.9885, "lon": 73.3242},
    {"name": "Samara", "lat": 53.2415, "lon": 50.2212},
    {"name": "Rostov-on-Don", "lat": 47.2357, "lon": 39.7015},
    {"name": "Ufa", "lat": 54.7388, "lon": 55.9721},
    {"name": "Krasnoyarsk", "lat": 56.0097, "lon": 92.7917},
    {"name": "Perm", "lat": 58.0104, "lon": 56.2502},
    {"name": "Voronezh", "lat": 51.6720, "lon": 39.1843},
    {"name": "Volgograd", "lat": 48.7080, "lon": 44.5133},
    {"name": "Krasnodar", "lat": 45.0393, "lon": 38.9872},
    {"name": "Saratov", "lat": 51.5303, "lon": 45.9530},
    {"name": "Tyumen", "lat": 57.1613, "lon": 65.5250},
    {"name": "Tolyatti", "lat": 53.5088, "lon": 49.4186},
    {"name": "Izhevsk", "lat": 56.8526, "lon": 53.2045},
    {"name": "Barnaul", "lat": 53.3481, "lon": 83.7798},
    {"name": "Ulyanovsk", "lat": 54.3142, "lon": 48.4031},
    {"name": "Irkutsk", "lat": 52.2871, "lon": 104.2807},
    {"name": "Khabarovsk", "lat": 48.4827, "lon": 135.0838},
    {"name": "Yaroslavl", "lat": 57.6261, "lon": 39.8845},
    {"name": "Vladivostok", "lat": 43.1155, "lon": 131.8855},
    {"name": "Makhachkala", "lat": 42.9831, "lon": 47.5046},
    {"name": "Tomsk", "lat": 56.4846, "lon": 84.9484},
    {"name": "Orenburg", "lat": 51.7875, "lon": 55.1010},
    {"name": "Kemerovo", "lat": 55.3556, "lon": 86.0860},
]

southern_russia_coord = {"lat": 43.5853, "lon": 39.7203}
southern_china_coord = {"lat": 24.4798, "lon": 118.0894}
american_cities = [
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"name": "Chicago", "lat": 41.8781, "lon": -87.6298},
    {"name": "Houston", "lat": 29.7604, "lon": -95.3698},
    {"name": "Phoenix", "lat": 33.4484, "lon": -112.0740},
    {"name": "Philadelphia", "lat": 39.9526, "lon": -75.1652},
    {"name": "San Antonio", "lat": 29.4241, "lon": -98.4936},
    {"name": "San Diego", "lat": 32.7157, "lon": -117.1611},
    {"name": "Dallas", "lat": 32.7767, "lon": -96.7970},
    {"name": "San Jose", "lat": 37.3382, "lon": -121.8863},
    {"name": "Austin", "lat": 30.2672, "lon": -97.7431},
    {"name": "Jacksonville", "lat": 30.3322, "lon": -81.6557},
    {"name": "Fort Worth", "lat": 32.7555, "lon": -97.3308},
    {"name": "Columbus", "lat": 39.9612, "lon": -82.9988},
    {"name": "Charlotte", "lat": 35.2271, "lon": -80.8431},
    {"name": "San Francisco", "lat": 37.7749, "lon": -122.4194},
    {"name": "Indianapolis", "lat": 39.7684, "lon": -86.1581},
    {"name": "Seattle", "lat": 47.6062, "lon": -122.3321},
    {"name": "Denver", "lat": 39.7392, "lon": -104.9903},
    {"name": "Washington, D.C.", "lat": 38.9072, "lon": -77.0369},
    {"name": "Boston", "lat": 42.3601, "lon": -71.0589},
    {"name": "El Paso", "lat": 31.7619, "lon": -106.4850},
    {"name": "Nashville", "lat": 36.1627, "lon": -86.7816},
    {"name": "Detroit", "lat": 42.3314, "lon": -83.0458},
    {"name": "Oklahoma City", "lat": 35.4676, "lon": -97.5164},
    {"name": "Portland", "lat": 45.5051, "lon": -122.6750},
    {"name": "Las Vegas", "lat": 36.1699, "lon": -115.1398},
    {"name": "Memphis", "lat": 35.1495, "lon": -90.0490},
    {"name": "Louisville", "lat": 38.2527, "lon": -85.7585},
    {"name": "Baltimore", "lat": 39.2904, "lon": -76.6122},
]

chinese_cities = [
    {"name": "Shanghai", "lat": 31.2304, "lon": 121.4737},
    {"name": "Beijing", "lat": 39.9042, "lon": 116.4074},
    {"name": "Chongqing", "lat": 29.4316, "lon": 106.9123},
    {"name": "Tianjin", "lat": 39.3434, "lon": 117.3616},
    {"name": "Guangzhou", "lat": 23.1291, "lon": 113.2644},
    {"name": "Shenzhen", "lat": 22.5431, "lon": 114.0579},
    {"name": "Dongguan", "lat": 23.0205, "lon": 113.7518},
    {"name": "Nanjing", "lat": 32.0603, "lon": 118.7969},
    {"name": "Hangzhou", "lat": 30.2741, "lon": 120.1551},
    {"name": "Wuhan", "lat": 30.5928, "lon": 114.3055},
    {"name": "Shenyang", "lat": 41.8057, "lon": 123.4315},
    {"name": "Chengdu", "lat": 30.5728, "lon": 104.0668},
    {"name": "Xi'an", "lat": 34.3416, "lon": 108.9398},
    {"name": "Harbin", "lat": 45.8038, "lon": 126.5349},
    {"name": "Suzhou", "lat": 31.2989, "lon": 120.5853},
    {"name": "Changchun", "lat": 43.8171, "lon": 125.3235},
    {"name": "Dalian", "lat": 38.9140, "lon": 121.6147},
    {"name": "Zhengzhou", "lat": 34.7466, "lon": 113.6254},
    {"name": "Qingdao", "lat": 36.0671, "lon": 120.3826},
    {"name": "Shijiazhuang", "lat": 38.0428, "lon": 114.5149},
    {"name": "Jinan", "lat": 36.6512, "lon": 117.1201},
    {"name": "Nanning", "lat": 22.8170, "lon": 108.3669},
    {"name": "Changsha", "lat": 28.2282, "lon": 112.9388},
    {"name": "Kunming", "lat": 25.0389, "lon": 102.7186},
    {"name": "Guiyang", "lat": 26.6477, "lon": 106.6302},
    {"name": "Nanchang", "lat": 28.6829, "lon": 115.8582},
    {"name": "Haikou", "lat": 20.0440, "lon": 110.1999},
    {"name": "Taiyuan", "lat": 37.8706, "lon": 112.5489},
    {"name": "Hefei", "lat": 31.8206, "lon": 117.2272},
    {"name": "Xiamen", "lat": 24.4798, "lon": 118.0894}
]


fig = go.Figure()

#ICBM trails from North Dakota to largest Russian cities
for city in russian_cities:
    fig.add_trace(
        go.Scattergeo(
            locationmode='ISO-3',
            lon=[north_dakota_coord['lon'], city['lon']],
            lat=[north_dakota_coord['lat'], city['lat']],
            mode='lines',
            line=dict(width=2, color='blue'),
            name=f'ICBM Silo to {city["name"]}'
        )
    )

#ICBM trails from Southern Russia to largest American cities
for city in american_cities:
    fig.add_trace(
        go.Scattergeo(
            locationmode='ISO-3',
            lon=[southern_russia_coord['lon'], city['lon']],
            lat=[southern_russia_coord['lat'], city['lat']],
            mode='lines',
            line=dict(width=2, color='red'),
            name=f'ICBM Silo to {city["name"]}'
        )
    )

for city in chinese_cities:
    fig.add_trace(
        go.Scattergeo(
            locationmode='ISO-3',
            lon=[north_dakota_coord['lon'], city['lon']],
            lat=[north_dakota_coord['lat'], city['lat']],
            mode='lines',
            line=dict(width=2, color='cyan'),
            name=f'ICBM Silo to {city["name"]}'
        )
    )

for city in american_cities:
    fig.add_trace(
        go.Scattergeo(
            locationmode='ISO-3',
            lon=[southern_china_coord['lon'], city['lon']],
            lat=[southern_china_coord['lat'], city['lat']],
            mode='lines',
            line=dict(width=2, color='orange'),
            name=f'ICBM Silo to {city["name"]}'
        )
    )

fig.update_layout(
    title_text='ICBM Trails from North Dakota to Russian Cities and Southern Russia to American Cities',
    showlegend=True,
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
)

fig.show()