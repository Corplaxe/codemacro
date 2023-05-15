class macro():
    def __init__(self) -> None:
        pass

    def clear(self):
        """
        clear the console
        """
        from os import system , name
        if name == 'nt':
            system('cls')
        else:
            system('clear')