print("Loan Calculator")
print()

print("$1000 over 10 years at 5% APR")
print()
amount = 1000
loanA = amount
for number in range (10):
  new = (loanA*5)/100
  loanA = loanA + new
  print("Year",number+1,"is" , round(loanA,2))
  
amount =loanA - amount
print()
print("You Paid $",round(amount,2), "in interest!")

