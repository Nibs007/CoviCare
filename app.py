# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:23:16 2021

@author: nibed
"""

import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table as dt

import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


dm = pd.read_csv("https://raw.githubusercontent.com/Nibs007/OxyCare/main/Refined_WBO2.csv")

dm.head()

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64




import urllib.request
img = urllib.request.urlretrieve("https://www.homecaremag.com/sites/default/files/O2-oxygen-507182002-_0.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())
tab1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ll = dm['Area'].values.tolist()
ll= list(set(ll))

body = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("This is a repository collected from various sources. Contacts have to be verified by user.", color="dark"))),
               
                dbc.Col(dcc.Dropdown(id='x2',
            options=[{'label': i, 'value': i} for i in ll], style={'height': '60px'},
            multi=False,
            placeholder="Select an area"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image.decode()), style={'height': '200px',"margin-left": "20px","margin-right":'10-px'})
])), dbc.Row(html.Div(id="grp1"))])], className="mt-2")])

    
tab1.layout = html.Div([body])

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64


tab2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])




import urllib.request
img = urllib.request.urlretrieve("https://raw.githubusercontent.com/mllover5901/dat/main/gender-equality.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())







app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
server = app.server

app.layout = html.Div([
    html.H1('OxyCare'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Oxygen Near You', value='tab-1-example',style={'color':'white'}),
        dcc.Tab(label='Coming Soon', value='tab-2-example',style={'color':'white'}),
    ],colors={
            "border": "white",
            "primary": "black",
            "background": "black"}),
    html.Div(id='tabs-content-example')
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1.layout
    elif tab == 'tab-2-example':
        return tab2.layout

@app.callback(Output('grp1', 'children'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=dm
            else: 
                dff = dm[dm['Area']==year]
               
       
            df1 = dff[['Area','State','Contact Number']]
         
            data = df1.to_dict('rows')
            columns =  [{"name": i, "id": i,} for i in (df1.columns)]
            return dt.DataTable(data=data, columns=columns,style_header={ 'whiteSpace': 'normal','height': 'auto','backgroundColor': 'rgb(30, 30, 30)','color':'white','font_size':18},
                style_table={'overflowX': 'auto'},
                style_cell={'backgroundColor': 'white',
                    'color': 'black','font_size':18,'height':100,'fontWeight': 'bold',
                    # all three widths are needed
                    'minWidth': '500px', 'width': '500px', 'maxWidth': '500px',
                    'overflow': 'hidden','border': '1px solid grey',"margin-left": "40px","margin-left": "40px",
                    'textOverflow': 'ellipsis','textAlign': 'center','whiteSpace': 'normal'
       
                })
               

@app.callback(Output('Graph41', 'figure'),
                                  [Input('x3', 'value')])
def update_figure2(year):
            global dff 
            dm1 = dm[dm['% Female in Executives']!='No Information Available']
            
            if year==None:

                dff=dm1
            else: 
                dff = dm1[dm1['Industry']==year]
               
               
                         
            dff['% Female in Executives']=dff['% Female in Executives'].astype(int)
            import numpy as np
            dff['% Female in Executives']=np.round(dff['% Female in Executives'],1)
            gr = dff.groupby('Year')['% Female in Executives'].mean()
            grt = pd.DataFrame(gr)
            grt.columns=['Count']
            grt.reset_index(inplace=True)

            layout3 = go.Layout(plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)')
            fig = go.Figure(layout=layout3)
            fig.add_trace(px.bar(grt, x='Year', y='Count').data[0])
            fig.update_traces(marker_color='grey')
            fig.add_trace(px.line(grt, x='Year', y='Count',color_discrete_map={

                 "Count": "goldenrod"
             }).data[0])

            fig['layout']['xaxis'].update(title='Year', range=[2011, 2021], dtick=2,autorange=False)
            fig.update_layout(width=500, height=500,title='Females as Chief Executives over time',xaxis_title='Year',yaxis_title='%Female in Exec',margin=dict(l=20))
            


            return fig



@app.callback(Output('Graph51', 'figure'),
                                  [Input('x3', 'value')])
def update_figure2(year):
            global dff 
            layout = go.Layout(title = 'Scatter',
                                    xaxis=dict(
                                        title= 'Count'
                                    ),
                                    yaxis=dict(
                                        title='Revenue'
                                    ) ) 
            if year==None:

                dff=dm
            else: 
                dff = dm[dm['Industry']==year]
                
            gr = dff.groupby('Year')['% Female in Board'].mean()
            grt = pd.DataFrame(gr)
            grt.columns=['Count']
            grt.reset_index(inplace=True)

            layout3 = go.Layout(plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)')
            fig = go.Figure(layout=layout3)
            fig.add_trace(px.bar(grt, x='Year', y='Count').data[0])
            fig.update_traces(marker_color='grey')
            fig.add_trace(px.line(grt, x='Year', y='Count',color_discrete_map={

                 "Count": "goldenrod"
             }).data[0])

            fig['layout']['xaxis'].update(title='Year', range=[2011, 2021], dtick=2,autorange=False)
            fig.update_layout(width=500, height=500,title='Female Representation in Board over time',xaxis_title='Year',yaxis_title='%Female in Board',margin=dict(l=20))
            


            fig.update_layout(layout3)
              
            return fig

           
         

@app.callback(Output('Graph61', 'figure'),
                                  [Input('x3', 'value')])
def update_figure3(year):
            global dff 

            if year==None:

                mer=mer1
            else: 
                mer = mer1[mer1['Industry']==year]
               
            lll = mer.columns    
         
            if len(dff)>1:
                layout3 = go.Layout(
                   title='Female Representation & Revenue (USD)',plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)',xaxis={'showgrid':False})
             
                figg= px.scatter( mer,x='Revenue Rank', y='% Female in Board',color='Female Rep Rank',hover_data=['Name','Year'],size=[10]*len(mer)) 
                figg.update_layout(layout3)
                figg.update_xaxes(categoryorder='array', categoryarray= ['Low','Medium','High'])
 
                
 
              
                return figg

            else:
                return 'Not enough data'

@app.callback(Output('Graph11', 'figure'),
                                  [Input('x3', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=mer1
            else: 
                dff = mer1[mer1['Industry']==year]
               
            pp = dff['Female Rep Rank'].value_counts()
            pp=pd.DataFrame(pp)
            pp.reset_index(inplace=True)
            pp.columns =['Rank','Number']
            
            if len(pp[pp['Rank']=='Very Low']['Number'])!=0 and len(pp[pp['Rank']=='High']['Number'])!=0:
                vh = pp[pp['Rank']=='High']['Number'].values[0]/pp['Number'].sum()
                pvh=round(vh*100,0)                          
                lv = pp[pp['Rank']=='Very Low']['Number'].values[0]/pp['Number'].sum()
                lvh=round(lv*100,0)
                pv =[str(pvh)+" % Companies in this sector have high female representation in board committee",str(lvh)+" % Companies in this sector have very low female representation in board committee"]
            elif len(pp[pp['Rank']=='Very Low']['Number'])==0 and len(pp[pp['Rank']=='High']['Number'])!=0 :
                vh = pp[pp['Rank']=='High']['Number'].values[0]/pp['Number'].sum()
                pvh=round(vh*100,0)       
                pv =[str(pvh)+" % Companies in this sector have high female representation in board committee"]
            elif len(pp[pp['Rank']=='High']['Number'])==0 and len(pp[pp['Rank']=='Very Low']['Number'])!=0:
                lv = pp[pp['Rank']=='Very Low']['Number'].values[0]/pp['Number'].sum()
                lvh=round(lv*100,0)
                pv =[str(lvh)+" % Companies in this sector have very low female representation in board committee"]
            else:
                pv =['Companies in this sector have medium female representation']
                

            if len(pv)>1:   
                pv=pd.DataFrame(pv[1:],columns=[pv[0]])                
                
                figd = go.Figure(data=[go.Table(
                    header=dict(values=list(pv.columns),
                                fill_color='orange',line_color='orange',font=dict(color='white',size=13),
                                        align='left'),
                    cells=dict(values=[pv[k].tolist() for k in pv.columns],
                             fill_color='white',line_color='orange',font=dict(color='black',size=13),
                                       align='left'))])

                figd.update_layout(width=500, height=300,margin=dict(l=50))
                return figd
                
            elif len(pv)==1:
                pv=pd.DataFrame(pv)  
                figd = go.Figure(data=[go.Table(
                    
                    header=dict(values=[pv[k].tolist() for k in pv.columns],
                             fill_color='orange',line_color='orange',font=dict(color='white',size=13),
                                       align='left'))])

                figd.update_layout(width=500, height=300,margin=dict(l=50))
                return figd
            
            
                

@app.callback(Output('Graph31', 'figure'),
                                  [Input('x3', 'value')])
def update_figure4(year):
            global dff 

            if year==None:

                dff=mer1
            else: 
                dff = mer1[mer1['Industry']==year]
               
            lll = dff.columns    
            
            if len(dff)>1:
                layout3 = go.Layout(
                   title='Female Rep & Employee Count',plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)',xaxis={'showgrid':False})
               
                
                fige= px.scatter( dff,x='Employee Rank', y='% Female in Board',color='Female Rep Rank',hover_data=['Name'],size=[10]*len(dff)) 
                fige.update_layout(layout3)
                fige.update_xaxes(categoryorder='array', categoryarray= ['Low','Medium','High'])
 
              
                return fige

            else:
                return 'Not enough data'

@app.callback(Output('Graph21', 'figure'),
                                  [Input('x3', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=dm
            else: 
                dff = dm[dm['Industry']==year]
               
         
            df1 = dff[['Name','Year','% Female in Board','% Female in Executives']]
            df1['% Female in Board']=round(df1['% Female in Board'],1)
            df1.drop_duplicates(inplace=True)
            fig = go.Figure(data=[go.Table(header=dict(values=df1.columns,align="left",fill_color='orange',line_color='orange',font=dict(color='white')),
                             cells=dict(values=[df1[k].tolist() for k in df1.columns], fill_color='white',line_color='orange',
                                       align='left'))
                                    ])
                                  
            fig.update_layout(width=500, height=500,margin=dict(l=20))
            return fig

@app.callback(Output('Graph5', 'figure'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=d1
            else: 
                dff = d1[d1['Company']==year]
               
       
            df1 = dff[['Year','Name','gender']]
            df1.columns=['Year','Board of Directors','Gender']
            df1.drop_duplicates(inplace=True)
           
            fig = go.Figure(data=[go.Table(header=dict(values=df1.columns,align="center",fill_color='orange',line_color='orange',font=dict(color='white',size=14)),
                             cells=dict(values=[df1[k].tolist() for k in df1.columns], fill_color='white',line_color='orange',font=dict(color='black',size=13),
                                       align='center'))
                                    ])
                                  
            fig.update_layout(width=500, height=500,title='Names of Board of Directors',margin=dict(l=20))
            return fig

d2.loc[d2['Count'].isnull(),'Count']='No Information Available'

@app.callback(Output('Graph8', 'figure'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
           
            if year==None:

                dff=d2
            else: 
                dff = d2[d2['Company']==year]
            
            dff=dff[dff['Count']!='No Information Available']   
            if len(dff)!=0:
                df1 = dff[['Year','Name','gender']]
                df1.columns=['Year','Company Executives','Gender']

                fig = go.Figure(data=[go.Table(header=dict(values=df1.columns,align="left",fill_color='orange',line_color='orange',font=dict(color='white',size=14)),
                                 cells=dict(values=[df1[k].tolist() for k in df1.columns], fill_color='white',line_color='orange',font=dict(color='black',size=13),
                                           align='left'))
                                        ])

                fig.update_layout(width=500, height=500,title='Names of Executive Officers',margin=dict(l=20))
                return fig
            else:
                fig = go.Figure(data=[go.Table(
                                 cells=dict(values=['No Information Available'], fill_color='white',line_color='orange',font=dict(color='black',size=13),
                                           align='left'))
                                        ])

                fig.update_layout(width=500, height=500,title='Names of Executive Officers',margin=dict(l=20))
                return fig
                



@app.callback(Output('Graph6', 'figure'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=d1
            else: 
                dff = d1[d1['Company']==year]
               
            fem = dff[dff['gender']=='F']
            gr = fem.groupby(['Year'])['Count'].mean()



            grt = pd.DataFrame(gr)
            grt.columns=['Count']
            grt.reset_index(inplace=True)
            
            layout3 = go.Layout(plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)')
            fig = go.Figure(layout=layout3)
            fig.add_trace(px.bar(grt, x='Year', y='Count').data[0])
            fig.update_traces(marker_color='grey')
            fig.add_trace(px.line(grt, x='Year', y='Count',color_discrete_map={
                 
                 "Count": "goldenrod"
             }).data[0])
            
                                  
            fig.update_layout(width=500, height=500,title='Female Representation in Board over time',margin=dict(l=20))
            fig['layout']['xaxis'].update(title='Year', range=[2011, 2021], dtick=2,autorange=False)
            fig['layout']['yaxis'].update(title='Percent Female in Board')
            return fig

@app.callback(Output('Graph9', 'figure'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=d2
            else: 
                dff = d2[d2['Comp1']==year]
            dff = dff[dff['Count']!='No Information Available']
            dff['Count']=dff['Count'].astype(int)
            fem = dff[dff['gender']=='F']
            gr = fem.groupby(['Year'])['Count'].mean()



            grt = pd.DataFrame(gr)
            grt.columns=['Count']
            grt.reset_index(inplace=True)
            
            layout3 = go.Layout(plot_bgcolor='rgb(290,248,255)',
                                             paper_bgcolor= 'rgb(290,255,255)')
            fig = go.Figure(layout=layout3)
            fig.add_trace(px.bar(grt, x='Year', y='Count').data[0])
            fig.update_traces(marker_color='grey')
            fig.add_trace(px.line(grt, x='Year', y='Count',color_discrete_map={
                 
                 "Count": "goldenrod"
             }).data[0])
            
                                  
            fig.update_layout(width=500, height=500,title='Females as Executives over time',margin=dict(l=20))
            fig['layout']['xaxis'].update(title='Year', range=[2011, 2021], dtick=2,autorange=False)
            fig['layout']['yaxis'].update(title='Percent Female as Executive')

            return fig

if __name__ == "__main__":
    app.run_server()