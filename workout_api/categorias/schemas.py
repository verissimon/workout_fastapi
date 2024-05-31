from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples=["Scale"], max_length=10)
    ]
