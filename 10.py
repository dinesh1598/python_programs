"""10.Football Points
Create a function that takes the number of wins, draws and losses and
calculates the number of points a football team has obtained so far.
wins get 3 points
draws get 1 point
losses get 0 points

    """
#Footbal teams

#method 1

def myfun():
    W=int(input("Enter the number of wins:"))
    D=int(input("Enter the how many matches the draw:"))
    L=int (input("Enter the count of match looses:"))
    return (W*3)+(D*1)+(L*0)
print("The final score is(method 1):",myfun())

#method2

class football:
    def __init__(self, wins, losses, draws):
        self.w = wins
        self.l = losses
        self.d= draws
    def score(self):
        w = self.w * 3
        d = self.d * 1
        scores = w + d
        return scores
W=int(input("Enter the number of wins (method2):"))
D=int(input("Enter the how many matches the draw (method2):"))
L=int (input("Enter the count of match looses (method2):"))

Total= football(W,D,L)
print("(method2) The final result is:",Total.score())