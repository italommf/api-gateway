from apis import ApiGateway
import streamlit as st

data = ApiGateway.conselho()

if data:

    st.markdown("**Texto Original:**")
    st.info(f"_**{data}**_") 

    traducao = ApiGateway.ingles_minion(data)

    if traducao:
        st.markdown("**Texto Traduzido para Navi:**")
        st.info(traducao)
else:
    st.write("Não foi possível obter os dados da API.")


