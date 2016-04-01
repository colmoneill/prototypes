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

  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.className = "bubble"
  console.log("created bubble div")
  div.setAttribute("style", "font-family: monospace; position: fixed; top: 10px !important; width: 300px; right: 10px !important; background-color: lightblue; padding: 20px; border-radius: 5px;")
  div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + prevCumulativeDist + " px or " + pxToMeters(prevCumulativeDist) + " cm <br> on " + window.location.host;

  var v = window.addEventListener("scroll", function(){
    //console.log("prevCumulativeDist at start of event listener " + prevCumulativeDist);
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = prevCumulativeDist;
    cumulativeDist = cumulativeDist + Math.abs(delta);
    div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToMeters(cumulativeDist) + " cm <br> on <code>" + window.location.host + "</code>";
    previousPos = currentPos;
    prevCumulativeDist = cumulativeDist;
    localStorage.prevCumulativeDist = [parseInt(prevCumulativeDist, 10) , datetime ];
    //console.log("prevCumulativeDist at END of event listener " + prevCumulativeDist);
  })
})
