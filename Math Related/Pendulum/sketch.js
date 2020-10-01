let ypos = 10;
let downvel = 1;
let coeff = 0.5;
let energy = 0;
function setup() {
    createCanvas(1280, 720);
  }
  
  function draw() {
    background(42);
    strokeWeight(0.01);
    if(ypos < 720 && energy > 0){
        circle(width/2,ypos,10);
        ypos += downvel;
        downvel += 0.098;
        energy += 1;
    }else{
        circle(width/2,ypos,10);
        ypos -= coeff*downvel;
        downvel += 0.098;
    }
    
  }