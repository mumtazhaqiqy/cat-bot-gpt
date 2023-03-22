import streamlit as st
import gpt

st.title('😺🤖 on txt file')

def read_file(file):
    file_content = file.read()
    return file_content


instruction = st.session_state.get('instruction', [])
user_instruction = st.text_area('😺🤖: give me your instruction', key='input')
if user_instruction:
    prompt = user_instruction
    # st.code(prompt)

uploaded_file = st.file_uploader("Choose a file", type="txt")
file_from_text = ''
if uploaded_file is not None:
    file_from_text = read_file(uploaded_file)
    # st.code(file_from_text)

output_file = st.text_input('output filename', key='output_file_name')
    
result = st.session_state.get('result', '')

if st.button('Send Request', key='send_request'):
    prompt = user_instruction + '\n' + file_from_text.decode('utf-8')
    result = gpt.sendPrompt(prompt, instruction)
    st.code(result)

if result is not '':
    st.download_button(
        label='Download',
        data=result,
        file_name=output_file,
        mime='text/plain'
    )
