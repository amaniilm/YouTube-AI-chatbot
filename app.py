from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import  streamlit as st
import os
st.set_page_config(
    page_title="YouTube AI Chatbot",
    page_icon="🎥"
)
st .title("🎥 YouTube video AI Chatbot")
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"]=st.secrets['GOOGLE_API_KEY']
else:
    load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()
url=st.text_input('enter your url')
question=st.text_input("ask your question")
if st.button("get result"):
    loader=YoutubeLoader.from_youtube_url(url,language=['en','hi'],add_video_info=False)
    docs=loader.load()
    prompt=PromptTemplate(
    template="""you are the AI assistant 
        use only the transcript to answer the following {question},from{topic}
        If the transcript does not contain the answer, say:
        "I couldn't find that information in the video."  """,
        input_variables=['question','topic']
    )
    chain=prompt|model|parser
    result=chain.invoke({'question':question,'topic':docs[0].page_content})
    st.success(result)
