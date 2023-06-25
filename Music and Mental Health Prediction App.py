# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle


import streamlit as st



# load saved model
loaded_model = pickle.load(open('D:/12. Hamoye/2. Week 2/2. Group Project/trained_model.sav', 'rb'))



# input_data = ( 20.,   4.,   1.,   1.,   0.,   0.,   7.,   1.,   1., 120.,   2.,
#          0.,   1.,   0.,   2.,   0.,   1.,   3.,   0.,   2.,   0.,   3.,
#          2.,   0.,   1.,   0.,   8.,   7.,   1.,   1.)


# Create a prediction Function

def Music_Mental_Health_Prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction == 0):
        print('Mental health Improved')
    elif (prediction == 1):
        print('Music had no effect')
    elif (prediction == 2):
        print('Music hhealth negatively affected')




 
def main():

    # give a title
    st.title('Music and Mental Health Prediction App')

    # getting data from user
    Age = st.text_input('Age')
    Primary_streaming_service = st.text_input('Primary_streaming_service')
    Hours_per_day= st.text_input('Hours_per_day')
    While_working = st.text_input('While_working')
    Instrumentalist = st.text_input('Instrumentalist')
    Composer = st.text_input('Yes/No')
    Fav_genre = st.text_input('Fav_genre')
    Exploratory = st.text_input('Exploratory')
    Foreign_languages = st.text_input('Foreign_languages')
    BPM = st.text_input('BPM')
    Frequency_Classical = st.text_input('Frequency_Classical')
    Frequency_Country = st.text_input('Frequency_Country')
    Frequency_EDM = st.text_input('Frequency_EDM')
    Frequency_Folk = st.text_input('Frequency_Folk')
    Frequency_Gospel = st.text_input('Frequency_Gospel')
    Frequency_Hip_hop = st.text_input('Frequency_Hip_hop')
    Frequency_Jazz= st.text_input('Frequency_Jazz')
    Frequency_K_pop = st.text_input('Frequency_K_pop')
    Frequency_Latin = st.text_input('Frequency_Latin')
    Frequency_Lofi = st.text_input('Frequency_Lofi')
    Frequency_Metal = st.text_input('Frequency_Metal')
    Frequency_Pop = st.text_input('Frequency_Pop')
    Frequency_RnB = st.text_input('Frequency_RnB')
    Frequency_Rap = st.text_input('Frequency_Rap')
    Frequency_Rock = st.text_input('Frequency_Rock')
    Frequency_Video_game_music = st.text_input('Frequency_Video_game_music')
    Anxiety = st.text_input('Anxiety')
    Depression = st.text_input('Depression')
    Insomnia = st.text_input('Insomnia')
    OCD = st.text_input('OCD')

    # code for prediction
    Music_Effect = ''
    if st.button('Music Effect'):
        Music_Effect = Music_Mental_Health_Prediction([ Age, Primary_streaming_service, Hours_per_day, While_working, Instrumentalist, Composer, Fav_genre, Exploratory, 
                                                     Foreign_languages, BPM, Frequency_Classical, Frequency_Country, Frequency_EDM, Frequency_Folk, Frequency_Gospel, 
                                                     Frequency_Hip_hop, Frequency_Jazz, Frequency_K_pop, Frequency_Latin, Frequency_Lofi, Frequency_Metal, 
                                                     Frequency_Pop, Frequency_RnB, Frequency_Rap, Frequency_Rock, Frequency_Video_game_music, Anxiety, 
                                                     Depression, Insomnia, OCD])
        
    st.success(Music_Effect)

if __name__ == '__main__':
    main()
    



    
