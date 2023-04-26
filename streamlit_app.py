from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))

import json
import urllib.request

url = 'https://data.sanantonio.gov/api/3/action/datastore_search?resource_id=20eb6d22-7eac-425a-85c1-fdb365fd3cd7&limit=100'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())
# print(response_dict)

st.title('311 - City Services')
st.header('ALL SERVICE CALLS')

# with st.echo(code_location='below'):
st.json(response_dict, expanded=False)

jsonData2 = []

jsonData2 = response_dict['result']['records']

# st.json(jsonData, expanded=False)

# jsonData2 = []
# for arr1 in jsonData:
#   try:
#     info = arr1['info']
#     jsonData2.append(info)
#   except KeyError:
#     pass
    
st.json(jsonData2, expanded=False)

# pd_object = pd.read_json(jsonData2, typ='series')
df = pd.DataFrame(jsonData2)
st.dataframe(df)
st.experimental_data_editor(df)
df2 = df.groupby(['Category'])['Category'].count()
st.table(df2)
st.bar_chart(df2, x=0, y=None)


import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.table(chart_data)

st.bar_chart(chart_data)
