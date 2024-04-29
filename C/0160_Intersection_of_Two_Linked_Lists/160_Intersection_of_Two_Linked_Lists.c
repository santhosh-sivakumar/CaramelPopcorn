int listLength(struct ListNode *head)
{
    int len = 0;
    while(head != NULL)
    {
        ++len;
        head = head->next;
    }

    return len;
}


struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int lenA = listLength(headA), lenB = listLength(headB);

    int i = 0;
    if(lenA > lenB)
    {
        for(i = 0; i < lenA - lenB; i++)
            headA = headA->next;
    }
    else
    {
        for(i = 0; i < lenB - lenA; i++)
        {
            headB = headB->next;
        }
    }

    while(headA != NULL && headB != NULL)
    {
        if(headA == headB)
            return headA; // (or) headB //
        headA = headA->next;
        headB = headB->next;
    }

    return NULL;
}