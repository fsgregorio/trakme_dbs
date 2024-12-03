import pytest
from datetime import datetime
from src.contrato import BaseCliente

def test_validacao_de_dados():

    dados_validos = {
            "campanha": "Campanha de Conversão",
            "conjunto_anuncios": "Público de Seguidores",
            "anuncios": "Black Friday",
            "data": datetime(2024,11,30),
            "valor_usado": 100.00,
            "impressoes": 1000000,
            "alcance": 500000,
            "cliques_link": 10000,
            "page_view": 8000,
            "conversas_iniciadas": 1000,
            "visitas_instagram": 5000,
            "leads": 500,
            "add_carrinho": 100,
            "checkout": 80,
            "compras": 30,
            "valor_compra": 15000.00,
            "reacoes": 2500,
            "comentarios": 500,
            "compartilhamentos": 250,
            "salvamentos": 100,
            "veiculacao": "active",
            "nivel_veiculacao": "ad",
            "inicio_relatorios": datetime(2024,11,1),
            "termino_relatorios": datetime(2024,11,30)
        }

    dados_cliente = BaseCliente(**dados_validos)
    
    assert dados_cliente.campanha == dados_validos["campanha"]
    assert dados_cliente.conjunto_anuncios == dados_validos["conjunto_anuncios"]
    assert dados_cliente.anuncios == dados_validos["anuncios"]
    assert dados_cliente.data == dados_validos["data"]
    assert dados_cliente.valor_usado == dados_validos["valor_usado"]
    assert dados_cliente.impressoes == dados_validos["impressoes"]
    assert dados_cliente.alcance == dados_validos["alcance"]
    assert dados_cliente.cliques_link == dados_validos["cliques_link"]
    assert dados_cliente.page_view == dados_validos["page_view"]
    assert dados_cliente.conversas_iniciadas == dados_validos["conversas_iniciadas"]
    assert dados_cliente.visitas_instagram == dados_validos["visitas_instagram"]
    assert dados_cliente.leads == dados_validos["leads"]
    assert dados_cliente.add_carrinho == dados_validos["add_carrinho"]
    assert dados_cliente.checkout == dados_validos["checkout"]
    assert dados_cliente.compras == dados_validos["compras"]
    assert dados_cliente.valor_compra == dados_validos["valor_compra"]
    assert dados_cliente.reacoes == dados_validos["reacoes"]
    assert dados_cliente.comentarios == dados_validos["comentarios"]
    assert dados_cliente.compartilhamentos == dados_validos["compartilhamentos"]
    assert dados_cliente.salvamentos == dados_validos["salvamentos"]
    assert dados_cliente.veiculacao == dados_validos["veiculacao"]
    assert dados_cliente.nivel_veiculacao == dados_validos["nivel_veiculacao"]
    assert dados_cliente.inicio_relatorios == dados_validos["inicio_relatorios"]
    assert dados_cliente.termino_relatorios == dados_validos["termino_relatorios"]