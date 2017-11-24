//<!--Carlos E Del Hierro G-->
var p1 = 'p0.html';
var p2 = 'p1.html';
var p3 = 'p2.html';
var p4 = 'p3.html';
var p0 = 'index.html';
var ubicacion = '';

function redir1() {
    var vale = document.getElementById('desTxt').value;

    if (vale) {
        var cookie_name = 'userubi';
        create_cookie(cookie_name, vale, 30, "/");
        //        var vale2 = retrieve_cookie(cookie_name);
        //        alert("valkuki:" + vale2);
        document.location.href = p2;
    } else {
        //alert("¿A dónde vas?");
        getLocation1();
        document.location.href = p1;
    }

}

function redir2() {
   
    document.location.href = p1;
}

function redir3() {

    document.location.href = p3;
}

function redir4() {

    document.location.href = p4;
}


function redir22() {

    document.location.href = p2;
}
