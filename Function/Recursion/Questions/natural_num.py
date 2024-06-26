def natural_num(self,n):
    if(n == 0):
        return
    natural_num(n-1)

natural_num(5)