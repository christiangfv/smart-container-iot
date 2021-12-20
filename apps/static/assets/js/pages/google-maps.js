'use strict';
$(document).ready(function() {
    var basic;
    basic = new GMaps({
        el: '#basic-map',
        lat: 21.217319,
        lng: 72.866472,
        scrollwheel: false
    });
    basic.addMarker({
        lat: 21.217319,
        lng: 72.866472,
        title: 'Marker with InfoWindow',
        infoWindow: {
            content: '<p><Phoenicoded></Phoenicoded> <br/> Buy Now at <a href="">Themeforest</a></p>'
        }
    });
})