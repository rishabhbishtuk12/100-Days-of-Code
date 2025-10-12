class job:
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name, salary, hoursWorked ):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")


class doctor(job):
    experience: None
    spec = None

    def __init__(self, salary, hoursWorked, experience, spec):
        self.name = "Doctor"
        self.hoursWorked = hoursWorked
        self.salary = salary
        self.experience = experience
        self.spec = spec

    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
        print(f"{self.experience:<10} {self.spec:>21}")


class teacher(job):
    subject = None
    position = None
    def __init__(self, name, hoursWorked, salary, subject, position):
        self.name = "Teacher"
        self.hoursWorked = hoursWorked
        self.salary = salary
        self.subject = subject
        self.position = position

    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
        print(f"{self.subject:<10} {self.position:>21}")
        
print("🌟Jobs Jobs Jobs!🌟")
lawyer = job("Lawyer", 100000 ,40)
lawyer.print()
doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()
teach = teacher("48", "50000","7", "CompSci", "Asst. Principal")
teach.print()

