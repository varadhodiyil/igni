import { Component , OnInit } from '@angular/core';
import {IgniserviceService} from '../../services/igniservice.service';
import {Login} from './login';
@Component({
  selector: 'app-dashboard',
  templateUrl: 'login.component.html'
})
export class LoginComponent implements OnInit {
  login = new Login();
  errors = '';
  constructor(private httpService: IgniserviceService) {

  }
  ngOnInit(): void {

  }
  do_login() {
    this.httpService.postLogin(this.login).subscribe(d => {
      console.log(d);
      if (d.status === false) {
        this.errors = d.error;
      }
    });
  }

 }
