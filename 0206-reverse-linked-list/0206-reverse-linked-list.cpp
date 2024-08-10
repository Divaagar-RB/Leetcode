class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* temp;
        ListNode* front;
        ListNode* prev;
        temp=head;
        prev=NULL;
    
        while(temp!=NULL){
                front=temp->next;
                temp->next=prev;
                prev=temp;
                temp=front;


        }
        
        return prev;

    }
};