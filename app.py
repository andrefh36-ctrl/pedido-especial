import streamlit as st
import time

# Configurações da página
st.set_page_config(page_title="Tenho uma pergunta...", page_icon="❤️")

# Título principal
st.title("Oi, [Kenia mendes]! 👋")

# Espaço para uma mensagem fofa
st.write("""
Minha princesa desde que a gente começou a ficar minha vida mudou totalmente como pessoa, você me fez ter outro pensamento como pessoa, 
e depois disso voce se tornou muito importante para min, portanto eu tem algo para lhe perguntar, perché ti amo mia principessa
""")

# Exibir uma foto de vocês (substitua pelo caminho do arquivo)
# st.image("sua_foto_com_ela.jpg", caption="Nossa melhor memória", use_container_width=True)

st.divider()

st.subheader("Eu tenho algo muito importante para te perguntar...")

# Botões de decisão
col1, col2 = st.columns(2)

with col1:
    if st.button("Sim! ❤️"):
        st.balloons()
        st.success("E então agente esta oficialmente namorando, essa foi  melhor decisão da sua vida! 
        Prometo te fazer a mulher mais feliz do mundo. 😍")
        st.snow() # Um efeito extra de charme

with col2:
    # Um pequeno truque: se ela tentar clicar no Não, a gente brinca um pouco
    if st.button("Não... 😢"):

        st.warning("Ops! Acho que o botão quebrou... tente o outro ali do lado! 😉")


