import random
pilihan = ["batu", "gunting", "kertas"]

user = input("pilih batu, gunting, atau keratas :").lower()

komputer = random.choice(pilihan)
print(f"komputer memilih : {komputer}")

if user == komputer:
    print("seri")
elif (
    (user == "batu" and komputer == "gunting")
    or
    (user == "kertas" and komputer == "batu")
    or
    (user == "gunting" and komputer == "kertas")
):
    print("kamu menang")
else:
    print("kamu kalah")