
def main(n, heights):
    max_height = max(heights)
    maxL = [-1]
    maxR = [-1]
    max_height_left = heights[0]
    for i in range(1, n):
        if max_height_left > heights[i]:
            maxL.append(max_height_left)
        else:
            max_height_left = heights[i]
            maxL.append(-1)
    max_height_right = heights[-1]
    for i in range(n - 2, -1, -1):
        if max_height_right > heights[i]:
            maxR.append(max_height_right)
        else:
            max_height_right = heights[i]
            maxR.append(-1)
    L = []
    for i in range(n):
        left = maxL[i]
        right = maxR[n-1-i]
        if (left == -1 or right == -1):
            L.append(0)
        else:
            L.append(max_height - heights[i] - abs(left - right))
    L += [0]
    s = []
    ma = 0
    for i in range(0, len(L)):
        j = i
        while len(s) > 0 and s[-1][0] >= L[i]:
            val, j = s.pop()
            ma = max(ma, (i-j)*val)
        s.append([L[i], j])
    print(ma)


n = int(input())
heights = list(map(int, input().split()))

main(n, heights)