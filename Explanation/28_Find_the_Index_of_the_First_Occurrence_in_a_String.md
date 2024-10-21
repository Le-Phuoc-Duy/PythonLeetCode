# 28. Find the Index of the First Occurrence in a String
## 1. Đề bài
`Link`: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
- Input: haystack = "sadbutsad", needle = "sad"
- Output: 0
- Explanation: "sad" occurs at index 0 and 6.
- The first occurrence is at index 0, so we return 0.

Example 2:
- Input: haystack = "leetcode", needle = "leeto"
- Output: -1
- Explanation: "leeto" did not occur in "leetcode", so we return -1.
## 2. Giải thích 
```python
return haystack.find(needle)
```
- Hàm `find` là một phương thức được sử dụng để tìm kiếm một chuỗi con (substring) trong một chuỗi lớn hơn và trả về chỉ số (index) của lần xuất hiện đầu tiên của chuỗi con đó. Nếu chuỗi con không được tìm thấy, hàm trả về -1. 
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.76 MB
    + Beats: 6.93%
