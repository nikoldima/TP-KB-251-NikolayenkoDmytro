import pytest
from student import Student
from studentlist import StudentList
from utils import Utils


def test_student_creation():
    s = Student("Alice", "111", "alice@gmail.com", "KB-251")
    assert s.name == "Alice"
    assert s.phone == "111"
    assert s.email == "alice@gmail.com"
    assert s.group == "KB-251"
    assert "Alice" in str(s)


def test_add_student():
    s_list = StudentList()
    s_list.add_student(Student("Bob Sponge", "111", "bob@gmail.com", "KB-251"))
    s_list.add_student(Student("Alice", "222", "alice@gmail.com", "KB-251"))

    assert len(s_list.students) == 2
    assert s_list.students[0].name == "Alice"
    assert s_list.students[1].name == "Bob Sponge"



def test_delete_student():
    s_list = StudentList()
    s_list.add_student(Student("Alice", "222", "alice@gmail.com", "KB-251"))
    s_list.add_student(Student("Bob Sponge", "111", "bob@gmail.com", "KB-251"))

    assert s_list.delete_student("Alice") is True
    assert len(s_list.students) == 1
    assert s_list.students[0].name == "Bob Sponge"
    assert s_list.delete_student("Nonexistent") is False




def test_update_student():
    s_list = StudentList()
    s_list.add_student(Student("Alice", "222", "alice@gmail.com", "KB-251"))
    s_list.add_student(Student("Bob Sponge", "111", "bob@gmail.com", "KB-251"))

    updated = Student("Zebra", "999", "zebra@gmail.com", "KB-251")
    assert s_list.update_student("Alice", updated) is True
    assert len(s_list.students) == 2
    assert s_list.students[0].name == "Bob Sponge"
    assert s_list.students[1].name == "Zebra"
    assert s_list.students[1].phone == "999"




def test_utils_save_and_load(tmp_path):
    test_file = tmp_path / "test_students.csv"
    utils = Utils()

    s_list = StudentList()
    s_list.add_student(Student("Emma Stone", "333", "emma@gmail.com", "KB-251"))
    s_list.add_student(Student("Bob Sponge", "111", "bob@gmail.com", "KB-251"))

    utils.save_data(test_file, s_list)
    loaded_list = utils.load_data(test_file)

    assert len(loaded_list.students) == 2
    assert loaded_list.students[0].name == "Bob Sponge"
    assert loaded_list.students[1].name == "Emma Stone"