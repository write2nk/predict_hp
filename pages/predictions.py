# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
xgb_model = load('assets/xgb_model.joblib')
print('Model loaded successfully')

import pandas as pd
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

@app.callback(
    Output('prediction-content', 'children'),
    [Input('annual-income', 'value'),
    Input('credit-score', 'value'),
    Input('loan-amount', 'value'),
    Input('loan-purpose', 'value'),
    Input('monthly-debts', 'value')]
)

def predict(annual_income, credit_score, loan_amount, loan_purpose, monthly_debts):
    df = pd.DataFrame(
        columns  = ['Annual_Income', 'Credit_Score', 'Loan_Amount', 'Loan_Purpose','Monthly_Debts'],
        data = [[annual_income, credit_score, loan_amount, loan_purpose, monthly_debts]]
    )

    y_pred = xgb_model.predict(df)[0]
    return 'The model predicted ', float("{:.2f}".format(y_pred)),'% interest rate for 36 months'

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictors', className='children'),
        dcc.Markdown('#### Annual Income'),
        dcc.Input(
            id = 'annual-income',
            placeholder = 'Enter annual Income',
            type = 'number',
            value = '10000',
            className='mb-5',
        ),

            
        dcc.Markdown('#### Credit Score'), 
        dcc.Slider(
            id='credit-score', 
            min=500, 
            max=1000, 
            #step=50, 
            value=500, 
            marks={n: str(n) for n in range(500,1100,100)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Loan Amount'), 
        dcc.Slider(
            id='loan-amount', 
            min=5, 
            max=55, 
            #step=10, 
            value=5, 
            marks={i: '{}k' .format(i) for i in range(5,60,10)},
            className='mb-5', 
        ), 
       
       

            
        dcc.Markdown('#### Loan Purpose'), 
        dcc.Dropdown(
            id='loan-purpose', 
            options = [
                {'label': 'Debt Consolidation', 'value': 'Debt Consolidation'}, 
                {'label': 'Business', 'value': 'Business'}, 
                {'label': 'Car Financing', 'value': 'Car Financing'}, 
                {'label': 'Green Loan', 'value': 'Green Loan'}, 
                {'label': 'Home Purchase', 'value': 'Home Purchase'},  
                {'label': 'Home Maintenance', 'value': 'Home Maintenance'},  
                {'label': 'Medical Expenses', 'value': 'Medical Expenses'},  
                {'label': 'Relocation', 'value': 'Relocation'},  
                {'label': 'Vacation', 'value': 'Vacation'},  
                {'label': 'Wedding Ceremony', 'value': 'Wedding Ceremony'},  
                {'label': 'Credit Card Refinancing', 'value': 'Credit Card Refinancing'},  
                {'label': 'Others', 'value': 'Others'},   
            ], 
            value = 'Select Loan Purpose', 
            className='mb-5', 
        ), 


        dcc.Markdown('#### Monthly Debt'), 
        dcc.Slider(
            id='monthly-debts', 
            min=500, 
            max=6500, 
            #step=500, 
            value=500, 
            marks={n: str(n) for n in range(500,7000,1000)}, 
            className='mb-5', 
        ),

                
    ],
    md=6,
)






column2 = dbc.Col(
    [
        html.H2('Predict Loan Interest', className='mb-5'),
        

        dcc.Markdown(
            """
            #### The prediction is dynamically shown below:
            #### How to use this App
            Use the controls at the left hand side to update your predicted loan interest rate, based on your annual income,
            credit score, loan amount, loan purpose, and monthly debts
        
            """
        ),

        html.Div(id='slider-output-container'),

        html.Div(id='slider-output-container1'),

        html.Div(id='slider-output-container2'),
        html.Div(id='dd-output-container'),

        html.Div(id='slider-output-container3'),

       


        html.Div(id='prediction-content', className='lead')


    ]
)




@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('annual-income', 'value')])
def update_output(value):
    return 'You have selected Annual Income = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container1', 'children'),
    [dash.dependencies.Input('credit-score', 'value')])
def update_output(value):
    return 'You have selected Credit Score = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container2', 'children'),
    [dash.dependencies.Input('loan-amount', 'value')])
def update_output(value):
    return 'You have selected Loan Amount = "{}"'.format(value)

@app.callback(
    Output('dd-output-container', 'children'),
    Input('loan-purpose', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container3', 'children'),
    [dash.dependencies.Input('monthly-debts', 'value')])
def update_output(value):
    return 'You have selected Monthly Debts = "{}"'.format(value)

layout = dbc.Row([column1, column2])