import module1 as m1


def main():

    print("\t\t\t===== ATTENDENCE TRACKER =====")
    while True:
        bunkBuddy = m1.Bunkbuddy()
        m1.custom_decorator(117)
        user_choice = input(
            "[M] Mark Attendence\n[V] View Details\n[R] Reset Data\n[W] Warnings\n[B] Bunk-o-Meter\n[Q] Quit\nChoice:")
        if user_choice == "M" or user_choice == "m":
            m1.decorator()
            bunkBuddy.subject_selection()
        elif user_choice == "V" or user_choice == "v":
            m1.decorator()

            bunkBuddy.view_details()
        elif user_choice == "R" or user_choice == "r":
            bunkBuddy.reset_data()
        elif user_choice == "Q" or user_choice == "q":
            m1.decorator()
            print("Thanks for using ")
            break
        elif user_choice == "W" or user_choice == "w":
            m1.decorator()
            bunkBuddy.warnings()
        elif user_choice == "B" or user_choice == "b":
            m1.decorator()
            bunkBuddy.bunkmeter()
        else:
            m1.decorator()
            print("Invalid Input")


if __name__ == "__main__":
    main()
