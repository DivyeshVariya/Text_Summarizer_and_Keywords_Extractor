import streamlit as st
import subprocess
import time
from streamlit_option_menu import option_menu
from PIL import Image
from transformers import pipeline
from keybert import KeyBERT

st.set_page_config(
     page_title ="Text Summerizer",
     page_icon ="icon.png",
layout="centered")

with st.sidebar:
 selected = option_menu(
	menu_title="Main Menu",
	options = [ "Home","Text Summerizer","Keyword Extractor","Login","Register"],
	icons = ["house","book","envelope","box-arrow-in-right","journal-text"],
	menu_icon = "cast",
	default_index = 0,
	# orientation = "horizontal", 
	styles={}
 )

 # placeholder = st.empty()
 # isclick = placeholder.button('delete this button')
 # if isclick:
 #     placeholder.empty()
 # if st.sidebar.button("new button"):
 #     st.title('Text Summerizer')
 #     text_input = st.text_area("Enter some text 👇", placeholder="Type something.....", height=300)
 #     if st.button('Submit'):
 #         summarizer = pipeline("summarization")
 #         summary_text = summarizer(text_input)[0]['summary_text']
 #         st.subheader("Summary :")
 #         st.write(summary_text)
st.title("Welcome to Easy, Efficient and Time saver tool world.....")
st.write("----------")
st.title('Text Summerizer')
st.write("A text summarizer is an online tool that wraps up a text to a specified short length. It condenses a long article to main points. The need for text summarizers is increasing day by day, because of time constraints. People are looking for shortcut methods to learn ideas in lesser time.")
st.write("It reduce the time for reading big articles and convert text into some meaningful summary text. So it is time saving application.")
image = Image.open("example_textSummizer.png")
st.image(image, caption='Text Summerizer Demo')

st.write("----------")
st.title('Keyword Extractor')
st.write("Keyword extraction is the automated process of extracting the most relevant words and expressions from text.")
st.write("Keyword extraction (also known as keyword detection or keyword analysis) is a text analysis technique that automatically extracts the most used and most important words and expressions from a text. It helps summarize the content of texts and recognize the main topics discussed.")
st.write("It uses machine learning artificial intelligence (AI) with natural language processing (NLP) to break down human language so that it can be understood and analyzed by machines. It’s used to find keywords from all manner of text: regular documents and business reports, social media comments, online forums and reviews, news reports, and more.")
image = Image.open("example_keywordExtract.png")
st.image(image, caption='Keyword Extraction Demo')

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if selected == "Text Summerizer":
        # st.title(f"You have selected {selected}")
        st.write("----------")
        st.title('Working Demo of Text Summerizer')
        text_input = st.text_area("Enter some text 👇",placeholder="Type something.....",height=300)
        if st.button('Submit'):
            if text_input!="":
                summarizer = pipeline("summarization")
                summary_text = summarizer(text_input)[0]['summary_text']
                st.subheader("Summary :")
                st.write(summary_text)
            else:
                st.write("Please Enter some text...")


elif selected == "Keyword Extractor":
        # st.title(f"You have selected {selected}")
        st.write("----------")
        st.title('Working Demo of Keyword Extractor')
        text_input = st.text_area("Enter some text 👇", placeholder="Type something.....",height=300)
        if st.button('Submit'):
            if text_input!="":
                kw_model = KeyBERT()
                keywords = kw_model.extract_keywords(text_input, keyphrase_ngram_range=(1, 1), stop_words='english',use_mmr=True, diversity=0.7)
                st.subheader("Extracted keywords :")
                for i in keywords:
                        st.write(i[0])
            else:
                st.write("Please Enter some text...")

elif selected == "Login":
        st.title("Login")
        user_name=st.sidebar.text_input("User Name : ",placeholder="divyesh")
        password=st.sidebar.text_input("Password :",placeholder="********")
        login=st.sidebar.button("Login")

        f=open("user_name.txt","r",encoding="utf-8")
        if f.mode=="r":
             register_user=f.read();
             f.close()
        f=open("password.txt","r",encoding="utf-8")
        if f.mode=="r":
             register_pass=f.read();
             f.close()
        if login:
            if user_name == register_user and password == register_pass:
                st.sidebar.write("Login successful....")
            elif user_name=="" and password=="":
                st.sidebar.write("Please ! Enter vaild input.....")
            else:
                st.sidebar.write("Oops ! In-vaild input. Login not successful.....")

elif selected == "Register":
        st.title("Register")
        user_name=st.sidebar.text_input("User Name : ",placeholder="divyesh")
        password=st.sidebar.text_input("Password :",placeholder="********")
        re_password=st.sidebar.text_input("Re-Password :",placeholder="********")
        register=st.sidebar.button("Register")

        if register:
            if user_name!="" and password==re_password:
                f=open("user_name.txt","w",encoding="utf-8")
                if f.mode=="w":
                        f.write(user_name);
                        f.close()
                f=open("password.txt","w",encoding="utf-8")
                if f.mode=="w":
                        f.write(password);
                        f.close()
                st.sidebar.write("Register successful.....")
            elif user_name=="" and password=="" and re_password=="":
                st.sidebar.write("Please ! Enter vaild input.....")
            else:
                st.sidebar.write("Oops ! In-vaild input. Register not successful.....")

else :
    st.title(f"Try out the demo Now....")

