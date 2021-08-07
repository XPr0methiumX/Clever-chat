import aiohttp 
import requests
import json

class AsyncClient():
    async def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium"):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}")
            fetch = await request.json()
            response = fetch["message"]
            await session.close()
            return response

class Client():
    def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium"):
        request = requests.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}")
        fetch = request.json()
        response = fetch["message"]
        return response