# 1980A - Problem Generator

**URL:** https://codeforces.com/problemset/problem/1980/A

```text
A. Problem Generator
time limit per test1 second
memory limit per test256 megabytes

Vlad is planning to hold 
m
𝑚
 rounds next month. Each round should contain one problem of difficulty levels 'A', 'B', 'C', 'D', 'E', 'F', and 'G'.

Vlad already has a bank of 
n
𝑛
 problems, where the 
i
𝑖
-th problem has a difficulty level of 
a
i
𝑎
𝑖
. There may not be enough of these problems, so he may have to come up with a few more problems.

Vlad wants to come up with as few problems as possible, so he asks you to find the minimum number of problems he needs to come up with in order to hold 
m
𝑚
 rounds.

For example, if 
m=1
𝑚
=
1
, 
n=10
𝑛
=
10
, 
a=
𝑎
=
 'BGECDCBDED', then he needs to come up with two problems: one of difficulty level 'A' and one of difficulty level 'F'.

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

The first line of each test case contains two integers 
n
𝑛
 and 
m
𝑚
 (
1≤n≤50
1
≤
𝑛
≤
50
, 
1≤m≤5
1
≤
𝑚
≤
5
) — the number of problems in the bank and the number of upcoming rounds, respectively.

The second line of each test case contains a string 
a
𝑎
 of 
n
𝑛
 characters from 'A' to 'G' — the difficulties of the problems in the bank.

Output

For each test case, output a single integer — the minimum number of problems that need to come up with to hold 
m
𝑚
 rounds.

Example
input
Copy
3
10 1
BGECDCBDED
10 2
BGECDCBDED
9 1
BBCDEFFGG
output
Copy
2
5
1

```