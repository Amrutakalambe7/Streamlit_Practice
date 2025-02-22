# Add widget to the app

import streamlit as st

#x= st.slider('x')

#st.write(x, 'squared is', x * x)

#st.text_input('Enter Your Name', key='name')

#st.session_state.name #access the value at any point with: st.session_state.amruta

#Use checkboxes to show/hide data
import streamlit as st
import pandas as pd
import numpy as np


#if st.checkbox('Show dataframe'):
    #chart_data = pd.DataFrame(
        #np.random.randn(20, 3),
        #columns=['a', 'b', 'c'])

    #chart_data


#Use a selectbox for options

#df = pd.DataFrame({
            #'first column': [1, 2, 3, 4],
            #'second column': [10, 20, 30, 40]})
    
#option = st.selectbox(
        #'Which number do you like best?',
        # df['first column'])
    
#'You selected: ', option

# Layout

# Add a selectbox to the sidebar:
#add_selectbox = st.sidebar.selectbox(
    #'How would you like to be contacted?',
    #('Email', 'Home phone', 'Mobile phone'))

# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
    #'Select a range of values',
    #0.0, 100.0, (25.0, 75.0))

import streamlit as st

#eft_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
#left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
#with right_column:
    #chosen = st.radio(
        #'Sorting hat',
        #("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    #st.write(f"You are in {chosen} house!")

#Show progress
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'