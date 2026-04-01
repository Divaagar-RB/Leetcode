class Solution {
public:
    string removeStars(string s) {
        stack<char> st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='*' && !st.empty()) st.pop();
            else st.push(s[i]);
        }
        string t;
        while(!st.empty()){
            t=t+st.top();
            st.pop();
        }
        reverse(t.begin(),t.end());
        return t;
    }
};