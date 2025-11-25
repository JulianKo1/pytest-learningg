import logging

def get_logger(name: str) -> logging.Logger:
    """
    Создает и возвращает логгер с заданным именем.

    Логгер:
    - Устанавливает уровень логирования DEBUG
    - Выводит логи в консоль (stdout)
    - Использует формат: "дата | имя логгера | уровень | сообщение"

    :param name: Имя логгера (обычно имя модуля или класса)
    :return: Конфигурированный logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )  # Формат логов: время | имя логгера | уровень | сообщение

    handler.setFormatter(formatter)  # Применяем формат к обработчику
    logger.addHandler(handler)  # Добавляем обработчик к логгеру

    return logger  # Возвращаем готовый логгер