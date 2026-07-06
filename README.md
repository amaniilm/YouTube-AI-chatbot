# YouTube-AI-chatbot
# YouTube AI Chatbot

## Introduction

This project is a simple AI chatbot that answers questions from a YouTube video. It uses the video's transcript to generate answers. If the answer is not available in the transcript, the chatbot tells the user that it could not find the information.

## Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini API
* YouTube Transcript API
* python-dotenv

## How It Works

1. Enter the YouTube video URL.
2. Enter your question related to the video.
3. The application loads the video transcript.
4. Gemini reads the transcript and generates an answer.
5. The answer is displayed on the screen.

## Project Structure

```text
youtube-ai-chatbot/
│── app.py
│── .env
│── requirements.txt
│── README.md
```

## Installation

Install all the required libraries using:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the Streamlit application:

```bash
streamlit run app.py
```

## What I Learned

* How to use LangChain with Google Gemini.
* How to load YouTube transcripts.
* How to create a Streamlit web application.
* How to use PromptTemplate and OutputParser in LangChain.

## Future Scope

* Add chat history.
* Improve the UI.
* Support more languages.
* Add video summarization.
* Allow users to upload videos.

## Author

**Anshul Yadav**

B.Tech (2nd Year)
