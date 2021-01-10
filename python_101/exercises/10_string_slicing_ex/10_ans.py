# 1. From the string "Welcome to Python 101: Strings", extract text and create/print a new string that says:
# * "1 Welcome Ring To Tyler"
# * Every first letter in a word should be capitalized(title format)

# 2. Print the same string backwards

msg = 'welcome to Python 101: Strings'

#My solution
sub_strs = ["1", "welcome", "ring", "to", "tyler"]

def search_str(sub_str, string):
    
    lower_str = string.lower()

    if sub_str in lower_str:    
        sub_idx = lower_str.index(sub_str)

        return lower_str[sub_idx:(len(sub_str) + sub_idx)]
    else: 
        extract_sub = []

        for letter in sub_str:
            extract_sub.append(lower_str[lower_str.index(letter)])
        
        return("".join(extract_sub))

def generate_msg(sub_strs, string):
    return_str = []

    for sub_str in sub_strs:
       return_str.append(search_str(sub_str, string))

    return " ".join(return_str)

new_msg = generate_msg(sub_strs, msg)

print(new_msg.title())

print(new_msg.title()[::-1])


#Instructor solution
msg='welcome to Python 101: Strings'

msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  

print(msg1.title())
print(msg1[::-1].title())