p,i,t,j=print,input,True,'123456789'
def d(g):
 for b in range(6,-1,-3):
  if b<6:p('-'*11)
  r=' | '.join(g[b:b+3]);p(' '+r)
def k(n,g):
 r=n//3*3;c=n%3
 for m in g[r:r+3],g[c::3],g[0::4],g[2::2]:
  if m.count(g[n])==3:return t   
 return False
def x(s,g):
 while t:
  n=i(s+' where? ')
  if n.isnumeric():
   n=int(n)-1
   if -1<n<9 and g[n] in j:return n
  p('nope')
def y():
 g=list(j);c=o=0;d(g)  
 while not o:
  s='XO'[c%2];l=x(s,g);g[l]=s;o=k(l,g);p();d(g);c+=1  
  if o:p(s+' wins')
  elif c==9:p('tie');o=t
p('tic tac toe\n');r=t

while r:
 y();r=i('again? (y/n) ')=='y'
p('bye')
