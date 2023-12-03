import sys
sys.path.append('../../../src')

from functools import reduce

from PythonFramework.Day import Day


class Day2(Day):
    def solvePartOne(self, data):
        return sum([d[0]for d in[list(reduce(lambda a,b:a+b,[[i+1 if{'red':12,'green':13,'blue':14}[a.split(' ')[2]]>=int(a.split(' ')[1])else 0 for a in b.split(',')]for b in l.split(':')[1].split(';')],[]))for i,l in enumerate(data)]if 0 not in d])

    def solvePartTwo(self, data):
        return sum([a*b*c for a,b,c in list(zip(*[[max(w)if len(w)>0 else 0 for w in[[int(v)for i,v in enumerate(x)if i%2==0 and x[i+1]==c]for x in[''.join(''.join(l.split(':')[1].split(';')).split(',')).split(' ')[1:]for l in data]]]for c in['red','green','blue']]))])


Day2().getResult()
