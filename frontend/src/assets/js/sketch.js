let strokeIndex = 0;
let index = 0;
let cat;
let prevx, prevy;

function setup() {
  var canvas = createCanvas(300, 255);
  canvas.parent('canvasForHTML');
  newCat();
}

function newCat() {
  loadJSON('/bear', gotCat);
}

setTimeout(function(){
var draw = setInterval(function() {
  if (cat) {
    let x = cat[strokeIndex][0][index];
    let y = cat[strokeIndex][1][index];
    stroke(0);
    strokeWeight(3);
    if (prevx !== undefined) {
      line(prevx, prevy, x, y);
    }
    index++;
    if (index === cat[strokeIndex][0].length) {
      strokeIndex++;
      prevx = undefined;
      prevy = undefined;
      index = 0;
      if (strokeIndex === cat.length) {
        cat = undefined;
        strokeIndex = 0;
        setTimeout(newCat, 250);
      }
    } else {
      prevx = x;
      prevy = y;
    }
}
},100);
},1000);

function gotCat(data) {
  background(250);
  cat = data.drawing;
}