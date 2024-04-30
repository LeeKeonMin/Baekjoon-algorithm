N = int (input())
result_list = list()

for i in range(0, N):
    Test = list(input())
    score = 0 
    temp_score = 1 

    for result in Test: 

        if result == 'O':
            score += temp_score
            temp_score += 1
        else:
            temp_score = 1

    
    result_list.append(score)

for scores in result_list:
    print(scores)

    
