from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novodev-coll-58c22e5dfa5743b6bcf2f213f07de59e',debug=False,docs_url='/laughing-elgamal-0b7b83a0ca6c11efac8a0242ac12000458/docs',openapi_url='/laughing-elgamal-0b7b83a0ca6c11efac8a0242ac12000458/openapi.json')

app.include_router(router, prefix='/laughing-elgamal-0b7b83a0ca6c11efac8a0242ac12000458/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()