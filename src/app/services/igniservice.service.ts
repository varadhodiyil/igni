import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { AppConfig } from '../config/app.config';
import 'rxjs/add/operator/map';

@Injectable()
export class IgniserviceService {

  constructor(private http: Http, private config: AppConfig) { }

  private headers = new Headers({'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Bearer ' + this.config.Authorization,
    'Accept': 'application/json, text/plain'
  });
  public getBaseAPIDomain() {
    return this.config.domain;
  }
  public getAuthorization() {
    return 'Bearer ' + this.config.Authorization;
  }
  public getTrack() {
    const options = new RequestOptions({ headers: this.headers });
    return this.http.get(this.config.Track , options).map((response: Response) => {
        return response.json();
    });
  }
  public getDashBoard(params: string = null) {
    const options = new RequestOptions({ headers: this.headers });
    return this.http.get(this.config.Dashboard , options).map((response: Response) => {
        return response.json();
    });
  }

  public getDevices() {
    const options = new RequestOptions({ headers: this.headers });
    return this.http.get(this.config.Devices , options).map((response: Response) => {
        return response.json();
    });
  }
  public getDeviceLogs(id: any , params: string) {
    const options = new RequestOptions({ headers: this.headers });
    return this.http.get(this.config.DeviceLogs + id + '/?' + params, options).map((response: Response) => {
        return response.json();
    });
  }

}
