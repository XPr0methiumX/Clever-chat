import aiohttp 
import requests
import json

class AsyncClient():
    async def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium", religion: str = None, favourite_actor: str = "Tom Cruise"):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}&religion={religion}&favouriteactor={favourite_actor}")
            fetch = await request.json()
            response = fetch["message"]
            await session.close()
            return response

class Client():
    def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium", religion: str = None, favourite_actor: str = "Tom Cruise"):
        request = requests.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}&religion={religion}&favouriteactor={favourite_actor}")
        fetch = request.json()
        response = fetch["message"]
        return response
