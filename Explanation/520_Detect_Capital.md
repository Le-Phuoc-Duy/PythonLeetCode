# 520. Detect Capital
## 1. Đề bài
`Link`: https://leetcode.com/problems/detect-capital/description/
We define the usage of capitals in a word to be right when one of the following cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right. 

Example 1: 
- Input: word = "USA"
- Output: true

Example 2: 
- Input: word = "FlaG"
- Output: false
## 2. Giải thích   
- Trong python, phương thức `upper()` trả về một chuỗi mới trong đó tất cả các ký tự chữ cái thường đã được chuyển thành chữ hoa. Cú pháp `string.upper()`
- Trong python, phương thức `lower()` trả về một chuỗi mới trong đó tất cả các ký tự chữ cái hoa đã được chuyển thành chữ thường. Cú pháp `string.lower()` 
```python
if word.upper() == word or word.lower() == word or word == (word[0].upper() + word[1:].lower()):
    return True
else:
    return False
``` 
- Kiểm tra nếu toàn bộ từ là chữ hoa `(word.upper())`.
- Kiểm tra nếu toàn bộ từ là chữ thường `(word.lower())`.
- Kiểm tra nếu chỉ có ký tự đầu tiên là chữ hoa và các ký tự còn lại là chữ thường `(word[0].upper() + word[1:].lower())`.
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.62 MB
    + Beats: 12.32%