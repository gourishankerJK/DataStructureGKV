#include <stdio.h>
#include <stdlib.h>

struct queue
{int size,front,rear,*Q;};

void creatqueue(struct queue *qu){
	printf("\nenter the size of queue: ");
	scanf("%d",&qu->size);
	qu->front=0;
	qu->rear=-1;
	qu->Q=(int *)malloc(qu->size*sizeof(int));
}

void push(struct queue *qu,int value){
	if(qu->rear==qu->size-1){
		printf("\nqueue is full");
	}
	else{
		qu->rear++;
		qu->Q[qu->rear]=value;
		printf("%d id added in queue\n",value);
		printf("\nfront : %d  rear: %d\n",qu->front,qu->rear);
	}
}

int pop(struct queue *qu){
	int x=0;
	if(qu->front>qu->rear){
		printf("\nqueue is empty");
	}
	else{
		x=qu->Q[qu->front];
		printf("\n%d is poped\n", qu->Q[qu->front]);
		qu->front++;
		
	}
	return x;

}

void display(struct queue *qu){
	for(int i=qu->front;i<=qu->rear;i++){
		printf("%d\n", qu->Q[i]);
	}
}

int main()
{
	struct queue qu;
	creatqueue(&qu);
	push(&qu,10);
	push(&qu,20);
	display(&qu);
	pop(&qu);
	push(&qu,30);
	pop(&qu);
	display(&qu);
	push(&qu,40);
	push(&qu,50);
	pop(&qu);
	push(&qu,60);
	display(&qu);
	pop(&qu);
	pop(&qu);
	pop(&qu);
	return 0;
}
