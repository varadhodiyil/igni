import { Component, OnInit } from '@angular/core';
declare const google: any;
@Component({
  selector: 'app-device',
  templateUrl: './device.component.html',
  styleUrls: ['./device.component.scss']
})
export class DeviceComponent implements OnInit {

  constructor() { }
  data = [
    {loc : 'Bondi Beach', lat: '-33.890542, 151.274856'},
    {loc : 'Coogee Beach', lat: '-34.02634,151.174933'},
    {loc : 'Cronulla Beach',  lat: '-34.025638, 151.176124'},
    {loc : 'Manly Beach',  lat: '-33.80010128657071, 151.28747820854187'},
    {loc : 'Maroubra Beach',  lat: '-33.950198, 151.259302'},
  ];
  attachSecretMessage(marker, text) {
    const infowindow = new google.maps.InfoWindow({
      content: text
    });
    marker.addListener('click', function() {
      infowindow.open(marker.get('map'), marker);
    });
  }
  ngOnInit() {
    let map;
    let centerLat = 39.909736;
    let centerLng =  -98.522109;
    if (this.data.length > 0) {
      const latlng = this.data[0].lat.split(',');
      centerLat = parseFloat(latlng[0]);
      centerLng = parseFloat(latlng[1]);
    }
    map = new google.maps.Map(document.getElementById('map'), {
      center: new google.maps.LatLng(centerLat, centerLng),
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
    });
    const markers = Array();
    for (let i = 0; i < this.data.length; i++) {
      const latlng = this.data[i].lat.split(',');
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(parseFloat(latlng[0]), parseFloat(latlng[1])),
        map: map,
        title: 'Click Me ' + i
      });
      markers.push(marker);
      this.attachSecretMessage(marker, this.data[i].loc);
    }

  }
}
