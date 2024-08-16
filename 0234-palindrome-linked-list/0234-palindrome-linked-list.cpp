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
    bool isPalindrome(ListNode* head) {
        
        if(head->next==NULL) return true;
        ListNode * slow=head;
        ListNode * fast=head ;
        ListNode * prev=NULL;
        ListNode * prevNode=NULL;
        while(fast!=NULL && fast->next!=NULL){
            fast = fast ->next->next;
            prev= slow;
            slow = slow->next;
            
        }
       ListNode * temp = slow;
       ListNode * front;
    
        while(temp!=NULL){
                front=temp->next;
                temp->next=prevNode;
                prevNode=temp;
                temp=front;


        }
        
        
        temp=head;
        while(prevNode!=NULL){
            
            if(prevNode->val!=temp->val){
                return false;
            }
            
            prevNode=prevNode->next;
            
            
            temp=temp->next;
        }
        
        
      return true;  
    }
};