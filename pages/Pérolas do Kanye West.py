from apis import kanye_rest, tradução_minion
import streamlit as st

data = kanye_rest.conselho()

if data:

    st.markdown("**Texto Original:**")
    st.info(f"_**{data}**_") 

    traducao = tradução_minion.ingles_minion(data)

    if traducao:
        st.markdown("**Texto Traduzido para Minion:**")
        st.info(traducao)
else:
    st.write("Não foi possível obter os dados da API.")


