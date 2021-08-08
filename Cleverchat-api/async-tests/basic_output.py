import asyncio
from clever_chat import AsyncClient

response = asyncio.get_event_loop().run_until_complete(AsyncClient.get_response("what is sunnydevelopment?"))
print(response)