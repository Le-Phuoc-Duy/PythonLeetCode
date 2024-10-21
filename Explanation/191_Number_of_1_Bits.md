# 191. Number of 1 Bits
## 1. Đề bài
`Link`: https://leetcode.com/problems/number-of-1-bits/description/
Given a positive integer n, write a function that returns the number of 
set bits in its binary representation (also known as the Hamming weight).

Example 1:
- Input: n = 11
- Output: 3
- Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
- Input: n = 128
- Output: 1
- Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
- Input: n = 2147483645
- Output: 30
- Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits. 


## 2. Giải thích 
```python
maxNumber = max(nums)
check = maxNumber*(maxNumber+1)//2 - sum(nums)
if check == 0:
    return maxNumber+1
return check
```
- Sử dụng hàm ```bin(n)``` để chuyển `n` thành một chuỗi biểu diễn nhị phân của `n`.
- Sử dụng hàm ```count('1')``` để đếm số lần xuất hiện của ký tự '1' trong chuỗi nhị phân của n.
- Trả về kết quả. 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.52 MB
    + Beats: 36.46%