# 이진 트리 : 자식 노드 최대 2개
# 완전 이진 트리 : 노드 삽입시 왼쪽부터 채워나간 트리
# 이진 탐색 트리 : 왼쪽 노드와 그 이하 자식 노드들이 현재의 노드보다 작아야하고, 
#                    오른쪽 노드와 그 이하 자식들을 현대의 노드보다 커야함
# AVL 트리 : 스스로 균형 잡는 트리
#            높이가 h일때 이진 탐색 트리의 시간복잡도 O(h)
# heap : 최대, 최소값을 찾아내는 연산을 하기 위한 완전 이진 트리를 기본으로한 자료구조
#        - max heap : 부모노드의 키 값 > 자식 노드 키 값             
#        - min heap : 부모노드의 키 값 < 자식 노드 키 값   

# 순회 :
# 1. 전위 순회(preorder) : 중간 - 왼 - 오
# 2. 중위 순회(inorder) : 왼 - 중간 - 오
# 3. 후위 순회(postorder) : 왼 - 오 - 중간

class Node:
    def __init__(self, value): # 이진 트리라서 left, right만 있음
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, root): # root 노드가 head (head에는 Node 인스턴스가 들어가는 듯)
        self.root = root
        
        self.preorderList = []
        self.inorderList = []
        self.postorderList = []
        
    def insert(self, value):
        self.current_node = self.root # 현재 노드는 root로 잡고
        
        while True: # 순회
            # insert value < 현재 노드 값
            if value < self.current_node.value:
                if self.current_node.left != None: # 현재 노드에 left 노드 있으면
                    self.current_node = self.current_node.left # 왼쪽 노드로 내려가기
                else: # 현재 노드에 left 노드 없으면
                    self.current_node.left = Node(value) # 현재 노드의 왼쪽에 삽입
                    break
            
            # insert value > 현재 노드 값
            else:
                if self.current_node.right != None: # 현재 노드에 right 노드 있으면
                    self.current_node = self.current_node.right # 오른쪽 노드로 내려가기
                else: # 현재 노드에 right 노드 없으면
                    self.current_node.right = Node(value) # 현재 노드의 오른쪽에 삽입
                    break
            
    def search(self, value):
        self.current_node = self.root
        
        while self.current_node:
            if self.current_node.value == value: # 값을 찾았을 경우
                return True
            elif value < self.current_node.value: # 찾는 값 < 현재 노드의 값 -> 왼쪽으로 내려가기
                self.current_node = self.current_node.left
            else: # 찾는 값 > 현재 노드의 값 -> 오른쪽으로 내려가기 
                self.current_node = self.current_node.right
        return False
    
    def delete(self, value):
        searched = False # 삭제할 값 존재 유무
        self.current_node = self.root
        self.parent = self.root
        
        # 삭제한 Node 탐색
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        # 삭제할 노드가 존재하지 않으면 종료
        if searched == False:
            return False
        
        # current_node = 삭제할 노드
        # Case 1 ) 삭제할 노드가 child를 가지고 있지 않은 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value: # 삭제할 노드 위치가 parent 노드의 왼쪽
                self.parent.left = None
            else: # 삭제할 노드 위치가 parent 노드의 오른쪽
                self.parent.right = None
                
            del self.current_node # child 없으니까 삭제
        
        # case 2 ) 삭제할 노드가 1개의 child를 가진 경우
        # case 2 - 1 ) 삭제 할 노드가 left child를 가진 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value: # 삭제할 노드 위치가 parent 노드의 왼쪽
                self.parent.left = self.current_node.left
            else: # 삭제할 노드 위치가 parent 노드의 오른쪽
                self.parent.right = self.current_node.left
        
        # case 2 - 2 ) 삭제 할 노드가 right child를 가진 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value: # 삭제할 노드 위치가 parent 노드의 왼쪽
                self.parent.left = self.current_node.right
            else: # 삭제할 노드 위치가 parent 노드의 오른쪽
                self.parent.right = self.current_node.right
            
        # case 3 ) 삭제 할 노드가 left, right 2개의 child를 가진 경우
        if self.current_node.left != None and self.current_node.right != None:
            # case 3-1) 삭제할 노드가 parent의 왼쪽에 위치
            if value < self.parent.value:
                # 대체할 노드 찾기 (= 삭제할 노드 다음으로 큰 값)
                # >> 삭제할 노드의 오른쪽 노드로 한번 옮겨간뒤, 가장 작은 node(= left node None일때까지 내려가기)
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                
                while self.change_node.left != None:
                    self.change_node.parent = self.change_node
                    self.change_node = self.change_node.left
                
                # 대체 노드의 right 노드 존재 여부
                if self.change_node.right != None: # right 노드 존재 O
                    # 대체할 노드는 사라질거니까, 대체할 노드의 parent와 삭제할 노드의 오른쪽 sub Tree 연결
                    self.change_node_parent.left = self.change_node.right
                else: # right 노드 존재 X
                    self.change_node_parent.left = None
                    
                # current 노드 사라지고, 그자리에 change_node로 대체
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
                
            # case 3-2) 삭제할 노드가 parent의 오른쪽에 위치
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                    
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                    
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
    
    # 선위순회
    def preorder(self):
        def _preorder(node):
            print(node.value, end = " ")
            self.preorderList.append(node.value)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    # 중위순회
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.value, end = " ")
            self.inorderList.append(node.value)
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
        
    # 후위순회
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.value, end = " ")
            self.postorderList.append(node.value)
        _postorder(self.root)

BST = NodeMgmt(Node(35))
BST.insert(20)
BST.insert(10)
BST.insert(5)
BST.insert(15)
BST.insert(30)
BST.insert(25)
BST.insert(28)
BST.insert(45)
BST.insert(40)

# 20 삭제하기전 중위 순회
BST.inorder()
print()

# 20 삭제
BST.delete(20)

# 20 삭제후 중위 순회
# >> root.left = 25 (35의 왼쪽 node)
# >> root.left.right = 30 (25의 오른쪽 node)
# >> root.left.right.left = 28 (30의 왼쪽 node)
BST.inorder()
print()
