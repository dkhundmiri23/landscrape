def main():
    tools = [
        {"name": "teeth", "cost": 0, "earning": 1},
        {"name": "rusty scissors", "cost": 5, "earning": 5},
        {"name": "old-timey push lawnmower", "cost": 25, "earning": 50},
        {"name": "fancy battery-powered lawnmower", "cost": 250, "earning": 100},
        {"name": "team of starving students", "cost": 500, "earning": 250}
    ]
    
    money = 0
    current_tool_index = 0

    while money < 1000 or current_tool_index < len(tools) - 1:
        current_tool = tools[current_tool_index]
        print(f"You are currently using your {current_tool['name']} and have ${money}.")
        print("What do you want to do?")
        print("1: Work")
        if current_tool_index < len(tools) - 1:
            print(f"2: Buy {tools[current_tool_index + 1]['name']} for ${tools[current_tool_index + 1]['cost']}")
        print("3: Quit")

        choice = input("> ").strip()

        if choice == "1":
            money += current_tool['earning']
            print(f"You earned ${current_tool['earning']}.\n")
        elif choice == "2" and current_tool_index < len(tools) - 1:
            if money >= tools[current_tool_index + 1]['cost']:
                money -= tools[current_tool_index + 1]['cost']
                current_tool_index += 1
                print(f"You bought {tools[current_tool_index]['name']}.\n")
            else:
                print(f"You don't have enough money to buy {tools[current_tool_index + 1]['name']}.\n")
        elif choice == "3":
            print("You decided to quit. Goodbye!")
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

    print("Congratulations! You have a team of starving students and $1000. You've won the game!")

if __name__ == "__main__":
    main()
