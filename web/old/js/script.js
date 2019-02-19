
function handleClick(callback){
    alert('clicked');
    if ( callback){
        callback();
    }
}

function doMore(){
    alert(' I can do more');
}

function doSomethingElse(){
    document.write('Test Message');
}