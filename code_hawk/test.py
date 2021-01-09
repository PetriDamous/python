def str_search(term, search_str):
    if term in search_str:
        return "Term found"
    else:
        return "Term not found"

string = "the dog ate the fox"

result_1 = str_search("fox", string)

result_2 = str_search("cat", string)

print(result_1)

print(result_2)

# val = "fox" in "dog ate the fox"

# print(val)