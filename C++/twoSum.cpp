class Solution
{
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> help;
		vector<int> result;
		for (int i = 0; i < nums.size(); ++i) {
			int numberToFind = target - nums[i];

			if (help.find(numberToFind) != help.end()) {
				result.push_back(help[numberToFind]);
				result.push_back(i);
			}
			help[nums[i]] = i;
		}
		return result;
	}
};