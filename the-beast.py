# Adding file variables to easily test against other inputs.
# Can easily be hard-coded to make it truly one line.
q = {
    1 : 'inputs/day-01.txt',
    2 : 'inputs/day-02.txt',
    3 : 'inputs/day-03.txt',
    4 : 'inputs/day-04.txt',
    5 : 'inputs/day-05.txt',
    6 : 'inputs/day-06.txt',
    7 : 'inputs/day-07.txt',
    8 : 'inputs/day-08.txt',
    9 : 'inputs/day-09.txt',
    10 : 'inputs/day-10.txt',
    11 : 'inputs/day-11.txt',
    # TODO: Day 12
    # TODO: Day 13
    14 : 'inputs/day-14.txt',
}

# I'm sorry.
print('Day 01 Part 1: ',max([sum([int(x)for x in g])for g in[k.split('\n')for k in open(q[1]).read().split('\n\n')]]),'\nDay 01 Part 2: ',sum(sorted([sum([int(x)for x in g])for g in[k.split('\n')for k in open(q[1]).read().split('\n\n')]],reverse=1)[0:3]),'\nDay 02 Part 1: ',sum([{'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}[x]for x in open(q[2]).read().split('\n')]),'\nDay 02 Part 2: ',sum([{'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}[x]for x in open(q[2]).read().split('\n')]),'\nDay 03 Part 1: ',sum([ord(x)-96 if x.islower() else ord(x)-38 for x in[set(x).intersection(y).pop()for x,y in[[i[:len(i)//2],i[len(i)//2:]]for i in open(q[3]).read().split('\n')]]]),'\nDay 03 Part 2: ',sum([ord(x)-96 if x.islower() else ord(x)-38 for x in[set(open(q[3]).read().split('\n')[i]).intersection(open(q[3]).read().split('\n')[i+1]).intersection(open(q[3]).read().split('\n')[i+2]).pop()for i in range(0,len(open(q[3]).read().split('\n')),3)]]),'\nDay 04 Part 1: ',sum([(n[0][0]>=n[1][0]and n[0][1]<=n[1][1])or(n[0][0]<=n[1][0]and n[0][1]>=n[1][1])for n in[[[int(x)for x in a.split('-')],[int(y)for y in b.split('-')]]for a,b in[x.split(',')for x in open(q[4]).read().split('\n')]]]),'\nDay 04 Part 2: ',sum([n[0][0]<=n[1][1]and n[0][1]>=n[1][0]for n in[[[int(x)for x in a.split('-')],[int(y)for y in b.split('-')]]for a,b in[x.split(',')for x in open(q[4]).read().split('\n')]]]),'\nDay 05 Part 1: ',''.join([c[0]for c in k] if not(f:=open(q[5]).read().split('\n'))or not(t:=[[int(x[1]),int(x[3]),int(x[5])]for x in[y.split(' ')for y in f[10:]]])or not(k:=[[]for i in range(9)])or not[k[j//4].append(l[j])for l in f[:8]for j in range(1,len(l),4) if l[j].isalpha()]or[k[p[2]-1].insert(0,k[p[1]-1].pop(0))for p in t for _ in range(p[0])] else ''),'\nDay 05 Part 2: ',''.join([c[0]for c in k] if not(f:=open(q[5]).read().split('\n'))or not(t:=[[int(x[1]),int(x[3]),int(x[5])]for x in[y.split(' ')for y in f[10:]]])or not(k:=[[]for _ in range(9)])or not[k[j//4].append(l[j])for l in f[:8]for j in range(1,len(l),4) if l[j].isalpha()]or[k[p[2]-1].insert(0,e)for p in t for e in reversed([k[p[1]-1].pop(0)for _ in range(p[0])])] else ''),'\nDay 06 Part 1: ',[i+1 for x in[open(q[6]).read()]for i in range(3,len(x)) if len(set(x[i-3:i+1]))==4][0],'\nDay 06 Part 2: ',[i+1 for x in[open(q[6]).read()]for i in range(13,len(x)) if len(set(x[i-13:i+1]))==14][0],'\nDay 07 Part 1: ',sum([x for x in u.values() if x<=100000] if not(u:={})and not(g:=[])and[((l[0]=='$'and l[1]=='cd')and(((l[2]=='/')and(g:=['//'])and not(u.update({'//':0})))or(l[2]=='..'and g.pop())or((h:='/'.join(g)+'/'+l[2])and not g.append(h)and(not u.get(h)and not u.update({h:0})))))or(l[0].isdigit()and[u.update({d:u[d]+int(l[0])})for d in g])for l in[c.split(' ')for c in open(q[7]).read().split('\n')]] else ''),'\nDay 07 Part 2: ',min([x for x in u.values() if x>u['//']-40000000]) if not(u:={})and not(g:=[])and[((l[0]=='$'and l[1]=='cd')and(((l[2]=='/')and(g:=['//'])and not(u.update({'//':0})))or(l[2]=='..'and g.pop())or((h:='/'.join(g)+'/'+l[2])and not g.append(h)and(not u.get(h)and not u.update({h:0})))))or(l[0].isdigit()and[u.update({d:u[d]+int(l[0])})for d in g])for l in[c.split(' ')for c in open(q[7]).read().split('\n')]] else '','\nDay 08 Part 1: ',sum([not bool([x for x in t[r][:c] if x>=t[r][c]]and[x for x in t[r][c+1:] if x>=t[r][c]]and[x[c]for i,x in enumerate(t) if x[c]>=t[r][c]and i<r]and[x[c]for i,x in enumerate(t) if x[c]>=t[r][c]and i>r])for t in[[[int(y)for y in x]for x in open(q[8]).read().split('\n')]]for r in range(len(t))for c in range(len(t[r]))]),'\nDay 08 Part 2: ',max([sum([(x<t[r][c])or(e:=1)for x in t[r][:c][::-1] if not e] if not(e:=False) else '')*sum([(x<t[r][c])or(e:=1)for x in t[r][c+1:] if not e] if not(e:=False) else '')*sum([(x[c]<t[r][c])or(e:=1)for i,x in reversed(list(enumerate(t))) if not e and i<r] if not(e:=False) else '')*sum([(x[c]<t[r][c])or(e:=1)for i,x in enumerate(t) if not e and i>r] if not(e:=False) else '')for t in[[[int(y)for y in x]for x in open(q[8]).read().split('\n')]]for r in range(len(t))for c in range(len(t[r]))]),'\nDay 09 Part 1: ',len(v)if(v:={(0,0)})and(r:=[0,0])and(w:=[0,0])and[((d=='R'and((w[1]==r[1]and w[0]==r[0]-1 and(w.insert(0,w.pop(0)+1)))or(w[1]>r[1]and w[0]==r[0]-1 and not(w.insert(0,w.pop(0)+1)or w.insert(1,w.pop(1)-1)))or(w[1]<r[1]and w[0]==r[0]-1 and not(w.insert(0,w.pop(0)+1)or w.insert(1,w.pop(1)+1)))or 1)and not r.insert(0,r.pop(0)+1))or(d=='L'and((w[1]==r[1]and w[0]==r[0]+1 and(w.insert(0,w.pop(0)-1)))or(w[1]>r[1]and w[0]==r[0]+1 and not(w.insert(0,w.pop(0)-1)or w.insert(1,w.pop(1)-1)))or(w[1]<r[1]and w[0]==r[0]+1 and not(w.insert(0,w.pop(0)-1)or w.insert(1,w.pop(1)+1)))or 1)and not r.insert(0,r.pop(0)-1))or(d=='U'and((w[1]==r[1]-1 and w[0]==r[0]and(w.insert(1,w.pop(1)+1)))or(w[1]==r[1]-1 and w[0]<r[0]and not(w.insert(0,w.pop(0)+1)or w.insert(1,w.pop(1)+1)))or(w[1]==r[1]-1 and w[0]>r[0]and not(w.insert(0,w.pop(0)-1)or w.insert(1,w.pop(1)+1)))or 1)and r.insert(1,r.pop(1)+1))or(d=='D'and((w[1]==r[1]+1 and w[0]==r[0]and(w.insert(1,w.pop(1)-1)))or(w[1]==r[1]+1 and w[0]<r[0]and not(w.insert(0,w.pop(0)+1)or w.insert(1,w.pop(1)-1)))or(w[1]==r[1]+1 and w[0]>r[0]and not(w.insert(0,w.pop(0)-1)or w.insert(1,w.pop(1)-1)))or 1)and not r.insert(1,r.pop(1)-1))or 1)and(v.add(tuple(w)))for d,n in(x.split(' ')for x in open(q[9]).read().split('\n'))for _ in range(int(n))] else '','\nDay 09 Part 2: ',len(v)if(v:={(0,0)})and(s:=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])and[not((d=='R'and s[0].insert(0,s[0].pop(0)+1))or(d=='L'and s[0].insert(0,s[0].pop(0)-1))or(d=='U'and s[0].insert(1,s[0].pop(1)+1))or(d=='D'and s[0].insert(1,s[0].pop(1)-1)))and[(s[i][0]<s[i-1][0]-1 and((s[i][1]==s[i-1][1]and(s[i].insert(0,s[i].pop(0)+1)))or(s[i][1]>s[i-1][1]and not(s[i].insert(0,s[i].pop(0)+1)or s[i].insert(1,s[i].pop(1)-1)))or(s[i][1]<s[i-1][1]and not(s[i].insert(0,s[i].pop(0)+1)or s[i].insert(1,s[i].pop(1)+1)))))or(s[i][0]>s[i-1][0]+1 and((s[i][1]==s[i-1][1]and(s[i].insert(0,s[i].pop(0)-1)))or(s[i][1]>s[i-1][1]and not(s[i].insert(0,s[i].pop(0)-1)or s[i].insert(1,s[i].pop(1)-1)))or(s[i][1]<s[i-1][1]and not(s[i].insert(0,s[i].pop(0)-1)or s[i].insert(1,s[i].pop(1)+1)))))or(s[i][1]<s[i-1][1]-1 and((s[i][0]==s[i-1][0]and(s[i].insert(1,s[i].pop(1)+1)))or(s[i][0]<s[i-1][0]and not(s[i].insert(0,s[i].pop(0)+1)or s[i].insert(1,s[i].pop(1)+1)))or(s[i][0]>s[i-1][0]and not(s[i].insert(0,s[i].pop(0)-1)or s[i].insert(1,s[i].pop(1)+1)))))or(s[i][1]>s[i-1][1]+1 and((s[i][0]==s[i-1][0]and(s[i].insert(1,s[i].pop(1)-1)))or(s[i][0]<s[i-1][0]and not(s[i].insert(0,s[i].pop(0)+1)or s[i].insert(1,s[i].pop(1)-1)))or(s[i][0]>s[i-1][0]and not(s[i].insert(0,s[i].pop(0)-1)or s[i].insert(1,s[i].pop(1)-1)))))or 1 for i in range(1,10)]and(v.add(tuple(s[9])))for d,n in(x.split(' ')for x in open(q[9]).read().split('\n'))for _ in range(int(n))] else '','\nDay 10 Part 1: ',sum(s) if not(s:=[])and(x:=1)and not(u:=0)and[[(c[0]=='addx')and[(u:=u+1)and((u+20)%40==0 and s.append(u*x))for _ in range(2)]and(x:=x+int(c[1]))]and[(c[0]=='noop')and[(u:=u+1)and((u+20)%40==0 and s.append(u*x))]]for c in[y.split(' ')for y in open(q[10]).read().split('\n')]] else '','\nDay 10 Part 2:\n',''.join(v[:-1]) if not(v:=[])and(x:=1)and not(e:=0 )and(s:=['#']*3+['.']*37)and not(t:=[])and[((c[0]=='addx'and[(e:=e+1)and([t.append('#' if s[e-((e//40)*40)-1]=='#' else '.')]or 1)for _ in range(2)]and((x:=x+int(c[1]))or 1)and(s:=['.']*40)and[s.pop(i)and s.insert(i,'#')for i in range(x-1,x+2) if i<40 and i>=0])or(c[0]=='noop'and[(e:=e+1)and t.append('#' if s[e-((e//40)*40)-1]=='#' else '.')]))for c in[y.split(' ')for y in open(q[10]).read().split('\n')]]and[not v.append(p)and((i+1)%40==0 and v.append('\n'))for i,p in enumerate(t)] else '','\nDay 11 Part 1: ',c[0]*c[1]if(f:=[[list(map(int,[a.replace(',','')for a in o[0][4:]])),(o[1][6]=='*'and((o[1][7]=='old'and(lambda a:a*a))or(lambda a,n=int(o[1][7]):a*n)))or((o[1][6]=='+'and((o[1][7]=='old'and(lambda a:a+a))or(lambda a,n=int(o[1][7]):a+n)))),int(o[2][5]),int(o[3][9]),int(o[4][9]),0]for o in[[z.split(' ')for z in y[1:]]for y in[x.split('\n')for x in open(q[11]).read().split('\n\n')]]])and[[[not(m.insert(5,m.pop(5)+1))and((m[1](i)//3%m[2]==0 and not f[m[3]][0].append(m[1](i)//3))or not f[m[4]][0].append(m[1](i)//3))for i in m[0]]and(not m.insert(1,[])and m.pop(0))for m in f]for _ in range(20)]and(c:=sorted([k[5]for k in f],reverse=1)) else '','\nDay 11 Part 2: ',c[0]*c[1]if(f:=[[list(map(int,[a.replace(',','')for a in o[0][4:]])),(o[1][6]=='*'and((o[1][7]=='old'and(lambda a:a*a))or(lambda a,n=int(o[1][7]):a*n)))or((o[1][6]=='+'and((o[1][7]=='old'and(lambda a:a+a))or(lambda a,n=int(o[1][7]):a+n)))),int(o[2][5]),int(o[3][9]),int(o[4][9]),0]for o in[[z.split(' ')for z in y[1:]]for y in[x.split('\n')for x in open(q[11]).read().split('\n\n')]]])and(l:=1)and([l:=l*k[2]for k in f])and[[[not(m.insert(5,m.pop(5)+1))and(((m[1](i)%l)%m[2]==0 and not f[m[3]][0].append(m[1](i)%l))or not f[m[4]][0].append(m[1](i)%l))for i in m[0]]and(not m.insert(1,[])and m.pop(0))for m in f]for _ in range(10000)]and(c:=sorted([k[5]for k in f],reverse=1)) else '','\nDay 14 Part 1: ',s if[(not(v := []))and[(l!=len(o)-1 and((len(v)==0 and v.extend(list(list())for _ in range(max(m[0],o[l+1][0])+1))or 1)and(0 < len(v)<=max(m[0],o[l+1][0])and v.extend([['.'for _ in range(len(v[0]))]for _ in range(max(m[0],o[l+1][0])-len(v)+2)])or 1)and(m[0]==o[l+1][0]and[(len(v[0])<=a and[c.extend(['.'for _ in range(a-len(c)+2)])for c in v]or 1)and(v[m[0]].pop(a)and v[m[0]].insert(a,'#'))for a in range(min(m[1],o[l+1][1]),max(m[1],o[l+1][1])+1)])or[v[b].pop(m[1])and v[b].insert(m[1],'#')for b in range(min(m[0],o[l+1][0]),max(m[0],o[l+1][0])+1)]))for o in [[list(map(int,z.split(',')))for z in y]for y in [x.split(' -> ')for x in open(q[14]).read().split('\n')]]for l,m in enumerate(o)]and[(not w)and((x := 500)and not(y := 0))and[(y+1 > len(v[0])-1 and(w := 1)and(s := s-1))or(y+1 > len(v[0])-1)or(v[x][y+1]=='.'and(y := y+1))or(v[x-1][y+1]=='.'and(x := x-1)and(y := y+1))or(v[x+1][y+1]=='.'and(x := x+1)and(y := y+1))for _ in range(len(v[0]))]and(v[x].pop(y)and not v[x].insert(y,'o')and(s := s+1))for _ in range(len(v[0])*5)]if(not(w := 0)and not(s := 0)) else ''] else '','\nDay 14 Part 2: ',s if[((not(v := []))and[(l!=len(o)-1 and((len(v)==0 and v.extend(list(list())for _ in range(max(m[0],o[l+1][0])+1))or 1)and(0 < len(v)<=max(m[0],o[l+1][0])and v.extend([['.'for _ in range(len(v[0]))]for _ in range(max(m[0],o[l+1][0])-len(v)+2)])or 1)and(m[0]==o[l+1][0]and[(len(v[0])<=a and[c.extend(['.'for _ in range(a-len(c)+2)])for c in v]or 1)and(v[m[0]].pop(a)and v[m[0]].insert(a,'#'))for a in range(min(m[1],o[l+1][1]),max(m[1],o[l+1][1])+1)])or[v[b].pop(m[1])and v[b].insert(m[1],'#')for b in range(min(m[0],o[l+1][0]),max(m[0],o[l+1][0])+1)]))for o in [[list(map(int,z.split(',')))for z in y]for y in [x.split(' -> ')for x in open(q[14]).read().split('\n')]]for l,m in enumerate(o)])and(v := [['.'for _ in range(len(v[0]))]for _ in range(len(v[0])+1)]+v+[['.'for _ in range(len(v[0]))]for _ in range(len(v[0])+1)])and[c.extend(['.','#'])for c in v]and[(not w)and((x := 500+len(v[0]))and not(y := 0))and[(y+1 >= len(v[0]))or(v[x][y+1]=='.'and(y := y+1))or(v[x-1][y+1]=='.'and((x := x-1)or 1)and(y := y+1))or(v[x+1][y+1]=='.'and(x := x+1)and(y := y+1))for _ in range(len(v[0]))]and(v[x].pop(y)and not v[x].insert(y,'o')and(s := s+1)and(v[500+len(v[0])][0]=='o'and(w := 1)))for _ in range(len(v[0])*500)]if(not(w := 0)and not(s := 0)) else ''] else '',sep='')