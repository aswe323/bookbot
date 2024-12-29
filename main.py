def wordcount(string):
    return len(string.split())
def count_lowered_unique_characters(string):
    string_low = string.lower()
    uniques = set(string_low)
    counted_chars = {}
    for char in uniques:
        counted_chars[char] = 0
        for a in string_low:
            if a == char:
                counted_chars[char] += 1
    return counted_chars

def sort_on(d):
    return d["num"]

def sort_dictionary(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"char": key, "num":dictionary[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
                
                    



def main():
    print("starting analysis")
    with open("books/frankenstein.txt") as file:
        file_content = file.read()
    print("Total number of words: " + str(wordcount(file_content)))
    counted_lowered = count_lowered_unique_characters(file_content)
    for counted in sort_dictionary(counted_lowered):
        if counted['char'] != "\n":
            print(f"{counted['char']} was found {counted['num']}")
     

main()
