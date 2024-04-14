struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode *tmp, *tmp1 = NULL, *tmp2 = head;

    while(tmp2 != NULL && tmp2->val == val)
    {
        tmp = tmp2;
        tmp2 = tmp2->next;
        head = tmp2;
        free(tmp);
    }

    while(tmp2 != NULL)
    {
        if(tmp2->val == val)
        {
            tmp = tmp2;
            tmp1->next = tmp2->next;
            tmp2 = tmp2->next;
            free(tmp);
        }
        else
        {
            tmp1 = tmp2;
            tmp2 = tmp2->next;
        }
    }

    return head;
}