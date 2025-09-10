                flat.append(k)
        result = [[0] * c for _ in range(r)]
        idx = 0
        for h in range(r):
            for f in range(c):
                result[h][f] = flat[idx]
                idx += 1
        return result