// Dev: Ted Clifford (c) 1.31.20
$(document).ready(function(){
//(function() {
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

        var lastMove = null;

        // Create handlers for screen touches
        htmlCanvas.addEventListener("touchstart", function (e) {
            mousePos = getTouchPos(htmlCanvas, e);
            lastMove = e;
            var i;
            for (i = 0; i < e.touches.length; i++) {
                var touch = e.touches[i];
                var mouseEvent = new MouseEvent("mousedown", {
                    clientX: touch.clientX,
                    clientY: touch.clientY
                });
                pickSector(mouseEvent);
                htmlCanvas.dispatchEvent(mouseEvent);
            }
        }, false);

        htmlCanvas.addEventListener("touchend", function (e) {
            var mouseEvent = new MouseEvent("mouseup", {});
            var redrawAction = true;
            var redrawDpad = true;
            var i;
            for (i = 0; i < e.changedTouches.length; i++) {
                console.log(e.changedTouches[i]);
                if (e.changedTouches[i].clientX < window.innerWidth/2) {
                    redrawAction = false;
                }
                else {
                    redrawDpad = false;
                }
            }

            if (redrawAction) { drawAction(); }
            if (redrawDpad) { drawDpad(); }
            htmlCanvas.dispatchEvent(mouseEvent);
        }, false);

        htmlCanvas.addEventListener("touchmove", function (e) {
            lastMove = e;
            var touch = e.touches[0];
            var mouseEvent = new MouseEvent("mousemove", {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            htmlCanvas.dispatchEvent(mouseEvent);
        }, false);

    }

    // Get the posiition of a touch relative to the canvas
    function getTouchPos(canvasDom, touchEvent) {
        var rect = canvasDom.getBoundingClientRect();
        return {
            x: touchEvent.touches[0].clientX - rect.left,
            y: touchEvent.touches[0].clientY - rect.top
        };
    }

    function pickSector(mouseEvent) {
        //Check if point is in up triangle
        if (checkInTriangle(mouseEvent.clientX, mouseEvent.clientY, 0, 0, window.innerWidth/2, 0, window.innerWidth/4, window.innerHeight/2)) {
            overlayUp();
            pressUp();
        }
        //Check if point is in down triangle
        else if (checkInTriangle(mouseEvent.clientX, mouseEvent.clientY, 0, window.innerHeight, window.innerWidth/2, window.innerHeight, window.innerWidth/4, window.innerHeight/2)) {
            overlayDown();
            pressDown();
        }
        //Check if point is in left triangle
        else if (checkInTriangle(mouseEvent.clientX, mouseEvent.clientY, 0, 0, 0, window.innerHeight, window.innerWidth/4, window.innerHeight/2)) {
            overlayLeft();
            pressLeft();
        }
        //Check if point is in right triangle
        else if (checkInTriangle(mouseEvent.clientX, mouseEvent.clientY, window.innerWidth/2, 0, window.innerWidth/2, window.innerHeight, window.innerWidth/4, window.innerHeight/2)) {
            overlayRight();
            pressRight();
        }
        //Check if point is in action area
        else if (mouseEvent.clientX > window.innerWidth/2) {
            overlayAction();
            pressAction(); 
        }

    }

    function checkInTriangle(x, y, x1, y1, x2, y2, x3, y3) {
        var A = area(x1, y1, x2, y2, x3, y3);
        var A1 = area(x, y, x2, y2, x3, y3);
        var A2 = area(x1, y1, x, y, x3, y3);
        var A3 = area(x1, y1, x2, y2, x, y);

        return (A1 + A2 + A3 == A);
    }


    // Returns the area of a given triangle of three points
    function area(x1, y1, x2 , y2, x3, y3) {
        return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
    }

    // Reset the entire screen
    function redraw() {
        drawDpad();
        drawAction();
    }
        
    // Reset the directional pad
    function drawDpad() {
        var pad = 10

        //Insert Up background
        context.beginPath();
        context.moveTo(0, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth / 2, 0);
        context.fillStyle = "yellow"
        //context.fillStyle = "DarkGoldenRod";
        context.fill();

        //Insert Up forground
        context.beginPath();
        context.moveTo(pad, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2 - pad);
        context.lineTo(window.innerWidth / 2 - pad, 0);
        context.fillStyle = "DarkSlateGray";
        //context.fillStyle = "Gold";
        context.fill();
        
        //Insert Down background
        context.beginPath();
        context.moveTo(0, window.innerHeight);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth / 2, window.innerHeight);
        context.fillStyle = "LawnGreen";
        //context.fillStyle = "DarkGreen";
        context.fill();
       
        //Insert Down forground
        context.beginPath();
        context.moveTo(pad, window.innerHeight);
        context.lineTo(window.innerWidth/4, window.innerHeight/2 + pad);
        context.lineTo(window.innerWidth / 2 - pad, window.innerHeight);
        context.fillStyle = "DarkSlateGray";
        //context.fillStyle = "Green";
        context.fill();

        //Insert Left background
        context.beginPath();
        context.moveTo(0, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(0, window.innerHeight);
        context.fillStyle = "CornFlowerBlue";
        //context.fillStyle = "DarkBlue";
        context.fill();
       
        //Insert Left forground
        context.beginPath();
        context.moveTo(0, pad);
        context.lineTo(window.innerWidth/4 - pad, window.innerHeight/2);
        context.lineTo(0, window.innerHeight - pad);
        context.fillStyle = "DarkSlateGray";
        //context.fillStyle = "CornflowerBlue";
        context.fill();

        //Insert Right background
        context.beginPath();
        context.moveTo(window.innerWidth/2, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth/2, window.innerHeight);
        context.fillStyle = "Red";
        //context.fillStyle = "DarkRed";
        context.fill();
       
        //Insert Right forground
        context.beginPath();
        context.moveTo(window.innerWidth/2, pad);
        context.lineTo(window.innerWidth/4 + pad, window.innerHeight/2);
        context.lineTo(window.innerWidth/2, window.innerHeight - pad);
        context.fillStyle = "DarkSlateGray";
        //context.fillStyle = "Red";
        context.fill();
    }

    // Reset the action button
    function drawAction() {
        var pad = 10;
        
        //Insert action background
        context.beginPath();
        context.fillStyle = "black";
        context.fillRect(window.innerWidth/2, 0, window.innerWidth/2, window.innerHeight);
        context.closePath();

        //Insert action foreground
        context.beginPath();
        context.fillStyle = "DarkSlateGray";
        context.fillRect(window.innerWidth/2 + pad, pad, window.innerWidth/2 - 2*pad , window.innerHeight - 2*pad);
        context.closePath();
    }

    function overlayAction() {
        context.beginPath();
        context.fillStyle = "black";
        context.fillRect(window.innerWidth/2, 0, window.innerWidth/2, window.innerHeight);
        context.closePath();
    }

    function overlayRight() {
        context.beginPath();
        context.moveTo(window.innerWidth/2, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth/2, window.innerHeight);
        context.fillStyle = "Red";
        //context.fillStyle = "DarkRed";
        context.fill();
    }

    function overlayLeft() {
        context.beginPath();
        context.moveTo(0, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(0, window.innerHeight);
        context.fillStyle = "CornFlowerBlue";
        //context.fillStyle = "DarkBlue";
        context.fill();
    }

    function overlayDown() {
        context.beginPath();
        context.moveTo(0, window.innerHeight);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth / 2, window.innerHeight);
        context.fillStyle = "LawnGreen";
        //context.fillStyle = "DarkGreen";
        context.fill();
    }

    function overlayUp() {
        context.beginPath();
        context.moveTo(0, 0);
        context.lineTo(window.innerWidth/4, window.innerHeight/2);
        context.lineTo(window.innerWidth / 2, 0);
        context.fillStyle = "yellow"
        //context.fillStyle = "DarkGoldenRod";
        context.fill();
    }

    function pressUp() {
        console.log("UP");
        $.post("controller.php",
            {
              command: "U\n",
            }
        );
 
    }

    function pressDown() {
        console.log("DOWN");
         $.post("controller.php",
            {
              command: "D\n",
            }
        );       
    }

    function pressLeft() {
        console.log("LEFT");
        $.post("controller.php",
            {
              command: "L\n",
            }
        ); 
    }

    function pressRight() {
        console.log("RIGHT");
        $.post("controller.php",
            {
              command: "R\n",
            }
        ); 
 
    }

    function pressAction() {
        console.log("ACTION");
        $.post("controller.php",
            {
              command: "T\n",
            }
        );
    }
    // Runs each time the DOM window resize event fires.
    // Resets the canvas dimensions to match window,
    // then draws the new borders accordingly.
    function resizeCanvas() {
        htmlCanvas.width = window.innerWidth;
        htmlCanvas.height = window.innerHeight;
        redraw();
    }
    });
//();
