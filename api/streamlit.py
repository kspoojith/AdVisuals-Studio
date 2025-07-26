import streamlit.web.bootstrap as bootstrap
import streamlit as st
import os
import sys
from pathlib import Path

def handler(request, context):
    # Set up environment
    os.environ['STREAMLIT_SERVER_PORT'] = '8080'
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false'
    
    # Get the path to app.py
    app_path = Path(__file__).parent.parent / "app.py"
    
    # Run Streamlit
    bootstrap.run(str(app_path), '', [], [])
    
    return {
        'statusCode': 200,
        'body': 'Streamlit app running'
    } 