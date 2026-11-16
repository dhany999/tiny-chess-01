# v26r: v20 search + set-D book (g6+g7), no contempt.
import zlib as z,base64 as b6
PL=(
"c-nPW=~n8>68`T~u#W;A((z;>454uwzzI==hzbieBXbgxFe&b5zugI<p0)21LsMN{bA4SI%{<o+6XU>j5?YWLLpOj6e>xrM$G$aRSV2h03#e;>C5iF{a)aZ66<W>`{L?tC*Us*5UTQa;m;2WBKh!~^gILJ1EadYn6nGYjxdJTk1<1<HHi~5&>-nr{8Lnx8f9&S?jE^2E"
"tJwkQjLBRNozmN7a6Ye@T{)xI#uR&g`S3dZ_!wSI5c5>GLdwV~(z>G#F6!!LY8Aeu)H!feGB~4pWVN>2<zUfe+>wj8%n^9wemg>vn|klM`DlF{jaIYnt@zd*m2`EQN8^XbvU}*+uhrS)!ZuUQZsqNy)u`Xw)5qkIZ0Vr35ZlyKb8Q%uY_C{xyK?SZhgD}axOyJjho$5s"
"wI~e6^z!C)cyctLr`p?})o|JsJyRSCp_VdljJZP<F8wQ{<=5P~Xs*SzH=G*n#X|^^hpK%i<+Z8A*xbW)sVeKan?le^D%ah|%gm{DdpS+scAl35q2oU;>X!fRiZ~<=I2<Z>=9tmN>Xa7N1#2^?xJRQaP_ezr%bj!Yr`lNg)U&oq_|yqog_c&iRxZ?ylB;Q^lKg1Dq0G8-"
"3ltTn@a`{Z;_r^yJfQP8Cv3xSJRWXOF2pBbE4;YQGo{&-Th+wD^>*7}8m6p(>R>62J118{z0=N%^8H!$q2gXNbboQn<PYn7?q+bV{NX`zaqj}aF$0tSb){U~c5?Pme7fSM$-B((NxZ#QTftMOsy1_S{k3_t6|?o$&97CE%nye{<F=kzFJ(<)Mq447wcPRhMjdCAkK6Li"
"MTzb3i?&o|S>ttkcfUz7zwh&Z&YH${s3g@uVt9T1#&>z<X?|v0d7e5@Z`hOD(qtv9ctjhG>PN|ChJMg7Hx;|{S`ePHZ1euPGemy9=KTJH9xK0IF7ma@i?;CaK0Q~jor?72EJoue?sD=P{u;1P+~c!zhh~GEE~^(Mx67H=Z|WxR+I;isJ`c_m)%d+u@+Z3D58bm_c&)J#"
"TDh&(2_Kw{FI;3SS5l+1oweRMv+7)2y=>g%W6-U>Tdxnn#`(z6dA6z4s&8*+?e(&9xOp6*!!z|nUChtf++8Lm=?g}^oekgKCx@%CQjzBDM7-X-Pu$d!&T@J)=gglJZ}AI-?jJsT_TqY)l00?WkEvP!nuFofEjtc{!?Uelxl%<T7<pTIAsdJ2L3q8?*s|}0w}tuhdoAma"
"PS$1_gqyJJmjz*aSI)0)D{i+yJq{0*)O^ccUq9Rn3rj!LU+!0(q}b&zj;`Lif_~`-?>zWLtBvzZ!#;H$pYqhHc{qFt%~yrzOSRFnHWVcHvRXCiyOZ2+rulyN)SPcBckP!==Kkn+{drpAeU)x`C+{2KwDw#pEUJGl3V#;P;WO<!ft`G1If382CBa$i6<2u`z2Egl#Sty^"
"i+Di`c$w|nuAdksMoz-loPh;cIJF#bN5L%haZs-!Mi3w)aFF5h_+NzNlZTif2(p5=xf~{EA^GIw79mKO0P&wBpI4DmrCZg5Y868y3+q*=RAH+M&&fxwG|)R+<OC=dIUeSUL^Q`2bNDG01^g@&Iqu^?Rnhy0+*VPqFLx1VNpk%f_1J!<P>|IIVh>EqPIQ0=1FASjnjQd;"
"lGi9m<>U<t%4Ja=BaoGtd}c$h;U<%(bIh9Rc_p?l`&PK{9nk3X=6xE>OHx8}%tW)@n`b1E9y5~IXE;7j;k|N}>@nF)JK?w?37A4<7(n!`8G)k7VuKe{Mx-*pE3*mLXE-Xd?i2)2-%!Pa1c~;99F78p35gH|%p{|4@N#5FqQev?#D*xnu#b?wDaLjtxLANm1k|had37g%"
"Hvj)=z|$Z)a9)i}`@6KCqE^Gv)cTJ!@{33;hBW%W>P8O8Vhs=oJEg5EMO0GXbnaGh-p+yHk+{s3B)xA)iEXl>M^0PLVrKbTXn{AvM09$Yc8Mz*t`m-&g@tL_F6HsIh7d<M6DH!Mj3;|O0yb^pDxk1!EX)zUNCinD*@E~V7c73#T%;tD6S?(WO(L;GZ`i{<148%+aU3jh"
"rW1x&_I&E+32TZOmr-z*8C(&6*$sbviOIx8L&6%%#5!u!e`Jyn_{G_hMm>8QmP)zpyj0@E$fY@PDGNm?K%VOFlmu4n6b|vR=6M#@6d$Bw@=ssvU8FcDQJ-1IZqsJJ_~Sfn?j-CL>`SRy?P>j3XNc_RdtXl=EFyfCilQ6q{}xta3ywnRXB0?*{D0dc7A+|v#20nn(k2Iq"
"&qDaBTf>W$Mcrq^NeKNY{UVegM?w6}<A_0kfd|7*9*X<52=lw5NQAhQCN@0@sek|F_xf#wCU&H#lEOlF8o?=Mg-n~;o`TTdEwEa$!0!5e{G5dGli~W`9h}(P$<D=Hr_7d7t2Drjm@=5Ux;9O;VFlJ;tpn@LgG5{XJPni#2fyuQI0{d0XqMvmoE)NAxtxoZxG(UU6J-x6"
"J-aV25oup}fkOGKp?3WgIYnx5AJ1hGGcr+wk%NoAOdc4D6V4oYe#Rq7@#I>EMjhbHVMs9qplyl)aXWOt5-upr#9}qX0L01>TsiZDAK4?Ogp5s*^iEKi%9SM9w{Z<|jF6egen{+~dAwA5e%OcjiG@W^Jb%Xq#5;au#BOcxy_1UdW^@;z@BpU}RT^Z}2R6RZsMPL9NPfsQ"
"f+SJ$e+1^!!ZIgC&A@PS8!_!DWe?!*8H0+fe9scX3G`eK#J5EYm{5Z{^rqiV-&CR6IKW>t;v(B`s^x+u7JY3LSc$r|srkO^M>}STkv{RZ*2%PK4ku=0pi_WdZDUtS8OkP&Mn(phWs-swGE1@8Rq+ekM@Cfo8k%WqpuwFi>a)YjNdHu$W7;f0=O8|YSw3+gvPalg&d7+C"
"J5hLYU^C`7IeT*x69mGAH?@F5L2NC)=v6gJ#)Oh1O~eko=mCbeqzsrLq&6rfYh|N#{krE(`xJw3c9I~a_gVRUs-NK``is6JGI^H8CrM9Ga7GcNm=QFa1%0gVIKVHAI6aBLKulNGXUHMdPPks+j*ocj;Oxi-`lc=p!Ro&OF!qE<<yTO4h8a|!=2^C+eMf(S0I|F{m1UgD"
"HdVw`CV%4!5Q8g-;TYhQ<G`C`eh*9rX-%9V3NkumG+bo(+LIr^PH<2Tj3Rb2AU@6xzLFn&Ua%xvy9yxkRuM!~#W>*6k;D#%qiWhE)|)b2LKuBHuFs+(NoWx#)`=tg7xst;$68f;lRnaCyO|9ih??b|pyFQuZob2}m^+;`k|z02CqW@c13Q(&5FcH3GzSSKj3{AD!Si0)"
"(fxV4H)r@hwqqWdkxs`A+61#DRa_zr+LjZ&EfS1f_PD6DmUuR0@_7zhv+M~w5+9SWRm+}O?2{Piv5I4RL@xiH*r#Zo1e5*r@caE9=~Xd?>ibb@d^~kE6D*Dw{?x_b4=!jAj*rd7%nN`{?M<U%qtC$LC!G91po4^IVTe+D#eS3y@)Dq`R9V6hgB#D7TAEL4q>g&zvJ_wz"
"U!8c&fFj0zRHw;2o~KC!^3giS(>-SY3qP54)Gh01bnVAf43wN)L0lGND~8Ql2j2o14144~K<dZsHCvJsgI;>(F0CNlFE&6Fer(GURU<?IZ^wpj2t3d?p%s9hN9UrW(FmzvT^Le`r!>B3@#G=paycFY`f=#K#3uxp)<=Uh6<-R=sFBgg36E{xo$Yv*J06^9CnX88O(R@B"
"La8L+JUivGM2L7a4r3w~u}jnaZe-cwb}Vx|uC8caBke<e$MwCRY6zk=!J68~3VS}a2HNyx=YL<m!7o!$cLq3!-$wZO{SCjE@zKN*`kNhkGu_Ym>>E<WXd-`t1!TGe4fas50|Tw7eL+Fu69*^O1~=mI%Zp>ZyhKCb+OWKEe+zvMV*3c_7`LJs5Dbb)1?hhW+RRGB_YaEd"
"rGrol7ud63C~dlqmB!Y^^WxxZ525tNUHDND(#1g}BU;1vbR?^YnWIG?reh{j?;q5`{{Y@`$gK"
)
exec(z.decompress(b6.b85decode(PL)))
