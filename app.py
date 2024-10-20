import streamlit as st 
import requests
import base64
from PIL import Image
import io

st.title("Text to Image Generator")
st.write("Enter a text description to generate an Image")


# Add sidebar for configuration
st.sidebar.header("Configuration")
api_url = st.sidebar.text_input(
    "Backend API URL",
    "https://a620-35-227-171-239.ngrok-free.app"  # You'll replace this with the ngrok URL from Colab
)

 # Main interface
text_prompt = st.text_input("Enter your prompt:", "A beautiful sunset over mountains")

if st.button("Generate Image"):
    if not api_url:
        st.error("Please enter the backend API URL in the sidebar")
        
    with st.spinner("Generating image..."):
        try:
            # Send request to Colab backend
            response = requests.post(
                f"{api_url}/generate",
                json = {"text":text_prompt}
            )
            
            if response.status_code == 200:
                    # Decode and display the image
                    image_data = base64.b64decode(response.json()["image"])
                    image = Image.open(io.BytesIO(image_data))
                    st.image(image, caption="Generated Image")
            else:
                st.error(f"Failed to generate image. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            
st.markdown("""
### Tips for better prompts:
- Be specific in your descriptions
- Include details about style, lighting, and composition
- Try different variations of your prompt
""")
## Footer
st.markdown(
"""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: #FAFAFA;
    text-align: center;
    padding: 10px;
    font-size: 14px;
}
</style>
<div class="footer">
    Created with ❤️ by DataSciLearn | <a href="https://github.com/jitender-insights" target="_blank">GitHub</a>
</div>
""",
unsafe_allow_html=True
)

            
        
            
            
    
        
        
    
        
    