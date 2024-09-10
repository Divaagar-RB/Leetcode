class Solution {
public: 
    void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void buildMaxHeap(vector<int>& arr) {
    int n = arr.size();
    for (int i = (n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

    void deleteRoot(vector<int>& heap) {
    int n = heap.size();
    heap[0] = heap[n - 1];

   
    heap.pop_back();

  
    heapify(heap, n - 1, 0);
}
    int findKthLargest(vector<int>& nums, int k) {
        buildMaxHeap(nums);
        for(int i=0;i<k-1;i++){
            deleteRoot(nums);
            
        }
        
        return nums[0];
        
    }
};