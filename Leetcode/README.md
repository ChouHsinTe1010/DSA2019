# Leet Code</br>
為了熟悉Python的語法以及喚醒之前學習Python的記憶，老師在學期初推薦了CodeSignal以及Leetcode。</br>
CodeSignal跟Leetcode都是充滿程式題目的平台，Leetcode的題目比較艱難，適合進階的人使用。而且Leetcode有許多企業考試題目，不過難度都非常高</br>
### 27_Remove Element</br>
題目：原地去除數字組合當中val的所有数字，返回的是數字組合要保留的之前位置。</br>
解法：在所有的值，取出i等於val，然後再刪除。
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/27%23_Remove%20Element_06170145.png)
### 111_Minimum Depth of Binary Tree</br>
題目：找深度最淺的樹</br>
原理：首先看是否有根，沒有的話就結束。有的話就判斷是左邊還右邊。
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/111%23_Minimum%20Depth%20of%20Binary%20Tree_06170145.png)
### 136_Single Number</br>
題目：給一個整數nums, 裡面只有一個數字出現一次，其他都是出現兩次，找出那個孤單的數字。</br>
原理：假如k有出現在n，有出現就append，沒有則remove
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/136%23_Single%20Number_06170145.png)
### 242_Valid Anagram</br>
題目:字謎與答案是否相等，例如 cat 與 cta 為 true ，因為皆包含字母 a、c、t。例如 cat 與 ctk 為 false ，因為有一個字母不符。</br>
原理：sort 是應用在 list 上的方法，sorted 可以對所有的對象排序。
list 的 sort 方法返回的是对已存在的进行操作，無返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是原有基礎上進行的操作。
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/242%23_Valid%20Anagram_06170145.png)
### 441_Arranging Coins</br>
題目：排列硬幣</br>
原理說明-我自畫的
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/Arrange%20Coins.png)

一開始我在第六行輸入有誤
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/441%23_Arranging%20Coins_06170145-1.png)
![](https://github.com/ChouHsinTe1010/DSA2019/blob/master/picture/441%23_Arranging%20Coins_06170145.png)
