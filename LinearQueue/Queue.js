const input = require("prompt-sync");
 
class queue{
    constructor(size=5){
        this.size=size;
        this.front=0;
        this.rear=-1;
        this.array= new Array(size);
    }
    push(value){
        if(this.rear==this.size-1){
            console.log("queue is full");
            return 0;
        }
        else{
            this.rear++;
            this.array[this.rear]=value;
            console.log(value, " is added in queue");
            console.log("front: ",this.front);
            console.log("rear: ",this.rear);
            return 1;
        }
    }
    pop(){
        if(this.front>this.rear){
            console.log("queue is empty");
            return 0;
        }
        else{
            console.log(this.array[this.front], " is poped");
            this.front++;
            console.log("front: ",this.front);
            console.log("rear: ",this.rear);
            return 1;

        }
    }

    display(){
        if(this.front>this.rear){
            console.log("queue is empty");
            return 0;
        }
        else{
            for(var i=this.front;i<=this.rear;i++){
                console.log(this.array[i]);
            }
        }
    }
}


var qu =new queue();
qu.push(1);
qu.push(2);
qu.push(3);
qu.display();
qu.pop();
qu.display();
qu.push(4);
qu.push(5);
qu.pop();
qu.push(6);
qu.display();
