class Solution {
public:
  
bool DFS(stack<int> &stackHistory, int node, vector<vector<int>> &graph, vector<int> &safeState) {
    stackHistory.push(node);

    if (safeState[node] == -1) {
        return false;
    }

    if (safeState[node] == 1) {
        return true;
    }

    safeState[node] = -1; 

    for (int j = 0; j < graph[node].size(); ++j) {
        int nextNode = graph[node][j];
        if (!DFS(stackHistory, nextNode, graph, safeState)) {
            safeState[nextNode] = -1; 
            return false;
        }
    }

    stackHistory.pop();
    safeState[node] = 1;
    return true;
}



    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> result;
        int nodes = graph.size();
    vector<int> safeState(nodes, 0); 
    stack<int> stackHistory;

    for (int i = 0; i < nodes; ++i) {
        if (safeState[i] == 0) { 
            DFS(stackHistory, i, graph, safeState);
        }
    }

  
    for (int i = 0; i < nodes; ++i) {
        if (safeState[i] == 1) {
          result.push_back(i);
        }
    }
        
     return result;   
        
    }
};