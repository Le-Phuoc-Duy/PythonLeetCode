# 66. Plus One
## 1. Đề bài
`Link`: https://leetcode.com/problems/plus-one/description/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits. 

Example 1: 
- Input: digits = [1,2,3]
- Output: [1,2,4]
- Explanation: The array represents the integer 123.
- Incrementing by one gives 123 + 1 = 124.
- Thus, the result should be [1,2,4].

Example 2: 
- Input: digits = [4,3,2,1]
- Output: [4,3,2,2]
- Explanation: The array represents the integer 4321.
- Incrementing by one gives 4321 + 1 = 4322.
- Thus, the result should be [4,3,2,2].

Example 3:
- Input: digits = [9]
- Output: [1,0]
- Explanation: The array represents the integer 9.
- Incrementing by one gives 9 + 1 = 10.
- Thus, the result should be [1,0].
## 2. Giải thích
### 2.1. Duyệt từ phải sang trái:
- Chương trình bắt đầu duyệt chữ số cuối cùng của mảng (chữ số thấp nhất) và kiểm tra từng chữ số. Điều này giúp dễ dàng xử lý việc "nhớ" khi có sự chuyển đổi từ 9 thành 0.
```python
t = len(digits) - 1
while(t>=0):
```
### 2.2. Xử lý từng chữ số:
```python
if digits[t] != 9:
    digits[t] = int(digits[t]) + 1
    break
```
- Nếu gặp một chữ số không phải 9, chương trình sẽ tăng giá trị của chữ số đó thêm 1 và dừng lại, vì không cần phải điều chỉnh các chữ số bên trái.
```python
digits[t] = 0
...
t = t - 1
```
- Nếu gặp chữ số 9, chương trình sẽ đặt nó thành 0 và tiếp tục kiểm tra chữ số bên trái.
### 2.3. Thêm chữ số mới nếu cần:
```python
if t == 0:
    digits.insert(0,1)
```
- Nếu xử lý đến chữ số đầu tiên của mảng và nó cũng là 9, chương trình sẽ thêm chữ số 1 vào đầu mảng. Điều này xảy ra trong trường hợp mảng ban đầu chỉ chứa các chữ số 9, ví dụ như `[9, 9, 9]`, sau khi tăng sẽ trở thành `[1, 0, 0, 0]`. 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.76 MB
    + Beats: 7.02%
