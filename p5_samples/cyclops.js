/* a sample program that draws a simple cyclops in the setup() without using the draw().
 */

function setup() {
  createCanvas(400, 400); // size of window
  background(220); // canvas color

  ellipse(200, 200, 150, 150); // the head

  //draws the black eye
  fill(0);
  ellipse(200, 175, 50, 50);

  //draws the pupil
  fill(240);
  ellipse(200, 175, 25, 25);

  // draws the mouth
  line(175, 235, 225, 235);
}

function draw() {
  fill(random (255),random (255),random (255));
  ellipse(200,175,25,25);
}
