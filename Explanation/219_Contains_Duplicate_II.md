# 219. Contains Duplicate II
## 1. Đề bài
`Link`: https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
- Input: nums = [1,2,3,1], k = 3
- Output: true

Example 2:
- Input: nums = [1,0,1,1], k = 1
- Output: true

Example 3:
- Input: nums = [1,2,3,1,2,3], k = 2
- Output: false
## 2. Giải thích 
### 2.1. Hướng giải quyết bài toán
- Bài toán trên khá giống với bài **1. Two Sum** (link tham khảo: https://leetcode.com/problems/two-sum/description/)
- Mục tiêu: Duyệt qua mảng nums và kiểm tra xem đã từng gặp phần tử này trước đó hay chưa.
    + Nếu đã gặp, kiểm tra khoảng cách giữa hai chỉ số của các phần tử giống nhau
    + Nếu khoảng cách này nhỏ hơn hoặc bằng k, trả về True.
    + Nếu không thỏa điều kiện, lưu chỉ số của phần tử hiện tại vào dictionary.
- Khi xét một phần tử có giá trị là A, ta cần kiểm tra xem có phần tử nào có giá trị tương tự tồn tại trong danh sách hay không. Cách tiếp cận đơn giản nhất là lặp qua toàn bộ danh sách với mỗi phần tử để kiểm tra, nhưng điều này có độ phức tạp O(n^2). Chúng ta có thể tối ưu bài toán để giảm độ phức tạp xuống O(n).
### 2.2. Quy trình giải thuật
```python
_dict = {}
for i,num in enumerate(nums): 
    if (num in _dict) and abs(_dict[num] - i)<= k:
        return True
    _dict[num] = i
```
- Khởi tạo một dictionary dict để lưu các phần tử và chỉ số của chúng.
- Duyệt qua mảng nums với chỉ số i và giá trị num:
    + Nếu num đã xuất hiện trong dict, kiểm tra điều kiện `|i - dict[num]| <= k`. Nếu đúng, trả về True.
    + Nếu num chưa xuất hiện hoặc điều kiện không thỏa mãn, cập nhật `dict[num] = i`.
- Nếu không tìm được cặp phần tử thỏa mãn, trả về False.
### 2.3. Tại sao lại sử dụng dictionary?
    + Khi sử dụng list, câu lệnh ```num in List``` có độ phức tạp O(n) do phải duyệt qua toàn bộ danh sách. Điều này không phù hợp cho bài toán cần tối ưu.
    + Trong khi đó, Dictionary giúp tra cứu xem một phần tử đã tồn tại trong mảng trước đó hay chưa với độ phức tạp là O(1).
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 15 ms
    + Beats: 99.92%
- Memory:
    + 29.88 MB
    + Beats: 57.14%