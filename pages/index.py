# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Should I proceed to get the loan or Not?
            
            This machine learning-based web app enables you to get a quick estimate of the possible interest rate you could get while seeking a loan from a lending club.

            The Lending Club may only  give you a direct estimate, however, you have to provide your name, and then they will import your credit score. 
            Although they say that this does not affect your credit score. Due to an anonymous convenient estimate, the Lending Club formula has been reversed
            using a machine learning model. This app is interactive and flexible to use, so click and play around with this to get the right estimate of your interest 
            rate for a better decision.

            ✅ RUN the App by clicking the Predict Button

            ❌ The App predicts only the loan interest rate

            """
        ),
        dcc.Link(dbc.Button('Make Prediction', color='dark'), href='/predictions')
    ],
    md=4,
)


df = pd.read_csv('/home/nkiru/data.csv')
fig = px.scatter(df, x = 'Credit Score', y = 'Interest Rate', color = 'Loan Purpose')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])