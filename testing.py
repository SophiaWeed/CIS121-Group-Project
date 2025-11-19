with open("Questions.txt","r") as file:
    questions_dict = {}
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            print("good")
            question, answer = parts
            questions_dict[question] = answer
