from typing import List
from decouple import config
from fastapi_mail import ConnectionConfig
from fastapi import FastAPI

from carts.routers import router as carts_router

from order.models import Order, OrderItem
from order.routers import router as orders_routers

from users.models import User
from users.routers import router as users_routers

from products.models import Product, Gallery
from products.routers import router as products_routers

from manager.products.routers import router as admin_products_routers
from manager.users.routers import router as admin_users_routers
from fastapi import FastAPI, Body, Depends

from users.models import UserSchema, UserLoginSchema
from users.auth_bearer import JWTBearer
from users.auth_handler import signJWT
from database import db_state_default
import database

database.db.connect()
database.db.create_tables([User, Product, Gallery, Order, OrderItem])
database.db.close()

TAGS_META = [
    {
        "name": "Carts",
        "description": "Add to cart, Get, Clear, delete item from cart",
    },
    {
        "name": "Users",
        "description": "Register, Activate, Detail user from user db"
    },
    {
        "name": "Products",
        "description": "GET list and by id from db."
    },
    {
        "name": "Orders",
        "description": "List order and Create order."
    },
    {
        "name": "Manage Products",
        "description": "Create, Delete, Update, Get Products by admin"
    },
    {
        "name": "Manage Users",
        "description": "Get users list and Delete User by admin."
    }
]
app = FastAPI(title="Shopping Cart",
              description="A shopping cart project",
              version="0.1.0",
              openapi_tags=TAGS_META,
              docs_url="/api/v1/docs")


@app.get("/")
def main_page():
    return {'swagger': 'localhost:8000/api/v1/docs'}


conf = ConnectionConfig(
    MAIL_USERNAME=config('MAIL_USERNAME'),
    MAIL_PASSWORD=config('MAIL_PASSWORD'),
    MAIL_FROM=config('MAIL_FROM'),
    MAIL_PORT=587,
    MAIL_SERVER="ftmkhosravy@gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)

app.include_router(router=carts_router, prefix="/api/v1/carts", tags=["Carts"])
app.include_router(router=users_routers, prefix="/api/v1/users", tags=["Users"])
app.include_router(router=products_routers, prefix="/api/v1/products", tags=["Products"])
app.include_router(router=orders_routers, prefix="/api/v1/orders", tags=["Orders"])
app.include_router(router=admin_products_routers, prefix="/api/v1/admin/products", tags=["Manage Products"])
app.include_router(router=admin_users_routers, prefix="/api/v1/admin/users", tags=["Manage Users"])

users = []


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
