import pytest
import datetime
from src.contrato import Trakme

def test_validacao_de_dados():

    dados_validos = {
            "Nome da Campanha": "Campanha de Conversão",
            "Nome do conjunto de anúncios": "Público de Seguidores",
            "Nome do anúncio": "Black Friday",
            "Dia": datetime.now(),
            "Valor usado (BRL)": 100.00,
            "Impressões": 1000000,
            "Alcance": 500000,
            "Cliques no link": 10000,
            "Visualizações da página de destino": 8000,
            "Conversas por mensagem iniciadas": 1000,
            "Visitas ao perfil do Instagram": 5000,
            "Leads": 500,
            "Adições ao carrinho": 100,
            "Finalizações de compra iniciadas": 80,
            "Compras": 30,
            "Valor de conversão da compra": 15000.00,
            "Reações à publicação": 2500,
            "Comentários na publicação": 500,
            "Compartilhamentos da publicação": 250,
            "Salvamentos da publicação": 100,
            "Status de veiculação": "active",
            "Nível de veiculação": "ad",
            "Início dos relatórios": datetime.now(),
            "Término dos relatórios": datetime.now()
        }

    dados_cliente = Trakme(**dados_validos)
    
    assert dados_cliente.campanha == dados_validos["Nome da Campanha"]
    assert dados_cliente.conjunto_anuncios == dados_validos["Nome do conjunto de anúncios"]
    assert dados_cliente.anuncio == dados_validos["Nome do anúncio"]
    assert dados_cliente.data == dados_validos["Dia"]
    assert dados_cliente.valor_usado == dados_validos["Valor usado (BRL)"]
    assert dados_cliente.impressoes == dados_validos["Impressões"]
    assert dados_cliente.alcance == dados_validos["Alcance"]
    assert dados_cliente.cliques_link == dados_validos["Cliques no link"]
    assert dados_cliente.page_view == dados_validos["Visualizações da página de destino"]
    assert dados_cliente.conversas_iniciadas == dados_validos["Conversas por mensagem iniciadas"]
    assert dados_cliente.visitas_instagram == dados_validos["Visitas ao perfil do Instagram"]
    assert dados_cliente.leads == dados_validos["Leads"]
    assert dados_cliente.add_carrinho == dados_validos["Adições ao carrinho"]
    assert dados_cliente.checkout == dados_validos["Finalizações de compra iniciadas"]
    assert dados_cliente.compras == dados_validos["Compras"]
    assert dados_cliente.valor_compra == dados_validos["Valor de conversão da compra"]
    assert dados_cliente.reacoes == dados_validos["Reações à publicação"]
    assert dados_cliente.comentarios == dados_validos["Comentários na publicação"]
    assert dados_cliente.compartilhamentos == dados_validos["Compartilhamentos da publicação"]
    assert dados_cliente.salvamentos == dados_validos["Salvamentos da publicação"]
    assert dados_cliente.veiculacao == dados_validos["Status de veiculação"]
    assert dados_cliente.nivel_veiculacao == dados_validos["Nível de veiculação"]
    assert dados_cliente.inicio_relatorio == dados_validos["Início dos relatórios"]
    assert dados_cliente.termino_relatorio == dados_validos["Término dos relatórios"]