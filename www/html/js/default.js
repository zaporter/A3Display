$(document).ready(function(){
	//code here...
	var code = $(".codemirror-textarea")[0];
	var editor = CodeMirror.fromTextArea(code, {
		lineNumbers : true,
        mode : "python"
        //, keyMap : "vim"
	});

	$("#preview-button").click(function(){
	    $.post("preview.php",
            {
              preview: "true",
              password: $("#password-field").val(),
              code: editor.getValue()
            },
            function(data,status){
              alert("Data: " + data + "\nStatus: " + status);
            });
          });

  	$("#upload-button").click(function(){
            $.post("upload.php",
            {
              preview: "false",
              password: $("#password-field").val(),
              code: editor.getValue()
            },
            function(data,status){
              alert("Data: " + data + "\nStatus: " + status);
            });
  	});
});

