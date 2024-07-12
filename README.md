# Image Chat Bot 🖼️🤖

## Overview
This project demonstrates a simple application using Gemini Vision Pro API to extract invoice information based on user input questions. It utilizes Streamlit for the user interface and Google Generative AI for processing and generating responses.

## Installation

### Prerequisites
- Python 3.10 or higher installed
- Access to Gemini Vision Pro API key
- Google Generative AI API key (stored in a .env file)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   cd Image-Chat-Bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Usage
   Running the Application Locally
   1. Set up your environment variables:
      - Create a .env file in the project root directory.
      - Add your Google Generative AI API key:
        ```makefile
        GOOGLE_API_KEY=<your_api_key>
        ```
  2. Start the Streamlit application:
     ```bash
     streamlit run app.py
     ```
  3. Access the application in your web browser at http://localhost:8501.
### Using the Application
- Input your prompt text in the provided text box.
- Upload an invoice image (JPEG, JPG, or PNG).
- Click the "Tell me about the invoice" button to generate responses based on the input prompt and uploaded image.


## Project Structure
The project structure is as follows:
```bash
Image-Chat-Bot/
│
├── app.py                    # Streamlit application script
├── setup.py                  # Setup script for dependencies
├── requirements.txt          # List of dependencies
└── .env                      # Environment variables file (not included in repository)
```
## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or a pull request.

## License
This project is licensed under the MIT License.

#Happy Coding! 
