import gpt
import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="CatBot GPT",
    page_icon="🐱",
)

def clear():
    st.session_state.clear()

def clear_text():
    st.session_state["temp"] = st.session_state["input"]
    
    if st.session_state["input"]:
        if(st.session_state["input"] != 'clear'):
            output=gpt.sendPrompt(st.session_state["input"], st.session_state['messages'])
            if(len(st.session_state['messages'])>=6):
                st.session_state['messages'] = st.session_state['messages'][-5:]
            #store the output
            st.session_state['past'].append(st.session_state["input"])
            st.session_state['generated'].append(output)
            # st.session_state['messages'].append({"role": "assistant", "content":output})
        else:
            clear()
    st.session_state["input"] = ""

st.title('😺🤖CatBot GPT')
st.write('Supported by BythjulSkruvat⭐⭐⭐⭐⭐')

st.sidebar.success('select a page above.')
st.sidebar.write("""
    ###### 21-03-2023
    ##### Yes it is now have a session history, so the bot is able to recall previous chat. and some improvement 👍 
    ###### 20-03-2023 
    ##### This CatBot (read: Chat Bot) utilizes the advanced GPT 3-5 Turbo model. At present, chat history is not saved, meaning the bot will not be able to recall previous conversations. Therefore, each time you initiate a chat, the bot will not remember what you have previously written.  
    ##### Anyway, feel free to use it when ChatGPT is unavailable, it's pretty often now 😜 
    ##### Todo: Add ability to upload file or document for ex: csv file
""")

if 'temp' not in st.session_state:
    st.session_state['temp'] = ""

user_input=st.text_area("😺🤖: Hey hooman, write your command here:", key='input', on_change=clear_text)
st.button('🗑️ clear history', key='clear', on_click=clear)
        
#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

st.sidebar.write(st.session_state['messages'])

# save this for later
# Imagine you are a professional translator, I want you to translate these strings to Finish, keep the original string as a reference in comma separated value.
