student = {
  'name': 'ravan',
  'class': '12',
  'roll_id': '67'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'ravan'})
print(student.keys() >= {'roll_id', 'name'})
