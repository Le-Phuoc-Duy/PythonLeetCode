# 69. Sqrt
## 1. Đề bài
`Link`: https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator. For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
- Input: x = 4
- Output: 2
- Explanation: The square root of 4 is 2, so we return 2.

Example 2:
- Input: x = 8
- Output: 2
- Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
## 2. Giải thích 
- Sử dụng phương pháp `binary search`
- Trường hợp đặc biệt: Nếu x là 0 hoặc 1, trả về chính x vì căn bậc hai của 0 và 1 đều là chính nó.
```python
if x == 0 or x == 1:
    return x
```
### 2.1. Tìm kiếm nhị phân
- Khởi tạo hai biến left và right đại diện cho khoảng giá trị có thể là căn bậc hai của x. Ban đầu, left là 1 và right là x.
```python
left = 1
right = x
```
- Tìm giá trị trung bình mid giữa left và right. Sau đó, kiểm tra xem bình phương của mid có nhỏ hơn hoặc bằng x hay không.
    + Nếu mid * mid <= x, căn bậc hai phải lớn hơn hoặc bằng mid, do đó, tiếp tục tìm kiếm ở nửa phải (cập nhật left = mid + 1).
    + Nếu mid * mid > x, căn bậc hai phải nhỏ hơn mid, vì vậy tiếp tục tìm kiếm ở nửa trái (cập nhật right = mid).
```python
    while left<right:
        mid = left + (right - left) // 2
        if(mid<=x/mid):
            left = mid + 1
        else:
            right = mid
```
- Lặp lại quá trình trên cho đến khi ```left >= right```
### 2.2. Một số lưu ý
- Sử dụng `mid = left + (right - left) // 2` thay vì `mid = (left + right ) // 2`:
    + Nếu `left` và `right` đều là những giá trị rất lớn, phép tính `left + right` có thể vượt quá giới hạn của kiểu dữ liệu.
    + Vì vậy khi sử dụng `mid = left + (right - left) // 2`, ta chỉ cộng thêm một giá trị nhỏ `((right - left) // 2)`, do đó sẽ tránh được tình trạng tràn số kể cả khi `left` và `right` rất lớn.
- Sử dụng `mid<=x/mid` thay vì `mid*mid<=x`
    + Tương tự như cách tính `mid` để tránh tràn số, việc sử dụng phép chia `mid <= x / mid` giúp giảm nguy cơ tràn số so với phép tính trực tiếp `mid * mid`.
    + Khi sử dụng phép chia `x / mid`, thay vì tính trực tiếp bình phương của `mid`, ta chỉ thực hiện phép chia. Do đó, ngay cả với những giá trị cực lớn của `x` và `mid`, ta vẫn đảm bảo rằng phép tính nằm trong giới hạn của kiểu dữ liệu và không gây tràn số.
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 1 ms
    + Beats: 99.49%
- Memory:
    + 16.56 MB
    + Beats: 31.1%