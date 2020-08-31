import java.util.Scanner;
public class Stack{
	int size=5,top=-1;
	int arr[]=new int[size];

	public void push(int value){
		if(top==size-1){
			System.out.println("\n        Stack Overflow.!\n");
		}
		else{
			top++;
			arr[top]=value;
		}
	}

	public int pop(){
		int x=0;
		if(top==-1){
			System.out.println("\n      Stack Underflow.!\n");
			return x;
		}
		else{
			x=arr[top];
			top--;
			return x;
		}
	}


	public String toString(){
    String s ="\n";
		if(top==-1){
			s = "       \nStack is Empty!\n";
		}
		else{
			for(int i=top;i>=0;i--)
			{
			  s+= Integer.toString(arr[i])+"\n" ;
		}

		}
		return s;
	}

	public static void main(String[] args) {
		Stack list = new Stack();
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the operation you want to perform:");
		System.out.println("Enter 1 to push");
		System.out.println("Enter 2 to pop");
		System.out.println("Enter 3 to exit");

		while (true){

		    System.out.print("Enter your choice:");
			  int	option = in.nextInt();
		    if (option == 1)
				{
				    System.out.print("Enter the value you want to push:");
				    int value = in.nextInt();
		        list.push(value);
		        System.out.println(list);}
		    else if (option == 2){
		        list.pop();
		        System.out.println(list);
					}
		    else if (option == 3){
		        break;
					}
				else{
					System.out.println("Invalid input :(");
				}
	}
	Stack list1 = new Stack();
	System.out.println(list1);
}
}
