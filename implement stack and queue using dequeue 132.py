from collections import deque

stack = deque()
print("1. push element")
print("2. pop element")
print("3. check size of stack")
print("4. display elements of stack")
print("5. exit")
while(True):
  n = int(input("Enter your choice "))
  if(n==1):
      x = input("Enter element")
      stack.append(x)

  elif(n==2):
      print("removed element is : ",stack.pop())

  elif(n==3):
      print("Size of stack is : ", len(stack))

  elif(n==4):
      print(stack)

  elif(n==5):
      exit()
  else:
      print("invalid choice")
      
# queues
q = deque()
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)



