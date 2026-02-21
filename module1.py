import os


class Bunkbuddy:
    def __init__(self):
        self.filename = "bunkbuddy"

    def subject_selection(self):
        try:
            which_subject_at_start = int(input(
                "Which Subject:\n1:Probability & Statistics\n2:Technical & Business Writing\n3:Digital Logic Design\n4:Introduction to Software Engineering\n5:Object Oriented Programming\n6:Discrete Structures\n\nSelect Subject:"))
            if which_subject_at_start == 1:
                self.attendence_marker(0)
            elif which_subject_at_start == 2:
                self.attendence_marker(1)
            elif which_subject_at_start == 3:
                self.attendence_marker(2)
            elif which_subject_at_start == 4:
                self.attendence_marker(3)
            elif which_subject_at_start == 5:
                self.attendence_marker(4)
            elif which_subject_at_start == 6:
                self.attendence_marker(5)
            else:
                print("Subject Not Found")
        except ValueError:
            print("Invalid Input,input must be a number")

    def attendence_marker(self, which_subject_to_mark):
        if not os.path.exists(self.filename):
            print("Storage File Does not Exist,Use Reset Function at main menu")
            return
        with open(self.filename, "r") as f:
            subject_list = f.readlines()
            subject_data = subject_list[which_subject_to_mark].strip().split(
                '|')
            subject_name = subject_data[0]
            subject_total_attend = int(subject_data[1])
            subject_my_attend = int(subject_data[2])
            subject_my_absent = int(subject_data[3])
            subject_canceled = int(subject_data[4])
            given_attendence = input(
                "[P]resent or [A]bsent or [C]anceled?\nMark:").lower()
            if given_attendence == "P" or given_attendence == "p":
                subject_total_attend += 1
                subject_my_attend += 1

            elif given_attendence == "A" or given_attendence == "a":
                subject_total_attend += 1
                subject_my_absent += 1

            elif given_attendence == "C" or given_attendence == "c":
                subject_canceled += 1
            else:
                print("Invalid Input")
                return
            if subject_total_attend > 0:
                percentage = subject_my_attend/subject_total_attend*100
            else:
                percentage = 0
            new_line = f"{subject_name}|{subject_total_attend}|{subject_my_attend}|{subject_my_absent}|{subject_canceled}|{percentage}\n"
            subject_list[which_subject_to_mark] = new_line
            with open(self.filename, "w") as f:
                for each_subject in subject_list:
                    f.write(each_subject)
            print("\t--Attendence Marked--")

    def view_details(self):
        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        subject_name = "Subject-Name"
        subject_presents = "Presents"
        subject_percentage = "Percentage"
        total_classs = "Total Classes"
        subject_absent = "Absent"
        subject_canceled = "Canceled"
        decorator()
        with open(self.filename, "r") as f:
            subject_list = f.readlines()
            custom_decorator(117)
            print(
                f"{subject_name:<40}{total_classs:<15}{subject_presents:<15}{subject_absent:<15}{subject_canceled:<15}{subject_percentage}")
            custom_decorator(117)
            for i in subject_list:
                subject_data = i.strip().split(
                    '|')
                subject_name = subject_data[0]
                subject_total_attend = int(subject_data[1])
                subject_my_attend = int(subject_data[2])
                subject_my_absents = int(subject_data[3])
                subject_canceled = int(subject_data[4])
                if subject_my_attend > 0:
                    calculated_percentage = int(
                        subject_my_attend)/int(subject_total_attend)*100
                    percentage = str(calculated_percentage)+"%"
                    print(
                        f"{subject_name:<40}{subject_total_attend:<15}{subject_my_attend:<15}{subject_my_absents:<15}{subject_canceled:<15}{percentage}")
                else:
                    No_data = "No Data"
                    print(
                        f"{subject_name:<40}{No_data:<15}{No_data:<15}{No_data:<15}{No_data:<15}{No_data}")

    def warnings(self):
        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        with open(self.filename, "r") as f:

            for subject_data in f:
                subject_select = subject_data.strip().split('|')
                subject_name = subject_select[0]
                subject_percentage = float(subject_select[5])
                if subject_percentage < 75:
                    print(
                        f"Attendence Low for Subject :{subject_name}\nAttendence:{subject_percentage}%")

    def reset_data(self):
        with open(self.filename, "w") as f:
            f.write("Probability & Statistics|0|0|0|0|0\n")
            f.write("Technical & Business Writing|0|0|0|0|0\n")
            f.write("Digital Logic Design|0|0|0|0|0\n")
            f.write("Introduction to Software Engineering|0|0|0|0|0\n")
            f.write("Object Oriented Programming|0|0|0|0|0\n")
            f.write("Discrete Structures|0|0|0|0|0")
            decorator()
            print("Reset Successfull")

    def bunkmeter(self):
        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        with open(self.filename, "r") as f:
            for subject_data in f:
                subject_select = subject_data.strip().split('|')
                subject_name = subject_select[0]
                subject_total_attend = int(subject_select[1])
                subject_my_attend = int(subject_select[2])
                try:
                    counter = 0
                    while (subject_my_attend/(subject_total_attend+counter+1))*100 >= 75:
                        counter += 1
                    print(
                        f"Skipable classes for subject {subject_name:<55}: {counter} ")
                except ZeroDivisionError:
                    print("No Class Data Available")


def decorator():
    print("="*40)


def custom_decorator(value):
    print("="*value)
