# 168. Excel Sheet Column Title
## 1. Đề bài
`Link`: https://leetcode.com/problems/excel-sheet-column-title/description/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Example 1:
- Input: columnNumber = 1
- Output: "A"

Example 2:
- Input: columnNumber = 28
- Output: "AB"

Example 3:
- Input: columnNumber = 701
- Output: "ZY"
## 2. Giải thích 
### 2.1. Khởi tạo biến lưu kết quả `result`:
```python
result = ""
``` 
### 2.2. Kiểm tra chuỗi bắt đầu bằng dấu đóng: 
```python
while columnNumber>0:
    columnNumber -= 1
    remainder = columnNumber%26
    result = chr(remainder + ord("A")) + result
    columnNumber //= 26
```
- Khi chia `columnNumber` cho 26, phần dư sẽ cho biết ký tự nào tương ứng với cột đó. Ví dụ: nếu `columnNumber` là 28, thì 28 % 26 sẽ cho ra 2, tương ứng với ký tự 'B'.
- Hàm `chr()` chuyển đổi mã ASCII thành ký tự. `ord("A")` cho chúng ta mã ASCII của ký tự 'A'. Kết hợp với remainder, chúng ta có thể xác định ký tự tương ứng. Ký tự này sau đó được thêm vào đầu chuỗi result
### 2.3. Tại sao cần có đoạn code `columnNumber -= 1`? 
- Trong Excel, các cột được đánh số từ 1 đến 26 cho các chữ cái từ A đến Z. Sau khi đến Z (26), cột tiếp theo sẽ là AA (27), rồi AB (28), v.v.
- Điều này giống như một hệ thống cơ số 26, nhưng với điểm bắt đầu là 1 thay vì 0.
- Do đó, để đảm bảo rằng giá trị columnNumber khớp với cách đánh số bắt đầu từ A, ta phải giảm columnNumber xuống một đơn vị
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.62 MB
    + Beats: 12.56%