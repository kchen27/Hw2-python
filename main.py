#Author: Kyle Chen kvc5823@psu.edu

def getGradePoint(grade):
  if grade == "A":
    gp = 4.0
  elif grade == "A-":
    gp = 3.67
  elif grade == "B+":
    gp = 3.33
  elif grade == "B":
    gp = 3.0
  elif grade == "B-":
    gp = 2.67
  elif grade == "C+":
    gp = 2.33
  elif grade == "C":
    gp = 2.0
  elif grade == "D":
    gp = 1.0
  else:
    gp = 0
  return float(gp)

def run():
  gp1 = str(input("Enter your course 1 letter grade:"))
  c1 = float(input("Enter your course 1 credit: "))
  gp1 = getGradePoint(gp1)
  print(f"Grade point for course 1 is: {gp1}")

  gp2 = str(input("Enter your course 2 letter grade:"))
  c2 = float(input("Enter your course 2 credit: "))
  gp2 = getGradePoint(gp2)
  print(f"Grade point for course 2 is: {gp2}")
  gp3 = str(input("Enter your course 3 letter grade:"))
  c3 = float(input("Enter your course 3 credit: "))
  gp3 = getGradePoint(gp3)
  print(f"Grade point for course 3 is: {gp3}")
  GPA = (gp1 * c1 + gp2 * c2 + gp3 * c3)/(c1 + c2 + c3)
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
    run()
