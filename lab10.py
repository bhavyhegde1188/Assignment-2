''' Develop a program that uses class Student which prompts 
 the user to enter marks in three subjects andcalculates total 
 marks, percentage and displays the score card details. ''' 
  
 class Student: 
     def _init_(self, name = "", usn = "", marks = []): 
         self.name = name 
         self.usn = usn 
         self.marks = list() 
     def getMarks(self): 
         for i in range(3): 
             (self.marks).append(float(input(f"Enter marks for subject {i+1}: "))) 
     def getdetails(self): 
         self.name = input("Enter the name: ") 
         self.usn = input("Enter the USN: ") 
     def display(self): 
     print("Score Card:") 
     print("Name:", self.name) 
     print("USN:", self.usn) 
     print("Marks in each subject:", self.marks) 
     total = 0 
     for x in self.marks: 
         total += x 
     print("Total Marks:", total) 
     print("Percentage:", total/3,'%') 
  
 x = Student() 
 x.getdetails() 
 x.getMarks() 
 x.display()
