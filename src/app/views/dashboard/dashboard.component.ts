import { Component, OnInit } from '@angular/core';
import {IgniserviceService} from '../../services/igniservice.service';
@Component({
  templateUrl: 'dashboard.component.html',
  styleUrls : ['dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  constructor(private httpService: IgniserviceService) {

  }

  ngOnInit(): void {
    this.httpService.getTrack().subscribe(data => {

    });
  }

}
