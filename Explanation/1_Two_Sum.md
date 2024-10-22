# 1. Two Sum
## 1. Đề bài
`Link`: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
- Input: nums = [2,7,11,15], target = 9
- Output: [0,1]
- Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
- Input: nums = [3,2,4], target = 6
- Output: [1,2]

Example 3:
- Input: nums = [3,3], target = 6
- Output: [0,1]
## 2. Giải thích 
- Khi xét một phần tử có giá trị là `A`, ta cần kiểm tra xem phần tử có giá trị `target - A` có tồn tại trong danh sách hay không. Cách tiếp cận đơn giản nhất là lặp qua toàn bộ danh sách với mỗi phần tử để kiểm tra, nhưng điều này có độ phức tạp O(n^2). Chúng ta có thể tối ưu bài toán để giảm độ phức tạp xuống O(n).
- Lưu ý rằng ta cần tránh việc sử dụng cùng một phần tử hai lần, do đó cần lưu trữ thông tin về các phần tử đã duyệt để đảm bảo kết quả trả về luôn dựa trên hai phần tử khác nhau.
    + Ví dụ: nums = [3,1,3], target = 6. Nếu kiểm tra `target - num` trên `nums` sẽ cho kết quả là [0,0]
```python
tmp = {}
for index, num in enumerate(nums):
    if target - num in tmp:
        ... 
    tmp[num] = index
```
- Tại sao lại sử dụng dictionary, không phải list?
    + Khi sử dụng list, câu lệnh ```if target - num in tmp``` có độ phức tạp O(n) do phải duyệt qua toàn bộ danh sách. Điều này không phù hợp cho bài toán cần tối ưu.
    + Trong khi đó, dictionary cho phép kiểm tra và truy xuất giá trị theo key với độ phức tạp O(1). Điều này giúp giảm đáng kể thời gian xử lý, đưa tổng độ phức tạp của thuật toán về O(n).
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 17.85 MB
    + Beats: 13.32%