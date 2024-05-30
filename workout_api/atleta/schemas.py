from typing import Annotated
from pydantic import Field, PositiveFloat, PositiveInt

from contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            description="Nome do atleta",
            examples=["João da Silva"],
        ),
    ]
    cpf: Annotated[
        str,
        Field(
            max_length=11,
            description="CPF do atleta",
            examples=["12345678912"],
        ),
    ]
    idade: Annotated[
        int,
        Field(
            PositiveInt,
            ge=16,
            description="Idade do atleta",
            examples=[25, 52],
        ),
    ]
    peso: Annotated[
        float,
        Field(
            PositiveFloat,
            description="Peso do atleta",
            examples=[80.5],
        ),
    ]
    altura: Annotated[
        float,
        Field(
            PositiveFloat,
            description="Altura do atleta",
            examples=[1.80],
        ),
    ]
    sexo: Annotated[
        str,
        Field(max_length=1, examples=["M", "F"], description="Sexo do atleta"),
    ]
