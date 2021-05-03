class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
count = 0
def doEvaluation(stack,operator,count):

     a = stack.pop()
     b = stack.pop()
     

     print('LD ',b)

     if(operator == "+"):
          print('AD ',a)
     elif(operator == "-"):
          print('SB ',a)
     elif(operator == "*"):
          print("ML ",a)
     else:
          print('DV ',a)

     
     
     strCount = str(count)
     result = ('Temp'+strCount)
     print('ST ',result)
     stack.push(result)

def postfix(expression):
     

     operands_Stack = Stack()#creates a stack to store the operands
     expAsList = expression.split()#stores all operands and operators in the 
        #expression in a list
     count = 0
     for a in expAsList:
          if a not in ['+','-','*','/']:
               
               operands_Stack.push(a)
          else:
               
               count+=1
               doEvaluation(operands_Stack,a,count)
                   
     
               
        
exp = input("Please enter postfix expression\n")
postfix(exp)
