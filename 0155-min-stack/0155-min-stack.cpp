class MinStack {
public:
     stack<int> st;
     int  minimum = INT_MAX;
      stack<int>mini;
    MinStack() {
        
       
        
    }
    
    void push(int val) {
        st.push(val);
        if( mini.empty()|| val<=mini.top() )
        {
           
            mini.push(val);
            cout<<mini.top()<<endl;
            
        }
        
    }
    
    void pop() {
        if(mini.top()==st.top()) mini.pop();
        st.pop();
        
    }
    
    int top() {
        return st.top();
        
    }
    
    int getMin() {
        return mini.top();
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */