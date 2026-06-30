# 1916A - 2023

**URL:** https://codeforces.com/problemset/problem/1916/A

```text
A. 2023
time limit per test1 second
memory limit per test256 megabytes

In a sequence 
a
𝑎
, whose product was equal to 
2023
2023
, 
k
𝑘
 numbers were removed, leaving a sequence 
b
𝑏
 of length 
n
𝑛
. Given the resulting sequence 
b
𝑏
, find any suitable sequence 
a
𝑎
 and output which 
k
𝑘
 elements were removed from it, or state that such a sequence could not have existed.

Notice that you are not guaranteed that such array exists.

Input

Each test consists of several test cases. The first line contains a single integer 
t
𝑡
 (
1≤t≤100
1
≤
𝑡
≤
100
) — the number of test cases. This is followed by a description of the test cases.

The first line of each test case contains two integers 
n
𝑛
 (
1≤n,k≤5
1
≤
𝑛
,
𝑘
≤
5
) — the size of sequence 
b
𝑏
 and the number of numbers removed from sequence 
a
𝑎
.

The second line contains 
n
𝑛
 integers 
b
1
,
b
2
,…,
b
n
𝑏
1
,
𝑏
2
,
…
,
𝑏
𝑛
 (
1≤
b
i
≤2023
1
≤
𝑏
𝑖
≤
2023
) — the remaining sequence. The values of 
b
i
𝑏
𝑖
 might not be divisors of 
2023
2023
.

Output

For each test case, output "YES" if the sequence 
a
𝑎
 exists, and in the following line output 
k
𝑘
 non-negative integers that were removed from the sequence 
a
𝑎
. If the sequence 
a
𝑎
 does not exist, output "NO" in a single line.

You can output the answer in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.

Example
input
Copy
7
2 2
5 2
3 1
7 17 7
4 2
1 289 1 1
3 1
7 17 17
1 1
289
1 1
2023
1 3
1
output
Copy
NO
NO
YES
7 1
YES
1
YES
7
YES
1
YES
7 17 17

Note

In third test case product is equal to 
289⋅7=2023
289
⋅
7
=
2023
.

In fourth test case product is already equal to 
2023
2023
.

In seventh test case product is equal to 
7⋅17⋅17=2023
7
⋅
17
⋅
17
=
2023
.
```