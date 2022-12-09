class Student(object):     
    def __init__(self, name, number):         
        self.name = name         
        self.scores = []         
        for count in range(number):             
            self.scores.append(0)      
    def getName(self):         
        return self.name      
    def setScore(self, i, score):         
        self.scores[i - 1] = score      
    def getScore(self, i):         
        return self.scores[i - 1]      
    def getAverage(self):         
        return sum(self.scores) / len(self.scores)      
    def getHighScore(self):         
        return max(self.scores)      
    def __str__(self):         
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))      
    def __eq__(self, other):         
        return self.name == other.name      
    def __lt__(self, other):         
        return self.name < other.name      
    def __ge__(self, other):         
        return self.name >= other.name   
def main():
    student1="Bale"
    student2="Ronaldo"
    student3="Messi"
    grade1="96"
    grade2="95"
    grade3="85"     
    s1 = Student('Bale',96)     
    s2 = Student('Ronaldo',95)     
    s3 = Student('Messi',85)     
    print("Is the score of " + student1 + " ("+grade1+")" +" equal to (=) "+ " ("+grade2+")" + grade2 +"? "+ str(s1 == s2))
    print("Is the score of " + student1 + " ("+grade1+")" +" less than to (<) "+ " ("+grade2+")" +"? "+ str(s1 < s2))
    print("Is the score of " + student1 +" ("+grade1+")" +" greater than or equal to (>=) "+ student2+" ("+grade2+")" +"? "+ str(s1 >= s2))                   
    print("Is the score of " + student1 +" ("+grade1+")" +" equal to (=) "+ student3 +" ("+grade3+")" +"? "+ str(s1 == s3))          
    print("Is the score of " + student1 +" ("+grade1+")" +" less than to <) "+ student3 +" ("+grade3+")" +"? "+ str(s1 < s3))     
    print("Is the score of " + student1 +" ("+grade1+")" +" greater than or equal to (>=) "+ student3 +" ("+grade3+")" +"? "+ str(s1 >= s3))          
    print("Is the score of " + student2 +" ("+grade2+")" +" equal to (=) "+ student3+" ("+grade3+")" +"? "+ str(s2 == s3))          
    print("Is the score of " + student2 +" ("+grade2+")" +" lessthan to (<) "+ student3+" ("+grade3+")" +"? "+ str(s2 < s3))     
    print("Is the score of " + student2 +" ("+grade2+")" +" greater than or equal to (>=) "+ student3+" ("+grade3+")" +"? "+ str(s2 >= s3))      
if __name__ == '__main__':     main() 