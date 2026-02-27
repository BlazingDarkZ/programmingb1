class Individual:
    """Base class representing an individual"""
    def __init__(self, full_name, years_old):
        self.full_name = full_name
        self.years_old = years_old

    def present(self):
        return f"Hi, I'm {self.full_name} and I'm {self.years_old} years old."


class Pupil(Individual):
    """Pupil class inheriting from Individual"""
    def __init__(self, full_name, years_old, pupil_number):
        super().__init__(full_name, years_old)
        self.pupil_number = pupil_number

    def present(self):
        return f"Hi, I'm {self.full_name}, a pupil. My number is {self.pupil_number} and I'm {self.years_old} years old."


class Instructor(Individual):
    """Instructor class inheriting from Individual"""
    def __init__(self, full_name, years_old, subject_area):
        super().__init__(full_name, years_old)
        self.subject_area = subject_area

    def present(self):
        return f"Hello, I'm {self.full_name}, an instructor. I teach {self.subject_area} and I'm {self.years_old} years old."


# Testing the classes
learner = Pupil("Steven", 21, "S001")
educator = Instructor("Kai", 29, "Programming")

print("=== School Management System ===")
print(learner.present())
print(educator.present())
print(f"\nPupil age: {learner.years_old}")
print(f"Instructor subject: {educator.subject_area}")