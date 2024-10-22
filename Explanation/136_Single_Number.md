# 136. Single Number
## 1. Đề bài
`Link`: https://leetcode.com/problems/single-number/description/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1: 
- Input: nums = [2,2,1]
- Output: 1

Example 2:
- Input: nums = [4,1,2,1,2]
- Output: 4

Example 3:
- Input: nums = [1]
- Output: 1
## 2. Giải thích 
### 2.1. Hướng giải quyết bài toán
- Theo đề bài, mỗi phần tử trong mảng chỉ xuất hiện một lần duy nhất, ngoại trừ một phần tử (gọi là mảng A). Chúng ta có thể giả định rằng tồn tại một mảng B, trong đó tất cả các phần tử đều xuất hiện hai lần. Từ đó, ta có thể dễ dàng nhận thấy rằng:
  
   `2*(tổng các phần tử trong B) - (tổng các phần tử trong A) = giá trị phần tử xuất hiện 1 lần`

### 2.2. Tạo mảng B
- Trong Python, `set()` là một kiểu dữ liệu cho phép chúng ta lưu trữ các phần tử một cách duy nhất, tức là không có phần tử nào lặp lại trong tập hợp. Nhờ vào đặc điểm này, chúng ta có thể dễ dàng tạo ra mảng B từ mảng A.
  
```python
return 2 * sum(set(nums)) - sum(nums)
```
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 19.15 MB
    + Beats: 23.21%
