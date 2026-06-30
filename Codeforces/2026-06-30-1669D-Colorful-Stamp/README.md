# 1669D - Colorful Stamp

**URL:** https://codeforces.com/problemset/problem/1669/D

```text
D. Colorful Stamp
time limit per test1 second
memory limit per test256 megabytes

A row of 
n
𝑛
 cells is given, all initially white. Using a stamp, you can stamp any two neighboring cells such that one becomes red and the other becomes blue. A stamp can be rotated, i.e. it can be used in both ways: as 
BR
B
R
 and as 
RB
R
B
.

During use, the stamp must completely fit on the given 
n
𝑛
 cells (it cannot be partially outside the cells). The stamp can be applied multiple times to the same cell. Each usage of the stamp recolors both cells that are under the stamp.

For example, one possible sequence of stamps to make the picture 
BRBBW
B
R
B
B
W
 could be 
WWWWW→WW
RB
–
–
–
W→
BR
–
–
–
RBW→B
RB
–
–
–
BW
WWWWW
→
WW
R
B
_
W
→
B
R
_
R
B
W
→
B
R
B
_
B
W
. Here 
W
W
, 
R
R
, and 
B
B
 represent a white, red, or blue cell, respectively, and the cells that the stamp is used on are marked with an underline.

Given a final picture, is it possible to make it using the stamp zero or more times?

Input

The first line contains an integer 
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
) — the number of test cases.

The first line of each test case contains an integer 
n
𝑛
 (
1≤n≤
10
5
1
≤
𝑛
≤
10
5
) — the length of the picture.

The second line of each test case contains a string 
s
𝑠
 — the picture you need to make. It is guaranteed that the length of 
s
𝑠
 is 
n
𝑛
 and that 
s
𝑠
 only consists of the characters 
W
W
, 
R
R
, and 
B
B
, representing a white, red, or blue cell, respectively.

It is guaranteed that the sum of 
n
𝑛
 over all test cases does not exceed 
10
5
10
5
.

Output

Output 
t
𝑡
 lines, each of which contains the answer to the corresponding test case. As an answer, output "YES" if it possible to make the picture using the stamp zero or more times, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example
input
Copy
12
5
BRBBW
1
B
2
WB
2
RW
3
BRB
3
RBB
7
WWWWWWW
9
RBWBWRRBW
10
BRBRBRBRRB
12
BBBRWWRRRWBR
10
BRBRBRBRBW
5
RBWBW
output
Copy
YES
NO
NO
NO
YES
YES
YES
NO
YES
NO
YES
NO

Note

The first test case is explained in the statement.

For the second, third, and fourth test cases, it is not possible to stamp a single cell, so the answer is "NO".

For the fifth test case, you can use the stamp as follows: 
WWW→W
RB
–
–
–
→
BR
–
–
–
B
WWW
→
W
R
B
_
→
B
R
_
B
.

For the sixth test case, you can use the stamp as follows: 
WWW→W
RB
–
–
–
→
RB
–
–
–
B
WWW
→
W
R
B
_
→
R
B
_
B
.

For the seventh test case, you don't need to use the stamp at all.
```