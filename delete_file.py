from pathlib import Path


def user_info():
    info = {1: 'skin_full_info.json', 2: 'my_inventory_info.json'}
    user_input = int(input('what to delete?\n1 - skin_full_info.json\n2 - my_inventory_info.json\n->'))
    return info.get(user_input)


def delete_file_with_scripts():
    try:
        file_path = Path(str(user_info()))
        file_path.unlink()
    except FileNotFoundError as msg_err:
        print(f'This file not found or was deleted:- {msg_err}')


if __name__ == "__main__":
    delete_file_with_scripts()
