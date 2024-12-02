import pytest
from src.contrato import db_trakme

def test_db_validate_data():

    dados_validos = {
            "dia": "",
            "veiculacao": "",
            "Nome da Campanha": ""
        }
    
