import { Component, OnInit } from '@angular/core';
declare const $: any;
declare const moment: any;

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {
  data_table = null;
  params = '';
  constructor() { }

  ngOnInit() {

    $(document).ready(function () {
      $('#table_id').DataTable( {pageResize: true});
    });
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
