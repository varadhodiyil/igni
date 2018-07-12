import { Component, OnInit } from '@angular/core';
import {IgniserviceService} from '../../services/igniservice.service';
import { Devices } from '../device/devices';
declare const moment: any;
declare const google: any;
declare const $: any;
@Component({
  selector: 'app-vehicle',
  templateUrl: './vehicle.component.html',
  styleUrls: ['./vehicle.component.scss']
})
export class VehicleComponent implements OnInit {

  constructor(private httpService: IgniserviceService) { }
  devices: Devices[];
  device_id = null;
  params = '';
  prev_infowindow = false ;
  attachSecretMessage(marker, text) {
    const infowindow = new google.maps.InfoWindow({
      content: text
    });
    marker.addListener('click', function() {
      if ( this.prev_infowindow) {
        console.log(this.prev_infowindow);
        this.prev_infowindow.close();
     }
     this.prev_infowindow = infowindow;
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
    // this.httpService.getDashBoard().subscribe(data => {
    //   this.devices = data.result;
    // });
    this.show_filtered_pins();
  }
  public show_filtered_pins() {
    this.httpService.getDashBoard(this.params).subscribe(data => {
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
    let loc = null;

    const markers = Array();
    const paths = [];
    let isBoundsSet = false;
    data.forEach(e => {
      if ( e.latitude !== undefined) {
        if (!isBoundsSet) {
          loc =  new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)),
          isBoundsSet = true;
        }
        const marker = new google.maps.Marker({
          position: new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)),
          map: map,
          title: e.name,
          icon : '/assets/img/forklift_yellow_h7.png'
        });
        markers.push(marker);
        this.attachSecretMessage(marker, e.address + ' at : ' + moment(e.updated_at).format('MMMM Do YYYY, h:mm:ss a'));
        paths.push(new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)));
        bounds.extend(new google.maps.LatLng(parseFloat(e.latitude), parseFloat(e.longitude)));
      }
    });

    bounds.extend(loc);
    map.fitBounds(bounds);

  }
}


