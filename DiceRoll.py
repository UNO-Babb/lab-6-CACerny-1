#DiceRoll.py
#Name: Caden Cerny
#Date: Mar. 2, 2025
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  num_rolls = 10000
  for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_sum = die1 + die2
    rolls[roll_sum - 2] += 1
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  print(f"Total Rolls: {num_rolls}\n")
  print(f"{'Sum':<5}{'Count':<10}{'Percentage'}")
  for i, count in enumerate(rolls):
        roll_sum = i + 2  
        percentage = (count / num_rolls) * 100
        print(f"{roll_sum:<5}{count:<10}{percentage:.2f}%")

if __name__ == '__main__':
  main()
