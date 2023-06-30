import os
import streamlit as st
from PIL import Image
import utils

# Path to store uploaded image.
image_path = 'uploaded_image.jpg'
modified_path = 'modified_image.jpg'

# Function block to handle image upload and deletion.
def show_uploaded_file(uploaded_file, image_path):

    # Save the uploaded file to the local disk.
    with open(image_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    utils.gray_it_up(image_path=image_path)

    # Display the image.
    st.image(image_path)
    st.image(modified_path)

    # After user presses the 'Back' button, delete the image file.
    if st.button('Reset'):
        try:
            os.remove(image_path)
            st.write('File deleted. You may now upload another file.')
        except Exception as e:
            st.write('Error occurred:', e)


# Main Application
def app():

    # Introduction
    st.title("Streamlit Image Upload Example")

    # Upload the image file.
    uploaded_file = st.file_uploader('Please upload a .jpg file', type=['jpg'])

    # If a file has been uploaded.
    if uploaded_file is not None:
        # View and remove the file.
        show_uploaded_file(uploaded_file, image_path)

# run the app
if __name__ == '__main__':
    app()
