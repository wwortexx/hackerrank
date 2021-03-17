# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    data = input().split(' ')
    height = int(data[0])
    width = int(data[1])
    i=0
    _mlist = [ c for c in range(1,height+1) if c%2!=0]
    for h in range(1, height+1):
        if h < int((height+1)/2):
            aux = len('.|.'*(_mlist[h-1]))
            print(
                ('-'*(int((width-aux)/2))).ljust(int((width-aux)/2)) 
                +('.|.'*(_mlist[h-1]))
                +('-'*(int((width-aux)/2))).rjust(int((width-aux)/2))
            )
        elif h == int((height+1)/2):
            print(
                ('-'*(int((width-7)/2))).ljust(int((width-7)/2))
                +('WELCOME')
                +('-'*(int((width-7)/2))).rjust(int((width-7)/2))
            )
        else:
            y = _mlist[-1-h+len(_mlist)]
            aux = len('.|.'*(y))
            print(
                ('-'*(int((width-aux)/2))).ljust(int((width-aux)/2)) 
                +('.|.'*(y))
                +('-'*(int((width-aux)/2))).rjust(int((width-aux)/2))
            )
