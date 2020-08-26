#include <stdio.h>
#include <stdlib.h>

struct stack {
  int size, top, *S;
};

void creatstack(struct stack *st) {
  printf("\nEnter the size of Stack: ");
  scanf("%d", &st->size);
  st->top = -1;
  st->S = (int *)malloc(st->size * sizeof(int));
}

void display(struct stack st) {
  for (int i = st.top; i >= 0; i--) {
    printf("\n%d", st.S[i]);
  }
}

void push(struct stack *st, int value) {
  if (st->top == st->size - 1) {
    printf("\nstack overflow\n");
  } else {
    st->top++;
    st->S[st->top] = value;
    printf("\n%d is added in stack\n", value);
  }

  int pop(struct stack * st) {
    int x = -1;
    if (st->top == -1) {
      printf("stack is underflow\n");
    } else {
      x = st->S[st->top];
      st->top--;
      printf("\n%d is removed from stack\n", x);
    }
    return x;
  }

  int main() {
    struct stack st;
    creatstack(&st);
    while (1) {
      printf("\npress 1 for push\npress 2 for pop\npress 3 for display\npress "
             "4 for exit\nenter choice: ");
      int choice;
      scanf("%d", &choice);
      if (choice == 1) {
        int value;
        printf("enter the value: ");
        scanf("%d", &value);
        push(&st, value);
      } else if (choice == 2) {
        pop(&st);
      } else if (choice == 3) {
        display(st);
      } else {
        break;
      }
    }
  }
