students={
  "rahul":75,
  "amit":32,
  "priya":88,
  "neha":39,
  "rohit":55
 }

for name,marks in students.items():
    if marks>=40:
        print(name, " is passed")
    else:
        print(name, " is fail")