class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def pri(self):
        print(self.name)
        print(self.rollnumber)
s1=student("hamsa",1)
s2 = student("venkat", 2)
s1.pri()
s2.pri()
