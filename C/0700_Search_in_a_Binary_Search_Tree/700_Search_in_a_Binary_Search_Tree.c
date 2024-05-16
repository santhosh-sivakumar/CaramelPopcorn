struct TreeNode* searchBST(struct TreeNode* root, int val) {
    
    while( root != NULL )
    {
        if( val < root->val )
            root = root->left;
        else if( val > root->val )
            root = root->right;
        else
            return root;
    }

    return NULL;
}