workout_records = []

def add_workout():

    while True:
        exercise_name = input("Enter exercise name: ").strip().lower()
        if exercise_name == "":
            print("Name cannot be empty")
        else:
            break

    valid_duration = False
    while not valid_duration:
        try:
            duration = int(input("Enter duration: "))
            if duration <= 0:
                print("Invalid input must be a positive number")
            else:
                valid_duration = True
                break
        except ValueError:
            print("Invalid input must be a positive number")

    valid_calories = False
    while not valid_calories:
        try:
            calories = int(input("Enter calories: "))
            if calories < 0:
                print("Invalid input must be a positive number")
            else:
                valid_calories = True
                break
        except ValueError:
            print("Invalid input must be a positive number")

    valid_intensity = False
    while not valid_intensity:
        try:
            workout_intensity = input("Enter workout intensity: ").strip().lower()
            if workout_intensity not in ("light", "moderate", "high"):
                print("Invalid input must be a valid workout intensity")
            else:
                valid_intensity = True
                break
        except ValueError:
            print("Invalid input for workout intensity")

    work_dict = {
        "exercise_name": exercise_name,
        "duration": duration,
        "calories": calories,
        "workout_intensity": workout_intensity
    }

    workout_records.append(work_dict)

    print("\nWorkout added Successfully")

def workout_statistics():

    if not workout_records:
        print("\nNo workout records added")
    else:
        total_duration = 0
        total_calories = 0
        for workout in workout_records:
            total_duration += workout["duration"]
            total_calories += workout["calories"]

        number_of_workouts = len(workout_records)
        average_workout_duration = total_duration / number_of_workouts

        print("\n--- Workout Statistics ---\n")
        print("Total Workouts:", number_of_workouts)
        print("Total Duration:", total_duration)
        print("Total Calories:", total_calories)
        print("Average Workout Duration:", average_workout_duration)

def display_workout():
    print("--- Workout Records ---\n")

    if not workout_records:
        print("No workout records added")
    else:
        for index, workout in enumerate(workout_records):
            index = index + 1
            print(f"Workout #{index}")
            print(f"Exercise name: {workout['exercise_name']}")
            print(f"Duration: {workout['duration']} minutes")
            print(f"Calories: {workout['calories']}")
            print(f"Workout intensity: {workout['workout_intensity']}\n")

def search_workout():
    user_input = input("Enter exercise name: ").strip().lower()

    workout_found = False
    if user_input == "":
        print("Please enter exercise name. The field cannot be empty")
    else:
        print("--- Search Results ---\n")
        for index, workout in enumerate(workout_records):
            index = index + 1
            if user_input == workout["exercise_name"]:
                print(f"{index}.")
                print(f"Exercise name: {workout['exercise_name']}")
                print(f"Duration: {workout['duration']} minutes")
                print(f"Calories: {workout['calories']}")
                print(f"Workout intensity: {workout['workout_intensity']}\n")

                workout_found = True
        if not workout_found:
            print("No matching workout found.")

def menu():
    while True:
        print("\n1. Add workout")
        print("2. Display workouts")
        print("3. Workout statistics")
        print("4. Search workout")
        print("5. Exit")

        valid_option = False
        while not valid_option:
            try:
                option = int(input("Enter your choice: "))
                if option not in (1, 2, 3, 4, 5):
                    print("Invalid option. Please enter a number from 1 to 5")
                else:
                    valid_option = True
                    break
            except ValueError:
                print("Invalid option. Please enter a number from 1 to 5")

        if option == 1:
            add_workout()
        elif option == 2:
            display_workout()
        elif option == 3:
            workout_statistics()
        elif option == 4:
            search_workout()
        elif option == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option")

menu()


