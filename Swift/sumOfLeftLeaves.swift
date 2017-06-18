/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func sumOfLeftLeaves(_ root: TreeNode?) -> Int {
        
        guard let root = root else {
            return 0
        }
        
        var result = 0
        
        if let leftNode = root.left {
            if leftNode.left == nil && leftNode.right == nil {
                result += leftNode.val
            } else {
                result += sumOfLeftLeaves(leftNode)
            }
        }
        
        result += sumOfLeftLeaves(root.right)
        
        return result
    }
}
