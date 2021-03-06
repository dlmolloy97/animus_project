def html_builder():
  import geopandas as gpd
  import altair as alt
  import numpy as np
  import pandas as pd
  df=gpd.read_file('Data/cleaned.shp')
  median_animus=np.nanmean(df['animus'])
  df['animus_difference']=(median_animus-df['animus'])/df['animus']
  chart=alt.Chart(df).mark_geoshape().encode(
    color=alt.Color('animus_difference:Q',
        scale=alt.Scale(scheme='redblue'),
        legend=alt.Legend(direction='horizontal')),
    tooltip=['dma_1', alt.Tooltip('animus_difference:Q', format='.1%')]
).properties(
    title={
      "text": ["Percent difference in racial animus by Designated Market Area"], 
      "subtitle": ["Degree of racial animus, as measured by Google searches for the N word, compared to the national median.","Based on Chae et al (2015)"],
      "color": "black",
      "subtitleColor": "black"
    }
)
  chart.save('animus.html')

