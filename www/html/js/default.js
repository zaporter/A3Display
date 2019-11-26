$(document).ready(function(){

	var code = $(".codemirror-textarea")[0];
	var editor = CodeMirror.fromTextArea(code, {
		lineNumbers : true,
        	mode : "python"
        	//, keyMap : "vim"
	});

	$.get('http://a3disp.dyn.wpi.edu/currentCode.txt',
		function(data) {
			currentCode = data;
			editor.setValue(currentCode);
		});
	

    $("#preview-button").click(function(){
        $.post("lol.php",
            {
              preview: "true",
              password: $("#password-field").val(),
              code: editor.getValue()
            },
            function(data,status){
                    M.toast({html: data})
            }
        );
    });
    
    $("#upload-button").click(function(){
        $.post("upload.php",
            {
              preview: "false",
              password: $("#password-field").val(),
              code: editor.getValue()
            },
            function(data,status){
                    M.toast({html: data})
            }
        );  	
    });
});

