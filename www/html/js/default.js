$(document).ready(function(){
	//code here...
	var code = $(".codemirror-textarea")[0];
	var editor = CodeMirror.fromTextArea(code, {
		lineNumbers : true,
        mode : "python"
        //, keyMap : "vim"
	});

    $("#preview-button").click(function(){
        $.post("lol.php",
            {
              preview: "true",
              password: $("#password-field").val(),
              code: editor.getValue()
            },
            function(data,status){
                if (status.equals("success")) {
                    M.toast({html: "Success"})
                }
                else {
                    M.toast({html: "Failed"});
                }
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

