import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Método e parâmetros
        method = req.method
        if method == "GET":
            return func.HttpResponse(json.dumps({"message": "Bem-vindo à API!"}), status_code=200)

        elif method == "POST":
            data = req.get_json()
            name = data.get("name")
            if not name:
                return func.HttpResponse("Campo 'name' não fornecido", status_code=400)

            return func.HttpResponse(json.dumps({"message": f"Olá, {name}!"}), status_code=200)

        else:
            return func.HttpResponse("Método não suportado", status_code=405)

    except Exception as e:
        return func.HttpResponse(f"Erro no servidor: {str(e)}", status_code=500)
