class StockSpanner {
public:
    stack<pair<int, int>> st;

    StockSpanner() {
        // No initialization needed
    }
    
    int next(int price) {
        int span = 1;
        
        // Calculate the span for the current price
        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;  // Accumulate the span
            st.pop();
        }
        
        // Push the current price and its span onto the stack
        st.push({price, span});
        
        return span;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
