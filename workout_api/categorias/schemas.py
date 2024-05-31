from typing import Annotated

from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples=["Scale"], max_length=21)
    ]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
