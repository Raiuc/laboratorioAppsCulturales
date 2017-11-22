//<!--Carlos E Del Hierro G-->
//var x = document.getElementById("mipos");
//var ubicacion = 'mixcoac';
// Enable the visual refresh
//google.maps.visualRefresh = true;
var map;
var markers = [];
var markers1 = [];
var infowindow;
var choro = [];

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
        url: 'assets/img/img/cirna.png',
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

//function toggleBounce(marker) {
//    if (marker.getAnimation() !== null) {
//        marker.setAnimation(null);
//    } else {
//        marker.setAnimation(google.maps.Animation.BOUNCE);
//    }
//}

function initialize(address) {

    var geoCoder = new google.maps.Geocoder(address)
    var request = {
        address: address
    };
    geoCoder.geocode(request, function (result, status) {
        var latlng = new google.maps.LatLng(result[0].geometry.location.lat(), result[0].geometry.location.lng());
        // alert('sin:' + address+latlng);
        var myOptions = {
            zoom: 18,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById('gmap'), myOptions);

        var marker = new google.maps.Marker({
            position: latlng,
            animation: google.maps.Animation.BOUNCE,
            icon: 'assets/img/img/circulon.png',
            map: map,
            title: address
        });
        //marker.addListener('click', toggleBounce(marker));
        marker.setMap(map);


        var ven = 'Bienvenido a: ' + address;
        var infowindow = new google.maps.InfoWindow({
            content: ven
        });
        infowindow.open(map, marker);

        setMarkers(map);

        map.setMapTypeId(google.maps.MapTypeId.HYBRID);


        var myCity = new google.maps.Circle({
            center: latlng,
            radius: 50,
            strokeColor: "white",
            strokeOpacity: 0.5,
            strokeWeight: 2,
            fillColor: "red",
            fillOpacity: 0.2
        });
        myCity.setMap(map);




        // alert(latlng);
        //          var ubi = document.getElementById('ubiTxt').value;
        //          var des = document.getElementById('desTxt').value;
        //            var llubi = new google.maps.LatLng(result[0].geometry.location.lat()+1, result[0].geometry.location.lng()-1);
        //            var lldes = new google.maps.LatLng(result[0].geometry.location.lat()+3, result[0].geometry.location.lng()-3);
        //            var llnex = new google.maps.LatLng(result[0].geometry.location.lat()+2, result[0].geometry.location.lng()-2);
        //           alert(ubi  + '/' + llubi + '/' + des + '/' + lldes);         
        //          var flightPath = new google.maps.Polyline({
        //                path: [llubi, lldes, llnex],
        //                strokeColor: "#0000FF",
        //                strokeOpacity: 0.8,
        //                strokeWeight: 2
        //              });
        //          flightPath.setMap(map);



    })
}
//--------------------------





//// Enable the visual refresh
//google.maps.visualRefresh = true;
//
//var map;
//function initialize() {
//  var mapOptions = {
//    zoom: 15,
//    mapTypeId: google.maps.MapTypeId.ROADMAP
//  };
//  map = new google.maps.Map(document.getElementById('map-canvas'),
//      mapOptions);
//    // Try HTML5 geolocation
//  if(navigator.geolocation) {
//    navigator.geolocation.getCurrentPosition(function(position) {
//      var pos = new google.maps.LatLng(position.coords.latitude,
//                                       position.coords.longitude);
//
//      var infowindow = new google.maps.InfoWindow({
//        map: map,
//        position: pos,
//        content: 'Location found using HTML5.'
//      });
//
//      map.setCenter(pos);
//    }, function() {
//      handleNoGeolocation(true);
//    });
//  } else {
//    // Browser doesn't support Geolocation
//    handleNoGeolocation(false);
//  }
//}
//
//function handleNoGeolocation(errorFlag) {
//  if (errorFlag) {
//    var content = 'Error: The Geolocation service failed.';
//  } else {
//    var content = 'Error: Your browser doesn\'t support geolocation.';
//  }
//
//  var options = {
//    map: map,
//    position: new google.maps.LatLng(60, 105),
//    content: content
//  };
//
//  var infowindow = new google.maps.InfoWindow(options);
//  map.setCenter(options.position);
//}
//
//google.maps.event.addDomListener(window, 'load', initialize);
//  
//
//
//
