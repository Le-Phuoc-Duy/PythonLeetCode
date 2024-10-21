# 21. Merge Two Sorted Lists
## 1. Đề bài
`Link`: https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
- Input: list1 = [1,2,4], list2 = [1,3,4]
- Output: [1,1,2,3,4,4]

Example 2:
- Input: list1 = [], list2 = []
- Output: []

Example 3:
- Input: list1 = [], list2 = [0]
- Output: [0] 

## 2. Giải thích
### 2.1. Hướng giải quyết bài toán
- Bắt đầu bằng việc so sánh giá trị của các node đầu tiên của list1 và list2.
- Node nào có giá trị nhỏ hơn sẽ được thêm vào danh sách liên kết kết quả.
- Tiếp tục so sánh các node kế tiếp cho đến khi hết một trong hai danh sách.
- Sau đó, nối phần còn lại của danh sách chưa hoàn tất vào kết quả. 
### 2.2. Quy trình giải thuật: 
- Tạo một node tạm thời `tmp` để làm đầu của danh sách kết quả.
- Dùng con trỏ `current` để theo dõi vị trí hiện tại trong danh sách kết quả.
```python
tmp = ListNode()
current = tmp
```
- Duyệt qua `list1` và `list2`:
    + Nếu giá trị của node trong `list1` nhỏ hơn hoặc bằng node trong `list2`, thêm node đó vào danh sách kết quả.
    + Ngược lại, thêm node của `list2` vào danh sách kết quả.
    + Di chuyển con trỏ của danh sách mà node vừa được thêm vào.  
```python
while list1 and list2:
    if(list1.val <= list2.val):
        current.next = list1
        list1 = list1.next 
    else:
        current.next = list2
        list2 = list2.next
    current = current.next
```
- Sau khi một trong hai danh sách kết thúc, nối phần còn lại của danh sách kia vào kết quả.
```python
if list1:
    current.next = list1
if list2:
    current.next = list2
```
- Trả về danh sách kết quả, bỏ qua node tạm thời `return tmp.next`.
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.54 MB
    + Beats: 47.3%
