import time
import keyboard
import random


pai=120
# pai=240
# 定义按下每个按键的持续时间（单位为秒）
key_duration = 60/pai/4

# 定义空格连续出现时的停顿时间（单位为秒）
space_duration = 60/pai


duration_sec=0.1



      


def play_string(string1):

    string= string1[0]





    pai=string1[1]

# 定义按下每个按键的持续时间（单位为秒）
    key_duration = 60/pai/4

# 定义空格连续出现时的停顿时间（单位为秒）
    space_duration = 60/pai


    duration_sec=0.1




    duration_sec=0.1
    pause_flag = False
    i = 0
    while i < len(string):
        char = string[i]

        if char.isdigit():
            duration_str = ''
            while i < len(string) and string[i].isdigit():
                duration_str += string[i]
                i += 1
            duration_sec = int(key_duration) / int(duration_str)+1
        
        elif char == ' ':
            time.sleep(key_duration)
            i += 1
            pause_flag = True

        elif char == '[':
            end_index = string.index(']', i)
            sub_string = string[i+1:end_index]
            for single_key in sub_string:
                keyboard.press(single_key)
            time.sleep(10/10000)
            for single_key in sub_string:
                keyboard.release(single_key)
            i = end_index + 1
            time.sleep(key_duration if key_duration!=duration_sec else duration_sec)
            pause_flag = False
        elif char == '\n':
            i += 1
        else:
            if i > 0 and char == string[i-1]:
                time.sleep(random.uniform(0.01, 0.02))
            
            keyboard.press(char)
            
            time.sleep(10/10000)
            print(key_duration if key_duration!=duration_sec else duration_sec)
            keyboard.release(char)
            time.sleep(key_duration if key_duration!=duration_sec else duration_sec)
            i += 1
            pause_flag = False

# music = "wqhq qhq qhqhg wqhq qhq  qewqw ghee ewe ewete eee ewwwwq wew wqhq qhq qhqhg ghet tet tewqq wqwewwqw qhwqqhqqq tteweh wetew tteweg wetwq qwertyteteeww qwqwqqwete"
# music="wqh[qz][b0][qa][hs][qd] [q0][h0][qz][yb][ga][s0][d0][w0][q0][t0][qn][c0][qn][jm][qa] [q0][e0][wn][qc][qn][m0][0a][g0][j0][e0][ev][0z][ev][wb][en] e2"
# # b=" qe[wj][qd][qh]jaghe"

# qhc 青花瓷60
qhc1='''[vw][nq][ah]sd we
[cw][bq][ag]sd we
[xw][nq][sh]d[gq]w h
[ze]bas[dq]w [me]t
[nt]c[ae]s[dw]g[hq]n
[xw][nq][sh]d[gq][dw][se][ne]
[zq]b[aq][sh][dq] qh
[zq][bh][ag]sd w[mq]h
[nq]c[aq][sh][dq] qe
[nw][cq][aq]sdg [bh]e
[ve]a[se][dw][ge] ew
[ve][at]s[de]ge [ve]e
[bw][xw][sw][dw][gw] qe
b[xw]sdg w[bq]h
[zq]b[aq][sh][dq] qh
[zq][bh][ag]sd g[mh]e
[nt]c[at][se][dt] te
[nw][cq][aq]sd w[bq]w
[ve][aw][sw][dq][gw] qh
[bw][xq][sq][dh][gq] qw
z[bq]nasasd
[zqr]b[ae]s[dw] t[bt]e
[vw][ae][sh]d[gw]e[vt]e
b[xw]sdg t[bt]e
[cw][me][sg]d[gw]e[ct]w
n[cq]asd q[bw]e
[vt][ay][st][de][gt]e[ve]w
[bw]xsdg q[bw]q
[zw]b[aq][sw]degt
z[be]asd t[bt]e
[vw][ae][sh]d[gw]e[vt]e
b[xw]sdg t[bt]e
[cw][me][sg]d[gw]e[ct]w
n[cq]asd q[bw]e
[vt][ay][st][de][gt]e[ve]w
[bw]xs[dg][ge] ww
z[bq]nasasd
'''




# 稻香81
daoxiang='''
a g [wt]eq b g [jt] 
n h [qwt] c s [qt] 
x n [qt] b g [qt] 
z b [asgw] q[asgw] qb [asgw] qw
z [be] [st]da b [xw] [sj] [dg]
n [ce] [at] d c [mw] [dj] [mg]
[xq] n a [ng][bq] x s [dg]
[zq] b [asg] a[asg] ab [asg]q[bq]q
[zq] [bh]qd [bq]q[bw]w[sw]w [ge] [sq]
[nq] [ch]qa [dq]q[cw]w[mw]w [de] [mq]
[xq] [nh]qa [nq]q[bw]w[sw]w [gq] [se]
[ze] b [asg] a[asgq] q [bq]q [asgq]q[bq]h
[zq] [bh]qd [bq]q[bw]w[sw]w [ge] [sq]
[nq] [ch]qa [dq]q[cw]w[mw]w [de] [mq]
x nq[aqr] nebw[sw]q[gw]q[se] 
[zq] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt bt bt [st]t [ge] [sw]q
[nq] [ce]e ae de ce [me]e [de] [mq]h
[xh] [nq]qa [nq]q[bw] [sw]w[gq] [se]
[ze] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt bt bt [st]t [ge] [sw]q
[nq] [ce]e ae de ce [me]e [de] [mq]h
[xh] [nq]qa [nq]q[bw] [sw]wg [sq]
[zq] b [asg] a[asg] ab [asg] b
z [be] [st]da b [xw] [sj] [dg]
n [ce] [at] d c [mw] [dj] [mg]
[xq] n a [ng][bq] x s [dg]
[zq] b [asg] a[asg] ab [asg] b
z [be] [st]da b [xw] [sj] [dg]
n [ce] [at] d c [mw] [dj] [mg]
[xq] n a [ng][bq] x s [dg]
[zq] b [asg] a[asg] ab [asg]q[bq]q
[zq] [bq]q[dq]h[bq] [bq]q[sq]q[gq] [sq]
nq[cq]q[aq]q[dq]q[cq]q[mq]q[dq] [mq]
x [nh]q[aq]h[nq]h[bq]q[sh]q gq[sq]q
[zq]q[bq]q[sq]q[adq]            qqq
[zq] [bq]q[dq]q[bq]q[be] [sw] gq[sq]q
[nq]q[cq]q[aq]q[dq]q[ce] [mw] dq[mq]h
[xg] [nq]q aq nh[bq]h[xq]h[sq] [dw]
[zw] [bq] s [bqt] d [bqt] [ae]e[be]e
[zt] [be] [de]e bebe[se]e[ge]e[se]e
[nt] [ce] [ae]e dece[me]e[de]e[me]e
[xt] [ne] ae[ne]e[bq] [sq] gq[sq]q
[zt]e[be] [de]w[bw] [sw]q[bq] [aq]w[be]
[zw] [bq] [dh]q[bq]q[bq]q[sq]q[gq]w[se]
[nw] [cq] [ah]q[dq]q[cq]q[mq]q[dq]w[mq]
x nq[aqr] nebw[sw]q[gw]q[se] 
[zq] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt bt bt [st]t [ge] [sw]q
[nq] [ce]e ae de ce [me]e [de] [mq]h
[xh] [nq]qa [nq]q[bw] [sw]w[gq] [se]
[ze] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt bt bt [st]t [ge] [sw]q
[nq] [ce]e ae de ce [me]e [de] [mq]h
[xh] [nq]qa [nq]q[bw] [sw]w[gw] [sq]
[zq] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt t bt [st]t [ge] wq
[nq] [ce]e ae e ce [me]e [de] qh
[xh] [nq]qa qq[bw] [sw]w[gq] e
[ze] b [asg] a[asg] ab [asge] [bt]
[zt] [bt]t dt bt bt [st]t [ge] [sw]q
[nq] [ce]e ae de ce [me]e [de] [mq]h
[xh] [nq]qa [nq]q[bw] [sw]w[gw] [sq]
[zq] b [asg] a[asg] ab [asg] b
z [be] [st]da b [xw] [sj] [dg]
n [ce] [at] d c [mw] [dj] [mg]
[xq] n a [ng][bq] s [gw] s
[ze] b [asg] a[asg] ab [asg] b
z [be] [st]da b [xw] [sj] [dg]
n [ce] [at] d c [mw] [dj] [mg]
[xq] n a [ng][bq] s [gw] s
[zq] b [af] b [zbad]

'''

