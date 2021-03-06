def ask(prompt: str, options: list) -> int:
    """
    Asks a user a question and displays a numerical list of options
    :param prompt: question prompt to display
    :param options: list of options
    :return: python index of selection
    """
    selected_option = ""
    while selected_option not in options:
        try:
            print(prompt)
            [print(f"\t{i + 1}: {options[i]}") for i in range(len(options))]
            selected_option = int(input("Enter Selection: ")) - 1
            if selected_option not in range(len(options)):
                raise ValueError
        except ValueError:
            print("Invalid input, please enter option number.")
        return selected_option
