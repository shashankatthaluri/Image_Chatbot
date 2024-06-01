from setuptools import find_packages, setup

setup(
    name="End-to-end-project-using-gemini",
    version="0.0.1",
    author="Shashank atthaluri",
    author_email="shashankatthaluri@gmail.com",
    install_requires=["google-generativeai",
                      "", 
                      "pinecone-client", "langchain", 
                      "flask", 
                      "python-dotenv", 
                      "langchain-community", 
                      "pypdf"
                      ],
    packages=find_packages()         
)