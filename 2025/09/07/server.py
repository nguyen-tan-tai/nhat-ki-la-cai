from fastapi import FastAPI
import uuid
import random
import time
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id):
    random_delay = random.uniform(0, 1)
    time.sleep(random_delay)
    return {"id": item_id, "uuid": str(uuid.uuid4()), "delay": random_delay}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)