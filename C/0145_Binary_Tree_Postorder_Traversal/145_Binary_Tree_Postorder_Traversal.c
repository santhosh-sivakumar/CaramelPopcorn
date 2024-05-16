/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int *OUT;
int rear;

void postorder(struct TreeNode* root)
{
    if(root == NULL)
        return;
    else
    {
        postorder(root->left);
        postorder(root->right);
        OUT[++rear] = root->val;
    }
}

int* postorderTraversal(struct TreeNode* root, int* returnSize) {

    OUT = (int*)malloc(100*sizeof(int));
    rear = -1;

    if(root == NULL)
    {
        *returnSize = 0;
        return OUT;
    }
    else
    {
        postorder(root);
        *returnSize = rear + 1;
        return OUT;
    }
}