text = "Any text for practice"
print(text.split())

print(text.replace("for", "on")) 


email = input("Enter your Email address: ")
print(email.split('@')[0])

cores = int(input("Enter cores of CPU: "))
hyperthreading = input("Do you have HT: ")
ram = int(input("Enter the RAM: "))

if hyperthreading == "yes": print(f"Your PC have {cores*2} threads, and you have {ram/cores/2} RAM on thread")
if hyperthreading == "Yes": print(f"Your PC have {cores*2} threads, and you have {ram/cores/2} RAM on thread")
if hyperthreading == "YES": print(f"Your PC have {cores*2} threads, and you have {ram/cores/2} RAM on thread")
if hyperthreading == "y": print(f"Your PC have {cores*2} threads, and you have {ram/cores/2} RAM on thread")
if hyperthreading == "Y": print(f"Your PC have {cores*2} threads, and you have {ram/cores/2} RAM on thread")

if hyperthreading == "no": print(f"Your PC have {cores} threads, and you have {ram/cores} RAM on thread")
if hyperthreading == "No": print(f"Your PC have {cores} threads, and you have {ram/cores} RAM on thread")
if hyperthreading == "NO": print(f"Your PC have {cores} threads, and you have {ram/cores} RAM on thread")
if hyperthreading == "n": print(f"Your PC have {cores} threads, and you have {ram/cores} RAM on thread")
if hyperthreading == "N": print(f"Your PC have {cores} threads, and you have {ram/cores} RAM on thread")