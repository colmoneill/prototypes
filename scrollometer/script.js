document.addEventListener("DOMContentLoaded", function(){
  console.log("ready")
  var initVertPos = window.scrollY,
      initHorizPos = window.scrollX,
      fullWidth = window.innerWidth,
      fullHeight = window.innerHeight,
      devicePixelRatio = window.devicePixelRatio,
      previousPos = 0,
      cumulativeDist = 0,
      prevCumulativeDist = localStorage.prevCumulativeDist;

  var currentdate = new Date();
  var datetime = "Last Sync: " + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();

  function pxToMeters(distance){
    return (distance * 0.02645833333333);
  }

  //document.head.insertAdjacentHTML( 'beforeend', '<link rel=stylesheet href="http://pzwart1.wdka.hro.nl/~colm/prototypes/scrollometer/bubble-styles.css">' );
  ///home/colm/ownCloud/PZI/Litteracy-as-a-dependency/prototypes/scrollometer/bubble-styles.css

  var div = document.createElement("div")
  document.body.appendChild(div)
  div.className = "bubble"
  div.style.position = "fixed";
  div.setAttribute("style", "font-family: monospace; position: fixed; top: 10; width: 300px; right: 10; background-color: lightblue; padding: 20px; border-radius: 5px;")
  div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + prevCumulativeDist + " px or " + pxToMeters(prevCumulativeDist) + " cm";

  var v = window.addEventListener("scroll", function(){
    var currentPos = window.scrollY;
    var delta = (currentPos - previousPos);
    cumulativeDist = parseInt(prevCumulativeDist);
    cumulativeDist = cumulativeDist + Math.abs(delta);
    div.innerHTML = "This page offers <code>" + fullHeight + " px</code> of potential or " + pxToMeters(fullHeight)*devicePixelRatio  + " cm <br><br> Your device pixel ratio is " + devicePixelRatio + " <br><br> and You've scrolled " + cumulativeDist + " px or " + pxToMeters(cumulativeDist) + " cm";
    previousPos = currentPos;
    prevCumulativeDist = cumulativeDist;
    localStorage.prevCumulativeDist = [prevCumulativeDist , datetime ];
  })
})
