import asyncio


async def start_strongman(name, power):
    print(f'{name} начинает соревнования')
    for i in range(1, 6):
        await asyncio.sleep(15/power)
        print(f'{name} поднял шар №{i}')
    print(f'{name} закончил соревнование')


async def start_tournament():
    print(f'Соревнование начинается')
    task_1 = asyncio.create_task(start_strongman('Персей', 3))
    task_2 = asyncio.create_task(start_strongman('Атлас', 4))
    task_3 = asyncio.create_task(start_strongman('Гермес', 5))
    task_4 = asyncio.create_task(start_strongman('Зевс', 14))
    for i in [task_1, task_2, task_3, task_4]:
        await i
    


asyncio.run(start_tournament())
