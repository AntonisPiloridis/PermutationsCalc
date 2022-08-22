function exportData(id,name){
    var text = document.getElementById(id).textContent;
    var file = new Blob([text],{type:"text"});
    var anchor = document.createElement("a");
    anchor.href = URL.createObjectURL(file);
    anchor.download = name
    anchor.click();
}