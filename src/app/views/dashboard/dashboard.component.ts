import { Component, OnInit } from '@angular/core';
import {IgniserviceService} from '../../services/igniservice.service';
import { Dashboard } from './dashboard';
@Component({
  templateUrl: 'dashboard.component.html',
  styleUrls : ['dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  dashboardResults: Dashboard[];
  constructor(private httpService: IgniserviceService) {

  }

  ngOnInit(): void {
    this.httpService.getDashBoard().subscribe(data => {
      this.dashboardResults = data.result;
    });
  }

}