# 七里香75
qilixang='''
sdgh
[nq] c [aq] de [vw] [aq] f [ah]qh
[bg] sh[gq] [sw] [ze] b [ms]d[bg]h
[nq] c [aq] de [vw] [aq] f [ah]q
[bw] s [gq] s [bsgj]         g
[nq] c [aj] [dq]q v a f [aq]
[bq] [sj] [gh] [sj]h zgb  m [bg]
[ng] c [af] [cd]gv z n [zg]
[bg] [xh] [ms] [xf]fzdb  m [bg]

[nq] c [aj] [dq]q v a f [aq]
[bq] [sj] [gq] [sw]wzqb [mq] [bj]
[nq] [cq]q ajdj vha  [fh] [aj]h
bgx  [msg] x [bgj]  g q 

[nq] c [ad] [ch] [vh] z [ng] [zw]
[bw] x [md] [xf]fzdb  m [bg]
[ng] [cf] [af] [cd]dvs zs na zd
bsx m [xf] [zd] b [mg] [bq]

[nq] c [ad] [ch] [vh] [zg] [ng] [zw]
[bw] [xd] [md] [xf] [zf] [bdg] [mg] [be]
[ne] [cw] [aw] [dq] [vq] [aw] [fq] [ae]
[be] swg s [bsgj]g q qq
n c a [dq] [vq] [aj] [fh] [ag] 
[bj] [sq] [gw] [sq]qz [bg] [mq] [bq]q
n c a [dq] [vq] [aj] [fh] [ag] 
[bw] [se] [gr] [se]ez [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag]
[bw] [sq] [gj] [sq]qz b m [bq]
[vq] [ae] [fw] [aq] [bq] [sj] [gw] [sq]q
z b d b z [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag] 
[bj] [sq] [gw] [sq]qz [bg] [mq] [bq]q
n c a [dq] [vq] [aj] [fh] [ag] 
[bw] [se] [gr] [se]ez [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag]
[bw] [sq] [gw] [sr]ezqb m [bq]
[vq] [ae] [fw] [aq] [bq] [sj] [gw] [sq]q
z b c b a v b v 
[ne] c [ae] [dw] [be] s [ge] [sw]
[ve] a [dy] [aw] [ve] a [dy] [aw]
[ne] c [ae] [dw] [be] s [ge] [sw]
[ve] a [dy] [aw] [ve] a [dh] j

[nq] [cw] [aj] [dq] [bj] [xh] [md] [xs]
[vh] z n z v z [aj] z
[nq] [cw] [aj] [dq] [bj] [xh] [md] [xs]d
[vh] z n z z [bg] [mq] [bq]q
n c a [dq] [vq] [aj] [fh] [ag] 
[bj] [sq] [gw] [sq]qz [bg] [mq] [bq]q
n c a [dq] [vq] [aj] [fh] [ag] 
[bw] [se] [gr] [se]ez [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag]
[bw] [sq] [gj] [sq]qz b m [bq]
[vq] [ae] [fw] [aq] [bq] [sj] [gw] [sq]q
z b d b z [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag] 
[bj] [sq] [gw] [sq]qz [bg] [mq] [bq]q
n c a [dq] [vq] [aj] [fh] [ag] 
[bw] [se] [gr] [se]ez [bg] [mq] [bq]q

n c a [dq] [vq] [aj] [fh] [ag]
[bw] [sq] [gw] [sr]ezqb m [bq]
[vq] [ae] [fw] [aq] [bq] [sj] [gw] [sq]q
z b c b a v b v 
[nq] c [aq] de [vw] [aq] f [ah]qh
[bg] sh[gq] [sw] [ze] b [ms]d[bg]h
[nq] c [aq] de [vw] [aq] f [ah]q
[bw] s [gq] s [gj]


'''

# 起风了120
qifengle='''
[vj]q[aw]ed te b s g
[cj]q[mw]ed te [nw]e[aq]w[dj]qg
[vj]q[aw]ed te b s g
[cj]q[mw]ed te [ndw]eqw[bsj]qg

[vj]q[aw]ed [at]eb s g s
[cj]q[mw]ed [mt]e [nw]e[aq]w[dj]qg
[vj]q[aw]ed [at]eb s g
[ndwy]ewh dnsdn

[zs] ca[bs] xa[cs]d g d
[zs] ba[xs] ca[bs] dsa n
[cs] xa[cs] ba[ns]d g d
[vs] xd[vs] [ba]s [ns]

[xs] va[ns] va [bs][xd][vg]d
[ns] xd[cs][ba]n 
dsas [va] z [xd]sas [ba] x 
[vd]sas z [ba] x c [na]s [bad]a

[vh] [ag]hd a [bj] [sh]jg s
[cj] [bh]jmdb  [nq] w[aq]j[dh][ag]
[vh] [ag]hd g[ah]g [bh][mg][as][mg]
z [bd] x c [na]s [bad]a
[vh] [ag]hd a [bj] [sh]jg s
[cj] [bh]jmdb  [nq] w[aq]j[dh][ag]
[vh] [ae]e dga [bh] [me]e sgmh
[cnh] c [nm] c [na]

q w [vqe] [ay]td [ay]tb [sy]tgws
[ce] [my]td [my]tn [dy]thed w
[vw] [aq]hd aq [bw] [sq]hgqs
[zqe] b a r[se]w [de]w [bq] w

[vqe] [ay]td [ay]tb [sy]tgws
[ce] [my]td [my]tn [dy]thed w
[vw] [aq]hdea w[bw] [sq]hgqs
[nq] c n m a
h e [vaw] qh e [bsw] qh q q

[vj]q[aw]ed [at]eb s g s
[cj]q[mw]ed [mt]e [nw]e[aq]w[dj]qg
[vj]q[aw]ed [at]eb s g
[ndwy]ewh dnsdn




'''


