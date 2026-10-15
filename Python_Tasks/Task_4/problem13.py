
# Problem 13: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    M = int(input())
    set1 = set(map(int, input().split()))

    N = int(input())
    set2 = set(map(int, input().split()))

    result = sorted(set1.symmetric_difference(set2))

    for number in result:
        print(number)
