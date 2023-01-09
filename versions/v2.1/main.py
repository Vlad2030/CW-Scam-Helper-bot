# импорт .py модулей
from avoca import bot  # бот
from loguru import logger


def Start():
    if "__main__" == __name__:
        logger.success("bot started!")
        bot.executor.start_polling(bot.dp, skip_updates=True)
        logger.warning("bot shutdown")


Start()
