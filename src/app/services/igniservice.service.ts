import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { AppConfig } from '../config/app.config';
import 'rxjs/add/operator/map';

@Injectable()
export class IgniserviceService {

  constructor(private http: Http, private config: AppConfig) { }

  private headers1 = new Headers({'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Bearer ' + this.config.Authorization,
    'Accept': 'application/json, text/plain',
    'x-api-key': this.config.xapikey});

  public getTrack() {
    const options = new RequestOptions({ headers: this.headers1 }); 
    return this.http.get(this.config.Track , options).map((response: Response) => {
        return response.json();
    });
  }

}
