import random
import time

print("💘 Welcome to the Funny Love Calculator! 💘")
name1 = input("Enter your name: ")
name2 = input("Enter your crush's name: ")

print(f"\nCalculating love between {name1} and {name2}...")
time.sleep(2)

percentage = random.randint(40, 100)
status = "🔥 True Love!" if percentage > 85 else "😊 Sweet!" if percentage > 60 else "🙂 It's complicated..."

print(f"\n❤️ {name1} + {name2} = {percentage}% Love!")
print(f"Status: {status}")
