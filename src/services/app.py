import streamlit as st
from services.blob_service import uploado_blob
from services.credit_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png","jpg","jpeg"])

    if upload_file is not None:
        fileName = upload_file.name

    blob_url = uploado_blob(upload_file, fileName)

    if blob_url:
        st.write(f"Arquivo{fileName} enviado com sucesso para azure blob")
        credit_card_info = analyze_credit_card(blob_url)
        show_image_validation(blob_url,credit_card_info)
    else:
        st.write(f"Erro ao enviar o arquivo {fileName} para storage")

def show_image_validation(blob_url,credit_card_info):
    st.image(blob_url, caption="imagem enviada")
    st.write("REsultado")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartao valido</h1>")
        st.write(f"Nome do titula: {credit_card_info['card_name']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartao invalido</h1>")
        st.write("este cartao nao e valido")

    if __name__ == "__main__":
        configure_interface()