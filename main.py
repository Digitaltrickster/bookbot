from stats import get_book_text
from stats import get_word_count
from stats import get_unique_word_count
from stats import get_char_count
import sys

def main():
    if len(sys.argv)<2:
        print("""Usage: python3 main.py <path_to_book>""")
        sys.exit(1)
    for pathnum in range(1,len(sys.argv)):
        path = sys.argv[pathnum]
        #print(get_book_text(path))    
        #print(f"{get_char_count(path)} unique words found in the document")
        #print(get_char_count(path))
        print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {get_word_count(path)} total words\n--------- Character Count -------\n")
    
        sorteditems = sorted(get_char_count(path).items(), key=lambda item: item[1], reverse=True)
        sorteddict = dict(sorteditems)
        for char in sorteddict.keys():
            print(f"{char}: {sorteddict[char]}\n")
main()
