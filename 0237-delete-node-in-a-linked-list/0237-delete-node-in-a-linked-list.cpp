/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode * former = node -> next;
        node->val = former-> val;
        node->next = former->next;
        former->next = NULL;
        delete(former);
        
        
        
        
        
        
    }
};