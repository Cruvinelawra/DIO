import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Recebendo solicitação para salvar arquivos no Storage Account.")
    try:
        connection_string = "<sua_connection_string>"
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_name = "meucontainer"
        container_client = blob_service_client.get_container_client(container_name)

        file = req.files.get('file')
        if not file:
            return func.HttpResponse("Nenhum arquivo enviado.", status_code=400)

        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file.stream, overwrite=True)

        return func.HttpResponse(f"Arquivo '{file.filename}' salvo com sucesso!", status_code=200)
    except Exception as e:
        logging.error(f"Erro ao salvar arquivo: {str(e)}")
        return func.HttpResponse("Erro interno no servidor.", status_code=500)

import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Recebendo solicitação para salvar dados no CosmosDB.")
    try:
        url = "<sua_url_cosmosdb>"
        key = "<sua_chave_cosmosdb>"
        database_name = "meubanco"
        container_name = "meucontainer"

        client = CosmosClient(url, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        data = req.get_json()
        container.create_item(data)

        return func.HttpResponse("Dados salvos com sucesso no CosmosDB!", status_code=200)
    except Exception as e:
        logging.error(f"Erro ao salvar dados: {str(e)}")
        return func.HttpResponse("Erro interno no servidor.", status_code=500)

import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Recebendo solicitação para filtrar registros no CosmosDB.")
    try:
        url = "<sua_url_cosmosdb>"
        key = "<sua_chave_cosmosdb>"
        database_name = "meubanco"
        container_name = "meucontainer"

        client = CosmosClient(url, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        query = req.params.get('query')
        if not query:
            return func.HttpResponse("Parâmetro 'query' não fornecido.", status_code=400)

        items = container.query_items(
            query=f"SELECT * FROM c WHERE {query}",
            enable_cross_partition_query=True
        )

        return func.HttpResponse(json.dumps(list(items)), status_code=200)
    except Exception as e:
        logging.error(f"Erro ao filtrar registros: {str(e)}")
        return func.HttpResponse("Erro interno no servidor.", status_code=500)

import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Recebendo solicitação para listar registros no CosmosDB.")
    try:
        url = "<sua_url_cosmosdb>"
        key = "<sua_chave_cosmosdb>"
        database_name = "meubanco"
        container_name = "meucontainer"

        client = CosmosClient(url, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        items = container.query_items(
            query="SELECT * FROM c",
            enable_cross_partition_query=True
        )

        return func.HttpResponse(json.dumps(list(items)), status_code=200)
    except Exception as e:
        logging.error(f"Erro ao listar registros: {str(e)}")
        return func.HttpResponse("Erro interno no servidor.", status_code=500)
