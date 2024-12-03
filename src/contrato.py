from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime

class BaseCliente(BaseModel):
    campanha: str
    conjunto_anuncios: str
    anuncios: str
    data: datetime
    valor_usado: PositiveFloat
    impressoes: PositiveInt
    alcance: PositiveInt
    cliques_link: PositiveInt
    page_view: PositiveInt
    conversas_iniciadas: PositiveInt
    visitas_instagram: PositiveInt
    leads: PositiveInt
    add_carrinho: PositiveInt
    checkout: PositiveInt
    compras: PositiveInt
    valor_compra: PositiveFloat
    reacoes: PositiveInt
    comentarios: PositiveInt
    compartilhamentos: PositiveInt
    salvamentos: PositiveInt
    veiculacao: str
    nivel_veiculacao: str
    inicio_relatorios: datetime
    termino_relatorios: datetime
        