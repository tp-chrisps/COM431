
class Student:
    def __init__(self, pid, pname, pcourse, pmark):
        self.id = pid
        self.name = pname
        self.course = pcourse
        self.mark = pmark

    def __str__(self):
        return f'{self.id}\t{self.name}\t{self.course}\t{self.mark}'

    def setMark(self, pmark):
        if (pmark >= 0) and (pmark <= 100):
            self.mark = pmark
            return True
        else:
            return False

    def printGrade(self):
        if self.mark >= 70:print("First")
        elif self.mark >= 60:print("2/1")
        elif self.mark >= 50:print("2/2")
        elif self.mark >= 40:print("Third")
        elif self.mark >= 0:print("Fail")
        else:print("Mark not set")