qingtian='''

n a g a v bng a z b g a a g m g 
n a g a v bng a z b g a a g m g 

n [at] [gt] [aq] [vq] bn[gw] [ae]
z [bt] [gt] [aq] [aq] [gw]e [mw]qg
n [at] [gt] [aq] [vq] bn[gw] [ae]
z [be] g [ae] [ar]e[gw]r [me]w[gq] 

[ng] [aq] [gq] [ae] [vr] [be]n[gw] [aq]w 
[ze] [be] [ge] [ae] [aw]e[gw]q [mq] g 
[ng] [aq] [gq] [ae] [vr] [be]n[gw] [aq]w 
[ze] [be] [ge] [ae] [aw]e[gw]q [mq] gq

nq[aq]q [gj]qaq vq[aq]q [gj]qaq 
zq[bq]q [gj]qaq aq[gq]q [mt]t gt 
nt[at]t [gt]t at vt[at]t [gt]r[ae]we 
z b g a a g [mw]q[gj]q 

[nh] [aj] [gq] [at] [vr] [ae] [gq] [aq] 
z b g a [aq]q[gq]q [me] [gq] 
[nh] [aj] [gq] [at] [vr] [ae] [gq]  aw 
b s g s [bsgj]   
[zd] [bs] [af] [bd] c [ba] [ag] [bj] 
[nq] [cj] [ag] [ca] n [ca] [bh] [mh] 
v [nh] [ag] [ng] b [mg] [sf] [md] 
[zs] [bd] [af] [bd] s b d b 

[cd] b [mg] bg m [bg] [mh] [bj] 
[nw] [cj] [aq] [dq] b c a [dq] 
[vq] [ag] [dg] [ah] [vg] [zf] [ns] [zd] 
[bf] [xg] [mh] [xa] [bh] xj[mj] x 

[zd] [bs] [af] [bd] c [ba] [ag] [bj] 
[nq] [cj] [ag] [ca] n [ca] [bh] [mh] 
v [nh] [ag] [ng] b [mg] [sf] [md] 
[zs] [bd] [af] [bd] s b d b 

[cd] b [mg] bg m [bg] [mh] [bj] 
[nw] [cj] [aq] [dq] b c a [dq] 
[vq] [ag] [dg] [ah] [vg] [zf] [vn] [zm] 
[ba] [xs] [md] xs [xb]  da z b [as] b[as]  [as]b [as] b[as] 
v n [ad] n[ad]  [ad]n [ad] n[ad] 
x n [af] n[af]  [af]n [af] n[af] 
v n [ad] v[bs]  sb s bq 

nq[aq]q [gj]qaq vq[aq]q [gj]qaq 
zq[bq]q [gj]qaq aq[gq]q [mt]t gt 
nt[at]t [gt]t at vt[at]t [gt]r[ae]we 
z b g a a g [mw]q[gj]q 


[nh] [aj] [gq] [at] [vr] [ae] [gq] aq 
z b g a [aq]q[gq]q [me] [gq] 
[nh] [aj] [gq] [at] [vr] [ae] [gq]  aw 
b s [gj] b j s g b [zd] [bs] [af] [bd] c [ba] [ag] [bj] 
[nq] [cj] [ag] [ca] n [ca] [bh] [mh] 
v [nh] [ag] [ng] b [mg] [sf] [md] 
[zs] [bd] [af] [bd] s b d b 

[cd] b [mg] bg m [bg] [mh] [bj] 
[nw] [cj] [aq] [dq] b c a [dq] 
[vq] [ag] [dg] [ah] [vg] [zf] [ns] [zd] 
[bf] [xg] [mh] [xa] [bh] xj[mj] x 

[zd] [bs] [af] [bd] c [ba] [ag] [bj] 
[nq] [cj] [ag] [ca] n [ca] [bh] [mh] 
v [nh] [ag] [ng] b [mg] [sf] [md] 
[zs] [bd] [af] [bd] s b d b 

[cd] b [mg] bg m [bg] [mh] [bj] 
[nw] [cj] [aq] [dq] b c a [dq] 
[vq] [ag] [dg] [ah] [vg] [zf] [vn] [zm] 
[ba] [xs] [md] xs [xb]  da 

[zq]q[bq] [aq]qb [sq]q[bq]q dq[bq]q 
vq[aq]q sq[aq]q [dq]q[aq]q g [aq]q 
[xq] [nq] [sq]q[nq]q [dq]q[nq]q g [nq]q 
[vq]q[aq]q gq[aq]q [bq]q[sq]q [gq]q sq 

[zq]q[bq] [aq]q[bq] [sq]q[bq]q dq[bq]q 
vq[aq]q sq[aq]q [dq]q[aq]q  gq[aq]q 
[xq] [nq] [sq]qn [dq]q[nq]q  gq[nq]q 
[vq]q[aq]q [gq]q[aq]q [bq]q[sq] g s 


'''

