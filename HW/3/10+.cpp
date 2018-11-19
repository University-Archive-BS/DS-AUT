/* A C++ program to count all values 
 smaller than a given value in Binary 
 Heap */
 
// A class for Min Heap 
class MinHeap 
{ 
    // pointer to array of elements in heap 
    int *harr; 
  
    // maximum possible size of min heap 
    int capacity; 
    int heap_size; // Current no. of elements. 
public: 
    // Constructor 
    MinHeap(int capacity); 
  
    // to heapify a subtree with root at 
    // given index 
    void MinHeapify(int ); 
  
    int parent(int i) { return (i-1)/2; } 
    int left(int i) { return (2*i + 1); } 
    int right(int i) { return (2*i + 2); } 
  
    // Inserts a new key 'k' 
    void insertKey(int k); 
  
    //Function to print count number of nodes smaller than x 
    int printSmallerThan(int x, int pos); 
}; 
  
// Function to count all elements smaller than x 
int MinHeap::printSmallerThan(int x, int pos=0) 
{ 
    int k = 0;
    if (harr[pos] >= x) 
    { 
        /* Skip this node and its descendants, 
          as they are all >= x . */
        return k; 
    } 
  
    k+=1;
  
    k+=printSmallerThan(x, left(pos)); 
    k+=printSmallerThan(x, right(pos)); 
    return k;
} 