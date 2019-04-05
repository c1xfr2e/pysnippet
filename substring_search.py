# implementation of brute force sub-string search


def brute_force(s, t):
    i = 0
    while i < len(s):
        j = 0
        while i < len(s) and j < len(t) and s[i] == t[j]:
            i += 1
            j += 1
        if j == len(t):
            return i - j
        else:
            i = i - j + 1

    return -1


# implementation details for KMP algorithm based on next array
def kmp_calc_next(s):
    next = [0] * len(s)
    j = -1
    next[0] = j
    for i in range(1, len(s)):
        while True:
            if j == -1 or s[j] == s[i - 1]:
                break
            else:
                j = next[j]
        j += 1
        next[i] = j

    return next


def kmp_search(s, t):
    next = kmp_calc_next(t)
    i = 0
    j = 0
    while i < len(s):
        while i < len(s) and j < len(t) and s[i] == t[j]:
            i += 1
            j += 1
        if j == len(t):
            return i - j
        elif next[j] != -1:
            j = next[j]
        else:
            j = 0
            i += 1

    return -1


# implementation details for Z algorithm
def z_naive(s):
    Z = [len(s)]

    for k in range(1, len(s)):
        n = 0
        while n + k < len(s) and s[n + k] == s[n]:
            n += 1
        Z.append(n)

    return Z


def z_advanced(s):
    """An advanced computation of Z-values of a string."""

    Z = [0] * len(s)
    Z[0] = len(s)

    rt = 0
    lt = 0

    for k in range(1, len(s)):
        if k > rt:
            # If k is outside the current Z-box, do naive computation.
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k + n - 1
        else:
            # If k is inside the current Z-box, consider two cases.
            p = k - lt  # Pair index.
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1

    return Z
