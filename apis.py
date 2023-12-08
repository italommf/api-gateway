import streamlit as st
import requests

class kanye_rest():

    def conselho():
        url = 'https://api.kanye.rest/' 
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote = data.get('quote') 
            return quote
        else:
            return None
        
class cat_images():

    def gatinho():
        url = 'https://api.thecatapi.com/v1/images/search' 
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                return data[0]['url']
            except Exception as e:
                st.error(f"Erro ao obter a URL da imagem: {e}")
                return None
        else:
            st.error(f"Erro ao obter a resposta da API: {response.status_code}")
            return None
        
class tradução_minion():

    def ingles_minion(data):            
        endpoint = 'https://api.funtranslations.com/translate/navi.json'
        payload = {'text': data}

        response = requests.post(endpoint, data = payload)

        if response.status_code == 200:
            translated_text = response.json().get('contents').get('translated')
            return translated_text
        else:
            st.error("Falha ao traduzir o texto.")
            return None