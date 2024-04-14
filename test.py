# from local_time import local_time
# import time


# while local_time() < '13:38:55':
#     time.sleep(3)
#     print("Not time")


# print("Time")


# import re

# text = "12.3 (3)"
# new_text = re.sub(r"\s+\(\d+\)$", "", text)
# print(new_text)  # Output: "123"



import ast

ltp = "12"
print(ast.literal_eval(ltp))