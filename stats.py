def count_words(text):
    return len(text.split())  

def count_characters(text):
    str = text.split()
    storage = {}
    print(len(str))
    storage[" "]=len(str)-1
    for l in str:
        temp=l.lower()
        for ch in range(0,len(temp)):
            if temp[ch] not in storage:
                storage[temp[ch]]=0
            storage[temp[ch]]+=1
    return storage  

def sort_dict(dict_words):
    temp=[]
    for key,val in dict_words.items():
        temp.append({"char" : key,"num":val})
    temp.sort(reverse=True,key=sort_helper)
    return temp

def sort_helper(dict_words):
    return dict_words["num"]
