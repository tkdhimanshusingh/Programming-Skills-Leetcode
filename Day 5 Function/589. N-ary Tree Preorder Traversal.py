class Solution:
    def preorder(self, root):
        r, q = [], root and [root]
        while q:
            node = q.pop()
            r.append(node.val)
            q += [c for c in node.children[::-1] if c]
        return r