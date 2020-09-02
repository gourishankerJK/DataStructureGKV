#include <iostream>
using namespace std;
struct queue {
  int size, front, rear, *list;
};

void createqueue(struct queue *Q) {
  cout << "\nEnter the size of queue: ";
  cin >> Q->size;
  Q->front = -1;
  Q->rear = -1;
  Q->list = new int[Q->size];
}
void insertion(int value, struct queue *Q) {
  // Queue full condition in CircularQueue
  if ((Q->rear == Q->size - 1 && Q->front == 0) or (Q->rear + 1 == Q->front)) {
    cout << "Queue is full !";
  } else if (Q->rear == -1) {
    Q->rear = 0;
    Q->front = 0;
    Q->list[Q->rear] = value;
  } else if ((Q->rear == Q->size - 1) && (Q->front > 0)) {
    Q->rear = 0;
    Q->list[Q->rear] = value;
  } else {
    Q->rear += 1;
    Q->list[Q->rear] = value;
  }
}
int deletion(struct queue *Q) {
  // Empty! Queue condition
  if (Q->front == -1) {
    cout << "            \nQueue is Empty!\n";
  } else if (Q->front == Q->rear) {
    int value = Q->list[Q->front];
    Q->front = -1;
    Q->rear = -1;
    return value;
  } else if ((Q->front == Q->size - 1) && (Q->rear >= 0)) {
    int value = Q->list[Q->front];
    Q->front = 0;
    return value;
  } else {
    int value = Q->list[Q->front];
    Q->front += 1;
    return value;
  }
}
void display(struct queue *Q) {
  cout << "Queue:";
  if (Q->front < Q->rear or Q->front == Q->rear and Q->front != -1) {
    for (int i = Q->front; i < Q->rear + 1; i++) {
      cout << Q->list[i] << "  ";
    }
  } else if (Q->front == -1) {
    cout << "\nQueue Empty!";
  } else {
    for (int i = Q->front; i < Q->size; i++) {
      cout << Q->list[i] << "  ";
    }
    for (int i = 0; i < (Q->rear) + 1; i++) {
      cout << Q->list[i] << "  ";
    }
  }
}
int main() {
  struct queue Q;
  createqueue(&Q);
  cout << "Enter the operation you want to perform:\n";
  cout << "Enter 1 to INSERT\n";
  cout << "Enter 2 to DELETE\n";
  cout << "Enter 4 to exit\n";
  cout << "Enter 3 to display\n";
  while (1) {
    cout << "\nEnter your choice:";
    int option;
    cin >> option;
    if (option == 1) {
      int value;
      cout << "\nEnter the value you want to INSERT:";
      cin >> value;
      insertion(value, &Q);
    } else if (option == 2) {
      int value;
      value = deletion(&Q);
    } else if (option == 4) {
      break;
    } else if (option == 3) {
      display(&Q);
    } else {
      cout << "Invalid option !";
    }
  }
  return 0;
}
