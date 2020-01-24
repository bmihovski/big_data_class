class Mapper:
    def map(self, data):
        returnval = []
        counts = {}
        for line in data:
            words = line.split()
            for w in words:
                counts[w] = counts.get(w, 0) + 1
            for w, c in counts.items():
                returnval.append((w, c))
            return returnval

