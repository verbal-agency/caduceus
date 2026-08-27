import asyncio

import httpx

from caduceus.app import app


def test_health_reports_a_stable_machine_readable_status() -> None:
    async def get_health() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport, base_url="http://testserver"
        ) as client:
            return await client.get("/health")

    response = asyncio.run(get_health())

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
