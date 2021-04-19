import uvicorn

from fastapi import FastAPI
from blog import models, database
from routers import blog, user, authentication

app = FastAPI(debug=True)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(database.engine)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
