from fastapi import APIRouter

#create an instance of APIRouter
router = APIRouter(
    prefix='/api', #set the prefix for all routes under this router
    tags=['HealthChecks'] #assign tags to the router for documentation purposes
)

#endpoint for health check
@router.get('/api/health', tags=['HealthChecks'])
def health():
    return {'status': 'OK'}