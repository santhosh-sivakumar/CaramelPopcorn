bool isPalindrome(struct ListNode* head) {
    struct ListNode* temp = head;
    int count = 0;
    
    while(temp != NULL) 
    {
        count++;
        temp = temp->next;
    }
    
    int* arr = malloc(count * sizeof(int));
    if(arr == NULL) 
    {
        return false;
    }
    
    temp = head;
    
    for(int i = 0; i < count; i++) 
    {
        arr[i] = temp->val;
        temp = temp->next;
    }
    
    for(int i = 0; i < count / 2; i++) 
    {
        if(arr[i] != arr[count - 1 - i]) 
        {
            free(arr);
            return false;
        }
    }
    
    free(arr);
    return true;
}
