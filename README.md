# About Me
<img src='tenor.gif'>
我是周欣德</br>
學校：東吳大學巨量資料管理學院
程式語言：

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

# Leetcode 
## [Codesignal](https://github.com/ChouHsinTe1010/DSA2019/tree/master/Codesignal)


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
- 重複以上動作直到全部數列處理完成。</br>
**時間複雜度**</br>

|      |Quick sort 時間複雜度        |
|------|:-------------------------:|                 
| Best time  |O(n^2) |
|Average Time|O(n)|
|Wrost Time  |O(n^2)|
## Week5
### Quick sort 

**時間複雜度**</br>

|      |Quick sort 時間複雜度        |
|------|:-------------------------:|                 
| Best time  |O(nlog n) |
|Average Time|O(nlog n)|
|Wrost Time  |O(n^2)|
## Week6
### Heap sort

**定義**</br>
使用heap這種資料結構所設計的一種排序演算法。heap是一個近似完全二元樹的結構，並同時滿足heap的性質：即子節點的鍵值或索引總是小於（或者大於）它的父節點。</br>
**建立步驟：**</br>
- 將所有數儲存到heap中
- 取出root，與子結點相比較
- 重新排序
- 直到heap成遞降次序</br>
**流程圖**</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/heapsort1.png)
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/heapsort2.png)
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/heapsort3.png)
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/heapsort4.png)
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/heapsort5.png)</br>
**時間複雜度**</br>

|      |Heap sort 時間複雜度        |
|------|:-------------------------:|                 
| Best time  |O(nlog n) |
|Average Time|O(nlog n)|
|Wrost Time  |O(nlog n)|
## Week7
### Merge sort</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/mergesort.png)</br>
**時間複雜度**</br>

|      |Merge sort 時間複雜度        |
|------|:-------------------------:|                 
| Best time  |O(nlog n) |
|Average Time|O(nlog n)|
|Wrost Time  |O(nlog n)|
## Week8
### Binary Tree
## Week9
### Binary Search Tree
**流程圖**</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BST.png)</br>
**搜尋search**</br>
1.搜尋方式如下，一開始比大小，然後再分別向下或是向左移動。</br>
2.直到找到值。</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BST%20Search.png)</br>
**新增insert**</br>
1.先判斷是有root</br>
2.要插入的值和root比較，如果較小的話會往左半部，而如果較大的話則往右半部</br>
3.繼續往下執行，會在遇到空值可以填入的時候停止。</br>
***比較特別的時候是遇到重複的數，會先有一個暫存的位置，再相接。***</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BST%20Insert.png)</br>
**刪除Delete**</br>
1.主要有4種情形，分別為無子節點、一個左子節點、一個右子節點以及兩個子節點。一個左子節點最複雜。因為會考慮到重複的數值。</br>
2.無子節點-只需要直接刪除，不需考慮其他狀況。</br>
3.一個右子節點-刪除後，將子節點往上移動。</br>
4.一個左子節點-刪除後，將子節點往上。但是有可能會遇到重複的情形。</br>
5.兩個子節點-考慮左側選取最大值，右側則選取最小值。</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BST%20Delete.png)</br>
**修改Modify**</br>
1.運用Delete、Insert兩個概念結合。</br>
2.先Delete再Insert。</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BST%20Modify.png)</br>
## Week10
### Red Black Tree
## Week11
### Hash Table
Hash function 老師提過好像每個人的身分證字號，具有唯一性。 </br>
***性質***</br>
- 運算速度快
- 不可逆性：無法從雜湊值推回原本的資料是什麼
- 如果兩個雜湊值是不相同的（根據同一函式），那麼這兩個雜湊值的原始輸入也是不相同的。
- 如果兩個雜湊值是相同的（根據同一函式），那麼這兩個雜湊值的原始輸入不一定是相同的。
- 即便輸入非常大的數據（key長度不同），輸出數值的長度都一樣長。
***流程圖***</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/hash%20table.png)
## Week12
### BFS
***流程圖***</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BFS%20VS%20DFS-BFS.png)
## Week13
### DFS
***流程圖***</br>
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/BFS%20VS%20DFS-DFS.png)

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
# 學習感想
我這學期學會最重要的能力就是自學，過往自己會很依賴老師、或是直接得到答案。但是我經過這學期後我發現自學是件很重要的能力，因為老師們教的專業能力，絕對無法滿足我們面對未來的競爭，因為技術是會無條件進步。我們現在運用套件來簡化流程，但是有時候如果套件更新了又或者是套件移除了。那麼我們難道就無法進行我們所要的動作了嗎？這個就有自我摸索自我學習，這樣得到的才是自己所學。

