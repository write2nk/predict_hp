# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            This web-based loan interest rate prediction model was developed for the purpose of estimating the interest rate of a loan for 36 months 
            and then compare it to what the lending club would give you as their own interest rate. It followed the systematic approach of data science,
            such as data wrangling and story telling, feature engineering, data visualization, exploratory data analysis (EDA) and application of machine learning model(train, 
            validate and predict loan interest rate) using extreme gradient boost (XGBoost) model. In the EDA, the target variable is multi-modal and right skewed with small
            percentage of outliers. 




            """
        ),

        html.Img(src='assets/target.png', className='img-fluid'),

        dcc.Markdown(

            """ 
            To ensure that the features are statistically correlated with the target variable, I used pearson correlation coefficient method and it is shown in Table 1. 
            Importanly, it is shown that Credit Score has a strong negative correlation with the Interest Rate, this implies that when the Credit Score is high the interest rate 
            is low. 
            """
        ),
        html.Img(src='assets/corr.png', className='img-fluid'),

    ],
)

layout = dbc.Row([column1])