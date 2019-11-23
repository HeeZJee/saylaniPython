#Write a program which takes 5 inputs from user for different subject’s

math = float(input("Enter your Mathematics obtained marks: "))
astrophysics = float(input("Enter your Astrophysics obtained marks: "))
cosmology = float(input("Enter your Cosmology obtained marks: "))
astronomy = float(input("Enter your Astronomy obtained marks: "))
programming = float(input("Enter your Programming obtained marks: "))

obt_marks = math + astrophysics + cosmology + astronomy + programming
percentage = (obt_marks/500)*100
if percentage <= 100 and percentage >= 80:
    print("\nCongrat! You passed with A+ grade with percentage of",percentage)
elif percentage <= 79 and percentage >= 70:
    print("\nExcellent! You passed with A grade with percentage of",percentage)
elif percentage <= 69 and percentage >= 60:
    print("\nNice! You passed with B grade with percentage of",percentage)
elif percentage <= 59 and percentage >= 50:
    print("\nPoor! You passed with C grade with percentage of",percentage)
elif percentage <= 49 and percentage >=0:
    print("Better Luck! You Failed the exam")
else:
    print("Your entered invalid values")    