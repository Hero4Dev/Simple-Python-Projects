secret_word = 'Rabat'
limit = 3
count = 0
answer = "" 


print("Welcome To Our Guess Game , Yo Have 3 chances To Guess If You Guessed Incorrect Your Pc Is Going To Crash !!")
while answer != secret_word and count != limit :
    answer = input("Your Answer : ")
    count += 1 
    if count == limit :
        print("You Lost")
        break 
else :
    print("You Won")