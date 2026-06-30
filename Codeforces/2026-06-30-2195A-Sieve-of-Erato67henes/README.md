# 2195A - Sieve of Erato67henes

**URL:** https://codeforces.com/problemset/problem/2195/A

```text
A. Sieve of Erato67henes
time limit per test1 second
memory limit per test256 megabytes

You are given 
n
𝑛
 positive integers 
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
.

Please determine if it is possible to select any number of elements in 
a
𝑎
, so that their product is 
67
67
.

Note that you may not select zero elements, as the product of zero elements is not defined in this problem.

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

The first line of each test case contains a single integer 
n
𝑛
 (
1≤n≤5
1
≤
𝑛
≤
5
).

The second line of each test case contains 
n
𝑛
 positive integers 
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
≤67
1
≤
𝑎
𝑖
≤
67
).

Output

If it is possible to select elements so that their product is 
67
67
, output "YES" on one line. Otherwise, output "NO" on one line.

You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.

Example
input
Copy
2
5
1 7 6 7 67
5
1 3 5 7 8
output
Copy
YES
NO
Note

In the first test case, you can select 
a
1
𝑎
1
 and 
a
5
𝑎
5
 to get 
a
1
⋅
a
5
=1⋅67=67
𝑎
1
⋅
𝑎
5
=
1
⋅
67
=
67
.

In the second test case, it is impossible to select any number of elements so that their product is 
67
67
.
```