#暗号
anhao='''

asdg
[cnh] gn[nah] g [xbmh] jm[msh] g 
[zbh] gb[adh] g [zbh] gb[bad] g 
[cnh] gn[nah] g [xbmh] jm[msh] g 
[zbh] gb[adh] g [zb] adg


[zg] [bd]g[sg] dg[ag]dda [ba]adg 
[ng] [cd]g[ag] dg[ng]dda [ca]adg 
[vg] [nd]g[ag] dg[nah]hhg [vg]gg 
[bh]h[xh]h [mh]gg [bsg]eer [xbe]qq 

[zg]d[bd] [ad]gg [ag]dda [ba]adg 
[ng] [cd]g [ag] dg[ng]dda [ca]adg 
[vg] [nd]g[ag] dg[nah]hhh [vh] g 
[bh]h[xh]h [mh]ggh [bsg]j h[xbh]ghj 

[cq] [mq]qsjmh cgm sg[md]f 
[ng] [cd]dnjaw dqa n [ch]q
[xw] [nh]q[aw] [nh]q[se]e[ne]w [aw] [nq]w
[be] [xq]w[se] [ge] [bse]w [xb]  

[cq] [mq]qsjmh cgm sg[md]f 
[ng] [cd]dnjaw dqa n [ch]q
[xw] [nh]q[aw] [nh]q[se]e[ne]w [aw] [nq]w
[be] [xq]w[se] [ge] [bse]w [xb]  
[za] [bs]dagb [dg] [bf]dafb 
[nd] [cs]daqdq n c [ad] c 
[vd] [ns]dawnw s n d [nq]w
[be] [se]egr[sw]w b s b [xb] 

[za] [bs]dagb [dg] [bf]dafb 
[nd] [cs]daqdq n c [ad] c 
[vd] [ns]dawnw s n d [nq]w
[be] [xe]esege [bs] wq[xb]j j
[zq]bas a zbas ab
zbas a zbas [zb] 
[za] [bs]dagb [dg] [bf]dafb 
[nd] [cs]daqdq n c [ad] c 
[vd] [ns]dawnw s n d [nq]w
[be] [se]egr[sw]w b s b [xb] 

[za] [bs]dagb [dg] [bf]dafb 
[nd] [cs]daqdq n c [ad] c 
[vd] [ns]dawnw s n d [nq]w
[be] [xe]esege [bs] wq[xb]j j

[nq] c [ah] [dg] [bmh] [cj] [msh] [mg] 
[zh] [bg] [ah] [bg] [dh] [bg] [ad] [bg] 
[nh] [cg] [ah] [dg] [bmh] [cj] [msh] [mg] 
[zh] [bg] [ah] [bg] b        

[zg]d[bd] [ad]gg [ag]dda [ba]adg 
[ng] [cd]g [ag] dg[ng]dda [ca]adg 
[vg] [nd]g[ag] dg[nah]hhh [vh] g 
[bh]h[xh]h [mh]ggh [bsg]j h[xbh]ghj


'''
# 发如雪
frx='''
[zb] ghq e[ba][baw] ew q 
[zb] ghq e[ba][baw] t[bae] [bq] 

[zw] [be]ed b [mw] [be]tsebw 
[nw] [ce]eg a [bw] [se]ygtse 
vwqa g ah[cq] [aw]wg [ah]q 
xwn d nh [bsq] we[xb]wb 

[zw] [be]ed b [mw] [be]tsebw 
[nw] [ce]eg aw[bw] [se]ygtse 
vwq a g ah[cq] [aw]wg [ah]q
x [nw]wd n [bsq] we[xb]wbq 

v a [dh]q[ah]q g [ah]qd [aw]q
c b [ah]q[dh]q g [dh]qaebq 
x n [se] [ne] [de] [ny] [st] [ne]e
bwx [sg] b [bs] g [xbw] ee

z [bw]ed [bt]ymtb [sq] [bw] 
[ne] [cy]t[adt] [ce]tb x [sg] [bt]y
[vdq] ay[gy]t[at]e [ce] [at]eg [aq]w
[xe] [nq]hdenw [bw] [sg] [xbw] ee 

z [bw]ed [bt]ymtb [sq] [bw] 
[ne] [cy]t[adt] [ce]tb x [sg] [bt]y
[vdq] ay[gy]t[at]e [ce] [at]eg aq 
[xh] [ne]wd nq[bsq] h [xbq] ww

[zq]qq[bg] [dq]qq[bq]g mq[bq]q [sq]e[bw]q 
n qq[cg] [adq] qq[cq] g bg[xg]g [sg]g[bw]q 
[vg]gg[aq] [dg]gg[ag]q cg[ag]g [dg]g[aw]q 
2xg[nq] [dg]g[ng]w [bs] g [xbw] ee 

1z [bw]ed [bt]ymtb [sq] [bw] 
[ne] [cy]t[adt] [ce]tb x [sg] [bt]y
[vdq] ay[gy]t[at]e [ce] [at]eg [aq]w
[xe] [nq]hdenw [bw] [sg] [xbw] ee

z [bw]ed [bt]ymtb [sq] [bw] 
[ne] [cy]t[adt] [ce]tb x [sgw] [be] 
[vw]qa gyat [ce] [at]e g aq
[xh] [ne]wd nq[bsq] h [xbq] ww

zq[be]w [de] [be]w[me] [be]w[se]t[be] 
n [ce]w[ade] [ce]w[be] [xq]w[sge] [bq] 
v [aq]w[de] [ah]g[cg] ah[dq] [aw] 
[xe] [ne]w[de]t[nq]w [be] [se]w[xbe]qq 

z [be]w[de] [be]w[me] [be]w[se]t[be] 
n [ce]w[ade] [ce]w[be] [xq]w[sge] [bq] 
v [aq]w[ge] [ah]g[cg] ah[gq] [aw] 
[xe] [ne]w[de]t[nq]w [bse] ew[xbe]qq [zbad] [bad] [zbaf] [baf] b[zaf]
[zbad] [bad] [zbaf] [baf] b[zaf]

'''
gyz='''

wjqh  wjqh wjqh wjqh
[vaw]jqh [bsw]jqh [ndw]jqh [bsw]jqh

[vaw][va] [vaj][va] [vaq][va] [vah][va]
[bsw][bs] [bsj][bs] [bsq][bs] [bsh][bs]
[ndw][nd] [ndj][nd] [ndq][nd] [ndh][nd]
[bsw][bs] [bsj][bs] [bsq][bs] [bsh][bs]

[nde] d d d d d dq[mw]q
[ade] d d d d d q[dw]q[dw]e
[vdh] dq[dh] dq[dh] dq[dw][dq]
[bdj] d d d d d dsas

[nde] d d d d d dq[mw]q
[ade] d d d d d q[dw]q[dw]e
[vdh] dq[dh] dq[dh] dq[de][dw]
[bdj] d d d d d dsas

[vah]q[dy] dy[dy]t [dy] 
[dy]t[bsy]t[dy]t 
[na]ed d d d d d [dh]q[vay]
dy[dy]t[dy]t [bsu] dy[du]y[du]y
[na]ed d d d d de[dt]e
[vaw] de[dw] de[bsw] de[dt]e[dt]e
[naw] de[dw] de[bsw] d d [dq]w
[vae] [dh] [dq] [de] [bsw] de[dw] [dq]
[cnh]cnsdhqe[qey]

hj[vq]w[nj]q [adq] [vq]j
[bq]w[mj]q [sgq] [bq]w
[nqe]w[aqe]w[dhqe] [nqe]w
[bqe] [mqt] [sgqe] [bh]j

[vq]w[nj]q [adq] [vq]j
[bq]w[mj]q [sgq] [bq]w
[nqe]w[aqe]w[dhqe] [nqe]w
[bqe] [mqt] [sgqe] [bqt]

[ve]nat[ade] vt[be][mt][sy]e [sgt]
[bt] [ne]adt[dhe] nt[be][mt][sy]e [sgt]
[bt]t [ve]n[aw] [adw] [vq]e
bm[sw] [sgw] [bq]h 
nc[ad] [adq] [adj] [bh]msdgwet
e w w qe w wqqq

[vhw] j q h [bw] j q h
[nw] j q h [bw] j q h
[vw] j q h [bw] j q h
[nw] j q h [bw] j q

hg[vh] ng[ah]g[nh]g
[bh] mg[sh]g[mh]g
ndc n m a m n
[bh]g [vh] ng[ah]g[nh]g
[bj] mh[sj]h[mj]h
ndc n m a


ete [vw] ne[adw] ve[bw] me[sgt]e[bt]e
[nw] ae[dhw] ne[bw] m [sg] [ba]s
[vad] [vah] [vaq] [vae] 
[bsw] [bs]e [bsw] [bsq]
[nadh]cnsdhqe [qey]eqhdn

hj[vq]w[nj]q [adq] [vq]j
[bq]w[mj]q [sgq] [bq]w
[nqe]w[aqe]w[dhqe] [nqe]w
[bqe] [mqt] [sgqe] [bh]j

hj[vq]w[nj]q [adq] [vq]j
[bq]w[mj]q [sgq] [bq]w
[nqe]w[aqe]w[dhqe] [nqe]w
[bqe] [mqt] [sgqe] [bqt]

[ve]nat[ade] vt[be][mt][sy]e [sgt]
[bt] [ne]adt[dhe] nt[be][mt][sy]e [sgt]
[bt]t [ve]n[aw] [adw] [vq]e
bm[sw] [sgw] [bq]h 
nc[ad] [adq] [adj] [bh]msdgwet
e w w qe w wqqq

[vhw] j q h [bw] j q h
[nw] j q h [bw] j q h
[vw] j q h [bw] j q h
[nw] j q h [bw] j q



'''


