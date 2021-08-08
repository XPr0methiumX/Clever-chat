
# Clever-chat

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) ![Stable version](https://img.shields.io/badge/Stable_Version-1.0.0-informational)

An API Wrapper for clever-chat (chatbot) in Python
## Features

- Easy to use
- Epic customizations
- Extremely fast responses
- No rate-limits

  
## Installation

```bash
  pip install clever_chat
```
    
## API Reference

#### Getting a response

```py
  # Synchronous Client
  import clever_chat
  from clever_chat import Client

  print(Client.get_response('Hello'))

  # Asynchronous Client
  import asyncio
  import clever_chat
  from clever_chat import AsyncClient

  response = asyncio.get_event_loop().run_until_complete(AsyncClient.get_response("Hello"))
  print(response)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `message` | `string` | **Required**. The message you're sending to the bot |

#### Customizations (Optional)

```py
  # Synchronous Client
  import clever_chat
  from clever_chat import Client

  print(Client.get_response('Hello', user_id, chatbot_gender, chatbot_name, developer_name, chatbot_age, birthday, birthplace, birthyear, religion, favouriteactor, favouriteactress, favouriteartist, favouriteauthor, favouriteband, favouritebook))

  # Asynchronous Client
  import asyncio
  import clever_chat
  from clever_chat import AsyncClient

  response = asyncio.get_event_loop().run_until_complete(AsyncClient.get_response("Hello", user_id, chatbot_gender, chatbot_name, developer_name, chatbot_age, birthday, birthplace, birthyear, religion, favouriteactor, favouriteactress, favouriteartist, favouriteauthor, favouriteband, favouritebook))
  print(response)
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id`      | `string` | **Optional**. ID of the message author (for discord only) |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `chatbot_gender`      | `string` | **Optional**. gender of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `chatbot_name`      | `string` | **Optional**. name of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `developer_name`      | `string` | **Optional**. name of the developer of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `chatbot_age`      | `string` | **Optional**. age of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `birthday`      | `string` | **Optional**. birthday of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `birthplace`      | `string` | **Optional**. birth place of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `birthyear`      | `string` | **Optional**. birth year of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `religion`      | `string` | **Optional**. religion of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouriteactor`      | `string` | **Optional**. favourite actor of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouriteactress`      | `string` | **Optional**. favourite actress of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouriteartist`      | `string` | **Optional**. favourite artist of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouriteauthor`      | `string` | **Optional**. favourite author of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouriteband`      | `string` | **Optional**. favourite band of the chatbot |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `favouritebook`      | `string` | **Optional**. favourite book of the chatbot |


  
## Authors

- [@Pr0methium](https://www.github.com/XPr0methiumX)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Contributing

Contributions are always welcome!

You can DM me on discord i.e. Pr0methium#0337 if you wanna contribute to this project!

  