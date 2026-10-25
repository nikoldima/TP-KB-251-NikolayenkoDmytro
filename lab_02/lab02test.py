import pytest
from lab02task import add_student, delete_student, update_student

def test_add_student():
    students = [{"name": "Bob Sponge", "phone": "111", "email": "bob@gmail.com", "group": "KB-251"}]
    new_student = {"name": "Alice", "phone": "222", "email": "alice@gmail.com", "group": "KB-251"}

    add_student(students, new_student)

    assert len(students) == 2
    assert students[0]["name"] == "Alice"
    assert students[1]["name"] == "Bob Sponge"

def test_delete_student():
    students = [
        {"name": "Alice", "phone": "222", "email": "alice@gmail.com", "group": "KB-251"},
        {"name": "Bob Sponge", "phone": "111", "email": "bob@gmail.com", "group": "KB-251"}
    ]

    result_success = delete_student(students, "Alice")
    assert result_success == True
    assert len(students) == 1
    assert students[0]["name"] == "Bob Sponge"

    result_fail = delete_student(students, "Nonexistent")
    assert result_fail == False
    assert len(students) == 1

def test_update_student():
    students = [
        {"name": "Alice", "phone": "222", "email": "alice@gmail.com", "group": "KB-251"},
        {"name": "Bob Sponge", "phone": "111", "email": "bob@gmail.com", "group": "KB-251"}
    ]
    updated_alice = {"name": "Zebra", "phone": "999", "email": "zebra@gmail.com", "group": "KB-251"}

    result = update_student(students, "Alice", updated_alice)

    assert result == True
    assert len(students) == 2
    assert students[0]["name"] == "Bob Sponge"
    assert students[1]["name"] == "Zebra"
    assert students[1]["phone"] == "999"