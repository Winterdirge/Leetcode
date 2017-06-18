class Solution
{
public:
	ListNode* addTwoNumbers(ListNode *l1, ListNode *l2) {
		ListNode *preHead = new ListNode(0);
		ListNode *node = preHead;
		int help = 0;
		while(l1 || l2 || help) {
			int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + help;
			help = sum / 10;
			node->next = new ListNode(sum % 10);
			node = node->next;
			l1 = l1 ? l1->next : l1;
			l2 = l2 ? l2->next : l2;
		}
		return preHead->next;
	}
};