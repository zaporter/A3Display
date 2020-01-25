(function() {
        var
        // Obtain a reference to the canvas element using its id.
        htmlCanvas = document.getElementById('myCanvas'),
        // Obtain a graphics context on the canvas element for drawing.
        context = htmlCanvas.getContext('2d');

       // Start listening to resize events and draw canvas.
       initialize();

       function initialize() {
           // Register an event listener to call the resizeCanvas() function 
           // each time the window is resized.
           window.addEventListener('resize', resizeCanvas, false);
           // Draw canvas border for the first time.
           resizeCanvas();

        }

        // Display custom canvas. In this case it's a blue, 5 pixel 
        // border that resizes along with the browser window.
        function redraw() {
           context.strokeStyle = 'blue';
           context.lineWidth = '5';
           context.strokeRect(0, 0, window.innerWidth, window.innerHeight);

	   context.moveTo(window.innerWidth / 2, 0);
	   context.lineTo(window.innerWidth, window.innerHeight);
	   context.stroke();

	   context.moveTo(window.innerWidth / 2, window.innerHeight);
	   context.lineTo(window.innerWidth, 0);
	   context.stroke();

	   context.moveTo(window.innerWidth / 2, 0);
	   context.lineTo(window.innerWidth / 2, window.innerHeight);       
	   context.stroke();
	}

        // Runs each time the DOM window resize event fires.
        // Resets the canvas dimensions to match window,
        // then draws the new borders accordingly.
        function resizeCanvas() {
            htmlCanvas.width = window.innerWidth;
            htmlCanvas.height = window.innerHeight;
            redraw();
        }
    })();
/*
var el = document.getElementById("myCanvas")[0];
el.addEventListener("touchstart", handleStart);
el.addEventListener("touchmove", handleMove);
el.addEventListener("touchend", handleEnd);
el.addEventListener("touchcancel", handleCancel);
*/
