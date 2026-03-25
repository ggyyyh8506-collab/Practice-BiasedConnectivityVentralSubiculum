#import modules
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns 

#set color palette
colors = sns.color_palette('muted', 10)

PFC_color = "#FFDB6E"
NAc_color = "#BF43CC"
LH_color = "#87FFE1"

#coronal: load datasets and plot
df = pd.read_csv("/Users/yuyihe/ExampleNeuroDatasets/BiasedConnectivityVentralSubiculum/coronal_CTBLabelled_dataset.csv")

#subsets of coronal data: PFC, NAc, LH
df_subset_PFC = df[df.Projection == 'PFC']
df_subset_NAc = df[df.Projection == 'NAc']
df_subset_LH = df[df.Projection == 'LH']

#plot data
fig = go.Figure()

#PFC
fig.add_trace(go.Scatter3d(
    x=df_subset_PFC['AP'],
    y=df_subset_PFC['ML'],
    z=df_subset_PFC['DV'],
    mode='markers',
    name='PFC',
    marker=dict(
        size=3,
        color=PFC_color,
        opacity=0.1
    )
))

#NAc
fig.add_trace(go.Scatter3d(
    x=df_subset_NAc['AP'],
    y=df_subset_NAc['ML'],
    z=df_subset_NAc['DV'],
    mode='markers',
    name='NAc',
    marker=dict(
        size=3,
        color=NAc_color,
        opacity=0.1
    )
))

#LH
fig.add_trace(go.Scatter3d(
    x=df_subset_LH['AP'],
    y=df_subset_LH['ML'],
    z=df_subset_LH['DV'],
    mode='markers',
    name='LH',
    marker=dict(
        size=3,
        color=LH_color,
        opacity=0.1
    )
))

#change layout
fig["layout"].update(
    scene=dict(
        xaxis_title='AP',
        yaxis_title='ML',
        zaxis_title='DV'
    ),
    width=800,
    height=800,
    legend=dict(itemsizing='constant')
)


fig.show()



#PFC: load datasets and plot
df_trio_pfc = pd.read_csv("/Users/yuyihe/ExampleNeuroDatasets/BiasedConnectivityVentralSubiculum/PFC_TRIO_cellcounts.csv")

fig_pfc = px.scatter_3d(df_trio_pfc, x='AP', y='ML', z = 'DV', color = 'color', opacity = 0.5)

fig_pfc["layout"].update(width = 1200, height = 800, autosize = False)
fig_pfc.update_traces(marker_size=3)

fig_pfc.show()


#LH: load datasets and plot
df_trio_lh = pd.read_csv("/Users/yuyihe/ExampleNeuroDatasets/BiasedConnectivityVentralSubiculum/LH_TRIO_cellcounts.csv")

fig_lh = px.scatter_3d(df_trio_lh, x='AP', y='ML', z = 'DV', color = 'color', opacity = 0.5)

fig_lh["layout"].update(width = 1200, height = 800, autosize = False)
fig_lh.update_traces(marker_size=3)

fig_lh.show()


#NAc: load datasets and plot
df_trio_nac = pd.read_csv("/Users/yuyihe/ExampleNeuroDatasets/BiasedConnectivityVentralSubiculum/NAc_TRIO_cellcounts.csv")

fig_nac = px.scatter_3d(df_trio_nac, x='AP', y='ML', z = 'DV', color = 'color', opacity = 0.5)

fig_nac["layout"].update(width = 1200, height = 800, autosize = False)
fig_nac.update_traces(marker_size=3)

fig_nac.show()
