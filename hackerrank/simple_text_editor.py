# What I learned 
# 1) use prev_stack to record the previous commands ( actually status of commands)

# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
stack = []
prev_stack = [] 
prev_stack.append(stack)
#edge : delete/print no letters 
#edge :  nothing to undo

for i in range(num): 
    op = input() 
    cmd = op.split()
    if cmd[0] == '4':
        if len(prev_stack)==0: 
            continue
            prev='4'
        else: 
            stack = prev_stack.pop()
                # return to prev stack 
    elif cmd[0] == '1': 
        prev_stack.append(stack.copy())
        for s in cmd[1]:
            stack.append(s)
    elif cmd[0] == '2': 
        prev_stack.append(stack.copy())
        for i in range(int(cmd[1])):
            stack.pop() 
    elif cmd[0] == '3':
        if len(stack)==0: 
            pass 
        else: 
            print(stack[int(cmd[1])-1]) 
        
        
    
        
        
            
