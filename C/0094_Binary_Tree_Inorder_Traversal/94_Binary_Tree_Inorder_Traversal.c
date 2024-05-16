int *OUT;
int rear;

void Inorder(struct TreeNode* root)
{
    if(root == NULL)
        return;
    else
    {
        Inorder(root->left);
        OUT[++rear] = root->val;
        Inorder(root->right);
    }
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {

    OUT = (int*)malloc(100*sizeof(int));
    rear = -1;

    if(root == NULL)
    {
        *returnSize = 0;
        return OUT;
    }
    else
    {
        Inorder(root);
        *returnSize = rear + 1;
        return OUT;
    }
}