# dio-ai-documents

# Projeto de Upload e Análise de Cartões de Crédito

Este projeto é uma aplicação Streamlit para upload de arquivos e análise de cartões de crédito utilizando serviços da Azure.

## Estrutura do Projeto

### Arquivo `app2.txt`

Este arquivo contém o código principal da aplicação Streamlit. Ele permite o upload de arquivos de imagem e utiliza serviços para enviar o arquivo para o Azure Blob Storage e analisar informações de cartões de crédito.

```python
import streamlit as st
from services.blob_service import uploado_blob
from services.credit_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    if upload_file is not None:
        fileName = upload_file.name
        blob_url = uploado_blob(upload_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para azure blob")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para storage")

def show_image_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="imagem enviada")
    st.write("Resultado")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão válido</h1>")
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão inválido</h1>")
        st.write("Este cartão não é válido")

if __name__ == "__main__":
    configure_interface()
```

### Arquivo blob_service2.txt
Este arquivo contém a implementação do serviço de upload para o Azure Blob Storage.
```
import os
import streamlit as st
from utils.Config import Config
from azure.storage.blob import BlobServiceClient

def uploado_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar arquivo: {ex}")
        return None
```
### Arquivo credit_service2.txt
Este arquivo contém a implementação do serviço de análise de cartões de crédito utilizando o Azure Document Intelligence.
```
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(card_url):
    credential = AzureKeyCredential(Config.KEY)
    document_intelligence_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
    card_info = document_intelligence_client.begin_analyze_document(
        "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
    )
    result = card_info.result()
```
### Arquivo requirements.txt
Este arquivo lista as dependências necessárias para executar a aplicação.
```
azure.core
azure-ai-documentintelligence
streamlit
azure-storage-blob
python-dotenv
```

### Como Executar
Clone o repositório.
Instale as dependências listadas em requirements.txt.
Execute o arquivo app2.txt para iniciar a aplicação Streamlit

### Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

### Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
