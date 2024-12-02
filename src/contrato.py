from pydantic import BaseModel
from datetime import datetime

class BaseCliente(BaseModel):
    campanha: str
    conjunto_anuncios: str
    anuncios: str
    data: datetime
    valor_usado: float
    impressoes: int
    alcance: int
    cliques_link: int
    page_view: int
    conversas_iniciadas: int
    visitas_instagram: int
    leads: int
    add_carrinho: int
    checkout: int
    compras: int
    valor_compra: float
    reacoes: int
    comentarios: int
    compartilhamentos: int
    salvamentos: int
    veiculacao: str
    nivel_veiculacao: str
    inicio_relatorios: datetime
    termino_relatorios: datetime
        