# 阳光快乐大男孩D
yianguangkuaileidananhai='''



q  j h 
[cng]h [nad]  [nad]  [nad]  [nad]  
[cn]  [nad]  [nadt]tt[nad]r [nade] w 
[xne]  [nadh]  [nad]  [nad]  [nad] w 
[cmj]  [ms]  [msw]ww[ms]q [msq] j 



[cn] hh[nah] h [nah] hh[nah] d 
[na] hh[nag] h [nah] h [nah] e 
[xnh] hh[vns] h [vnse] e [vnse] h 
[cmd] gg[bm] gd[bmg] g [bmg] h 

[cne] hh[nah]hhh [nah] h [nah] d 
[na] hh[nah] h [nae] e [nae] h 
[xnh]hh [vnsh] h [vnse] hh[vnsh] h 
[cmg]g g[mdg] gg[mdh] h [mdq] h 

[zvh]hhh [vnah] h [vnah]hh [vnah] h 
[xbh] g [bmsg] h [bmse]  h[bms] e 
[cnh]hhh [nadh] hh[nade] h [nadh] h 
[zbg]  g[bad] d [badg]  h[bad] e 

[zvh]hh[vnah] h [vnah]hh[vna]d [vnah] h 
[xbh] h[bms]g [bmsh] e[bms]h [bms] ee
[cne]ee[nade] ee[nade]e e[nade]ee [nade]eee 
[cme]eee eeee e e [cme] e 



[cny] t [nady] t[cny]   [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cme] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe][bmse] [xbe] 
[zvy] we[vnah] h[zv]  [zve] [vnae] [zvw] 
[cme] e [bmdt] e[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zve] [vnae] [zve] 
[cmg] h [bmdq] h[cm]  [cme] [bmde] [cmg] 



[cnah] hgh h   h h g 
h h h h e e [cne] e 
[xnw] qw[vns] w w [xnw] [vnsw] [xnw] 
[cmg] hg[bmd]hh h [cme] [bmde] [cme]e

[cne] g [nadh] h   [cne] [nade] [cng] 
[cnh] g [nadh] t e [cne] [nade] [cne] 
[xnw] qw[vns] w   [xnw] [vnsw] [xnw] 
[cmh] gh[bmd]hq h [cme] [bmdw] [cme] 

[zvh]gq [vnah]  [zv]  [zve] [vnae]e[zve]e 
[xbe] e [bmse] h[xb]e [xbe] [bmse]w[xbe] 
[cnh]hqh [nadh]  [cn]  [cne] [nade]e[cne]e 
[zbe] e [bade] e[zb]e [zbh] [bade] [zbe] 

[zve] e[vnae]e [vnae]wt[vna]e [vnae] e 
[xbe] e[bms]e [bmse] h[bms]  [bmse] h 
[cne]ee[nade] ee[nade]e e[nade]ee [nade]eee 
[cme]eee eeee e e [cme] e 



[cny] t [nady] t[cny]   [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cme] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe][bmse] [xbe] 
[zvy] we[vnah] h[zv]  [zve] [vnae] [zvw] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zve] [vnae] [zve] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 



[cnae] ewe h   q q q 
q hq qh e e e e 
[xvnw] www q w w   q 
[cmg] h h q [cnah]  e e 

[cne] ew[cnt] e [cne]eew [cne] h 
[cnq] qq[cn]qte [cne] ew[cne] e 
[xnw] qw[xn] w [xne] w [xne] w 
[cmw] ww wq w [cm] [ce] e 

 
[cny] t [nady] t[cny]   [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnae] h[zv]  [zvh] [vnah] [zvh] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe][bmse] [xbe] 
[zvy] we[vnah] h[zv]  [zve] [vnae] [zvw] 
[cmg] h [bmdq] h[cm]  [cm] [bmde] [cme] 

[cny] t [nady] t[cny]  [cn] [nade] [cne] 
[xby] t [bmsy] t[xby]  [xbe] [bmsw] [xbq] 
[zvw] w [vnaw] e[zv]  [zvh] [vnah] [zvh] 
[cng] h [nadq] h[cn]h [cn] [nad] [cn] 

'''
# 偏爱
pianai='''


[nq]cdj gqt[vt]za[fh]  [aq]w
[bw] s [gt] s j   qjgd 
[nq][cj][dq]e  gqt[vt]za[fr]  [ae] 
[bw] s g s [bsgj]  b   


n c [adh]j[aq]n[vq] z [naf]f  
b x [sg] [bg] [bade] w [bmw]q q
n c [ad]q[aw][nq]v z [na] dd
[bh] xg[sg] b [bsdg]  qjgd  

n c [adh]q[aq]n[vq] [zw]e[na] [vq]e
z b [ad] [be]e[bsw]t  [bmt] jq
nw[cq]  [ad] anv z [nae]r[ve]r 
[be] [xq]qsh[bw]  g s [bt]wjg 

x n [sr] [dr] [br] [xe]es [gw]e
n c [ad] [ce]e[ve]yz  [naw] [vq]q
x n s [nh]h[dh] [nj] [gq]enw 
[bw] x s b [ge] s [bs]   


[nq] [cq] [adq] ca[vq]qzq[na] va
[bq] [xj]hsg[bs]d[ba]   [bme]wqh
[nq] wce[ad] ch[vq] wze[na] vh
[bq] [xw]es b [sdg] s b [xb] 

[nq] [cq] [adq] [cj]h[vh]jzq[na] [va]a
[bq] [xq]j[sh]gbs[bad]  [bme]w[bq]h
[ne] c [ade]wqh[ve] z [nae]wqh 
bq[sw] g s [sg] q bjhq

ng[ch] [ad] c v z [nat]rer
bw[se]wg s [sg]   [bq]jhj
[nq] c [ad] c [vh] zg[na]sds
[bs] x s g [bsgj]  b   



n c [adh]j[aq]n[vq] z [naf]f  
b x [sg] [bg] [bade] t [bmw]q q
n c [ad]q[aw][nq]v z [na] dd
[bh] xg[sg] b [bsdg]  qjgd  

n c [adh]q[aq]n[vq] [zw]e[na] [vq]e
z b [ad] [be]e[bst]t y[bm] ew
nqc [ad] anv z [nae]r[ve]r 
[be] [xq]qsh[bw]  g s [bt]wjg 

x n [sr] [dr] [br] [xe]es [gw]e
n c [ad] [ce]e[ve]yz  [naw] [vq]q
x n s [nh]h[dh] [nj] [gq]enw 
[bw] x s b [ge] s [bsu]  

[nq] [cq] [adq] ca[vq]qzq[na] va
[bq] [xj]hsg[bs]d[ba]   [bme]wqh
[nq] wce[ad] ch[vq] wze[na] vh
[bq] [xw]es b [sdg] s b [xb] 

[nq] [cq] [adq] [cj]h[vh]jzq[na] [va]a
[bq] [xq]j[sh]gbs[bad]  [bme]w[bq]h
[ne] c [ade]wqh[ve] z [nae]wqh 
bq[sw] g s [sg] q [bj]hh [nq] [cq] [adq] ca[vq]qzq[na] va
[bq] [xj]hsg[bs]d[ba]   [bme]wqh
[nq] wce[ad] ch[vq] wze[na] vh
[bq] [xw]es b [sdg] s b [xb] 

[nq] [cq] [adq] [cj]h[vh]jzq[na] [va]a
[bq] [xq]j[sh]gbs[bad]  [bme]w[bq]h
[ne] c [ade]wqh[ve] z [nae]wqh 
bq[sw] g s [sg] q bjhq

ng[ch] [ad] c v z [nat]rer
bw[se]wg s [sg]   [bq]jhj
[nq] c [ad] c [vh] zg[na]sds
[bs] x s g [bsgj]       


'''

