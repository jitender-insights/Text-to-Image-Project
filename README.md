# AI Image Generator

This project is a Streamlit-based web application with a FastAPI backend for generating images using various AI models from Stability AI, RunwayML, and other providers available on Hugging Face.

## Features

- Select from multiple AI models for image generation
- Enter custom text prompts to generate images
- View model information and descriptions
- Attractive and responsive user interface
- FastAPI backend for scalability

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jitender-insights/Text-to-Image-Project.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Kindly run the backend code in Google Collab by changing run time to T4 GPU(Mandatory)

## Usage

Run the application:

```
streamlit run app.py
```

Open your web browser and go to `http://localhost:8501` to use the app.
