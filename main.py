#v8:90k LMR+tempo BP
import json as j,os,urllib.request as u,base64;H=os.getenv("MAKEFUN_ENV_URL")
MV=0,100,280,320,479,929,0;PS=base64.b85decode("fPjF2fPjF2&ePV(=F-*Lhn<zIsGqEdZ;*bEj)0GIW`l}}hJk=-YKet)c7B6xVTgHKTyle9fPjF2fPjF2K1($<c1cD$eR||vguZ-oio=1*$(z1@n3%1lp{bdXe}$iwmZO4zZi<bTl8=jWX>o#pf`DmkHfd&PZCz?RMKUflX%$;eb(Eu4S)YPxcc);fw04|wnUR#DnwgJ^jf#<%k&u9gj+vN`h?$g+laz~whlZ4pd4h3ta&dNcqn)9IrJ=a8x1G4dx4xphlcSuWt(%#TfQ68al6-f1WL<D;b7N9sR%BLZXI*AeOIl%OV^vg3VrXuKer{o4hJkn(#hBQdj-b4Dl+3x9eygCo$iJ(CfpC_QnUr&Sa&dlpe|BtYVtR9RaCLBHTyB7EadB%}Sz=*xVO(BT")
KD=-33,-31,-18,-14,14,18,31,33;BD=-17,-15,15,17;RD=-16,-1,1,16;GD=BD+RD
DD=0,0,KD,BD,RD,GD,GD;CM={0:13,4:12,7:14,112:7,116:3,119:11}
TT={};ST=[];Z=1e6;KL=[0]*99;TM=0
def V(p,s):a=abs(p);f=s&7;r=s>>4;i=(56-8*r+f,r*8+7-f)[p<0];return(MV[a]+(a<6 and PS[a*64+i-64]-128))*(p>0 or-1)
def A(s,by):
 for o in 15,17:
  t=s-o*by
  if not t&136 and B[t]==by:return 1
 for d in KD+GD:
  t=s+d
  if not t&136 and B[t]==(2+(d in GD)*4)*by:return 1
 for d in GD:
  t=s+d
  while not t&136 and not B[t]:t+=d
  if not t&136 and B[t]in(5*by,(3+(d in RD))*by):return 1
 return 0
def G(cp):
 ms=[];b=B
 for f,p in enumerate(b):
  if p*S<1:continue
  a=abs(p)
  if a==1:
   d=16*p;pr=(f+d)>>4 in(0,7)
   for t in(f+d,f+d-1,f+d+1):
    if t&136:continue
    v=b[t]
    if t==f+d and(v or cp and not pr):continue
    elif v and v*p>0:continue
    elif t!=f+d and(v*p>0 or not v and t!=E):continue
    if pr:ms+=[f|t<<7|q<<14 for q in(5,4,3,2)]
    else:
     ms.append(f|t<<7)
     if t==f+d and f>>4 in(1,6)and not b[t+d]:ms.append(f|t+d<<7)
  else:
   for d in DD[a]:
    t=f
    while 1:
     t+=d
     if t&136:break
     v=b[t]
     if v*p<0 or not v and not cp:ms.append(f|t<<7)
     if v or a%4==2:break
   if a==6 and not cp:
    for kf,kt,rt in(4,6,1),(4,2,2),(116,118,4),(116,114,8):
     tr=(kf+kt)//2
     if f==kf and C&rt and not(A(kf,-S)or A(tr,-S)or A(kt,-S))and not(b[tr]|b[kt]|b[kt-1]):ms.append(kf|kt<<7)
 return ms
def M(m):
 global S,C,E,EV,KP,BP
 ST.append((B*1,S,C,E,EV,KP*1,BP));f=m&127;t=m>>7&127;pr=m>>14;p=B[f];v=B[t];w=t;a=abs(p)
 if a==1 and t==E and not v:w=t-16*p;v=B[w];B[w]=0
 np=pr*p if pr else p;EV+=V(np,t)-V(p,f)-(V(v,w)if v else 0)
 B[f]=0;B[t]=np
 if a==6 and abs(t-f)==2:rf=t+1-3*(t&7<6);rt=t-1+2*(t&7<6);B[rt],B[rf]=B[rf],0;EV+=V(B[rt],rt)-V(B[rt],rf)
 if a==6:KP[p<0]=t
 if 3 in(v,-v,pr):o=BP;BP=30*((B.count(3)>1)-(B.count(-3)>1));EV+=BP-o
 C&=CM.get(f,15)&CM.get(t,15);E=(f+t)//2 if a==1 and abs(t-f)>16 else-1;S=-S
def W():
 global S,C,E,EV,KP,BP,B;B,S,C,E,EV,KP,BP=ST.pop()
def R(d,a,b,pl):
 global ND,TM
 ND+=1
 if ND>9e4:raise KeyError
 if d<-6:return EV*S+10
 ic=A(KP[S<0],-S);d+=ic*(d>0)
 w=d<1
 if w:
  if not ic:
   if EV*S+10>=b:return b
   a=max(a,EV*S+10)
  ms=G(not ic)
 else:k=(tuple(B),S);TM=TT.get(k);ms=G(0)
 ms=[(-2e6*(m==TM)-5e5*(m==KL[pl])-MV[abs(B[m>>7&127])]*16+MV[abs(B[m&127])]-800*(m>>14),m)for m in ms];ms.sort()
 sc=-Z;bm=0;n=0
 for _,m in ms:
  n+=1;c=B[m>>7&127];M(m)
  if A(KP[S>0],S):W();continue
  s=-R(d-1-(n>3 and d>2 and not c and not ic),-b,-a,pl+1);W()
  if s>sc:sc=s;bm=m
  a=max(a,s)
  if a>=b:
   if not(w or c):KL[pl]=m
   break
 if w:return pl-Z if ic and not bm else a
 if sc==-Z:return pl-Z if ic else 0
 TT[k]=bm;return sc
def U(m):f=m&127;t=m>>7&127;q=m>>14;return'%c%d%c%d'%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1)+(q and'nbrq'[q-2]or'')
def P(mv):v=mv.encode();f=v[1]*16+v[0]-881;t=v[3]*16+v[2]-881;q=b'nbrq'.find(v[4])+2 if mv[4:]else 0;return f|t<<7|q<<14
def F(g):
 global ND,B,S,C,E,EV,KP,BP
 del ST[:]
 if len(TT)>6e4:TT.clear()
 K=[4,2,3,5,6,3,2,4];B=K+[0]*8+[1]*8+[0]*72+[-1]*8+[0]*8+[-x for x in K]+[0]*8;S=1;C=15;E=-1;EV=0;KP=[4,116];BP=0
 for mv in g['moves']:M(P(mv))
 ms=[P(x)for x in g['legal_moves']];ND=0;bm=ms[0]
 for d in range(1,32):
  try:
   a=-Z
   for m in ms:
    M(m);s=-R(d-1,-Z,-a,1);W()
    if s>a:a=s;bm=m
   ms.sort(key=bm.__ne__)
  except KeyError:break
 return U(bm)
def T(p,b):return j.load(u.urlopen(H+p,j.dumps(b).encode()))
while(g:=T('/game',{}))['status']!='done':
 while g['status']=='your_move':g=T('/move',{'game':g['game'],'move':F(g)})
