class LRUCache
{
public:
    int size;
    int count = 0;
   
    struct Node
    {
        int key;
        int value;
        Node *previous;
        Node *next;
        Node(int data, int valued)
        {
            key = data;
            value = valued;
            previous = NULL;
            next = NULL;
        }

    } ;
    Node *head = new Node(0,0);
    Node *tail = new Node(1,1);
        
    unordered_map<int, Node*> mp;
    LRUCache(int capacity)
    {

        size = capacity;
        head->next = tail;
        tail->previous = head;
        
    }

    int get(int key)
    {

        if (mp.find(key) != mp.end())
        {
            Node *val = mp[key];
            remove(val);
            insert(val);
            return val->value;
        }
        else
        {
            return -1;
        }
    }

    void put(int key, int value)
    {
        if (mp.find(key) != mp.end())
        {
            Node *existing = mp[key];
            existing->value = value;
            remove(existing);
            insert(existing);
        }
        else
        {
            if (count == size)
            {
                mp.erase(tail->previous->key);
                remove(tail->previous);
                count--;
            }
            Node *created = new Node(key, value);
            insert(created);
            mp[key] = created;
            count++;
        }
    }
    void remove(Node *val)
    {
        Node *temp = val;
        Node *next;
        Node *prev = temp->previous;
         
        next = temp->next;
       
        prev->next = next;
        
        
            next->previous = prev;
        
    }
    void insert(Node *val)
    {
      
        Node *temp = val;
       temp->next = head->next;
       temp->previous = head;
       head->next->previous=temp;
       head->next = temp;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */