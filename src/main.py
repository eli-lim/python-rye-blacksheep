from dataclasses import dataclass
from typing import List

from blacksheep import Application, get
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info


app = Application()

docs = OpenAPIHandler(info=Info(title="Example API", version="0.0.1"))
docs.bind_app(app)


@dataclass
class User:
    user_id: int
    name: str


@get("/users")
async def users() -> List[User]:
    """
    List all users!
    """
    return [
        User(1, "Alice"),
        User(2, "Bob"),
        User(3, "Charlie"),
    ]
