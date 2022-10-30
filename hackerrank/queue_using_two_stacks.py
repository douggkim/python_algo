# What I learned 
# 1) Keep two stacks - one for the most current data , one for reversed stack 
# 2) Only swap stacks when deleting an element
# Enter your code here. Read input from STDIN. Print output to STDOUT
r = input()
in_st = []
out_st = []
for i in range(int(r)): 
    r1 = input()
    cmd_list  = r1.split()
    # if enqueue
    if cmd_list[0] == '1': 
        in_st.append(cmd_list[1])
    elif cmd_list[0]== '2':
        if len(out_st)!=0: 
            out_st.pop() 
        elif len(in_st)!=0: 
            while len(in_st)!=0: 
                out_st.append(in_st.pop())
            out_st.pop() 
        else:
            pass  
    else: 
        if len(out_st)!=0: 
            print(out_st[-1])
        elif len(in_st)!=0:
            print(in_st[0])
        else: 
            print('no queue left')
