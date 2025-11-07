from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state):
    player_inventory = game_state["player_inventory"]

    if not player_inventory:
        print("Ваш инвентарь пуст!\n")
    else:
        inventory_items = ", ".join(player_inventory)
        print(f"В Вашем инвентаре: {inventory_items}")


def move_player(game_state, direction):
    player_inventory = game_state["player_inventory"]
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    if direction in room_data["exits"].keys():
        if room_data["exits"][direction] == "treasure_room":
            if "rusty_key" in player_inventory:
                print(
                    "\nВы используете найденный ключ, "
                    "чтобы открыть путь в комнату сокровищ."
                )
            else:
                print("\nДверь заперта. Нужен ключ, чтобы пройти дальше.")
                return

        game_state["current_room"] = room_data["exits"][direction]
        game_state["steps_taken"] += 1

        random_event(game_state)
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.\n")


def take_item(game_state, item_name):
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    if room_data["items"] is None:
        print("Предметов в комнате нет.\n")
    elif item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.\n")
    elif item_name in game_state["player_inventory"]:
        print("У вас уже имеется такой предмет в инвентаре.\n")
    elif item_name in room_data["items"]:
        game_state["player_inventory"].append(item_name)
        room_data["items"].remove(item_name)

        print(f"Вы подняли: {item_name}\n")
    else:
        print("Нельзя пойти в этом направлении.\n")


def use_item(game_state, item_name):
    player_inventory = game_state["player_inventory"]

    if item_name in player_inventory:
        match item_name:
            case "torch":
                print("Во круг вас стало светлее...\n")
            case "sword":
                print("Вы чувствуете как становитесь увереннее...")
            case "bronze_box":
                if "rusty_key" in player_inventory:
                    print("Вы открыли шкатулку. В ней ничего нет.")
                else:
                    print("Вы открыли шкатулку и обнаружили в ней rusty_key.")
                    game_state["player_inventory"].append("rusty_key")
            case _:
                print("Вы не знаете как использовать этот предмет...\n")
    else:
        print("У вас нет такого предмета.\n")
