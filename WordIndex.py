#WordIndex.py
#Name: Caden Cerny
#Date: Mar. 2, 2025
#Assignment: Lab 6

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  
  for line_num, line in enumerate(textFile, start=1):
    words_in_line = line.split()
    for word in words_in_line:
      word = word.lower().strip(".,!?;:()[]{}\"'")
      if word not in words:
        words[word] = []
      if line_num not in words[word]:
        words[word].append(line_num)
    print("Word Index:")
    for word, line_numbers in sorted(words.items()): 
        print(f"{word}: {', '.join(map(str, line_numbers))}")
  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)


if __name__ == '__main__':
  main()
