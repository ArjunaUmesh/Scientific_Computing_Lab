
import sympy as sp
a,b,c,x,y,z=sp.symbols('a,b,c,x,y,z')
def quadraticInterpolation(p0,p1,p2,t):
    
    expr= a + b*(x-p1[0]) + c*(x-p0[0])*(x-p1[0])
    print('f(x) : ',expr)
    
    b0=p0[1]
    expr=expr.replace(a,b0)
    
    b1=(p1[1]-p0[1])/(p1[0]-p0[0])
    expr=expr.replace(b,b1)
    
    b2=((p2[1]-p1[1])/(p2[0]-p1[0])-b1)/(p2[0]-p0[0])
    expr=expr.replace(c,b2)
    
    print('b0={},b1={},b2={}'.format(b0,b1,b2))
    
    print('f(x) : ',expr)
    print('f({}) : {} '.format(t,expr.replace(x,t)))
    print('')

p00=[1,0]
p01=[4,1.386294]
p02=[6,1.791759]
a0=2.75

p10=[0,659]
p11=[2,705]
p12=[3,729]
a1=2.75

p20=[0,4]
p21=[1,3]
p22=[4,24]
a2=2.8';
.]'

p30=[93,11.38]
p31=[96.2,12.80]
p32=[100,14.70]
a3=94.5


quadraticInterpolation(p00, p01, p02, a0)

quadraticInterpolation(p10, p11, p12, a1)

quadraticInterpolation(p20, p21, p22, a2)

quadraticInterpolation(p30, p31, p32, a3)