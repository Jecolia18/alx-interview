#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_w, bens_w = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes_num = [True for _ in range(1, n + 1, 1)]
    primes_num[0] = False
    for i, is_prime in enumerate(primes_num, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes_num[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes_num[0: n])))
        bens_w += primes_count % 2 == 0
        marias_w += primes_count % 2 == 1
    if marias_w == bens_w:
        return None
    return 'Maria' if marias_w > bens_w else 'Ben'
