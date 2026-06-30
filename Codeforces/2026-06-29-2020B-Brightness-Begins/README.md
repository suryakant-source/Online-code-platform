# 2020B - Brightness Begins

**URL:** https://codeforces.com/problemset/problem/2020/B

```text
B. Brightness Begins
time limit per test1 second
memory limit per test256 megabytes

Imagine you have 
n
𝑛
 light bulbs numbered 
1,2,…,n
1
,
2
,
…
,
𝑛
. Initially, all bulbs are on. To flip the state of a bulb means to turn it off if it used to be on, and to turn it on otherwise.

Next, you do the following:

for each 
i=1,2,…,n
𝑖
=
1
,
2
,
…
,
𝑛
, flip the state of all bulbs 
j
𝑗
 such that 
j
𝑗
 is divisible by 
i
†
𝑖
†
.

After performing all operations, there will be several bulbs that are still on. Your goal is to make this number exactly 
k
𝑘
.

Find the smallest suitable 
n
𝑛
 such that after performing the operations there will be exactly 
k
𝑘
 bulbs on. We can show that an answer always exists.

†
†
 An integer 
x
𝑥
 is divisible by 
y
𝑦
 if there exists an integer 
z
𝑧
 such that 
x=y⋅z
𝑥
=
𝑦
⋅
𝑧
.

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

The only line of each test case contains a single integer 
k
𝑘
 (
1≤k≤
10
18
1
≤
𝑘
≤
10
18
).

Output

For each test case, output 
n
𝑛
 — the minimum number of bulbs.

Example
input
Copy
3
1
3
8
output
Copy
2
5
11

Note

In the first test case, the minimum number of bulbs is 
2
2
. Let's denote the state of all bulbs with an array, where 
1
1
 corresponds to a turned on bulb, and 
0
0
 corresponds to a turned off bulb. Initially, the array is 
[1,1]
[
1
,
1
]
.

After performing the operation with 
i=1
𝑖
=
1
, the array becomes 
[
0
–
,
0
–
]
[
0
_
,
0
_
]
.
After performing the operation with 
i=2
𝑖
=
2
, the array becomes 
[0,
1
–
]
[
0
,
1
_
]
.

In the end, there are 
k=1
𝑘
=
1
 bulbs on. We can also show that the answer cannot be less than 
2
2
.

In the second test case, the minimum number of bulbs is 
5
5
. Initially, the array is 
[1,1,1,1,1]
[
1
,
1
,
1
,
1
,
1
]
.

After performing the operation with 
i=1
𝑖
=
1
, the array becomes 
[
0
–
,
0
–
,
0
–
,
0
–
,
0
–
]
[
0
_
,
0
_
,
0
_
,
0
_
,
0
_
]
.
After performing the operation with 
i=2
𝑖
=
2
, the array becomes 
[0,
1
–
,0,
1
–
,0]
[
0
,
1
_
,
0
,
1
_
,
0
]
.
After performing the operation with 
i=3
𝑖
=
3
, the array becomes 
[0,1,
1
–
,1,0]
[
0
,
1
,
1
_
,
1
,
0
]
.
After performing the operation with 
i=4
𝑖
=
4
, the array becomes 
[0,1,1,
0
–
,0]
[
0
,
1
,
1
,
0
_
,
0
]
.
After performing the operation with 
i=5
𝑖
=
5
, the array becomes 
[0,1,1,0,
1
–
]
[
0
,
1
,
1
,
0
,
1
_
]
.

In the end, there are 
k=3
𝑘
=
3
 bulbs on. We can also show that the answer cannot be smaller than 
5
5
.
```