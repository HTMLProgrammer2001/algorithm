def reduction_distance(s1, s2):
    cache = {}
    
    def rec(a, b):
        # get from cache
        if (a,b) in cache:
            return cache[(a, b)]

        result = None

        # one of string end
        if a == 0 or b == 0:
            result = max(a, b)

        # same chars
        elif s1[a - 1] == s2[b - 1]:
            result = rec(a - 1, b - 1)

        # return minimum from possible operations(insert, delete, replace)
        else:
            result = 1 + min(
                rec(a - 1, b),
                rec(a, b - 1),
                rec(a - 1, b - 1)
            )

        # set to cache
        cache[(a, b)] = result
        
        return result

    return rec(len(s1), len(s2))
