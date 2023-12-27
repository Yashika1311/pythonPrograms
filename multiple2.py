# class LU:
#     def lets(self):
#         LU = {1:'Sub= C++  Trainer = Sai Sir  Duration = 1month',
#                2:"Sub = Java  Trainer = Prasad Sir  Duration = 3month", 
#                3:"Sub = Python   Trainer = Saurabh Sir   Duration = 4month"}
        
# class ITM:
#     def itm(self):
#         ITM = {1:"Sub = Maths   Trainer = Sumeet Sir  Duration = 1year ",
#                2:"Sub = Physics Trainer = Kalpana Mam   Duration = 2year ",
#                3:"Sub = Statistics  Trainer = Sheetal Mam  Duration = 1.5year"}
        
# class Child(LU , ITM):
#     def info(self,class_selected):
#         self.option=input("enter 'L' for Lets upgrade and 'I' for ITM" )
#         if self.option=="L":
#            print(LU.lets())

#         elif self.option=="I":
#             print(ITM.itm())

#         elif self.option=="LI":
#             print(LU.lets(),ITM.itm())

# name=input("enter student name:")
# age=int(input("Enter the age"))

# obj= Child()
# obj.info()

class LetsUpgrade:
    lu_courses=[{'Subject': 'Math', 'Trainer': 'Saikiran', 'Duration': 100},
                {'Subject': 'Python', 'Trainer': 'Saikiran', 'Duration': 150},
                {'Subject': 'Web design', 'Trainer': 'Prasad', 'Duration': 130}]

class ITM:
    itm_courses=[{'Subject': 'Math', 'Trainer': 'Sheetal', 'Duration': 90},
                {'Subject': 'DSA', 'Trainer': 'Sumit', 'Duration': 200},
                {'Subject': 'Computer Fundamentals', 'Trainer': 'Sumit', 'Duration': 150}]

class CourseSelector(LetsUpgrade, ITM):
    def print_subjects(self, selected_class):
        if selected_class == 'LetsUpgrade':
            subjects = [course['Subject'] for course in self.lu_courses]
        elif selected_class == 'ITM':
            subjects = [course['Subject'] for course in self.itm_courses]
        else:
            subjects = []

        if not subjects:
            print(f"No subjects available for {selected_class}")
            return

        print(f"Available subjects for {selected_class}: {subjects}")

        selected_subject = input("Enter the subject you want details for: ")

        if selected_subject in subjects:
            if selected_class == 'LetsUpgrade':
                selected_course = next(course for course in self.lu_courses if course['Subject'] == selected_subject)
            elif selected_class == 'ITM':
                selected_course = next(course for course in self.itm_courses if course['Subject'] == selected_subject)

            print(f"\nDetails of {selected_subject} in {selected_class}:")
            print(f"Trainer: {selected_course['Trainer']} sir")
            print(f"Duration: {selected_course['Duration']} hours")
        else:
            print(f"{selected_subject} is not available in {selected_class}")

course_selector = CourseSelector()

selected_class = input("Enter the class (LetsUpgrade or ITM): ")
course_selector.print_subjects(selected_class)