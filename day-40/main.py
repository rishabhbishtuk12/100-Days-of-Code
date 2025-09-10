detailsList={"name":"","date of birth":"","phone number":"","email":"","address":""}
print("🌟Contact Card🌟")
detailsList["name"]=input("\nInput your name: ")
detailsList["date of birth"]=input("\nInput your date of birth: ")
detailsList["phone number"]=input("\nInput your telephone number: ")
detailsList["email"]=input("\nIInput your email: ")
detailsList["address"]=input("\nInput your address: ")
print("\n------------------------------------------------\n")
print(f'Hi {detailsList["name"]}. Our dictionary says that you were born on {detailsList["date of birth"]}, we can call you on {detailsList["phone number"]}, email {detailsList["email"]}, or write {detailsList["address"]}')