#一路向北67
ylxb='''
[zgw] [bgw] [sgw] [bqe] [dqe] [bqt] [sqt] [bq] 
[vq] [zq] [nq] [aq] [fq] [aq] [ng]h[vq] 
[cngw] [cgw] [agw] [dqe] [gqe] [dqt] [aqt] [cqt] 
[vqt] [zqr] [nqe] [aqr] [fqr] [aqr] [nqr] [vqe] 

[zgw] [bgw] [sgw] [bqe] [dqe] [bqt] [sqt] [bq] 
[vq] [zq] [nq] [aq] [fq] [aq] [ng]h[vq] 
[cngw] [cgw] [agw] [dqe] [gqe] [dqt] [aqt] [cqt] 
[zvnqt] [qr] [qe] [qr]             

x n a [sf] f d s a 
[cns] d m a      g d 
[xvf] n a [sf] f d s a 
[cns] [ca] m a   a [bd] g 

[vg] z [va] n [ah] g [ng] [vd] 
[cg] b a b [cnh] [cg] [ag] [cd] 
[xd] [vs] n x [ah] g [ng] [xs]d
[bd] xsb m s   s d 

[xvf] n a [sf] f d s a 
[cns] d m a      g d 
[xvf] n a [sf] f d s a 
[cns] [ca]am a   a [bd] j 

[vj] [aq] f [aq] [hq] [aw] [fq] [aj] 
[cj] [mq] s [mq] [nq] [cw] [aq] [cw] 
[xqe] [nw] s [nq] [dq] [nw] [sq] [nw] 
[xbqe] [swr] [gqe] [sjw] [bs] g [xbg] w 
[vw] [aq]qf [aqe] [bqe] [sw] [gj] [sh] 
[ch] [mg]gs m n [cg] [ag] [dq] 
[xq] [nf] d [nq] [bj] [sj] [gq] [sw] 
[zw] [bqe][qe]s b [ad] g [bsg] w 

[vw] [aq]qf [aqe] [bqe] [sw] [gj] [sh] 
[ch] [mg] [sg] [md]wnqc [ad] [cg] 
[xg] [vh]an xa[bf] [xd] [ms] [xa]a
z b s b [ad] [bg] [sg] [bw] 

[vw] [aq]qf [aqe] [bqe] [sw] [gj] [sh]h
c [mg]gs m n [cg] [ag] [dq] 
[xq] [nf] d [nq] [bj] [sj] [gq] [sw] 
[zw] [bqe][qe]s b [ad] [qy] [bsqt] [qe] 

[vw] [aq]qf [aqe] [bw] [sq] [gj] [sh] 
[ch] [mg] [sg] [md]wnqc [ad] [cg] 
[xg] [vh]an xa[bf] [xd] [ms] [xa]a
z b s b [ad] b s [bg] 

[xng] ha  a [xbmf] d s
a    
'''

#城南花已开
zhemdr='''
h q 
[vaw] eh     [bsw] eh   t 
[nde]w e   t e   h q 
[vaw] eh      [bsw] eg   d 
[ndh] q j  gh    h q 

[vaw] eh      [bsw] eh   t 
[nde]w e  t e    h q 
[vaw] eh     [bsw] eg  d 
[ndq] j h  gh         

[vae]qhf eqhf eqhf eqhf 
[bse]qjg eqjg eqjg eqjg 
[vae]qhf eqhf eqhf eqhf 
[bse]qjg eqjg eqjg eqjg 

[ve]w[ae]nv danv dan[vw] [de][aw][ne][vy] 
[be]t[ae]mb damb damb [dq]a[mw]b 
[ve]w[ae]nv danv dan[va] da[nq]v 
[bj]q[aj]mb da[mg]b damb damb 

[ve]w[ae]nv danv dan[vw] [de][aw][ne][vy] 
[be]t[ae]mb damb damb [dq]a[mw]b 
[ve]w[ae]nv danv dan[vq] [dq]an[vw] 
[mj]bcz mbcz mbcz mbcz 

jgda jgda j dadgqj 


[vg] z [na] z [bg] [xf]dm [xf] 
[ng] aq[dhw] [ae] [zw] [bq] [dj] [aq] 
[vg] z [na] z [bg] [xf]dm [xf] 
[ng] c [cna]  [cns]  d[zbg]sa 

[vg] z [na] z [bg] [xf]dm [xf] 
[ng] aq[dhw] [ae] [zw] [bq] [dj] [aq] 
[vg] z [na] z [bs] [xd]sm [xb] 
[bs] x m x [xbm]  h q 


[vaw] eh     [bsw] eh   t 
[nde]w e   t e   h q 
[vaw] eh      [bsw] eg   d 
[ndh] q j  gh    h q 

[vw] [ae]hd a [bw] [se]hg [st] 
[ne]wde h [dt] [ze] b [dh] [aq] 
[vw] [ae]hd a [bw] [xe]gm b 
[ndq] j h  gh         
'''

# 鸡你太美
jntm='''
[de] [ed] [ed] [nh] c n [cy] n [ec]en [rc]rn [ec]en [cq]qn 
[ce] [en] [ce] [ny] c n [cy] n [ce]en [cr]rn [ec]en [cq]qn 
[ce] [en] [ce] [vy] z v z b [xe]eb [rx]rn [ec]en [cq]qn 
[ce] [en] [ce] [vy] z v [zy] b [xe]eb [xr]rn [ec]en [cq]qc n c 
e [vy]e[ez]e[ev]e[ez]wbe[wx]ebe[ex]e[ny] [ec]e[ne]e[ec]e[ce]enec [en]w[ev] z v z b x b x [wn]ec [wn]ec [cw]en c 
[en]e[vy]e[ez]e[ev]e[ez] [wb]e[xw]ebe[xe] [tn]e[ec]e[en]e[ce] [wc]e[wn]ece[en]e[vy] [ez]e[ev]e[ez]wbq[wx] [bq]w[xq]wne[cw] [nq]w[cq]wce[nh] c n v z v
[zh] [eb]r[xe]r[be] [xh] n c n [ch] [tcg]h[nh][gt][ch] n [vh] z v [zh] [eb]r[xe]r[be] [xh] n c n [ch] [ctg]h[hn][tg][ch] [nh] [vq] z [vr] z [be] x b [xh] n c [ne] c [wn] [ec] [wn] [cq] [vh] z v [zh] [btg][yh][xh][gt][bhy] [xh] [nde] c n [ch] [ctg]h[nh][gt][ch] [nh] [vq] z [vq] z [ub] x [bt] x [en] c [ne] [cq] [un] c [nt] c [ve] z v z v [ez] [ev] [ze] c
e e e [ny] c n [cy] n [ec]en [cr]rn [ec]en [cq]qn [ce] [en] [ce] [ny] c n [yc]yn [ce]en [rc]rn [ec]en [cq]qn [ce] [en] [ce] [yv] z v [zy] b [xe]eb [rx]rn [ec]en [qc]qn [ec] [en] [ce] [vy] z v [yz]yb [xe]eb [rx]rn [ce]en [cq]qn c [nq] [cuj] [vh] z v z b x [bgt] x [nh] c [nq] [cj] [ch] n [cg] n [vh] z [vh] z [btg] x [bw] x [tn] [ce] [wn]e[cw]q[nw] [ce] [wn]q[ch][gt][vh] z 
[vy] z [ub] x [by] [ux] [qn] [cu] [ny] c [nt] [ce] [nw] [cq] [ve] z [vr] z [ve] z [ve] zy uezw
'''


