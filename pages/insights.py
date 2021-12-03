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
        
            ## Insights
            When the dataset has two or more correlated features, then from the point of view of the model, any of these correlated features can be used as the predictor, 
            with no concrete preference of one over the others. By Applying feature importance, one can identify the top most important features that can help the model predict correctly 
            and perhaps reduce bias and overfitting. Fig.1 shows the feature importance of the predictor variables of the lending club dataset.
            """
        ),

         html.Img(src='assets/fi.png', className='img-fluid'),

        dcc.Markdown(
            """
        
            ##### Machine Learning Explainability
            When using black box machine learning algorithms like boosting, it may be hard to understand the association between predictors and model outcome. For instance, I already 
            have the feature importance. Although one may know which feature is significantly influencing the outcome based on the importance calculation,  but it may be difficult to detect 
            the direction of its influence towards the prediction. This is where the Partial Dependence plot and SHAP values plays important role in the prediction process. 

            Partial dependence plots show the relationship between 1-2 individual features and the target variable — by showing how predictions partially depend on the isolated features. 
            This is useful for ensuring the impact of each variable on another variable. Fig. 2 shows the impact of credit score, and loan amount for predicting interest rate. 
            """
        ),
        html.Img(src='assets/pdp1.png', className='img-fluid'),

        dcc.Markdown(
            """
            In conclusion, I have discovered that credit score plays important role while estimating the interest rate. Infact the higher the credit score, the lower the loan interest rate, which would 
            help an intending individual to make a better informed decision. This is a decision based system that helps individuals to answer critical analytic questions like ‘what..if...else’ analysis when 
            planning to visit the lending club for a loan.

            Thank you for using the app, if you have found this app useful, kindly share to increase visibility. 
            """
        ),

    ],
)

layout = dbc.Row([column1])