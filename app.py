import streamlit as st
import pandas as pd
import numpy as np
#import plotly.figure_factory as ff

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=["col1", "col2", "col3"]
# )

# st.line_chart(
#     chart_data,
#     x="col1",
#     y=["col2", "col3"],
#     color=["#FF0000", "#0000FF"],  # Optional
# )
st.write("teste")


# Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

#st.bar_chart(chart_data)
#st.area_chart(chart_data)
#st.line_chart (chart_data)

df = pd.read_csv("teste.csv")
#df = df.set_index("Despesa/Receita")
#st.bar_chart(df,x="Despesa/Receita")
st.area_chart(df)
st.line_chart (df) 
    #st.bokeh_chart (df) não tem
st.altair_chart (df) 
#st.plotly_chart (df)  não tem
 #st.pydeck_chart (df, height=20) erro
st.scatter_chart (df) 
    #st.graphviz_chart (df) erro
    #st.vega_lite_chart (df) erro

# st.write("Um gráfico usando panda e numpy")
# chart_data = pd.DataFrame(
#      np.random.randn(22, 3),

#      columns=["a", "b", "c"])
# st.line_chart(chart_data)

# df =  pd.read_csv('profitloss.csv')

# chart_data = pd.DataFrame(df)

#st.altair_chart(chart_data)
st.write("um texto qquer")
st.button("um botão qquer","","clique para fazer nada" )

st.write ("um data frame panda")
df = pd.DataFrame({
 'first column': [1, 2, 30, 4],
 'second column': [10, 30, 50, 40]
})

df

st.write ("um data frame numpy, especifico para operações numéricas")
#linhas, coluna
dataframe = np.random.randn(4, 5)
st.dataframe(dataframe)

st.write ("um mapa do panda")
map_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.map(map_data)

st.write ("um data frame panda com numpy para highlights")
dataframe = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_min(axis=0))

