student_scores =[78, 65, 89, 86, 55, 91, 64, 89, 72, 
                 92, 85, 94, 91, 88, 79, 68, 90, 73, 
                 84, 82,1000]

total_score = sum(student_scores)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
    
print(f"Max score: {max_score}")
