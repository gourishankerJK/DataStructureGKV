const input = require("prompt-sync")();

class stack{
    constructor(size=5){
        this.size=size;
        this.array = new Array(size);
        this.top=-1;
        console.log("stack created of size", size);
    }

    push(value){
        if(this.top==this.size-1){
            console.log("stack is overflow");
            return 0;
        }
        else{
            this.top++;
            this.array[this.top]=value;
            console.log(value," is added in stack");
        }
    }

    pop(){
        if(this.top==-1){
            console.log("stack is underflow");
        }
        else{
            console.log(this.array[this.top], " is poped");
            this.top--;
        }
    }

    display(){
        if(this.top==-1){
            console.log("stack is Empty!");
        }
        else{
            for(var i=this.top; i>=0;i--){
                console.log(this.array[i]);
            }
        }
    }
}

var st = new stack();
console.log("1: push \n2: pop \n3: display\n4: exit");
while(true){
    var x=input("enter choice: ");
    if(x==1){
        var value = Number(input("enter value: "));
        st.push(value);
    }
    else if(x==2){
        st.pop();
    }
    else if(x==3){
        st.display();
    }
    else{
        break;
    }
}
