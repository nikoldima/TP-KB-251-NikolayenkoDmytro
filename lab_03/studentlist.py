class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)

    def delete_student(self, name):
        for item in self.students:
            if item.name == name:
                self.students.remove(item)
                return True
        return False

    def find_student(self, name):
        for item in self.students:
            if item.name == name:
                return item
        return None

    def update_student(self, old_name, updated_student):
        if self.delete_student(old_name):
            self.add_student(updated_student)
            return True
        return False

    def print_all(self):
        for student in self.students:
            print(student)