# 菊次郎的夏天
Kikujirossummer='''
ndhd vafa bsgs zbab

ndhd vafa bsgs zb[ag]q [bw]e

[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gese zb[ag]q [bw]e

[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gtse zb[ae][br]

[bt] [st]t g [st] [vt] [ae]q f [ae]r

[ct] [mt]t d [mt] [nt] [de]q h [dq]w

[xe] [ne]e s [ne] [ve] [ay] [fw]ew [aq]

[bw] s [gw] [sw]w [bw] [sj] gq[sw]e
[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gese zb[ag]q [bw]e

[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gtse zb[ae][br]

[bt] [st]t g [st] [vt] [ae]q f [ae]r

[ct] [mt]t d [mt] [nt] [de]q h [dq]w

[xe] [ne]e s [ne] [bse] wewqh

[zq] b [aw] [bt] [ne] dhd

[ve] a [fq] [ae] [bw] sgs
 
[zt] b [at] [bw]q [nt] d [ht] [dw]q

[vt] a [ft] [aw]q [bj] sgs[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gese zb[ag]q [bw]e

[nw] [dq]q hd va [fg]q [aw]e

[bw] [sq]w gtse zb[ae][br]

[bt] [st]t g [st] [vt] [ae]q f [ae]r

[ct] [mt]t d [mt] [nt] [de]q h [dq]w

[xe] [ne]e s [ne] [bse] wewqh

[zq] b [aw] [bt] [ne] dhd

[ve] a [fq] [ae] [bw] sgs
 
[zt] b [at] [bw]q [nt] d [ht] [dw]q

[vt] a [ft] [aw]q [bj] sgs
[zct]gqw [zct]wqg

[zvt]gqw [zvt]wqg

[zbt]gqw [zbt]wqg

[zvt]gq[zcw] tw[czq]g

[zct]g[zcq]w [zct]w[zcq]g

[zvt]g[zvq]w [zvt]w[zvq]g

[zbt]g[zbq]w [zbt]w[zbq]g

[zvt]gq[zcw] tw[czq]g

[bq]afg [bq]gfa

[nq]afg [nq]gfa

[mq]afg [mq]gfa

[nq]af[bg] qg[nf]a

[bq]a[bf]g [bq]g[bf]a

[nq]a[nf]g [nq]g[nf]a

[mq]a[mf]g [mq]g[mf]a

[nq]af[bg] qg[nf]a
[zt]g [bq]w [st]w [dq]g

[xt]g [sq]w [ft]w [gq]g

[ct]g [dq]w [gt]w q g

[vft]gq [cdw] tw [xsq]g

[zt]g [bq]w [st]w [dq]g

[xt]g [sq]w [ft]w [gq]g

[ct]g [dq]w [gt]w q g

[vft]gq [cdw] tw [xsq]g
[bt] tt d t [vt] eq a

er [ct] tt m t [nt] eq d

qw [xe] ee n e [bse]

wewqh [zq] b [aq] b

[nj] c n g [vd] z [va] d

[bs] x [bg]qwe 

[zw] [bq]q [aq] b

[nj] c n g [vh] z 

[vh]jqw [be]r[xw] [bg]qwe

[zw] [bq]q [aq] b

[nj] c n g [vd] z [va] d

[bs] x [bg]qwe 

[zw] [bq]q a 

[vry] [cet] [xwr] [zbgwe]
'''

# 大鱼
dayu='''
[vad]sdh [bsd]sdj [nd]sdq [sj] [mg]
[vad]sdh [bsd]sdj [ng]cacm
[vad]sdh [bsd]sdj [nd][cs][nd]q [sj] [mg]
[xvns]dn [cbms]dn b[cn]cacm

[vh][aq][dq][gw][hw]eey
[ct]ma[de][gw]
[vh][aq][gq][sw][hw]ee
[ch]mgasj
[vh][aq][dq][gw][hw]eey
[ct]ma[de][gw]
[xvnw]eh [cbmw]eh g[nh]camn

[nh][bq] [vw]adq[bh]s[gh]q
[nw]dhq [ne]d[bse]t
[vy]a[dy]t [be][sw][gq]w
z[be]sbd [ah]q
[vw]sgq [bh]a[dh]q
[nw]d[hq] [adhe]
[xvnw]eh [cbmw]eh g[nh]camsa

[nd][bdg][vdq]adj[bad] ds
[na]c[na]s [zcnd] [nd][bs]
[va]z[dh]q [bj][sh]gs 
[nd]cnmam[nd][bdg]
[vdq]adj[bad] ds
[na]c[na]s[zcnd]
[xvns]dn [cbms]dn b[cn]camn

[vad]sdh [bsd]sdj [nd]sdq [sj] [mg]
[vad]sdh [bsd]sdj [ng]cacm
[vad]sdh [bsd]sdj [nd]sdq [sj] [mg]
[xvns]dn [cbms]dnb [cn]camn
[cn]camn

dg[vdh]a[dh] [hjh]g [bh]sg
[nad]cnmam[nd][bdg]
[vdh]a[dh] [hjh]g [bh]s[gj]
[ndq]cnmam[nh][bqe]
[vhw]a[dh][qe] [bhw]s[gj]
[nj]c[ng]m[ad]mnc
[xvnw]eh [cbmw]eh g[nh]camn

[xvns]dn [cbms]dn b
[zcn]camsads
[nadh]
'''
# 来不及
laibuji='''
 [ny]dqj [et] y [ve]aqj [ry] 
 [bu]sjh [wt] w [zbde] g  
 [xr] n [fhe] w [ce] m [dq] j 
 [nh]cna d s  [cn]   
 [naq] j [nah] g [vnd] s [vnd]  
 [xbs] d [xbg] s [zbd]  a m 
 [zcn] g [cn] d [zvn] a [zv]  
 [xbm] a [xbs]b n [zcn]  [cn] na

 [vns] ds [vn]d  [xbs] dg [xb] d 
 [cb] n [zc]  [zcn]  [zcn] na 
 [zvns] ds [zvn]d  [xbg] d [xbs] dd 
 [zb]  [zb]  b   [bq]jg 

 [vnd] g [vn] a [bms]  [bmq]jg 
 [cbd] g [cb] s [nad]  [cna] na 
 [vns] ds [vn]d  [bms] dgbm 
 [cb] n [zc]  [zcn]  hhg 
 [vnah]hh hg [nah] q [bmsh]hh hg [msh] q 
 [cnah]hh hh [nah]hhh [naw]ewh [na] hhg
 [vnah]hhg [nah] q [bmsh]hhg [msh] q 
 [cnah]hhh [nah] h [na]  [na] we 
 [vnat]yte [naw]ewh [bmsw]  [ms] we 
 [cbmt]yte [bmw]ewh [cnaw]e  [na] hq 
 [vnaw] ew [na]e  [bmst] e [msw] gh 
 [cna]  [na]  [cna] [cna] y t 
 [zve] a [afy] t [xbw] s [sgw] q 
 [cnw] d [dht] w [cne] d [bsy] t 
 [zve] a [afy] t [xbw] s [sgw] q 
 [cnw] d [dht] w [cne] d [bsy] t 

 [zve] a [afy] t 
 [xbw] s [sgw] q [cnw] dq [dhw] t 
 [cne] d [bsy] t [vade]  y t 
 [bsgw]  j q [cnaj] q j g 
h   
'''
# 没有共产党就没有新中国

