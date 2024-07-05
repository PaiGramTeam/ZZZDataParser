from httpx import AsyncClient

client = AsyncClient(timeout=120.0, follow_redirects=True)
