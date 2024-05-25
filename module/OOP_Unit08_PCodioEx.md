
```python
# Polymorphism Ex. 1
"""Use the Lottery class given as the parent class.
Create the PowerBall class as a child class of Lottery.
Override the shuffle method so that it returns a list of six random integers between 1 and 99."""

import random

class Lottery:
  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

class PowerBall(Lottery):
    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results

# Example usage
lottery_game = Lottery()
print("Lottery numbers:", lottery_game.shuffle())

power_ball_game = PowerBall()
print("PowerBall numbers:", power_ball_game.shuffle())
```

```python
# Polymorphism Ex. 1 Output

Lottery numbers: [12, 19, 7, 1, 4]
PowerBall numbers: [68, 52, 17, 24, 43, 53]
```

---

```python
# Polymorphism Ex. 2
"""Complete the Airplane and Train classes so that when an instance of each is passed to the passengers function,
they will return the total number of passengers on board."""

class Airplane:
    def __init__(self, first_class, business_class, coach):
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        return self.first_class + self.business_class + self.coach

class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5

def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')

# Example usage
airplane = Airplane(20, 50, 150)
train = Train(30, 40, 50, 60, 70)

passengers(airplane)
passengers(train)
```

```python
# Polymorphism Ex. 2 Output

There are 220 passengers on board.
There are 250 passengers on board.
```

---

```python
# Polymorphism Ex. 3
"""Create the class Characters which has the attribute phrases which is a list of strings passed as a parameter.
Overload the <, >, and == operators so that you can make comparisons based on the total number of characters in the string."""

class Characters:
    def __init__(self, phrases):
        self.phrases = phrases

    def __len__(self):
        total_chars = 0
        for phrase in self.phrases:
            total_chars += len(phrase)
        return total_chars

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __eq__(self, other):
        return len(self) == len(other)

# Example usage
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)

print(c1 > c2)  # prints 'True'
print(c1 < c2)  # prints 'False'
print(c1 == c1) # prints 'True'
```

```python
# Polymorphism Ex. 3 Output

True
False
True
```

---

```python
# Polymorphism Ex. 4
"""Create the Median that has the method calculate_median that calculates the median of the integers passed to the method.
Use method overloading so that this method can accept anywhere from two to five parameters."""

class Median:
    def calculate_median(self, *numbers):
        num_list = sorted(numbers)
        length = len(num_list)

        if length % 2 == 0:
            middle1 = num_list[length // 2 - 1]
            middle2 = num_list[length // 2]
            return (middle1 + middle2) / 2
        else:
            return num_list[length // 2]

# Example usage
m = Median()
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))
```

```python
# Polymorphism Ex. 4 Output

3
5.0
7
3.5
```

---

```python
# Polymorphism Ex. 5
"""Create the class Stars which is a child class of Substitute.
Then override the swap_words method so that every third word is replaced by a series of *.
If the word has three letters then it should be replaced with ***.
The number of * should match the number of characters in the word. Write the new string to self.answer_file."""

source_file = '/home/codio/workspace/code/polymorphism/text_1_exercise5.txt'
answer_file = '/home/codio/workspace/code/polymorphism/answer_exercise5.txt'

class Substitute:
  def __init__(self, source_file, answer_file):
    self.source_file = source_file
    self.answer_file = answer_file
    self.words = None
    
  def string_to_list(self):
    '''Read text file, turn it into a
    2D list of words for each line'''
    words = []
    with open(self.source_file, 'r') as file_object:
      lines = file_object.read().split('\n')
      for line in lines:
        words.append(line.split())
    self.words = words
    
  def list_to_string(self):
    '''Convert 2D list back into a 
    string with newline characters'''
    lines = []
    for line in self.words:
      lines.append(' '.join(line))
    string = '\n'.join(lines)
    self.words = string
  
  def swap_words(self):
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 5 == 0:
          word = line[i]
          line[i] = 'HELLO'
    self.list_to_string()


class Stars(Substitute):
  def swap_words(self):
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 3 == 0:
          word = line[i]
          line[i] = '*' * len(word)
    self.list_to_string()
    file = open(self.answer_file, 'w')
    file.writelines(self.words)
    file.close()
    
s = Stars(source_file, answer_file)
s.swap_words()
```

```python
# Polymorphism Ex. 5 Output

It is * truth universally ************* that a ****** man in ********** of a **** fortune, must ** in want ** a wife.
However little ***** the feelings ** views of **** a man *** be on *** first entering * neighbourhood, this ***** is so **** fixed in *** minds of *** surrounding families, **** he is ********** the rightful ******** of some *** or other ** their daughters.
“My dear *** Bennet,” said *** lady to *** one day, ***** you heard **** Netherfield Park ** let at ******
Mr. Bennet ******* that he *** not.
```

---
[Return to Module 2 Unit 8](OOP_Unit08.md)
