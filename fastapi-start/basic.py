from enum import Enum
from typing import Union, List, Set, Dict

from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Required, Field, HttpUrl, EmailStr


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "alexnet on the move"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# @app.get("/items/")
# async def read_item(skip: int=0, limit: int=10):
#     return fake_items_db[skip : skip+limit]


# # 선택적 파라미터
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# 쿼리 파라미터 형변환
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "this is an item that has a lot of description"}
#         )
#     return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "this is an item that has a lot of description"}
        )
    return item


# request body
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# # request body + path parameter
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# # request body + path parameter + query parameter
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# # query parameter validation
# @app.get("/items/")
# async def read_items(q: str = Query(default=Required, min_length=3, max_length=50)):
#     results = {"items" : [{"item_name": "Foo"}, {"item_name": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# # query parameter list
# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default=None)):
#     query_items = {"q": q}
#     return query_items


# # query parameter list with default
# @app.get("/items/")
# async def read_items(q: List[str] = Query(default=["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items


# # query parameter : add a title , description, alias (docs)
# @app.get("/items/")
# async def read_items(
#         q: Union[str, None] = Query(
#             default=None,
#             title="Query222",
#             description="Query string for the items to search in the database that have a good match",
#             alias="item-query",
#             min_length=3,
#             deprecated=False, )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Exclude query parameter from OpenAPI
# @app.get("/items/")
# async def read_items(
#         hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     else:
#         return {"hidden_query": "Not found"}


# # path parameter & validation (gt, ge, lt, le)
# @app.get("/items/{item_id}")
# async def read_items(
#         item_id: int = Path(title="The ID of the item to get", gt=5, le=1000),
#         q: Union[str, None] = Query(default=None, alias="item_query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# mix path, query, body parameters
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# multiple body parameter
class User(BaseModel):
    user_name: str
    full_name: Union[str, None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item:Item, user:User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results


# # singular values in body
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item:Item, user:User, importance: int = Body()):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results


# # multiple body params & query
# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int,
#         item: Item,
#         user: User,
#         importance: int = Body(gt=0),
#         q: Union[str, None] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


# Embed a single body parameter
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item:Item = Body(embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results


# # Body - Field
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = Field(
#         default=None, title="the description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="the price must be greater than zero")
#     tax: Union[float, None] = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(embed=True)):
#     results = {"item_id": item_id, "item":item}
#     return results


# Body - Nested Model
class Image(BaseModel):
    url: HttpUrl
    name: str


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     images: Union[List[Image], None] = None

#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# # deep nested
# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     items: List[Item]
#
#
# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer
#
#
# @app.post("/images/multiple/")
# async def create_multiple_images(images: List[Image]):
#     return images
#
#
# @app.post("/index-weights/")
# async def create_index_weights(weights: Dict[int, float]):
#     return weights


## Declare Request Example Data

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }

# class Item(BaseModel):
#     name: str = Field(example="Foo")
#     description: Union[str, None] = Field(default=None, example="A very nice Item")
#     price: float = Field(example=354.2)
#     tax: Union[float, None] = Field(default=None, example=3.2)

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# # Extra Data Type
#
# from datetime import datetime, time, timedelta
# from uuid import UUID
#
# @app.put("/items/{item_id}")
# async def read_items(
#         item_id: UUID,
#         start_datetime: Union[datetime, None] = Body(default=None),
#         end_datetime: Union[datetime, None] = Body(default=None),
#         repeat_at: Union[time, None] = Body(default=None),
#         process_after: Union[timedelta, None] = Body(default=None),
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }
#
# @app.get("/items/")
# async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
#     return {"ads_id": ads_id}


# header parameter

@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent" : user_agent}


# # Response Model
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []
#
#
# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# Response Model : Return the same input data
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# Response Model encoding parameters
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"},)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


# Multiple Model
class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None


def fake_password_hasher(raw_passowrd:str):
    return "supersecret" + raw_passowrd


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved