import aiohttp 
import requests
import json

class AsyncClient():
    async def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium", age: str = "8", birthday: str = "March 18", birthplace: str = "acobot.ai", birthyear: str = "2012", religion: str = "Christian", favouriteactor: str = "Tom Hanks", favouriteactress: str = "Julia Roberts", favouriteartist: str = "Leonardo da Vinci", favouriteauthor: str = "Ernest Hemingway", favouriteband: str = "Beatles", favouritebook: str = "The Odyssey"):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}&age={age}&birthday={birthday}&birthplace={birthplace}&birthyear={birthyear}&religion={religion}&favouriteactor={favouriteactor}&favouriteactress={favouriteactress}&favouriteartist={favouriteartist}&favouriteauthor={favouriteauthor}&favouriteband={favouriteband}&favouritebook={favouritebook}")
            fetch = await request.json()
            response = fetch["message"]
            await session.close()
            return response

class Client():
    def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "Clever Bot", developer_name: str = "Pr0methium", age: str = "8", birthday: str = "March 18", birthplace: str = "acobot.ai", birthyear: str = "2012", religion: str = "Christian", favouriteactor: str = "Tom Hanks", favouriteactress: str = "Julia Roberts", favouriteartist: str = "Leonardo da Vinci", favouriteauthor: str = "Ernest Hemingway", favouriteband: str = "Beatles", favouritebook: str = "The Odyssey"):
        request = requests.get(f"https://noideawhatthisis.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}&age={age}&birthday={birthday}&birthplace={birthplace}&birthyear={birthyear}&religion={religion}&favouriteactor={favouriteactor}&favouriteactress={favouriteactress}&favouriteartist={favouriteartist}&favouriteauthor={favouriteauthor}&favouriteband={favouriteband}&favouritebook={favouritebook}")
        fetch = request.json()
        response = fetch["message"]
        return response