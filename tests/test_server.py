from blacksheep.testing import TestClient

from src.main import app


# See https://www.neoteroi.dev/blacksheep/testing/
async def test_server():
    # the application needs to handle its start event, to recreate a valid scenario
    await app.start()

    client = TestClient(app)

    response = await client.get("/users")
    body = await response.json()

    assert response.status == 200
    assert body == [
        {"name": "Alice", "user_id": 1},
        {"name": "Bob", "user_id": 2},
        {"name": "Charlie", "user_id": 3},
    ]
