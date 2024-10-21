# 70. Climbing Stairs
## 1. Đề bài
`Link`: https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
- Input: n = 2
- Output: 2
- Explanation: There are two ways to climb to the top.
    + 1 step + 1 step
    + 2 steps
Example 2 
- Input: n = 3
- Output: 3
- Explanation: There are three ways to climb to the top.
    + 1 step + 1 step + 1 step
    + 1 step + 2 steps
    + 2 steps + 1 step
## 2. Giải thích
### 2.1. Hướng giải quyết bài toán:
- Gọi f(n) là một hàm số biểu thị số cách riêng biệt để leo lên đỉnh cầu thang có n bậc
- Tại mỗi bậc n, ta có thể:
    + Đến từ bậc **n-1** (bằng cách leo 1 bậc)
    + Đến từ bậc **n-2** (bằng cách leo 2 bậc)
- Do đó, số cách để đến bậc n là tổng của số cách đến bậc n-1 và bậc n-2. Điều này dẫn đến công thức truy hồi:
```f(n) = f(n−1) + f(n−2)```

### 2.2. Khởi tạo giá trị ban đầu
- Các trường hợp cơ bản là:
    + Nếu n == 1, có duy nhất 1 cách để leo lên đỉnh (bước 1).
    + Nếu n == 2, có 2 cách để leo lên đỉnh (bước 1 + bước 1, hoặc bước 2).  
```python
first, second = 1, 2
```
### 2.3. Tính toán số cách leo
- Sử dụng biến first và second để lần lượt lưu số cách để leo lên bậc thang thứ n-1 và n-2. 
- Mỗi lần tính được `third` (số cách leo lên bậc n), ta cập nhật lại `first` và `second`.
```python
for i in range(3, n + 1):
    third = first + second
    first = second
    second = third
```
- Dùng vòng lặp từ 3 đến n để tính toán số cách leo cho các bậc tiếp theo. 

## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.57 MB
    + Beats: 27.18%
