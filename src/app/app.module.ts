import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { LocationStrategy, HashLocationStrategy } from '@angular/common';
import { HttpModule  } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { PerfectScrollbarModule } from 'ngx-perfect-scrollbar';
import { PERFECT_SCROLLBAR_CONFIG } from 'ngx-perfect-scrollbar';
import { PerfectScrollbarConfigInterface } from 'ngx-perfect-scrollbar';

const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true
};
import { AppConfig } from './config/app.config';

import { AppComponent } from './app.component';

// Import containers
import { DefaultLayoutComponent } from './containers';


import { LoginComponent } from './views/login/login.component';
import { RegisterComponent } from './views/register/register.component';
import { IgniserviceService } from './services/igniservice.service';

const APP_CONTAINERS = [
  DefaultLayoutComponent
];

import {
  AppAsideModule,
  AppBreadcrumbModule,
  AppHeaderModule,
  AppFooterModule,
  AppSidebarModule,
} from '@coreui/angular';

// Import routing module
import { AppRoutingModule } from './app.routing';

// Import 3rd party components
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { TabsModule } from 'ngx-bootstrap/tabs';
import { ChartsModule } from 'ng2-charts/ng2-charts';
import { VehicleComponent } from './mapping/vehicle/vehicle.component';
import { DeviceComponent } from './mapping/device/device.component';
import { VehicleReportComponent } from './report/vehicle-report/vehicle-report.component';
import { DeviceReportComponent } from './report/device-report/device-report.component';
import { DistanceComponent } from './report/distance/distance.component';
import { IgnitionComponent } from './report/ignition/ignition.component';
import { AdminComponent } from './admin/admin.component';
@NgModule({
  imports: [
    HttpModule,
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    AppAsideModule,
    AppBreadcrumbModule.forRoot(),
    AppFooterModule,
    AppHeaderModule,
    AppSidebarModule,
    PerfectScrollbarModule,
    BsDropdownModule.forRoot(),
    TabsModule.forRoot(),
    ChartsModule,
  ],
  declarations: [
    AppComponent,
    ...APP_CONTAINERS,
    // P404Component,
    // P500Component,
    LoginComponent,
    RegisterComponent,
    VehicleComponent,
    DeviceComponent,
    VehicleReportComponent,
    DeviceReportComponent,
    DistanceComponent,
    IgnitionComponent,
    AdminComponent
  ],
  providers: [
    {
      provide: LocationStrategy,
      useClass: HashLocationStrategy
  },
  AppConfig,
  IgniserviceService,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
