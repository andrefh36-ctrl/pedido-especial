import streamlit as st
import time

# Configurações da página
st.set_page_config(page_title="Tenho uma pergunta...", page_icon="❤️")

# Título principal
st.title("Oi, [Nome dela]! 👋")

# Espaço para uma mensagem fofa
st.write("""
Desde que a gente começou a conversar, minha vida ficou muito mais colorida. 
Passamos por momentos incríveis e eu não consigo parar de pensar no quanto 
você me faz bem. 
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
        st.success("A melhor decisão da minha vida! Prometo te fazer a pessoa mais feliz do mundo. 😍")
        st.snow() # Um efeito extra de charme

with col2:
    # Um pequeno truque: se ela tentar clicar no Não, a gente brinca um pouco
    if st.button("Não... 😢"):
        st.warning("Ops! Acho que o botão quebrou... tente o outro ali do lado! 😉")