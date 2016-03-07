document.addEventListener("DOMContentLoaded", function(){
  console.log("ready")
  var initVertPos = window.scrollY,
      initHorizPos = window.scrollX,
      myWidth = window.innerWidth,
      fullHeight = window.innerHeight,
      previousPos = 0,
      cumulativeDist = 0,


  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.style.position = "fixed"
  div.style.top = "0"

  var v = window.addEventListener("scroll", function(){
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = cumulativeDist + Math.abs(delta);
    console.log("current position:" + currentPos + " previous position:" + previousPos + " cumulative distance:" + cumulativeDist);
    //console.log("vertical scroll position", vertPos);
    //var distInCm = pxToMeters(vertPos);
    div.innerHTML = "You've scrolled " + cumulativeDist;
    previousPos = currentPos;
  })

})
