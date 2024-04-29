/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* insertEnd(int value, struct ListNode *head)
{
    struct ListNode *tmp = head;
    if(head == NULL)
    {
        head = (struct ListNode*)malloc(sizeof(struct ListNode));
        head->val = value;
        head->next = NULL;
    }
    else
    {
        struct ListNode *newNode = (struct ListNode*)malloc(sizeof(struct ListNode));

        while(tmp->next != NULL)
            tmp = tmp->next;
        
        newNode->val = value;
        newNode->next = NULL;

        tmp->next = newNode;
    }

    return head;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *L1 = list1, *L2 = list2, *L3 = NULL;

    while(L1 != NULL && L2 != NULL)
    {
        if(L1->val < L2->val)
        {
            L3 = insertEnd(L1->val, L3);
            L1 = L1->next;
        }
        else
        {
            L3 = insertEnd(L2->val, L3);
            L2 = L2->next;
        }
    }

    if(L1 != NULL)
    {
        while(L1 != NULL)
        {
            L3 = insertEnd(L1->val, L3);
            L1 = L1->next;
        }
    }
    else
    {
        while(L2 != NULL)
        {
            L3 = insertEnd(L2->val, L3);
            L2 = L2->next;
        }
    }

    return L3;
}