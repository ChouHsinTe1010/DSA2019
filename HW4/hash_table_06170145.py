from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
 
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
      

    def add(self, key):
       
        key_MD5 = self.MyCryptoMD5(key)
        key_bucket=key_MD5%(self.capacity)
        if self.data[key_bucket] is None:
            self.data[key_bucket] = ListNode(key_MD5)
        elif self.data[key_bucket].val != key_MD5:
            cur = self.data[key_bucket]
            while cur.next is not None:
                if cur.next.val == key_MD5:
                    print("this key is duplicated")
                    return None
                else:
                    cur=cur.next
            cur.next = ListNode(key_MD5)
        else:
            '''print("this key is duplicated")'''
                     
    def remove(self, key):
        
        key_MD5 = self.MyCryptoMD5(key)
        key_bucket = key_MD5 % (self.capacity)
        cur = self.data[key_bucket]
        pre = None
        while cur is not None:
            if cur.val ==key_MD5:
                if pre is None:
                    self.data[key_bucket]=cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur=cur.next
                    

    def contains(self, key):
        
        key_MD5= self.MyCryptoMD5(key)
        key_bucket= key_MD5%(self.capacity)
        cur = self.data[key_bucket]
        while cur is not None:
            if cur.val == key_MD5:
                return True
            cur=cur.next
        return False    
        
        
    def MyCryptoMD5(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()
        int(h.hexdigest(), 16)
        return int(h.hexdigest(), 16)

