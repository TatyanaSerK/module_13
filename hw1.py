import asyncio

async def  start_strongman(name, power):
    # В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
    # После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>'
    # с задержкой обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
    # В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования'.
    print(f'Силач {name} начал соревнования.')
    ball = 1
    while ball < 6:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball}')
        ball += 1
    print(f'Силач {name} закончил соревнования!')


async def start_tournament():
    # асинхронная функция start_tournament, в которой создаются 3 задачи для функций start_strongman.
    # поставьте каждую задачу в ожидание (await).
    task1 = asyncio.create_task( start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())