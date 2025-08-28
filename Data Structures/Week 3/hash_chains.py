# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems = []
        # Dictionary with bucket index mapping to a list (chain) of strings
        self.chains = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.chains[query.ind])
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
        else:
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            index = self._hash_func(query.s)
            chain = self.chains[index]
            if query.type == 'find':
                self.write_search_result(query.s in chain)
            elif query.type == 'add':
                if query.s not in chain:
                    chain.insert(0, query.s)  # Insert at beginning
            elif query.type == 'del':
                if query.s in chain:
                    chain.remove(query.s)

    def process_queries(self):
        n = int(input())
        for _ in range(n):
            self.process_query(Query(input().split()))

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
