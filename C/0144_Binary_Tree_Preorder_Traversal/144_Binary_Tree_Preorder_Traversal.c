int *OUT;
int rear;

void Preorder(struct TreeNode* root)
{
    if(root == NULL)
        return;
    else
    {
        OUT[++rear] = root->val;
        Preorder(root->left);
        Preorder(root->right);
    }
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {

    OUT = (int*)malloc(100*sizeof(int));
    rear = -1;

    if(root == NULL)
    {
        *returnSize = 0;
        return OUT;
    }
    else
    {
        Preorder(root);
        *returnSize = rear + 1;
        return OUT;
    }
}