class Reducer:
    def reduce(self, d):
        returnval = []
        for k, v in d.items():
            returnval.append(f'{k}\t{sum(v)}')
        return returnval

