/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    map<int,map<int, vector<int>>> mpp;
    vector<vector<int> > verticalTraversal(TreeNode* root) {
     vector<vector<int> > result;
       myfunction(root,0,0);
       for ( auto &pair : mpp)
       {
           vector<int> temp;
           for( auto &row: pair.second){
               sort(row.second.begin(),row.second.end());
               temp.insert(temp.end(),row.second.begin(),row.second.end());
           }
           result.push_back(temp);
           temp.clear();
       }
       return result;
    }
    void myfunction(TreeNode * root ,int vertical, int level){
        if(root==NULL){
            return ;
        }
       mpp[vertical][level].push_back(root->val);
       myfunction(root->left,vertical-1,level+1);
       myfunction(root->right, vertical+1,level+1);

       
    }

};