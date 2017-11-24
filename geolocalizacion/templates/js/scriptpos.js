//<!--Carlos E Del Hierro G-->
var myCenter;
var mylat;
var mylon;
var map;
var markers = [];
var markers1 = [];
var infowindow;
var choro = [];

function showPosition1(position) {

    window.mylat = position.coords.latitude;
    window.mylon = position.coords.longitude;
    var cookie_name = 'userpos';
    create_cookie(cookie_name, window.mylat, 30, "/");
    var cookie_name1 = 'userpos1';
    create_cookie(cookie_name1, window.mylon, 30, "/");
    //alert("lat"+mylat);
    //alert("lon"+mylon);


}

function getLocation1() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition1);
        
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    return 0;
}

function setMarkers(map) {
    // Adds markers to the map.
    var beaches = [
              ['Capilla de las Ánimas', 19.4349528, -99.13327570000001, 2],
              ['Museo del Templo Mayor', 19.4346038, -99.13188100000002, 2],
              ['Gran Hotel Ciudad de México', 19.4320832, -99.13459169999999, 2],
              ['Antiguo Palacio del Ayuntamiento', 19.431609, -99.133798, 2],
              ['Paseo de la Reforma 255, Cuauhtémoc', 19.4292104, -99.1644382, 2],
              ['Torre Latinoamericana', 19.43393, -99.14056, 2]
            ];

    var peaches = [
              ['La Plaza Garibaldi ', 19.440651, -99.138906, 2],
              ['Templo de San Andrés', 19.436027, -99.13947, 2],
              ['Alameda Central', 19.435727, -99.143947, 2],
              ['Plaza de Santo Domingo', 19.437274, -99.133791, 2],
              ['Plaza de la Constitución', 19.432603, -99.133205, 2]
            ];
    //var beaches = localidades;


    // Marker sizes are expressed as a Size of X,Y where the origin of the image
    // (0,0) is located in the top left of the image.

    // Origins, anchor positions and coordinates of the marker increase in the X
    // direction to the right and in the Y direction down.
    var image11 = {
        url: 'assets/img/img/patri.png',
        // This marker is 20 pixels wide by 32 pixels high.
        size: new google.maps.Size(72, 72),
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(0, 32)
    };

    var image21 = {
        url: 'assets/img/img/cirrosa.png',
        // This marker is 20 pixels wide by 32 pixels high.
        size: new google.maps.Size(72, 72),
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(0, 32)
    };
    // Shapes define the clickable region of the icon. The type defines an HTML
    // <area> element 'poly' which traces out a polygon as a series of X,Y points.
    // The final coordinate closes the poly by connecting to the first coordinate.
    var shape = {
        coords: [1, 1, 1, 20, 18, 20, 18, 1],
        type: 'poly'
    };

    infowindow = new google.maps.InfoWindow();
    for (var i = 0; i < beaches.length; i++) {
        var beach = beaches[i];
        var marker1 = new google.maps.Marker({
            position: {
                lat: beach[1],
                lng: beach[2]
            },
            map: map,
            icon: image11,
            shape: shape,
            title: beach[0],
            zIndex: beach[3]
        });
        markers.push(marker1);

        choro[i] = "<a class='btn btn-simple btn-success' href='index.html'>" + beach[0] + "</a> ";

        google.maps.event.addListener(marker1, 'click', (function (marker1, i) {
            return function () {
                infowindow.setContent("Patrimonio: " + choro[i]);
                infowindow.setOptions({
                    maxWidth: 200
                });
                infowindow.open(map, marker1);
            }
        })(marker1, i));

        //alert("beach");
    }

    for (var i = 0; i < peaches.length; i++) {
        var peach = peaches[i];
        var marker2 = new google.maps.Marker({
            position: {
                lat: peach[1],
                lng: peach[2]
            },
            map: map,
            icon: image21,
            shape: shape,
            title: peach[0],
            zIndex: peach[3]
        });
        markers1.push(marker2);
        // alert(beach);
    }
}

function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

function clearMarkers() {
    setMapOnAll(null);
}

function showMarkers() {
    setMapOnAll(map);
}

function showclearMarkers() {
    var onoff = document.getElementById('prendemaps').checked;
    //alert(onoff);
    // onoff = val.valueOf();
    if (onoff) {
        showMarkers();
    } else {
        clearMarkers();
    }
}



function setMapOnAll1(map) {
    for (var i = 0; i < markers1.length; i++) {
        markers1[i].setMap(map);
    }
}
function clearMarkers1() {
    setMapOnAll1(null);
}

function showMarkers1() {
    setMapOnAll1(map);
}

function showclearMarkers1() {
    var onoff1 = document.getElementById('prendemaps1').checked;
    //alert(onoff);
    // onoff = val.valueOf();
    if (onoff1) {
        showMarkers1();
    } else {
        clearMarkers1();
    }
}
function myMap() {



    var cookie_name = 'userpos';
    var res = retrieve_cookie(cookie_name);
    var cookie_name1 = 'userpos1';
    var res1 = retrieve_cookie(cookie_name1);
    //alert("lat" + res);
    //alert("lon" + res1);
    myCenter = new google.maps.LatLng(res, res1);
    //alert("lanlon:", myCenter);
    if (myCenter) {
        //alert('Cookie with name "' + cookie_name + '" value is ' + '"' res + '"');
        var resant = res;
        //alert("lanlonerr:", myCenter);
    } else {
        //alert('Cookie with name "' + cookie_name + '" does not exist...');
        myCenter = new google.maps.LatLng(19.4338879, -99.1408185);
        //alert("valió");
    }

    var image111 = {
        url: 'assets/img/img/locator.png',
        // This marker is 20 pixels wide by 32 pixels high.
        size: new google.maps.Size(72, 72),
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(0, 32)
    };
    //alert("coord:" + window.myCenter);

    map = new google.maps.Map(document.getElementById('gmap'), {
        zoom: 14,
        center: myCenter,
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            position: google.maps.ControlPosition.TOP_CENTER
        },
        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        },
        scaleControl: true,
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
        fullscreenControl: true
    });

    var marker = new google.maps.Marker({
        position: myCenter,
        map: map,
        title: 'Aquí andas!',
        icon: image111,
        zIndex: 1
    });




    setMarkers(map);


}
//
//  $(document).ready(function(){
//        
//     getLocation1();
//       myMap();
//       
//    });

// Data for the markers consisting of a name, a LatLng and a zIndex for the
// order in which these markers should display on top of each other.

function llamar() {
    document.getElementById('idfalse').src = "archivoPHP.php";
    return false;
}

