def ask(prompt: str, options: list):
    selected_option = ""
    while selected_option not in options:
        try:
            print(prompt)
            [print(f"\t{i + 1}: {options[i]}") for i in range(len(options))]
            selected_option = int(input("Enter Selection: ")) - 1
            if selected_option not in range(len(options)):
                raise ValueError
            return selected_option
        except ValueError:
            print("Invalid input, please enter option number.")
