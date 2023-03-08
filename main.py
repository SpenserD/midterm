print("Spenser Deremiah")

def name_and_grade(last_name, first_initial, grade):

   # Format sentence below
  sentence = "Last Name, First Initial, Grade ~> {last_name}, {first_initial}. {grade}".format(last_name = "Deremiah", first_initial = "S", grade = "9th")
  

  # Don't forget to return the formatted sentence
  return sentence
print(name_and_grade("S", "Deremiah", 9))

def consecutive_numbers(n):

  number_list = []

  for i in range(1, n):
    number_list.append(i)

  return number_list

print(consecutive_numbers(9))

def factors(n):

  factor_list = []

  for i in range(1, n):
    
    if n % i == 0:
      factor_list.append(i)
      

  return factor_list

print(factors(100))

def grade(n):

  sentence = "Grade = {grade}".format(grade = (n))

  return sentence

print(grade(100))
