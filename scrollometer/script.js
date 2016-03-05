document.addEventListener("DOMContentLoaded", function(){
  console.log("ready")
  var initVertPos = window.scrollY,
    initHorizPos = window.scrollX;

  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.style.position = "fixed"
  var v = window.addEventListener("scroll", function(){
    vertPos = window.scrollY;
    console.log("vertical scroll position", vertPos);
    var distInCm = pxToMeters(vertPos);
    div.innerHTML = "You've scrolled " + distInCm + " Centimeters! aka:" + vertPos + "px"
  })

  //oral note: comare prev pos and current pos, in abs() for counting both ways 

  // look at the current vertPos, ?? in sequence ??, and add the difference of the biggest value to the current value
  var distanceCalculator = window.addEventListener("scroll", function(){
    for
  })


})
