from typing import Annotated, Optional
from pydantic import Field, PositiveFloat, PositiveInt

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin


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
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str],
        Field(None, description="Nome do atleta", example="Joao", max_length=50),
    ]
    idade: Annotated[
        Optional[int], Field(None, description="Idade do atleta", example=25)
    ]
