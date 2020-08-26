#include <iostream>
using namespace std;
struct queue{
	int size,front,rear,*Q;
};

void creatqueue(struct queue *qu){
	cout<<"\nenter the size of queue: ";
	cin>>qu->size;
	qu->front=0;
	qu->rear=-1;
	qu->Q=new int[qu->size];
}

void push(struct queue *qu,int value){
	if(qu->rear==qu->size-1){
		cout<<"\nqueue is full";
	}
	else{
		qu->rear++;
		qu->Q[qu->rear]=value;
		cout<<"\n"<<value<<" is added in queue";
		cout<<"\nfront : "<<qu->front;
		cout<<"\nrear: "<<qu->rear;
	}
}

int pop(struct queue *qu){
	int x=0;
	if(qu->front>qu->rear){
		cout<<"\nqueue is empty";
	}
	else{
		x=qu->Q[qu->front];
		cout<<"\n"<<qu->Q[qu->front]<<" is poped";
		qu->front++;
		cout<<"\nfront : "<<qu->front;
		cout<<"\nrear: "<<qu->rear;
	}
	return x;

}

void display(struct queue *qu){
	for(int i=qu->front;i<=qu->rear;i++){
		cout<<"\n"<<qu->Q[i];
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



