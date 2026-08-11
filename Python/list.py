# res = 6*(6+1)//2

# sum = 18
# for i in l:
#     sum = sum + i

# [1,2,3,4,5]

# 1---2,3,4,5,1
# 2---3,4,5,1,2
# 3---4,5,1,2,3
# 4---5,1,2,3,4
# 5---1,2,3,4,5

# def second_highest_score(scores):
#     unique_scores = sorted(set(scores))
    
#     if len(unique_scores) < 2:
#         return "No second-highest score"
    
#     return unique_scores[-2]

# def find_missing_number(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i + 1] != numbers[i] + 1:
#             return numbers[i] + 1

def rotate_list(lst, k):
    n = len(lst)
    
    if n == 0:
        return lst
    
    k = k % n
    
    return lst[-k:] + lst[:-k]
