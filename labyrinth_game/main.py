#!/usr/bin/env python3
from labyrinth_game.player_actions import (
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    get_input,
    show_help,
    solve_puzzle,
)

game_state = {
    "player_inventory": [],  # Инвентарь игрока
    "current_room": "entrance",  # Текущая комната
    "game_over": False,  # Значения окончания игры
    "steps_taken": 0,  # Количество шагов
}


def process_command(game_state, command):
    user_command = command.split()

    match user_command[0]:
        case "help":
            show_help()
        case "look":
            describe_current_room(game_state)
        case "use":
            use_item(game_state, user_command[1])
        case "go" | "north" | "south" | "west" | "east":
            move_player(game_state, user_command[-1])
        case "take":
            take_item(game_state, user_command[1])
        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case "inventory":
            show_inventory(game_state)
        case "quit":
            game_state["game_over"] = True
            print("\nСпасибо за игру! До свидания!\n")
        case _:
            print("Такая команда отсутствует!\n")


def main():
    # print("Первая попытка запустить проект!")
    print("Добро пожаловать в Лабиринт сокровищ!\n")

    describe_current_room(game_state)

    while not game_state["game_over"]:
        user_command = get_input("\n> Введите команду: ")
        process_command(game_state, user_command)


if __name__ == "__main__":
    main()
