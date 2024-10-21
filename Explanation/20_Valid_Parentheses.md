# 20. Valid Parentheses
## 1. Đề bài
`Link`: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1: 
- Input: s = "()"
- Output: true

Example 2:
- Input: s = "()[]{}"
- Output: true

Example 3:
- Input: s = "(]"
- Output: false

Example 4:
- Input: s = "([])"
- Output: true
## 2. Giải thích
### 2.1. Khởi tạo dictionary `myDict`:
```python
myDict = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```
- Sử dụng dictionary để ánh xạ các dấu ngoặc đóng đến dấu ngoặc mở tương ứng. Mỗi dấu ngoặc đóng sẽ phải khớp với dấu ngoặc mở tương ứng.
### 2.2. Kiểm tra chuỗi bắt đầu bằng dấu đóng: 
```python
if s[0] in myDict.keys():
    return False
```
- Nếu ký tự đầu tiên của chuỗi là một dấu ngoặc đóng, chuỗi đó không hợp lệ, vì một chuỗi hợp lệ phải bắt đầu bằng dấu ngoặc mở. Do đó, nếu điều kiện này đúng, hàm trả về `False`.
### 2.3. Sử dụng stack để kiểm tra
```python
stack = []
```
- Cơ chế của stack là Last In, First Out (LIFO), phù hợp để giải quyết bài toán này, vì dấu ngoặc mở gần nhất phải được đóng trước. 
```python
for i in s:
    if i in myDict.values():
        stack.append(i)
```
- Nếu ký tự hiện tại là một dấu ngoặc mở, ta thêm nó vào stack.
```python
else:
    if len(stack) == 0:
        return False
    if stack.pop() != myDict[i]:
        return False
```
- Nếu ký tự hiện tại là một dấu ngoặc đóng, chương trình thực hiện các bước sau:
    + Nếu stack rỗng (tức là không có dấu ngoặc mở nào trước đó), chuỗi không hợp lệ, trả về `False`.
    + Nếu stack không rỗng, chương trình lấy phần tử cuối cùng của stack (dấu ngoặc mở gần nhất) so sánh với dấu ngoặc đóng hiện tại. Nếu không khớp, chuỗi không hợp lệ, trả về `False`.
- Sau khi duyệt hết chuỗi, nếu stack rỗng, tức là tất cả các dấu ngoặc mở đều đã được đóng đúng cách, chuỗi hợp lệ và hàm trả về `True`. Nếu stack còn phần tử, chuỗi không hợp lệ và trả về `False`.
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.74 MB
    + Beats: 23.2%
