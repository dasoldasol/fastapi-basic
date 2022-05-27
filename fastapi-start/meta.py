from fastapi import FastAPI

## Description
# description = """
# DasolSeoApp API helps you do awesome stuff :>
#
# ## Items
# You can **read items**.
#
# ## Users
#
# You will be able to:
#
# * **Create users** (_not implemented_).
# * **Read users** (_not implemented_).
# """
#
# app = FastAPI(
#     title="DasolSeoApp",
#     description=description,
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact={
#         "name": "Deadpoolio the Amazing",
#         "url": "http://x-force.example.com/contact/",
#         "email": "dp@x-force.example.com",
#     },
#     license_info={
#         "name": "Apache 2.0",
#         "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
#         },
# )
#
#
# @app.get("/items/")
# async def read_items():
#     return [{"name": "Katana"}]


## Tags
# tags_metadata = [
#     {
#         "name": "users",
#         "description": "Operations with users. The **login** logic is also here.",
#     },
#     {
#         "name": "items",
#         "description": "Manage items. So _fancy_ they have their own docs.",
#         "externalDocs": {
#             "description": "Items external docs",
#             "url": "https://fastapi.tiangolo.com/",
#         },
#     },
# ]
#
# app = FastAPI(openapi_tags=tags_metadata)
#
#
# @app.get("/users/", tags=["users"])
# async def get_users():
#     return [{"name": "Harry"}, {"name": "Ron"}]
#
#
# @app.get("/items/", tags=["items"])
# async def get_items():
#     return [{"name": "wand"}, {"name": "flying broom"}]


## OpenAPI URL
# app = FastAPI(openapi_url="/api/v1/openapi.json")

## DocsURL
app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


## Use Staticfiles : serve static files automatically from a directory
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
