document.addEventListener("DOMContentLoaded", function(){
  console.log("ready")
  var initVertPos = window.scrollY,
      initHorizPos = window.scrollX,
      fullWidth = window.innerWidth,
      fullHeight = window.innerHeight,
      devicePixelRatio = window.devicePixelRatio,
      previousPos = 0,
      cumulativeDist = 0;


  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

function getPPI(){
 // create an empty element
 var div = document.createElement("div");
 // give it an absolute size of one inch
 div.style.width="1in";
 // append it to the body
 var body = document.getElementsByTagName("body")[0];
 body.appendChild(div);
 // read the computed width
 var ppi = document.defaultView.getComputedStyle(div, null).getPropertyValue('width');
 // remove it again
 body.removeChild(div);
 // and return the value
 return parseFloat(ppi);
}

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.className = "bubble"


  var v = window.addEventListener("scroll", function(){
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = cumulativeDist + Math.abs(delta);
    console.log("current position:" + currentPos + " previous position:" + previousPos + " cumulative distance:" + cumulativeDist);
    //console.log("vertical scroll position", vertPos);
    //var distInCm = pxToMeters(vertPos);
    div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToMeters(cumulativeDist) + " cm";
    previousPos = currentPos;
  })
})
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
