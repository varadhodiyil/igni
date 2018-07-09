import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// Import Containers
import { DefaultLayoutComponent } from './containers';


import { LoginComponent } from './views/login/login.component';
import { RegisterComponent } from './views/register/register.component';
import { VehicleComponent } from './mapping/vehicle/vehicle.component';
import { DeviceComponent } from './mapping/device/device.component';
import { VehicleReportComponent } from './report/vehicle-report/vehicle-report.component';
import { DeviceReportComponent } from './report/device-report/device-report.component';
import { DistanceComponent } from './report/distance/distance.component';
import { IgnitionComponent } from './report/ignition/ignition.component';
import { AdminComponent } from './admin/admin.component';
export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: LoginComponent,
    data: {
      title: 'Login Page'
    }
  },
  {
    path: 'register',
    component: RegisterComponent,
    data: {
      title: 'Register Page'
    }
  },
  {
    path: '',
    component: DefaultLayoutComponent,
    data: {
      title: 'Home'
    },
    children: [
      {
        path: 'dashboard',
        loadChildren: './views/dashboard/dashboard.module#DashboardModule'
      },
      {
        path: 'maps/vehicle',
        component: VehicleComponent,
        data: {
          title: 'Mapping - Vehicle'
        }
      },
      {
        path: 'maps/device',
        component: DeviceComponent,
        data: {
          title: 'Mapping - Device'
        }
      },
      {
        path: 'report/vehicle',
        component: VehicleReportComponent,
        data: {
          title: 'Report - Vehicle'
        }
      },
      {
        path: 'report/device',
        component: DeviceReportComponent,
        data: {
          title: 'Report - Device'
        }
      },
      {
        path: 'report/distance',
        component: DistanceComponent,
        data: {
          title: 'Report - Distance'
        }
      },
      {
        path: 'report/ignition',
        component: IgnitionComponent,
        data: {
          title: 'Report - Ignition'
        }
      },
      {
        path: 'admin',
        component: AdminComponent,
        data: {
          title: 'Admin'
        }
      },
    ]
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
