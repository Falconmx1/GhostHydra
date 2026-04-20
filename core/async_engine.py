import asyncio

async def run_async(passwords, worker, limit=10):
    semaphore = asyncio.Semaphore(limit)

    async def sem_task(pwd):
        async with semaphore:
            await worker(pwd)

    tasks = [asyncio.create_task(sem_task(p)) for p in passwords]
    await asyncio.gather(*tasks)
