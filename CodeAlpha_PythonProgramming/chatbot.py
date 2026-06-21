
def chatbot_response(user):

    if user == "hi":
       return "hi!"
    elif user == "hello":
        return "hello!"
    elif user == "how are you":
        return "iam fine, thanks!"
    elif user  == "what is your name":
        return"my name is chatbot!"      
    elif user == "bye":
        return "good bye!"
    else:
        return "sorry,i don't understand that."  
print("welcome to simple python chatbot!")
print("type 'bye' to exit.")    
while True:     
    user = input("you: ").lower()   
    response = chatbot_response(user)
    print("Bot:",response)
    if user == "bye":
        break
     
