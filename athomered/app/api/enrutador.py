
from fastapi import APIRouter
from . import acceso, profesional_panel, familiar_panel, preferencias, admin

api = APIRouter(prefix="/api/v1")
api.include_router(acceso.router, prefix="/acceso", tags=["acceso"])
api.include_router(profesional_panel.router, prefix="/profesional", tags=["panel profesional"])
api.include_router(familiar_panel.router, prefix="/familiar", tags=["panel familiar"])
api.include_router(preferencias.router, prefix="/preferencias", tags=["preferencias"])
api.include_router(admin.router, prefix="/admin", tags=["admin"])
