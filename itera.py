#牛顿迭代法求解开n次方

def nthroot(n,a):  #
    err=1e-10
    if n<1 and n%2==0 and a<0:return False
    xk=a/n
    xk1=xk*(1-1/n)+a/(n*(xk**(n-1)))
    print('xk1={}:fx={}'.format(xk1,xk1**n))
    i=1
    while(abs(xk1-xk)>err and i<100):
        xk=xk1
        xk1=xk*(1-1/n)+a/(n*(xk**(n-1)))
        i=i+1
        print('xk1={}:fx={}'.format(xk1,xk1**n))
    print('iterate number:{}'.format(i))
    return xk1

n=3
a=50000000000
print('x=',nthroot(n,a))