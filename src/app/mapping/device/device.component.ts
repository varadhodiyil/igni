import { Component, OnInit } from '@angular/core';
import {IgniserviceService} from '../../services/igniservice.service';
import { Devices } from './devices';

declare const moment: any;
declare const google: any;
declare const $: any;
@Component({
  selector: 'app-device',
  templateUrl: './device.component.html',
  styleUrls: ['./device.component.scss']
})
export class DeviceComponent implements OnInit {

  constructor(private httpService: IgniserviceService) { }
  devices: Devices[];
  device_id = null;
  params = '';
  attachSecretMessage(marker, text) {
    const infowindow = new google.maps.InfoWindow({
      content: text
    });
    marker.addListener('click', function() {
      infowindow.open(marker.get('map'), marker);
    });
  }
  serialize_params(data) {
    return Object.keys(data).map(key => `${key}=${encodeURIComponent(data[key])}`).join('&');
  }
  set_params(key , value) {
    // remove any preceding url and split
    const querystring = this.params;
    const querystrings = querystring.substring(querystring.indexOf('?') + 1).split('&');
    const params = {}; let pair; const d = decodeURIComponent;
    // march and parse
    for (let i = querystrings.length - 1; i >= 0; i--) {
      pair = querystrings[i].split('=');
      console.log(pair);
      if ( pair[0].length > 0 ) {
        params[d(pair[0])] = d(pair[1] || '');
      }
    }
    params[key] = value;

    return this.serialize_params(params);
}
  ngOnInit() {
    const self = this;
    $(document).ready(function () {
      $(function () {
        $('#rangepicker').daterangepicker({
          startDate: moment().startOf('month'),
          maxDate: moment(),
        }, function (start, end, label) {
           self.params = self.set_params('start_date',  moment(start).format('DD-MM-YYYY'));
           self.params = self.set_params('end_date',  moment(end).format('DD-MM-YYYY'));
          self.show_filtered_pins();
        });
      });
    });
    this.httpService.getDevices().subscribe(data => {
      this.devices = data.result;
      if (this.devices.length > 0 ) {
        this.device_id = this.devices[0].id;
        this.show_filtered_pins();
      }
    });

  }
  public show_filtered_pins() {
    this.httpService.getDeviceLogs(this.device_id , this.params).subscribe(data => {
      data = data.result;
      this.initMap(data);
    });
  }
  public initMap(data) {
    let map;
    let centerLat = 39.909736;
    let centerLng =  -98.522109;
    if (data.length > 0) {
      const latlng = data[0].latitude;
      centerLat = parseFloat(data[0].latitude);
      centerLng = parseFloat(data[0].longitude);
    }
    map = new google.maps.Map(document.getElementById('map'), {
      center: new google.maps.LatLng(centerLat, centerLng),
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
    });
    const bounds  = new google.maps.LatLngBounds();
    const loc = new google.maps.LatLng(centerLat, centerLng);
    bounds.extend(loc);
    map.fitBounds(bounds);
    const markers = Array();
    const paths = [];
    data.forEach(e => {
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)),
        map: map,
        title: e.address
      });
      markers.push(marker);
      this.attachSecretMessage(marker, e.address + ' at : ' + moment(e.updated_at).format('MMMM Do YYYY, h:mm:ss a'));
      paths.push(new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)));
    });
    const poly_line = new google.maps.Polyline({
      path: paths,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 5,
      map: map
  });
    // map.addPolyLine(poly_line);
    poly_line.setMap(map);

  }
}
