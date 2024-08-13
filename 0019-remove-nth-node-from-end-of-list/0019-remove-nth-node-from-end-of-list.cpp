/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        int count =0;
        ListNode* temp = head;
        if(head->next==NULL) return NULL;
        
        while(temp!=NULL){
            temp=temp->next;
            count++;
        }
        
        int need = count - n;
        ListNode * prev = NULL;
        ListNode * next = NULL;
        temp = head;
        for(int i=0;i<need;i++){
            next = temp->next;
            prev=temp;
            temp=temp->next;
            
        }
        if(temp==head) return head->next;
        
        prev->next = temp->next;
        temp->next = NULL;
        return head;
        
        
        
        
        
        
    }
};