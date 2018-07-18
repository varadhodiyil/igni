import { Component, OnInit } from '@angular/core';
import { Vehicle } from '../vehicle-report/vehicle';
import { IgniserviceService } from '../../services/igniservice.service';

declare const $: any;
declare const moment: any;

@Component({
  selector: 'app-ignition',
  templateUrl: './ignition.component.html',
  styleUrls: ['./ignition.component.scss']
})
export class IgnitionComponent implements OnInit {

  constructor(private httpService: IgniserviceService) { }

  vehicle = new Vehicle();
  data_table = null;
  params = '';
  vehicles = [1, 2, 3];
  ngOnInit() {
    const self = this;
    $(document).ready(function () {
      $('#table_id').DataTable();
      $(function () {
        $('#daterange').daterangepicker({
          startDate: moment().startOf('month'),
          maxDate: moment(),
        }, function (start, end, label) {
          self.params = self.set_params('start_date', moment(start).format('DD-MM-YYYY'));
          self.params = self.set_params('end_date', moment(end).format('DD-MM-YYYY'));
          self.set_data(self.params);
        });
      });
    });
    self.set_data(null);
  }
  serialize_params(data) {
    return Object.keys(data).map(key => `${key}=${encodeURIComponent(data[key])}`).join('&');
  }
  set_params(key, value) {
    // remove any preceding url and split
    const querystring = this.params;
    const querystrings = querystring.substring(querystring.indexOf('?') + 1).split('&');
    const params = {}; let pair; const d = decodeURIComponent;
    // march and parse
    for (let i = querystrings.length - 1; i >= 0; i--) {
      pair = querystrings[i].split('=');
      console.log(pair);
      if (pair[0].length > 0) {
        params[d(pair[0])] = d(pair[1] || '');
      }
    }
    params[key] = value;

    return this.serialize_params(params);
  }
  set_report_type() {
    this.params = this.set_params('report_type', this.vehicle.report_type);
    this.set_data(this.params);
  }
  set_vehicle_number() {
    this.params = this.set_params('vehicle_number', this.vehicle.vehicle_number);
    this.set_data(this.params);
  }
  set_data(params) {
    const self = this;
    let data_url = this.httpService.getBaseAPIDomain() + 'device/logs/?' + params;
    if (this.vehicle.vehicle_number !== undefined) {
      console.log(this.vehicle.vehicle_number, typeof (this.vehicle.vehicle_number), this.vehicle.vehicle_number !== undefined);
      data_url = this.httpService.getBaseAPIDomain() + 'device/logs/' + this.vehicle.vehicle_number + '/?' + params;
    }
    if (this.data_table !== null) {
      this.data_table.destroy();
    }
    this.data_table = $('#table_id').DataTable({
      stateSave: true,
      ajax: {
        dataSrc: 'result',
      },
      'sAjaxSource': data_url,
      'fnServerData': function (sSource, aoData, fnCallback, oSettings) {
        oSettings.jqXHR = $.ajax({
          'dataType': 'json',
          'type': 'GET',
          'url': sSource,
          'data': aoData,
          'success': fnCallback,
          headers: {
            'Authorization': self.httpService.getAuthorization()
          },
        });
      },
      'columns': [
        { 'data': 'id' },
        { 'data': 'device_name' },
        { 'data': 'updated_at' },
        { 'data': 'latitude' },
        { 'data': 'longitude' },
        { 'data': 'speed' },
        { 'data': 'altitude' },
        { 'data': 'odometer' },
        { 'data': 'address' },
        { 'data': 'fuel_level' },
        { 'data': 'temperature' },
        { 'data': 'ac_status' },
        { 'data': 'fuel_diff' },
      ],
      'columnDefs': [{
        'targets': 'no-sort',
        'orderable': false,
      }]
    });
  }


}
