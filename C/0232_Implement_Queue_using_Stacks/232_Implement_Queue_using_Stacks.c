typedef struct node {
    int data;
    struct node* next;
} Node;

typedef struct {
    Node* front;
    Node* rear;
} MyQueue;

MyQueue* myQueueCreate() {
    MyQueue* obj = (MyQueue*)malloc(sizeof(MyQueue));
    obj->front = NULL;
    obj->rear = NULL;
    return obj;
}

void myQueuePush(MyQueue* obj, int x) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = x;
    newNode->next = NULL;

    if (obj->front == NULL && obj->rear == NULL) {
        obj->front = newNode;
        obj->rear = newNode;
    } else {
        obj->rear->next = newNode;
        obj->rear = newNode;
    }
}

int myQueuePop(MyQueue* obj) {
    if (obj->front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }

    Node* temp = obj->front;
    int poppedData = temp->data;
    obj->front = obj->front->next;

    if (obj->front == NULL) {
        obj->rear = NULL;
    }

    free(temp);
    return poppedData;
}

int myQueuePeek(MyQueue* obj) {
    if (obj->front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }

    return obj->front->data;
}

bool myQueueEmpty(MyQueue* obj) {
    return obj->front == NULL;
}

void myQueueFree(MyQueue* obj) {
    while (obj->front != NULL) {
        Node* temp = obj->front;
        obj->front = obj->front->next;
        free(temp);
    }
    free(obj);
}