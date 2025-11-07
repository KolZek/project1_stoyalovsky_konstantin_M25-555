ROOMS = {
    "entrance": {
        "description": "Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.",  # noqa: E501
        "exits": {"north": "hall", "east": "trap_room"},
        "items": ["torch"],
        "puzzle": None,
    },
    "hall": {
        "description": "Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.",  # noqa: E501
        "exits": {"south": "entrance", "west": "library", "north": "treasure_room"},
        "items": [],
        "puzzle": (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.',  # noqa: E501
            ("10", "десять", "ten"),
        ),
    },
    "trap_room": {
        "description": 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',  # noqa: E501
        "exits": {"west": "entrance", "south": "jail"},
        "items": ["treasure_key"],
        "puzzle": (
            'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")',  # noqa: E501
            ("шаг шаг шаг", "step step step"),
        ),
    },
    "library": {
        "description": "Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.",  # noqa: E501
        "exits": {"east": "hall", "north": "armory"},
        "items": ["ancient_book"],
        "puzzle": (
            'В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)',  # noqa: E501
            ("резонанс", "resonance"),
        ),
    },
    "armory": {
        "description": "Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.",  # noqa: E501
        "exits": {"south": "library"},
        "items": ["sword", "bronze_box"],
        "puzzle": None,
    },
    "treasure_room": {
        "description": "Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.",  # noqa: E501
        "exits": {"south": "hall"},
        "items": ["treasure_chest"],
        "puzzle": (
            "Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )",  # noqa: E501
            ("10", "десять", "ten"),
        ),
    },
    "jail": {
        "description": "Старая тюрьма... Когда-то здесь находились заключенные.",
        "exits": {"west": "armory"},
        "items": ["rusty_key"],
        "puzzle": None,
    },
    "dining_room": {
        "description": "Кажется, это похоже на столовую. Здесь должна быть еда.",
        "exits": {"north": "jail", "south": "hall"},
        "items": ["gold_apple"],
        "puzzle": (
            'Сундук с провизией где-то тут, но в темноте ничего не видно. "Не жжёт ладонь, переносной огонь, что это?" (ответ одно слово)',  # noqa: E501
            ("лом", "scrap", "crowbar"),
        ),
    },
}


REWARD_ITEMS = [
    "philosopher_stone",
    "master_sword",
    "gravity_gun",
    "wolfs_medallion",
    "morph_ball",
    "portal_gun",
    "bfg_9000",
    "hidden_blade",
    "pokeball_master",
    "infinity_gauntlet",
]


MAX_DAMAGE_ROLL = 9
MAX_RANDOM_EVENT = 3


COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение",
}
