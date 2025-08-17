print("Enter obtained marks for the following subjects:")
maths=int(input("Maths:"))
eng=int(input("English:"))
spanish=int(input("Spanish:"))
science=int(input("Science:"))
sum=maths+eng+spanish+science
print("The sum of your marks are:",sum)
perc=(sum/400)*100
print("The percentage of your total marks are",perc)