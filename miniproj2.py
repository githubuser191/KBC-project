print("\nWELCOME TO KAUN BANEGA CROREPATI")
question = [
    ["What is the name of the Prime Minister of India?", "Adityanath Yogi", "Narendra Modi", "Amit Shah", "Rahul Gandhi", 2],
    ["How many districts are there in Uttar Pradesh?", "56", "67", "75", "76", 3],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Who is known as the Missile Man of India?", "Dr. APJ Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha", "C.V. Raman", 1]
]
levels=[1000,2000,4000,8000]
reward=0

for i in range(len(question)):
    print(f"\nquestion for Rs.{levels[i]}")
    print(f"{1+i}.{question[i][0]}")
    print(f'a.{question[i][1]}       b.{question[i][2]}       c.{question[i][3]}       d.{question[i][4]}')
    try:
        reply=int(input('Enter your answer(1-4):'))
        if(reply==question[i][5]):
            print("✅ Correct answer!")
            reward = levels[i]
        else:
            print("❌ Wrong answer! Game over.")
            break
    except:
        print("invalid input! please enter your answer(1-4) ")
        break
print(f"\n🏆 You have won Rs.{reward}. Thank you for playing!")
    
    
    
    
