# 58. Length of Last Word
## 1. Đề bài
`Link`: https://leetcode.com/problems/length-of-last-word/description/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximalsubstring consisting of non-space characters only.

Example 1: 
- Input: s = "Hello World"
- Output: 5
- Explanation: The last word is "World" with length 5. 

Example 2:
- Input: s = "   fly me   to   the moon  "
- Output: 4
- Explanation: The last word is "moon" with length 4.

Example 3:
- Input: s = "luffy is still joyboy"
- Output: 6
- Explanation: The last word is "joyboy" with length 6.
## 2. Giải thích 
```python
return len(s.split()[-1]) 
```
- Phương thức `split()` được sử dụng để tách chuỗi thành một danh sách các phần tử dựa trên một ký tự phân cách nhất định. 
    + Khi phương thức `split()` được gọi mà không có tham số nào, Python sẽ tự động tách chuỗi dựa trên khoảng trắng (spaces, tabs, newline) và loại bỏ tất cả các khoảng trắng dư thừa.
- Sau khi tách, đoạn code sử dụng chỉ số `-1` để lấy từ cuối cùng trong danh sách.
- Cuối cùng, hàm `len()` được sử dụng để tính chiều dài của từ cuối cùng vừa lấy được 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.76 MB
    + Beats: 23.9%
