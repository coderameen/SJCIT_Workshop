class StudentDetail:
    #constructor
    def __init__(self,usn,name,marks):
        self.usn = usn
        self.name = name
        self.marks = marks
    
    def display_details(self):
        print(f"The student usn is {self.usn} | name: {self.name} | marks: {self.marks}")
        
s1 = StudentDetail("CS01","Calvin",95)
s1.display_details()

s2 = StudentDetail("CS02","BOB",87)
s2.display_details()