from aiogram import types
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
from bot import bot, dp
from aiogram.dispatcher.dispatcher import Bot, Dispatcher
from apps.main.handlers import dp

load_dotenv()

app = FastAPI()

WEBHOOK_PATH = f"/bot/{os.environ.get('BOT_TOKEN')}"
WEBHOOK_URL = os.environ.get("WEB_URL") + WEBHOOK_PATH

@app.on_event("startup")
async def on_startup():
    webhook = await bot.get_webhook_info()

    if webhook.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    tgUpdate = types.Update(**update)

    Dispatcher.set_current(dp)
    Bot.set_current(bot)

    await dp.process_update(tgUpdate)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8004, reload=False, workers=1)

    
