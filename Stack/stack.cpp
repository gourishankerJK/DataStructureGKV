#include<iostream>
using namespace std;

struct stack{int size,top,*S;};


void creatstack(struct stack *st){
	cout<<"\nenter the size of stack\n";
	cin>>st->size;
	st->top=-1;
	st->S=new int[st->size];
}


void push(struct stack *st,int value){
	if(st->top==st->size-1){
		cout<<"\nstack overflow \n";
	}
	else{
		st->top++;
		st->S[st->top]=value;
		cout<<"\n"<<value<<" is added in stack\n";
	}
}

int pop(struct stack *st){
	int x=-1;
	if(st->top==-1){
		cout<<"\n stack is underflow\n";
	}
	else{
		x=st->S[st->top];
		st->top--;
		cout<<"\n"<<x<<" is removed from stack\n";
	}
	return x;
}
void display(struct stack *st){
	for(int i=st->top;i>=0;i--){
		cout<<"\n"<<st->S[i];
	}
}


int main(){
	struct stack st;
	creatstack(&st);
	while(true){
		cout<<"\npress 1 for push\npress 2 for pop\npress 3 for display\npress 4 for exit\nenter choice: ";
		int i;
		cin>>i;
		if (i==1)
		{
			int value;
			cout<<"enter the value: ";
			cin>>value;
			push(&st,value);
		}
		else if (i==2)
		{
			pop(&st);
		}
		else if (i==3)
		{
			display(&st);
		}
		else
		{
			break;
		}
	}

}









