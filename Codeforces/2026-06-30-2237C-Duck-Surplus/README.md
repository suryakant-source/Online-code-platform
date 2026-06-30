# 2237C - Duck Surplus

**URL:** https://codeforces.com/problemset/problem/2237/C

```text
C. Duck Surplus
time limit per test2 seconds
memory limit per test256 megabytes

Ja the Ghost is playing with rubber ducks again! There are 
n
𝑛
 piles of rubber ducks arranged in a row from left to right. Initially, the 
i
𝑖
-th pile contains 
a
i
𝑎
𝑖
 rubber ducks.

While the sequence 
a
𝑎
 is not sorted in nondecreasing order, Ja must perform the following operation:

Choose two adjacent piles such that the left pile contains more ducks than the right pile. Ja swaps these two piles, and then adds the number of ducks in the new left pile to the new right pile.

Formally, choose an index 
i
𝑖
 such that 
1≤i<n
1
≤
𝑖
<
𝑛
 and 
a
i
>
a
i+1
𝑎
𝑖
>
𝑎
𝑖
+
1
. Then replace the adjacent pair 
(
a
i
,
a
i+1
)
(
𝑎
𝑖
,
𝑎
𝑖
+
1
)
 with 
(
a
i+1
,
a
i
+
a
i+1
)
(
𝑎
𝑖
+
1
,
𝑎
𝑖
+
𝑎
𝑖
+
1
)
.

For example, if two adjacent piles contain 
7
7
 and 
3
3
 rubber ducks, then after the operation they contain 
3
3
 and 
10
10
 rubber ducks.

Ja may choose any index satisfying the condition above at each step. It can be shown that, regardless of his choices, the process eventually ends with the sequence sorted in nondecreasing order.

Ja wants the largest pile at the end of the process to contain as few rubber ducks as possible. Determine the minimum possible value of the largest pile.

Input

Each test contains multiple test cases. The first line contains the number of test cases 
t
𝑡
 (
1≤t≤
10
4
1
≤
𝑡
≤
10
4
). The description of the test cases follows.

The first line of each test case contains 
n
𝑛
 (
1≤n≤2⋅
10
5
1
≤
𝑛
≤
2
⋅
10
5
) — the number of piles.

The second line of each test case contains 
n
𝑛
 integers 
a
1
,
a
2
,…,
a
n
𝑎
1
,
𝑎
2
,
…
,
𝑎
𝑛
 (
1≤
a
i
≤
10
9
1
≤
𝑎
𝑖
≤
10
9
) — the number of ducks in each pile.

It is guaranteed that the sum of 
n
𝑛
 over all test cases does not exceed 
2⋅
10
5
2
⋅
10
5
.

Output

For each test case, output a single integer — the minimum possible value of the largest pile.

Example
input
Copy
10
4
1 2 2 5
2
7 3
3
3 2 1
5
2 2 1 3 3
4
3 1 4 2
5
1 4 3 2 5
6
6 2 5 1 4 3
7
2 7 1 6 3 5 4
8
8 1 7 2 6 3 5 4
5
1000000000 999999999 999999998 999999997 999999996
output
Copy
5
10
6
3
6
14
21
26
36
4999999990
Note

In the transformations below, the two underlined numbers are the adjacent pair just obtained by the operation.

In the first test case, the sequence is already sorted in nondecreasing order. Therefore Ja does not perform any operation, and the answer is 
5
5
.

In the second test case, Ja has only one possible operation:
[7,3]→[
3
–
,
10
–
–
–
].
[
7
,
3
]
→
[
3
_
,
10
_
]
.
The sequence is then sorted, so the answer is 
10
10
.

In the third test case, Ja can perform the following operations:
[3,2,1]→[
2
–
,
5
–
,1]→[2,
1
–
,
6
–
]→[
1
–
,
3
–
,6].
[
3
,
2
,
1
]
→
[
2
_
,
5
_
,
1
]
→
[
2
,
1
_
,
6
_
]
→
[
1
_
,
3
_
,
6
]
.
The largest pile contains 
6
6
 ducks. If Ja first chooses the last two piles instead, the final largest pile would contain 
7
7
 ducks. Therefore the answer is 
6
6
.

In the fourth test case, Ja cannot choose the first two piles at the beginning, because 
2
2
 is not greater than 
2
2
. One possible process is
[2,2,1,3,3]→[2,
1
–
,
3
–
,3,3]→[
1
–
,
3
–
,3,3,3].
[
2
,
2
,
1
,
3
,
3
]
→
[
2
,
1
_
,
3
_
,
3
,
3
]
→
[
1
_
,
3
_
,
3
,
3
,
3
]
.
Thus the answer is 
3
3
.

In the fifth test case, one optimal process is
[3,1,4,2]→[
1
–
,
4
–
,4,2]→[1,4,
2
–
,
6
–
]→[1,
2
–
,
6
–
,6].
[
3
,
1
,
4
,
2
]
→
[
1
_
,
4
_
,
4
,
2
]
→
[
1
,
4
,
2
_
,
6
_
]
→
[
1
,
2
_
,
6
_
,
6
]
.
Therefore the answer is 
6
6
.
```