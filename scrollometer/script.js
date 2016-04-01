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
      prevCumulativeDist = parseInt(localStorage.prevCumulativeDist),
      currentdate = new Date(),
      datetime = "Last entry: " + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();
  console.log("found previous CumulativeDist: " + prevCumulativeDist )
  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.className = "bubble"
  console.log("created bubble div")
  div.setAttribute("style", "font-family: monospace; position: fixed; top: 10px !important; width: 300px; right: 10px !important; background-color: lightblue; padding: 20px; border-radius: 5px;")
  div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + prevCumulativeDist + " px or " + pxToMeters(prevCumulativeDist) + " cm";

  var v = window.addEventListener("scroll", function(){
    console.log("prevCumulativeDist at start of event listener " + prevCumulativeDist);
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = parseInt(prevCumulativeDist);
    cumulativeDist = cumulativeDist + Math.abs(delta);
    div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToMeters(cumulativeDist) + " cm";
    previousPos = currentPos;
    prevCumulativeDist = cumulativeDist;
    localStorage.prevCumulativeDist = [parseInt(prevCumulativeDist) , datetime ];
    console.log("prevCumulativeDist at END of event listener " + prevCumulativeDist);
  })
})
