# 645. Set Mismatch
## 1. Đề bài
`Link`: https://leetcode.com/problems/set-mismatch/description/

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
- Input: nums = [1,2,2,4]
- Output: [2,3]

Example 2:
- Input: nums = [1,1]
- Output: [1,2]
## 2. Giải thích    
### 2.1. Hướng giải quyết bài toán
- Duyệt qua mảng nums để **tìm số bị lặp lại**.
    + Khi xét một phần tử có giá trị là A, ta cần kiểm tra xem có phần tử nào có giá trị tương tự tồn tại trong danh sách hay không. Cách tiếp cận đơn giản nhất là lặp qua toàn bộ danh sách với mỗi phần tử để kiểm tra, nhưng điều này có độ phức tạp O(n^2). Chúng ta có thể tối ưu bài toán để giảm độ phức tạp xuống O(n).
- Tính toán **số bị mất**
    + Tính tổng của các số từ 1 đến n theo công thức: `Total_sum = n(n+1)/2`
    + Sau đó, tính tổng của các phần tử trong nums.

    + Gọi số bị mất là `lossNumber`, số bị lặp lại là `repetitionNumber`
    + Vì nums là 1 dãy số liên tục, nên `1 + ... + repetitionNumber + lossNumber+... =  n(n+1)/2 = Total_sum`
    + Ta có `1 + ... + repetitionNumber + repetitionNumber +... =  sum(nums)`
    + Vì cậy: `lossNumber = total_su m− (sum(nums) − repetitionNumber)`
### 2.2. Quy trình giải thuật
```python
visited = {}
repetitionNumber = 0 
for idx, num in enumerate(nums):
    if num in visited:
        repetitionNumber = num
        break            
    visited[num] = idx
```
- Khởi tạo một dictionary `visited` để lưu các phần tử và chỉ số của chúng.
- Duyệt qua mảng `nums` với chỉ số i và giá trị num:
    + Nếu num đã xuất hiện trong `visited`, gán `num` cho `repetitionNumber`
    + Nếu num chưa xuất hiện hoặc điều kiện không thỏa mãn, cập nhật `visited[num] = idx`.
```python
n = len(nums)
lossNumber = n*(n+1)//2 -sum(nums) + repetitionNumber
```
- Tính toán lossNumber 
### 2.3. Tại sao lại sử dụng dictionary?
- Khi sử dụng list, câu lệnh ```num in visited``` có độ phức tạp O(n) do phải duyệt qua toàn bộ danh sách. Điều này không phù hợp cho bài toán cần tối ưu.
- Trong khi đó, Dictionary giúp tra cứu xem một phần tử đã tồn tại trong mảng trước đó hay chưa với độ phức tạp là O(1).



## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 4 ms
    + Beats: 99.81%
- Memory:
    + 17.93 MB
    + Beats: 70.52%