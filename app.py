import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load external CSS
with open('C:/Users/tripa/PycharmProjects/Medicine Recommendation System/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load medicine-dataframe from pickle in the form of dictionary
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)

# Load similarity-vector-data from pickle in the form of dictionary
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_medicines = [medicines.iloc[i[0]].Drug_Name for i in medicines_list]
    return recommended_medicines

# Streamlit app frontend
st.title('Medicine Recommender System')

# Sidebar for user input
st.sidebar.title('Select Medicine')
selected_medicine_name = st.sidebar.selectbox(
    'Choose a medicine for recommendations here ',
    medicines['Drug_Name'].values
)

# Display recommendations
if st.sidebar.button('Recommend Medicine'):
    recommendations = recommend(selected_medicine_name)
    st.sidebar.title('Recommended Medicines')
    for idx, recommended_med in enumerate(recommendations, start=1):
        st.sidebar.write(f"{idx}. {recommended_med}")
        st.sidebar.markdown(f"[Purchase on PharmEasy](https://pharmeasy.in/search/all?name={recommended_med})")

# Main content
st.subheader('About Medicine Recommender System')
st.write('Welcome to the Medicine Recommender System! Use the sidebar to select a medicine and receive recommendations.')
st.write('Your Health, Our Recommendation: Discover the Right Medicines.')
# Image
image = Image.open('images/best-health-insurance-plans-sixteen_nine-sixteen_nine.jpg')
st.image(image, caption='Recommended Medicines', use_column_width=True)

st.write('Made by:\n'
         '1) Megha Soni\n'
         '2) Himali Suroshi\n'
         '3) Pragya Tripathi')