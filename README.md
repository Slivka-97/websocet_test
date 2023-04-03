# websocet_test

Задача:

Написать программу на Python, которая КАЖДЫЕ 5 СЕКУНД запрашивает данные по HTTP в любом публичном API, и транслирует их 1 РАЗ В СЕКУНДУ посредством вебсокет-сервера по адресу `"ws://0.0.0.0:9000/test"` всем клиентам в виде JSON такого вида:
{
"timestamp": 1677571936,  # Время последнего обновления информации из источника.
"data": {...}   # Последние данные в любом формате, хоть строкой.
}
(Пример источника данных: https://blockchain.info/ticker)

Python 3.10
1. Создаем виртуальное окружение python `-m venv venv`, активируем на Windows `venv\Scripts\activate.bat`, на Linux `source venv/bin/activate`
2. Устанавливаем зависимости: `pip install -r requirements.txt` 
3. Создаем сервер: `python web.py` при удачном создании должно появиться сообщение (Server listening on Port 9000)
4. Создаем клиента `python client.py`
