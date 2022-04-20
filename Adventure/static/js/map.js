let targetRadius = document.getElementById("targetRadius").textContent

var id, target, options;
target = {
  latitude : document.getElementById("targetLat").textContent, 
  longitude: document.getElementById("targetLng").textContent
};
options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

var map = L.map('map', {
  center: [target.latitude, target.longitude],
  zoom: 16,
  maxZoom: 20,
});
var fingerprint_url = document.getElementById("fingerprint_icon").textContent
var myIcon = L.icon({
  iconUrl: fingerprint_url,
  iconSize: [38, 95],
  // iconAnchor: [22, 94],
  // popupAnchor: [-3, -76],
});

L.marker([target.latitude, target.longitude], {icon: myIcon}).addTo(map);
var marker = L.marker(map.getCenter()).addTo(map)

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 20,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: 'pk.eyJ1IjoiY29sZXlyYW5nZWwiLCJhIjoiY2wyNTV0ZzA4MDJoZzNpbzVoczA4djExbiJ9.vfsbjOg633lQPgqOEzeKmQ'
}).addTo(map);

var circle = L.circle([target.latitude, target.longitude], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: targetRadius / 3.28084
}).addTo(map);

function updateMap(latlng){
  marker.setLatLng(latlng);
  map.panTo(latlng)
}

function round(value, precision) {
    var multiplier = Math.pow(10, precision || 0);
    return Math.round(value * multiplier) / multiplier;
}

function getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2) {
    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2-lat1);  // deg2rad below
    var dLon = deg2rad(lon2-lon1); 
    var a = 
      Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
      Math.sin(dLon/2) * Math.sin(dLon/2)
      ; 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; // Distance in km
    return round(d * 3280.84 / 5, 0) * 5;
  }
  
  function deg2rad(deg) {
    return deg * (Math.PI/180)
  }

function success(pos) {
  var crd = pos.coords;
  crd.lat = crd.latitude
  crd.lng = crd.longitude
  updateMap(crd)
  let feet = document.getElementById("feet")
  let feetFromTarget = getDistanceFromLatLonInKm(crd.latitude, crd.longitude, target.latitude, target.longitude)
  feet.textContent = `${feetFromTarget} feet`
  if (feetFromTarget <= targetRadius) {
    document.getElementById("map").classList.add("map_arrived_shadow")
    document.getElementById("feet").classList.add("displayNone")
    if (document.getElementById("required").textContent == "True"){
    document.getElementById("message").classList.remove("displayNone")
    document.getElementById("Answer").classList.remove("displayNone")
    }
    document.getElementById("map_instrunction").textContent = "You are in proximity"
    document.getElementById("distance").textContent = "Nearby"
    navigator.geolocation.clearWatch(id);
  }
}

function error(err) {
  console.log(err.code)
  console.log(err.message)
  // console.warn('ERROR(' + err.code + '): ' + err.message);
}

if (document.getElementById("required").textContent == "True"){
  document.getElementById("message").classList.add("displayNone")
  document.getElementById("Answer").classList.add("displayNone")
}

id = navigator.geolocation.watchPosition(success, error, options);