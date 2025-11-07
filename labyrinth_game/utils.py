import math
import random

from labyrinth_game.constants import (
    COMMANDS,
    MAX_DAMAGE_ROLL,
    MAX_RANDOM_EVENT,
    REWARD_ITEMS,
    ROOMS,
)


def get_input(prompt="> "):
    """Обработка ввода пользователя."""
    try:
        user_input = input(prompt).strip().lower()
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def describe_current_room(game_state):
    """Описание текущей комнаты."""
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    room_items = "--отсутсвуют--"
    if room_data["items"]:
        room_items = ", ".join(room_data["items"])

    print(f"\n== {current_room.upper()} ==")
    print(f"{room_data['description']}\n")
    print(f"Заметные предметы: {room_items}\n")

    room_exits = room_data["exits"]
    if room_exits:
        print("Доступные выходы:")
        for direction, room in room_exits.items():
            print(f"  - {direction}: {room}")
    else:
        print("Выходов нет... Кажется, это ловушка.\n")

    if room_data["puzzle"]:
        print("Кажется, здесь есть загадка (используйте команду solve).\n")


def solve_puzzle(game_state):
    """Решение загадок."""
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    if room_data["puzzle"]:
        print(f"{room_data['puzzle'][0]}\n")

        while True:
            user_answer = get_input("> Ваш ответ: ")

            if user_answer not in room_data["puzzle"][-1]:
                print("Неверно. Попробуйте снова.\n")

                if current_room == "trap_room":
                    trigger_trap(game_state)
            else:
                print("Ваш ответ верный!\n")
                break

        random_reward = random.choice(REWARD_ITEMS)
        room_data["puzzle"] = None

        game_state["player_inventory"].append(random_reward)
        print(f"В получаете награду: {random_reward}")
    else:
        print("Загадок здесь нет.\n")


def attempt_open_treasure(game_state):
    """Попытка открыть сокровщие."""
    player_inventory = game_state["player_inventory"]
    current_room = game_state["current_room"]

    if "treasure_key" in player_inventory:
        print("\nВы применяете ключ, и замок щёлкает. Сундук открыт!\n")
        ROOMS[current_room]["items"].remove("treasure_chest")

        print("== В сундуке сокровище! Вы победили! ==\n\n")
        game_state["game_over"] = True
    else:
        print("Сундук заперт. ... Ввести код? (да/нет)\n")
        user_answer = get_input("> Ваш ответ: ")

        if user_answer == "нет":
            print("Вы отступаете от сундука.")
        else:
            print(ROOMS[current_room]["puzzle"][0])
            user_answer = get_input("> Введите код: ")

            if user_answer in ROOMS[current_room]["puzzle"][1]:
                print("\n\n== Вы ввели верный код! Вы победили! ==\n\n")
                game_state["game_over"] = True
            else:
                print("Увы, код неверный.\n")
                print("Вы отступаете от сундука.")


def pseudo_random(seed, modulo):
    """Псевдослучайный генератор."""
    seed_sin = math.sin(seed * 12.9898)
    seed_mltp = seed_sin * 43758.5453
    fact_part = seed_mltp - math.floor(seed_mltp)
    num_range = fact_part * modulo
    return int(num_range)


def trigger_trap(game_state):
    """Обработка срабатывания ловушки."""
    print("\nЛовушка активирована! Пол стал дрожать...\n")

    player_inventory = game_state["player_inventory"]
    if player_inventory:
        random_num = pseudo_random(game_state["steps_taken"], len(player_inventory))
        print(
            "Из вашего инвентаря таинственным образом "
            f"исчезает {player_inventory[random_num]}..."
        )
        player_inventory[random_num].remove()
    else:
        random_num = pseudo_random(game_state["steps_taken"], MAX_DAMAGE_ROLL)
        if random_num < 3:
            print("\nВы угодили в ловушку!\n")
            game_state["game_over"] = True
        else:
            print("\nНу и ну! Вы чуть не угодили в ловушку.\n")


def random_event(game_state):
    """Вероятность случайного события при передвижении игрока."""
    player_inventory = game_state["player_inventory"]
    current_room = game_state["current_room"]

    random_num = pseudo_random(game_state["steps_taken"], MAX_DAMAGE_ROLL)
    if random_num <= 2:
        random_num = pseudo_random(game_state["steps_taken"], MAX_RANDOM_EVENT)
        match random_num:
            case 0:
                print("\nВы обнаружили монетку!\n")
                ROOMS[current_room]["items"].append("coin")
            case 1:
                if "sword" in player_inventory:
                    print(
                        "\nВы услышали шорох... "
                        "Достав меч вы отпугнули неизвестное существо!\n"
                    )
                else:
                    print(
                        "\nВы услышали шорох... "
                        "Из темноты слышится - «Чего трясешься, а?»\n"
                    )
            case 3:
                if "torch" not in player_inventory and current_room == "trap_room":
                    print("\nВы в опасности!\n")
                    trigger_trap(game_state)


def show_help():
    """Вывод подсказки."""
    print("\nДоступные команды:")
    for command, mean in COMMANDS.items():
        print(f"{command:<16} {mean}")
