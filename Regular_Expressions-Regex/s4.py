import re
def substitutor():
    sentence1 = "It is raining outside"
    print(re.sub(r"raining","sunny",sentence1))

    sentence2 = "Thankyou very very much"
    print(re.sub(r"very","so",sentence2,count = 1))

substitutor()    