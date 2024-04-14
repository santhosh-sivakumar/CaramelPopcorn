struct ListNode* insert(struct ListNode *head, int val)
{
    struct ListNode *ptr = (struct ListNode*)malloc(sizeof(struct ListNode));
    ptr->val = val;
    ptr->next = head;
    head = ptr;

    return head;
}

bool isPalindrome(struct ListNode* head) 
{
    struct ListNode *tmp  = head, *tmp1 = NULL;

    while(tmp != NULL)
    {
        tmp1 = insert(tmp1, tmp->val);
        tmp = tmp->next;
    }

    tmp = head;
    while(tmp != NULL && tmp1 != NULL)
    {
        if(tmp->val != tmp1->val)
            return false;
        
        tmp = tmp->next;
        tmp1 = tmp1->next;
    }

    return true;
}