# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        output = []
        
        def dfs(root):
            if not root:
                output.append("N")
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(output)
            
        

    def deserialize(self, data):
        stream = data.split(",")
        self.i = 0
        
        def dfs(stream):
            if stream[self.i]=="N":
                self.i += 1
                return None
            node = TreeNode(int(stream[self.i]))
            self.i += 1
            node.left = dfs(stream)
            node.right = dfs(stream)
            return node
        
        return dfs(stream)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))