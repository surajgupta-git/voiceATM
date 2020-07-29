import speech_recognition as sr
import time

def listenword():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r1.adjust_for_ambient_noise(source)
            audio = r1.listen(source)
            text = r1.recognize_google(audio)
            return text
        except:
            return "error"

def receiptprint():
    print("Do you need a receipt")
    print("🔊🔊")
    while(1):
            choice=listenword()
            if "yes" in choice:
                    print("collect your receipt",end="\n\n")
                    print("Thank You")
                    break
            elif "no" in choice:
                    print("Save Environement",end="\n\n")
                    print("Thank You")
                    break
            else:
                    print("could  not recognize say again")
                    print("🔊🔊")
                    continue

def navigate():
    print("do you want to proceed or go back or cancel")
    print("🔊🔊")
    while(True):
        textlistened=listenword()
        if "proceed" in textlistened:
                print("dispensing: "+format(amount),end="\n\n")
                receiptprint()
                exit()
        elif "go back" in textlistened:
                break
        elif "cancel" in textlistened:
                print("cancelling transaction")
                exit()
        else:
                print("could not recognize say again")
                print("🔊🔊")
                continue
    if(textlistened=="go back"):
        return

print("\n","************** Welcome to Voice controlled ATM ******************",end="\n\n")
print("Insert your card",end="\n\n")
time.sleep(2)
print("card inserted, PIN entered and Authentication successful",end="\n\n")
time.sleep(2)
print("Choose savings account or Current account")
print("🔊🔊")
while(True):
        textlistened=listenword()
        if "savings account" in textlistened:
            print("savings account is selected",end="\n\n")
            print("Choose Fast cash or withdrawal")
            print("🔊🔊")
            while(True):
                textlistened=listenword()
                if "fast cash" in textlistened :
                    print("You selected :Fast cash",end="\n\n")
                    while(True):
                        print("choose 500/ 1000/ 2000/ 5000")
                        print("🔊🔊")
                        arr=["500","1000","2000","5000"]
                        amount=listenword()
                        if amount in arr:
                            print("amount: "+format(amount))
                            navigate()
                            continue
                            break
                        elif "cancel" in amount:
                            print("cancelling transaction")
                            exit()
                        else:
                            print("could not recognize say again")
                            print("🔊🔊")
                            continue
                    break
                elif "withdrawal" in textlistened:
                    print("you selected: withdrawal",end="\n\n")
                    while(True):
                        print("amount to withdraw ???")
                        print("🔊🔊")
                        amount=listenword()
                        if "cancel" in amount:
                            print("cancelling transaction")
                            exit()
                        elif amount.isnumeric():
                            print("amount: "+format(amount))
                            navigate()
                            continue
                            break
                        else:
                            print("could not recognize say again")
                            print("🔊🔊")
                            continue
                    break
                elif "cancel" in textlistened:
                    print("cancelling transaction")
                    exit()
                else:
                    print("could  not recognize say again")
                    print("🔊🔊")
                    continue
            break
        elif "current account" in textlistened:
            print("current account is selected",end="\n\n")
            print("Choose Fast cash or withdrawal")
            print("🔊🔊")
            while(True):
                textlistened=listenword()
                if "fast cash" in textlistened :
                    print("You selected :Fast cash",end="\n\n")
                    while(True):
                        print("choose 500/ 1000/ 2000/ 5000")
                        print("🔊🔊")
                        arr=["500","1000","2000","5000"]    
                        amount=listenword()
                        if amount in arr:
                            print("amount: "+format(amount),end="\n\n")
                            navigate()
                            continue
                            break
                        elif "cancel" in amount:
                            print("cancelling transaction")
                            exit()
                        else:
                            print("could not recognize say again")
                            print("🔊🔊")
                            continue
                    break
                elif "withdrawal" in textlistened:
                    print("you selected: withdrawal",end="\n\n")
                    while(True):
                        print("amount to withdraw ???")
                        print("🔊🔊")
                        amount=listenword()
                        if "cancel" in amount:
                            print("cancelling transaction")
                            exit()
                        elif amount.isnumeric():
                            print("amount: "+format(amount),end="\n\n")
                            navigate()
                            continue
                            break
                        else:
                            print("could not recognize say again")
                            print("🔊🔊")
                            continue
                    break
                elif "cancel" in textlistened:
                    print("cancelling transaction")
                    exit()
                else:
                    print("could not recognize say again")
                    print("🔊🔊")
                    continue
        elif "cancel" in textlistened:
                    print("cancelling transaction")
                    exit()
        else:
            print("could not recognize say again")
            print("🔊🔊")
            continue


                
            
