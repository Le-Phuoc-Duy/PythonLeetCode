# 268. Missing Number
## 1. Đề bài
`Link`: https://leetcode.com/problems/missing-number/description/

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
- Input: nums = [3,0,1]
- Output: 2
- Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
- Input: nums = [0,1]
- Output: 2
- Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
- Input: nums = [9,6,4,2,3,5,7,0,1]
- Output: 8
- Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
## 2. Giải thích 
### 2.1. Hướng giải quyết bài toán
- Sử dụng công thức tổng dãy số tự nhiên, tính tổng của dãy số tự nhiên từ **0** đến **n**: ```Sum = n(n+1)/2```
- Tính tổng của dãy số từ 0 đến n và trừ đi tổng các phần tử trong mảng nums. Số chênh lệch giữa hai tổng này chính là số bị thiếu.
### 2.2. Quy trình giải thuật
- Kiểm tra mảng: Nếu min(nums) == 1, nghĩa là số 0 bị thiếu, trả về 0.
```python
if min(nums) == 1:
    return 0
```
- Tìm số lớn nhất: Tìm số lớn nhất trong mảng nums và tính tổng của dãy từ 0 đến số lớn nhất.
- Tính số thiếu: Lấy hiệu giữa tổng dãy và tổng các phần tử của mảng nums.
    + Nếu hiệu bằng 0, nghĩa là số bị thiếu là maxNumber + 1. Ví dụ mảng [0,1,2] thì số bị thiếu là 3
    + Nếu không, trả về giá trị của hiệu (số bị thiếu). 
```python
maxNumber = max(nums)
check = maxNumber*(maxNumber+1)//2 - sum(nums)
if check == 0:
    return maxNumber+1
return check
``` 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 17.61 MB
    + Beats: 95.71%