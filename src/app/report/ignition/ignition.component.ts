import { Component, OnInit } from '@angular/core';
import {Vehicle} from '../vehicle-report/vehicle';
declare const $: any;
declare const moment: any;

@Component({
  selector: 'app-ignition',
  templateUrl: './ignition.component.html',
  styleUrls: ['./ignition.component.scss']
})
export class IgnitionComponent implements OnInit {

  constructor() { }

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
           self.params = self.set_params('start_date',  moment(start).format('DD-MM-YYYY'));
           self.params = self.set_params('end_date',  moment(end).format('DD-MM-YYYY'));
          self.set_data(self.params);
        });
      });
    });
    // self.set_data(null);
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
  set_report_type() {
    this.params = this.set_params('report_type', this.vehicle.report_type);
    this.set_data(this.params);
  }
  set_vehicle_number() {
    this.params = this.set_params('vehicle_number', this.vehicle.vehicle_number);
    this.set_data(this.params);
  }
  set_data(params) {
    if (this.data_table !== null ) {
      this.data_table.destroy();
    }
      this.data_table = $('#table_id').DataTable( {
      'ajax': 'backend/get_all_rr.php?' + params,
      'scrollY': true,
      'scrollX': true,
      // "columns": [
      //         { "data": "rr_date" },
      //         { "data": "rr_number" },
      //         { "data": "party" },
      //         { "data": "no_of_pack" },
      //         { "data": "station" },
      //   { "data": "weight" },
      //   { "data": "rr_amount" },
      //         { "data": "expense" },
      //   { "data": "other_charge" },
      //   { "data": "cgst" },
      //         { "data": "sgst" },
      //         { "data": "igst" },
      //         { "data": "total" },
      //         { "data": "paid" },
      //   { "data": "previous_balance" },
      //   { "data": "grand_total" },
      //         { "data": "dispatch" },
      //   { "data": "remarks" },
      //   { "data": "edit" }
      // ],
      'columnDefs': [ {
        'targets'  : 'no-sort',
        'orderable': false,
        }]
      } );
  }


}