没有共产党就没有新中国='''

q ghhgfqqhq w  e w qewq e



'''
猪猪侠='''
we  t e w q h q h [qw] e we  t e  [wq] h q h [qnw] n nn [qn] [hn] nn n n n n [cbadg]  [dg] [cbadh] [dh] [xbmgj] [gj] [xbm] [gj] [gj] [xbmgj] [fh] [dgcba] [dg]  [cbadh] [dh] [gjxbm] [gj] [xbm] [gj] [gj] [xbmgj] [fh] [cbadg] [dg]  [cbadh] [dh] [xbmgj] [gj] [xbm] [gj] [gj] [xbmgj] [fh]  [dgcba] [dg]  [cbadh] [dh] [gjxbm] [gj] [gj] [xbmgj] [gj] [gj] [gj] [gjxbm] [gj] [gjw] [gjw] [xbmgjw] [gjw] [gjw] [gjw] [xbmgjw] [gjw] [gjwr] [gjwr] [xb] [mgjwr] [gjwr] [gjwr] [gj] [wr] [xbmgjwr] [gjwr] [gjwt] [gjwt] [gjwtxbm] [gjwt] [gjwt]  [xbm] [ze] [bade]  [ze] [qbad] [ez] r [bad] e z e [ba] [dr] e [xw] w [nsf] [xt] y [nsfw] w x  [nsf] x [nsf]  [tb] [xbmt] [bt]  [xbmw] [bt] y [xbm] t b t [xbmy] t [rv] r [zvn] r [br] t r [xb] m e [zd] g [hbad] q [qzw] q [bad] [ze]  [bade] [ez] [qbad]  [ez] r [bad] e z e [rbad] e [xw] w [ns] f w [xty] [wnsf] w x q [nsf] h [gdx] s [nsf] [bg] [xb] g [bg] [xbs] [gb] h [xb] g b g [hx] b j [vfq] [fq] [zv] [vgj] [gj] [zv] [dq] [za] s a [bz] c z g [hbzc] j [fqv] [fq] [zv] [fq] v [fq] [zv] [fq] v [fq] [zv] [fq] [gjv] [gj] [zvhq] [jw] [gb] g [hxbm] g   [xbm] g [gj] [gj] [hqxbm] [gj]    [dgz]  [dgbad] [dhz] [baddh] [gj] [gj] [xbm] [gj] [gj] [gj] [fhxbm] [dgz] [dg] [bad] [zdh] [dhbad] [gj] [gj] [xbm] [gj] [gj] [gj] [xb] [mfh] [zdg] [dgbad]  [dhz] [dhbad] [gj] [gj] [xbm] [gj] [gj] [gj] [fhxbm]  [zdg] [dgbad] [dh] z [baddh] [gj]  [gj] [xb] m [gj] [gj] [gj] [fhxbm]  [fq] [zvnfq] q [gw] [gwxbm] [dq] z q [bad] q [zh] g [gbad] [fq]  [fqzvn] q [gw] [gwxbm] [dq] z q [bad] q [hz] g [badg] [fq]  [zvnfq] [qgw] [xbmgw] [dq] z q [bad] q [hz] g [gbad] [afq] [zv] [afq] [sgw] [xbsgw] [aq] [dq] z [bad] t [ez]  [wbad] q z h [badq] h [zqw] [ebad] [we] z  [badt] e [zw] [qh] [qbad] h [zw] [badq] h z  [bad] [gz] h h [bad] d g z h [bad]  [zgh] h [bad] [dg] z h [bad]   z [cb] a q  h g d s  a n

'''



# 圣诞快乐，劳伦斯先生
MerryChristmasMrLawrence='''

 [fgqe]weyew eweyew
 [fhje]wetew ewetew
 [dgjw]qwtwq wqwtwq
 [ndgw]qwtwq [basj]hjejh

 [fgqe]weyew eweyew
 [fhje]wetew ewetew
 [dgjw]qwuwq twquwq
 [ndgw]qwuwq twquwq

 [fgqe]weyew eweyew
 [fhje]wetew ewetew
 [dgjw]qwtwq wqwtwq
 [ndgw]qwtwq [basj]hjejh

 [fgqe]weyew eweyew
 [fhje]wetew ewetew
 [dgjw]qwuwq twquwq
 [ndgw]qwuwq twqu

 [vas]dsns b sdsdgd [ns]dsna
n [dq] [bsj]gd [vas]dsns
b sdsdgd [ns]dsan  [xb]

'''

def zd():
    qhc2=[qhc1,60]
    qifengle2=[qifengle,100]
    daoxiang2=[daoxiang,100]
    qilixang2=[qilixang,75]
    qingtian2=[qingtian,81]
    frx2=[frx,58]
    anhao2=[anhao,63]
    gyz2=[gyz,120]
    ygdnh=[yianguangkuaileidananhai,110]
    ylxb2=[ylxb,67]
    pianai2=[pianai,70]
    zhemdr2=[zhemdr,72]
    jntm2=[jntm,107]
    zwmzghggg2=[zwmzghggg,30]
    laibuji2=[laibuji,54]
    MerryChristmasMrLawrence2=[MerryChristmasMrLawrence,80]
    dayu2=[dayu,50]
    Kikujirossummer2=[Kikujirossummer,90]
    猪猪侠2=[猪猪侠,90]
    a={"青花瓷":qhc2,"七里香":qilixang2,"稻香":daoxiang2,"起风了":qifengle2,"晴天":qingtian2,"暗号":anhao2,"发如雪":frx2,"孤勇者":gyz2,"阳光快乐大男孩":ygdnh,"偏爱":pianai2,"一路向北":ylxb2,"这世界那么多人":zhemdr2,"鸡你太美":jntm2,"中华民族共和国国歌":zwmzghggg2,"圣诞快乐，劳伦斯先生":MerryChristmasMrLawrence2,"大鱼":dayu2,"菊次郎的夏天":Kikujirossummer2,"猪猪侠":猪猪侠2}
    for key in a.keys():
        print("选歌"+key)
    str=input()
    time.sleep(2)
    play_string(a[str])


while True:
    a = input("按回车开始查询，按 1 结束：")
    if a == "1":
        break
    else:
        zd()