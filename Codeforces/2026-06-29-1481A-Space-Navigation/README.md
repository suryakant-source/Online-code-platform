# 1481A - Space Navigation 

**URL:** https://codeforces.com/problemset/problem/1481/A

```text
A. Space Navigation
time limit per test2 seconds
memory limit per test256 megabytes

You were dreaming that you are traveling to a planet named Planetforces on your personal spaceship. Unfortunately, its piloting system was corrupted and now you need to fix it in order to reach Planetforces.

Space can be represented as the 
XY
𝑋
𝑌
 plane. You are starting at point 
(0,0)
(
0
,
0
)
, and Planetforces is located in point 
(
p
x
,
p
y
)
(
𝑝
𝑥
,
𝑝
𝑦
)
.

The piloting system of your spaceship follows its list of orders which can be represented as a string 
s
𝑠
. The system reads 
s
𝑠
 from left to right. Suppose you are at point 
(x,y)
(
𝑥
,
𝑦
)
 and current order is 
s
i
𝑠
𝑖
:

if 
s
i
=U
𝑠
𝑖
=
U
, you move to 
(x,y+1)
(
𝑥
,
𝑦
+
1
)
;
if 
s
i
=D
𝑠
𝑖
=
D
, you move to 
(x,y−1)
(
𝑥
,
𝑦
−
1
)
;
if 
s
i
=R
𝑠
𝑖
=
R
, you move to 
(x+1,y)
(
𝑥
+
1
,
𝑦
)
;
if 
s
i
=L
𝑠
𝑖
=
L
, you move to 
(x−1,y)
(
𝑥
−
1
,
𝑦
)
.

Since string 
s
𝑠
 could be corrupted, there is a possibility that you won't reach Planetforces in the end. Fortunately, you can delete some orders from 
s
𝑠
 but you can't change their positions.

Can you delete several orders (possibly, zero) from 
s
𝑠
 in such a way, that you'll reach Planetforces after the system processes all orders?

Input

The first line contains a single integer 
t
𝑡
 (
1≤t≤1000
1
≤
𝑡
≤
1000
) — the number of test cases.

Each test case consists of two lines. The first line in each test case contains two integers 
p
x
𝑝
𝑥
 and 
p
y
𝑝
𝑦
 (
−
10
5
≤
p
x
,
p
y
≤
10
5
−
10
5
≤
𝑝
𝑥
,
𝑝
𝑦
≤
10
5
; 
(
p
x
,
p
y
)≠(0,0)
(
𝑝
𝑥
,
𝑝
𝑦
)
≠
(
0
,
0
)
) — the coordinates of Planetforces 
(
p
x
,
p
y
)
(
𝑝
𝑥
,
𝑝
𝑦
)
.

The second line contains the string 
s
𝑠
 (
1≤|s|≤
10
5
1
≤
|
𝑠
|
≤
10
5
: 
|s|
|
𝑠
|
 is the length of string 
s
𝑠
) — the list of orders.

It is guaranteed that the sum of 
|s|
|
𝑠
|
 over all test cases does not exceed 
10
5
10
5
.

Output

For each test case, print "YES" if you can delete several orders (possibly, zero) from 
s
𝑠
 in such a way, that you'll reach Planetforces. Otherwise, print "NO". You can print each letter in any case (upper or lower).

Example
input
Copy
6
10 5
RRRRRRRRRRUUUUU
1 1
UDDDRLLL
-3 -5
LDLDLDDDR
1 2
LLLLUU
3 -2
RDULRLLDR
-1 6
RUDURUUUUR

output
Copy
YES
YES
YES
NO
YES
NO

Note

In the first case, you don't need to modify 
s
𝑠
, since the given 
s
𝑠
 will bring you to Planetforces.

In the second case, you can delete orders 
s
2
𝑠
2
, 
s
3
𝑠
3
, 
s
4
𝑠
4
, 
s
6
𝑠
6
, 
s
7
𝑠
7
 and 
s
8
𝑠
8
, so 
s
𝑠
 becomes equal to "UR".

In the third test case, you have to delete order 
s
9
𝑠
9
, otherwise, you won't finish in the position of Planetforces.
```