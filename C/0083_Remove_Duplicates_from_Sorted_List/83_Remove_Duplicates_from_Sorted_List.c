/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL)
    {
        return head;
    }
    else
    {
        struct ListNode *ptr = head, *tmp = head->next;

        while(tmp != NULL)
        {
            if(ptr->val == tmp->val)
            {
                ptr->next = tmp->next;
                free(tmp);
                tmp = ptr->next;
            }
            else
            {
                ptr = tmp;
                tmp = tmp->next;
            }
        }    

        return head;

    }
}