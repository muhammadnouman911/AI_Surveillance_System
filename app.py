import streamlit as st
from realtime_detection import generate_webcam_feed
from upload_media_analysis import analyze_uploaded_media
import tempfile

st.set_page_config(page_title="Face Analysis", layout="wide")

# Sidebar for navigation
option = st.sidebar.radio("Navigation", ["Real-Time Detection", "Upload Media"])

if option == "Real-Time Detection":
    st.title("Real-Time Face Analysis")
    st.write("Click the button below to start webcam detection.")

    if st.button("Start Webcam Detection"):
        st.write("Streaming live from your webcam...")
        
        # A placeholder in Streamlit to display frames
        frame_placeholder = st.empty()

        # Pull frames from generator and display
        for frame_data in generate_webcam_feed():
            # 'channels="BGR"' ensures the correct color interpretation
            frame_placeholder.image(frame_data, channels="BGR", use_column_width=False)

elif option == "Upload Media":
    st.title("Upload Image or Video for Analysis")
    
    # Supported file types
    uploaded_file = st.file_uploader(
        "Upload an image or video", 
        type=["jpg", "jpeg", "png", "mp4", "avi", "mov", "mkv"]
    )

    if uploaded_file is not None:
        # Use tempfile to write uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_file_path = temp_file.name

        st.write("Analyzing your media...")
        
        # Pass the temporary file path to the analysis function
        results = analyze_uploaded_media(temp_file_path)

        st.write("Analysis Results:")
        st.json(results)
