age=int(input("enter your age : "))
learner_license=input("yes or no : ").lower()=="yes"
if (learner_license):
    driving_test_score=int(input("enter your score : "))
    if driving_test_score>=60:
        print("you got license : ")
    else:
        print("driving test score is not enough : ")
else:
    print("Learner license is not available : ")