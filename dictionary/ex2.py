students={
  "rahul":75,
  "amit":32,
  "priya":88,
  "neha":39,
  "rohit":55
 }

for name,marks in students.items():
    if marks>=40:
        if marks>=80:
            print("EXCELLENT")
        elif(marks>=60):
            print("good")
        else:
            print("avg")
    else:
        print("fail")