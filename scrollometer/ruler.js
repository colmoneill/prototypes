var isDragging=false;
var DDX=0;
var DSV=0;
function handleMouseDown(e){
  if(document.getElementById("adjuster").value!=''){
    isDragging=true;DDX=e.clientX;
    DSV=document.getElementById("ppi").value;
    }
  }
function handleMouseUp(e){isDragging=false;}
function handleMouseOut(e){isDragging=false;}
function handleMouseMove(e){
  if((isDragging)&&(document.getElementById("adjuster").value!='')){
    var MouseX=parseInt(e.clientX-DDX);
    document.getElementById("ppi").value=parseFloat(DSV)+MouseX/10;
    drawruler();
    drawAdjuster();
  }
}

var c=document.getElementById("ruler");
c.addEventListener("mousedown", handleMouseDown);
c.addEventListener("mouseup", handleMouseUp);
c.addEventListener("mouseout", handleMouseOut);
c.addEventListener("mousemove", handleMouseMove);
var rulers= ["","A4 Paper (portrait)","A4 Paper (landscape)",
"US One Dollar Bill (long)","US One Dollar Bill (width)","20 EURO Note (long)",
"Standard CD Diameter"];
var rulers_inch= [0,8.264,11.681,6.14,2.61,5.236,4.724];
