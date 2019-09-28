# Declare dictionary with dictionary key and value
students = {
    "Alice": {"id": "ID0001", "age": 26, "grade": "A"},
    "Tunde": {"id": "ID0002", "age": 28, "grade": "B"},
    "Robert": {"id": "ID0003", "age": 30, "grade": "C"},
    "Elean": {"id": "ID0004", "age": 32, "grade": "D"},
    "Victoria": {"id": "ID0005", "age": 34, "grade": "E"},
}
print(students["Tunde"]["age"])
# To get a specific data from above dictionary we do:
print(students["Robert"]["id"], students["Robert"]["grade"])
# We can access Elean id or age by using index as:
