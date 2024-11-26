from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(card_url):
        credential = AzureKeyCredential(Config.KEY)

        document_intelligence_client = DocumentIntelligenceClient(Config.ENDPOINT,credential)

        card_info = document_intelligence_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source= card_url)
            )
        result = card_info.result()
