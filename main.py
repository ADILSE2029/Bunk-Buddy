import module1 as m1
bunkBuddy = m1.Bunkbuddy()
print("\t\t\t===== ATTENDENCE TRACKER =====")
while True:
    m1.custom_decorator(117)
    user_given_choice_at_start_about_process = input(
        "[M] Mark Attendence\n[V] View Details\n[R] Reset Data\n[W] Warnings\n[B] Bunk-o-Meter\n[Q] Quit\nChoice:")
    if user_given_choice_at_start_about_process == "M" or user_given_choice_at_start_about_process == "m":
        m1.decorator()
        bunkBuddy.subject_selection()
    elif user_given_choice_at_start_about_process == "V" or user_given_choice_at_start_about_process == "v":
        m1.decorator()

        bunkBuddy.view_details()
    elif user_given_choice_at_start_about_process == "R" or user_given_choice_at_start_about_process == "r":
        bunkBuddy.reset_data()
    elif user_given_choice_at_start_about_process == "Q" or user_given_choice_at_start_about_process == "q":
        m1.decorator()
        print("Thanks for using ")
        break
    elif user_given_choice_at_start_about_process == "W" or user_given_choice_at_start_about_process == "w":
        m1.decorator()
        bunkBuddy.warnings()
    elif user_given_choice_at_start_about_process == "B" or user_given_choice_at_start_about_process == "b":
        m1.decorator()
        bunkBuddy.bunkmeter()
    else:
        m1.decorator()
        print("Invalid Input")
