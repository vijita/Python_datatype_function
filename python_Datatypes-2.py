# Python feud / let the battle begin...

def game(question,answer,total_count):
    """
    Input question, answer & total_count
    Output score
    """
    print(question)
    mylist = ["first", "second", "third"]
    print("Guess the top 3 answers to get the maximum points")
    mylist[0] = input("Enter your first guess ")
    mylist[1] = input("Enter your second guess ")
    mylist[2] = input("Enter your third guess ")
    guess1 = answer.count(mylist[0])
    guess2 = answer.count(mylist[1])
    guess3 = answer.count(mylist[2])
    score = guess1 + guess2 + guess3
    print("Congrats! Your score is", score)
    
    set_answer = set(answer)
    
    dict_fr_set = dict.fromkeys(set_answer,True)
    
    
    for i in range(0,total_count-1):
        dict_fr_set.update([(answer[i],answer.count(answer[i]))])
        
    print("The answers on the board are",dict_fr_set)
    return(score)

print("Welcome to python feud")

print("We asked 100 people")


question = "What fruit do you eat the most often?"
answer = 'Orange', 'Banana', 'Banana','Apple', 'Persimmon', 'Banana', 'Banana', 'Mango', 'Banana', 'Banana', 'Banana', 'Banana', 'Banana', 'Strawberries', 'Orange', 'Banana', 'Banana', 'Banana', 'Banana', 'Blueberries', 'Banana', 'Banana', 'Strawberries', 'Banana', 'Blueberries', 'Banana', 'Banana', 'Banana', 'Apple', 'Apple', 'Apple', 'Apple', 'Banana', 'Apple', 'Apple', 'Apple', 'Apple', 'Banana', 'Apple', 'Banana', 'Orange', 'Banana', 'Banana', 'Apple', 'Apple', 'Apple', 'Avocado', 'Apple', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple', 'Apple', 'Orange', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple', 'Apple', 'Orange', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple', 'Apple', 'Orange', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple', 'Apple', 'Orange', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple', 'Apple', 'Orange', 'Mango', 'Orange', 'Dates', 'Blueberries', 'Strawberries', 'Banana', 'Apple'
total_count = len(answer)
score1 = game(question,answer,total_count)

question = "What is your favourite hobby?"
answer = 'drawing', 'singing', 'painting', 'dancing', 'photography', 'painting','drawing', 'singing', 'painting', 'dancing', 'photography', 'painting',
total_count = len(answer)
score2 = game(question,answer,total_count)

print("total is", score1 + score2)




















