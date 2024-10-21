# 94. Binary Tree Inorder Traversal
## 1. Đề bài
`Link`: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
- Input: root = [1,null,2,3]
- Output: [1,3,2]

Example 2:
- Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
- Output: [4,2,6,5,7,1,3,9,8] 

Example 3: 
- Input: root = [] 
- Output: []

Example 4: 
- Input: root = [1] 
- Output: [1]
## 2. Giải thích 
### 2.1. Hướng giải quyết bài toán:
- Inorder Traversal là một cách duyệt cây nhị phân theo thứ tự: `Trái -> Gốc -> Phải`
- Tại mỗi nút, chúng ta sẽ:
    + Gọi đệ quy để duyệt cây con bên trái.
    + Thêm giá trị của nút hiện tại vào danh sách kết quả.
    + Gọi đệ quy để duyệt cây con bên phải.
### 2.2. Định nghĩa hàm đệ quy: 
```python
ans = []  
def inorder(node: TreeNode):
    if node:
        inorder(node.left)
        ans.append(node.val)
        inorder(node.right)
```  
- Tạo một danh sách `ans` để chứa kết quả.
- Xây dựng một hàm đệ quy `inorder(node)`:
    + Nếu node không phải là **None**, trước tiên ta sẽ gọi hàm đệ quy trên cây con bên trái node.left.
    + Sau đó thêm giá trị của node.val vào danh sách ans.
    + Cuối cùng, gọi hàm đệ quy trên cây con bên phải node.right.
- Sau khi quá trình duyệt kết thúc, danh sách ans chứa các giá trị được duyệt theo thứ tự inorder sẽ được trả về.
## 3. Kết quả (dựa trên leetcode)
- Runtime:
    + 0 ms
    + Beats: 100%
- Memory:
    + 16.68 MB
    + Beats: 6.25%