#WordCount.py
#Name: Caden Cerny
#Date: Mar. 2, 2025
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')

  lines = textFile.readlines()
  line_count = len(lines)
  word_count = sum(len(line.split()) for line in lines)
  char_count = sum(len(line) for line in lines)

  print("Line: ", line_count)
  print("Words: ", word_count)
  print("Characters: ", char_count)
  

if __name__ == '__main__':
  main()
