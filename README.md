# About Me
<img src='tenor.gif'>
我是周欣德</br>
學校：東吳大學巨量資料管理學院

# 作業集
## [HW1](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW1)
### [1.quicksort程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW1/quick%20sort.py)
## [HW2](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW2)
### [1.heapsort流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW2/Heap%20Sort%20%E6%B5%81%E7%A8%8B%E5%9C%96%26%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)
### [2.mergesort流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW2/Merge%20Sort%E6%B5%81%E7%A8%8B%E5%9C%96%26%20%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)
### [3.heapsort程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW2/heap_sort_06170145.py)
### [4.mergesort程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW2/merge_sort_06170145.py)
### [5.比較](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW2/heapsort%20VS%20mergesort.docx)
## [HW3](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW3)
### [1.BST流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW3/binary_search_tree_06170145_%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)
### [2.BST程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW3/binary_search_tree_06170145.py)
### [3.功能說明](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW3/binary_search_tree_06170145_%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.docx)
## [HW4](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW4)
### [1.hash table流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW4/06170145_hash_table%20%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%26%E5%8E%9F%E7%90%86%26%E6%B5%81%E7%A8%8B%E5%9C%96%E8%AA%AA%E6%98%8E.ipynb)
### [2.hash table程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW4/hash_table_06170145.py)
## [HW5](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW5)
### [1.BFS流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW5/06170145%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)
### [2.BFS程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW5/BFS_06170145.py)
## [HW6](https://github.com/ChouHsinTe1010/DSA2019/tree/master/HW6)
### [1.Dijkstra流程圖](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW6/DijkstraHW%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)
### [2.Dijkstra程式碼](https://github.com/ChouHsinTe1010/DSA2019/blob/master/HW6/Dijkstra_06170145.py)
# R
# Leetcode 
----------
# 資料結構與演算法課程內容
## Week1

## Week2
### **LinkedList**
**Linked List簡介**</br>
Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點。

|      |Linked List                |Array                      |
|------|:-------------------------:|:-------------------------:|                   
|優點   |可以非連續</br>可動態增加、刪除空間</br> |循序存取速度快</br>可靠度高          |
|缺點   |因指標斷裂資料就遺失 |大部分的空間被浪費|
## Week3
### Stack&Queue
**Stack功能：**</br>
- 存取數據的方式為「後進先出」
- Push :將資料放入
- Pop :把「最上面」的資料移除

**Stack實現方法：**</br>
- DFS(深度優先搜尋)

**Queue功能**</br>
- 存取數據的方式為「先進先出」
- Push :將資料從「後方」放入，又稱之enqueue
- Pop :把「最下面」的資料移除又稱之dequeue

**Stack實現方法：**</br>
- BFS(廣度優先搜尋)
## Week4
### Insertion sort
**插入排序法(Insertion Sort)，是一種簡單容易理解的排序演算法，其概念是利用另一個數列來存放已排序部分，逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。**</br>

- 從尚未排序數列取出一元素。
- 由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面。
- 重複以上動作直到全部數列處理完成。
## Week5
### Quick sort 

**時間複雜度**</br>
|      |quicksort時間複雜度          |
|------|:-------------------------:|                  
|Best time|O(nlog n)               |
|Average time|O(nlog n)            |
|wrost time|O(n2)                  |
## Week6
### Heap sort
## Week7
### Merge sort
## Week8
### Binary Tree
## Week9
### Binary Search Tree
## Week10
### Red Black Tree
## Week11
### Hash Table
## Week12
### BFS
## Week13
### DFS
## Week14
### MST-Kruskal
## Week15
### Shortest_path-Dijkstra
## Week16
- review
## Week17
- final exam
## Week18
- no class
