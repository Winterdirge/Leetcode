class Solution {
    func towSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        for (index, value) in nums.enumerated() {
            if let other = dict[target - value] {
                return [other, index]
            }
            dict[value] = index
        }
        return []
    }
}
