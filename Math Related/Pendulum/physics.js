class PhysicsObject{
    constructor(){
        this.position = createVector(width/2,0);
        this.velocity = createVector(0,0)
        this.acceleration = createVector();
        this.gravity = createVector(0,-90.81);
    }

    update(){
        this.position.add(this.velocity);
        this.velocity.add(this.gravity);
    }

    ball(radius){
        strokeWeight(5);
        stroke(255);
        circle(this.position.x,this.position.y,radius/2);
    }
}