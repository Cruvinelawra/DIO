import json
import re
import logging

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True

def main(req):
    logging.info('validação de CPF.')
    try:
        req_body = req.get_json()
        cpf = req_body.get('cpf')
        if not cpf:
            return {
                "status_code": 400,
                "body": json.dumps({
                    "error": "CPF não fornecido."
                })
            }
        is_valid = validar_cpf(cpf)
        return {
            "status_code": 200,
            "body": json.dumps({
                "cpf": cpf,
                "valid": is_valid,
                "message": "CPF válido" if is_valid else "CPF inválido"
            })
        }
    except Exception as e:
        logging.error(f"Erro ao processar: {str(e)}")
        return {
            "status_code": 500,
            "body": json.dumps({
                "error": "Erro interno."
            })
        }
