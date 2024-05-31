from fastapi import APIRouter, status
from workout_api.atleta.models import AtletaModel
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.get("/", summary="Listar atletas", status_code=status.HTTP_200_OK)
async def get_atletas():
    pass

@router.post("/", summary="Cadastrar atleta", status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency, atleta_in):
    pass