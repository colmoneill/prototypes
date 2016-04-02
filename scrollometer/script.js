document.addEventListener("DOMContentLoaded", function(){
  console.log("ready")
  var initVertPos = window.scrollY,
      initHorizPos = window.scrollX,
      fullWidth = window.innerWidth,
      fullHeight = window.innerHeight,
      devicePixelRatio = window.devicePixelRatio,
      previousPos = 0,
      cumulativeDist = 0,
      prevCumulativeDist = 0,
      currentdate = new Date(),
      datetime = "Last entry: " + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();

  if (localStorage.prevCumulativeDist){
    var prevCumulativeDist = parseInt(localStorage.prevCumulativeDist, 10);
    console.log("previous cumulative distance found, using it");
  }
  else {
    var prevCumulativeDist = 0;
    console.log("no previous cumulative distance found, starting from 0");
  }

  function pxToCm(distance){
    return (distance * 0.0264);
  }

  function pxToM(distance){
    return (distance * 0.000264);
  }

  var bigdiv = document.createElement("div")
  document.body.appendChild(bigdiv)
  bigdiv.className = "big-bubble"
  bigdiv.id = "big-bubble"
  bigdiv.setAttribute("style", "opacity: 0; z-index: 9999; font-family: monospace; position: fixed; top: 10px !important; width: 300px; right: 10px !important; background-color: lightblue; padding: 20px; border-radius: 5px;")
  bigdiv.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToCm(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToM(cumulativeDist) + " meters! <br> on <code>" + window.location.host + "</code>";

  var smalldiv = document.createElement("div")
  document.body.appendChild(smalldiv)
  smalldiv.className = "small-bubble"
  smalldiv.id = "small-bubble"
  smalldiv.setAttribute("style", "opacity: 1; z-index: 9999; font-family: monospace; position: fixed; top: 10px !important; width: 200px; right: 10px !important; background-color: lightblue; padding: 10px; border-radius: 5px;")
  smalldiv.innerHTML = "Distance: " + pxToM(cumulativeDist) + " m";

  var scrollListener = window.addEventListener("scroll", function(){
    //console.log("prevCumulativeDist at start of event listener " + prevCumulativeDist);
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = prevCumulativeDist;
    cumulativeDist = cumulativeDist + Math.abs(delta);
    smalldiv.innerHTML = "Distance: " + pxToM(cumulativeDist) + " m";
    bigdiv.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToCm(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToM(cumulativeDist) + " meters! <br> on <code>" + window.location.host + "</code>";
    previousPos = currentPos;
    prevCumulativeDist = cumulativeDist;
    localStorage.prevCumulativeDist = [parseInt(prevCumulativeDist, 10) , datetime ];
    //console.log("prevCumulativeDist at END of event listener " + prevCumulativeDist);
  });

  var smallerdiv = document.getElementById("small-bubble");
  var biggerdiv = document.getElementById("big-bubble");

  smallerdiv.addEventListener("mouseover", function(){
    smalldiv.style.opacity = "0"
    bigdiv.style.opacity = "1"
  })
  biggerdiv.addEventListener("mouseleave", function(){
    smalldiv.style.opacity = "1"
    bigdiv.style.opacity = "0"
  })
})
