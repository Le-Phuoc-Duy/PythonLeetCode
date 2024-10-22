# 14. Longest Common Prefix
## 1. Đề bài
`Link`: https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
- Input: strs = ["flower","flow","flight"]
- Output: "fl"

Example 2:
- Input: strs = ["dog","racecar","car"]
- Output: ""
- Explanation: There is no common prefix among the input strings.
## 2. Giải thích 
### 2.1. Hướng giải quyết bài toán
- Để xác định tiền tố chung dài nhất giữa một tập hợp các chuỗi, chúng ta cần kiểm tra chuỗi ngắn nhất trong danh sách các chuỗi. Điều này là vì không thể có một tiền tố chung nào dài hơn chuỗi ngắn nhất.
- Sử dụng một vòng lặp để kiểm tra từng chuỗi từ danh sách xem chuỗi ngắn nhất có phải là tiền tố chung hay không. Nếu chuỗi ngắn nhất không phải là tiền tố chung, giảm độ dài của chuỗi ngắn nhất bằng cách loại bỏ ký tự cuối cùng và tiếp tục kiểm tra cho đến khi tìm thấy một tiền tố chung hoặc chuỗi ngắn nhất trở thành chuỗi rỗng.
### 2.2. Xác định chuỗi ngắn nhất
```python
shortest = strs[0]
for s in strs:
    if(len(s)<len(shortest)):
        shortest = s   
```
- Đoạn mã trên sẽ lặp qua từng chuỗi trong danh sách và cập nhật biến shortest nếu tìm thấy chuỗi nào ngắn hơn.
### 2.3. Kiểm tra tiền tố chung
```python
while(len(shortest)>=0):
    flag = True 
    for s in strs:
        if s.find(shortest) != 0:
            flag = False
            break
    if flag:
        break
    else:
        shortest = shortest[0:len(shortest)-1]
```

## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 2 ms
    + Beats: 99.89%
- Memory:
    + 16.61 MB
    + Beats: 14%
