def convert_to_numeric(score):
    return float(score )

def sum_of_middle_three(score1,score2,score3,score4,score5):
    return ((score1+score2+score3+score4+score5)-(min(score1,score2,score3,score4,score5)+max(score1,score2,score3,score4,score5))/3)

def score_to_rating_string(avg_score):
    if (0<=avg_score<1):
        return "Terrible"
    elif(1<=avg_score<2):
        return "Bad"
    elif (2<=avg_score<3):
        return "Ok"
    elif (3<=avg_score<4):
        return "Good"
    else:
        return "Excellent"

def score_to_rating(score1,score2,score3,score4,score5):
    score1=convert_to_numeric(score1)
    score2=convert_to_numeric(score2)
    score3=convert_to_numeric(score3)
    score4=convert_to_numeric(score4)
    score5=convert_to_numeric(score5)

    average_score = sum_of_middle_three((score1,score2,score3,score4,score5)
    
    rating = score_to_rating_string(average_score)
    return rating
