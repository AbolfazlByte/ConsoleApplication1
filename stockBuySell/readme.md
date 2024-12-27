# Stock Buy and Sell Task

## Problem Description
Given the cost of stock on each day in an array `A[]` of size `N`, the task is to find all the segments of days on which buying and selling the stock can generate profit. If no profit can be generated, return an empty list.

### Example 1:
**Input:**
```
N = 7
A[] = {100,180,260,310,40,535,695}
```
**Output:**
```
1
```
**Explanation:**
One possible solution is (0 3) (4 6). We can buy stock on day 0 and sell it on day 3 for maximum profit. Then, buy stock on day 4 and sell it on day 6.

### Example 2:
**Input:**
```
N = 5
A[] = {4,2,2,2,4}
```
**Output:**
```
1
```
**Explanation:**
One of the multiple possible solutions is (3 4). Buy stock on day 3 and sell it on day 4 for maximum profit.

## Your Task
Implement the function `stockBuySell()` which takes the following parameters:
- An array `A[]` representing stock prices for `N` days
- An integer `N` representing the size of the array

### Function Output:
The function must return a 2D list of integers containing all the buy-sell pairs. Each pair is represented as:
- The first value indicates the day to **buy** the stock.
- The second value indicates the day to **sell** the stock.

If no profit can be made, return an empty list.

### Example Code Structure:
```python
def stockBuySell(A, N):
    # Your implementation here
    pass
```

## Constraints:
- 2 ≤ N ≤ 10<sup>6</sup>
- 0 ≤ A[i] ≤ 10<sup>6</sup>

## Expected Complexity
- **Time Complexity:** O(N)
- **Auxiliary Space:** O(N)

## Notes
- Multiple solutions can exist for the same input.
- The driver code will verify the correctness by checking if the output matches any valid solution.
- If no profit is possible, the driver code will output "No Profit."
