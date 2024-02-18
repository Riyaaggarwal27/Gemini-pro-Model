from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-pro')
def get_gemini_response(question,prompt):
    response = model.start_chat(history=[])  # Start a new chat session
    response=model.generate_content([prompt[0],question])
    return response.text
## func to retrieve query from databse
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    # for row in rows:
    #     print(row)
    return rows

prompt=[
    """
You are an expert in converting english questions to sql query!
the sql databse has the name user_details ,products and orders  and has following columns-user_name,first_name,
last_name\n\nFor example,\n-how many males are present?,
the sql command will be something like Count(*)from user_details;
also sql code should not have ``` in beginning or end and sql word in output
"""
]
if 'chat_history'not in st.session_state:
    st.session_state['chat_history']=[]

#streamlit app
st.set_page_config(page_title="SQL retriever",layout="wide")

st.header("Gemini Pro LLM Chatbot")
st.subheader("--Responding to SQL queries")

question=st.text_input("You: ",key="input")
submit=st.button("Respond to the query")


# chat_history=[]
if submit:
   
    output=get_gemini_response(question,prompt)
    # print(output)
    st.session_state['chat_history'].append(("You",question))

    response=read_sql_query(output,"users.db")
    st.session_state['chat_history'].append(("Bot",response))
   
    st.subheader("Response")
    for row in response:
        # print(row)
        st.write(row)
   

    # chat_history.append(("Bot",response))

st.subheader("Chat history:")
for role, text in st.session_state['chat_history']:
    st.write(f"<b>{role}:</b> {text}", unsafe_allow_html=True)