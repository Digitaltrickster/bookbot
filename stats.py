def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents

def get_word_count(path_to_file):
    return len(get_book_text(path_to_file).split())

def get_unique_word_count(path_to_file):
    mylist=get_book_text(path_to_file).lower().split()
    myset=set(mylist)
    return len(myset)

def get_char_count(path_to_file):
    mylist=get_book_text(path_to_file).lower()
        
    charcount={}
    for word in mylist.split():
        for char in word:
            if char not in charcount:
                charcount[char]=0
            charcount[char]+=1    
    return dict(sorted(charcount.items()))
