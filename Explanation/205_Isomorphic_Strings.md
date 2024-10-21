# 205_Isomorphic_Strings
## 1. Đề bài
`Link`: https://leetcode.com/problems/isomorphic-strings/description/
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
- Input: s = "egg", t = "add"
- Output: true
- Explanation: The strings s and t can be made identical by:
    + Mapping 'e' to 'a'.
    + Mapping 'g' to 'd'.

Example 2:
- Input: s = "foo", t = "bar"
- Output: false
- Explanation: The strings s and t cannot be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
- Input: s = "paper", t = "title"
- Output: true
## 2. Giải thích 
### 2.1. Kiểm tra độ dài
- Đầu tiên, kiểm tra xem hai chuỗi s và t có cùng độ dài hay không. Nếu không, chúng không thể là isomorphic, do đó trả về False.
```python
if len(s) != len(t):
    return False
```  
### 2.2. Sử dụng dictionary để theo dõi ánh xạ
```python
mapDict = {}
tmp = ""
for idx,c in enumerate(s):
    if c not in mapDict:
        mapDict[c] = t[idx]
        tmp += t[idx]
    else: 
        tmp += mapDict[c] 
```  
- Biến ```tmp``` được sử dụng để lưu các kí tự với phép ánh xạ đúng 
- Sử dụng một dictionary ```mapDict``` để lưu phép ánh xạ giữa các ký tự của chuỗi `s` và `t` (với key là kí tự được ánh xạ trong `s`, value là kí tự ánh xạ đến trong `t`)
- Duyệt qua từng ký tự trong chuỗi s:
    + Nếu ký tự chưa xuất hiện trong ```mapDict```, ánh xạ ký tự đó đến ký tự tương ứng trong `t` và lưu lại trong biến `tmp`.
    + Nếu ký tự đã xuất hiện trong ```mapDict```, thực hiện ánh xạ tương ứng lưu vào `tmp`.
### 2.3. Kiểm tra ánh xạ duy nhất
```python
if len(set(mapDict.values())) != len(list(mapDict.values())):
   return False
``` 
- Khi xong bước 2.2, `mapDict` có thể có các giá trị 1 value, nhưng lại có 2 key. Để kiểm tra trường hợp này, ta ép `mapDict.values()` thành kiểu dữ liệu set() và list().  
    + Nếu độ dài không bằng nhau, trả về False.
    + Nếu độ dài bằng nhau, ta kiểm tra tmp có bằng t hay không (vì tmp là chuỗi với phép ánh xạ đùng)
```python
return tmp == t
``` 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 3 ms
    + Beats: 99.9%
- Memory:
    + 16.92 MB
    + Beats: 18.59%