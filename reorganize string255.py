class Solution:
    def reorganizeString(self, s: str) -> str:
        # solution 1
        # AC, 81.26% speed, 98.61% memory
        counter = collections.Counter(s)
        kvs = sorted(counter.items(), key=operator.itemgetter(1))
        if kvs[-1][1] - 1 > sum([kv[1] for kv in kvs[:-1]]):
            return ''
        s = [list(itertools.repeat(*kvs[-1]))]
        l = kvs[-1][1]
        tmp = list()
        for k, v in kvs[:-1][::-1]:
            if len(tmp) + v < l:
                tmp += list(itertools.repeat(k, v))
            else:
                v -= l - len(tmp)
                s.append(tmp + list(itertools.repeat(k, l - len(tmp))))
                tmp = list(itertools.repeat(k, v))
        s.append(tmp + list(itertools.repeat("", l - len(tmp))))
        return ''.join(itertools.chain(*zip(*s)))
