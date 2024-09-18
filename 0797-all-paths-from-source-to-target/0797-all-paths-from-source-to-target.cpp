class Solution {
public:
    vector<vector<int>> result;
    
    void dfs(int node, vector<int> &Path, vector<vector<int>>& graph, int target) {
        // Add the current node to the path
        Path.push_back(node);

        // If the current node is the target, add the path to the result
        if (node == target) {
            result.push_back(Path);
        } else {
            // Explore all neighbors of the current node
            for (int ele : graph[node]) {
                dfs(ele, Path, graph, target);
            }
        }

        // Backtrack: Remove the current node from the path
        Path.pop_back();
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> Path; // Current path
        int target = graph.size() - 1; // The target node is the last node
        dfs(0, Path, graph, target); // Start DFS from the source node (0)
        return result;
    }
};
