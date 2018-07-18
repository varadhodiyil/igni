import { environment } from '../../environments/environment';

export class AppConfig {
    public readonly domain = environment.apiUrl;
    public readonly xapikey = 'dABlAHMAdAA=';
    public readonly support = '';
    // public readonly Authorization = JSON.parse(localStorage.getItem('Authorization'));
    public readonly Authorization = 'b3e84f07f791fd221073843d7ce2e4508d5982d4';

    public readonly Login = this.domain + 'auth/login/';
    public readonly Track = this.domain + 'Track';
    public readonly Dashboard = this.domain + 'dashboard/';
    public readonly Devices = this.domain + 'device/';
    public readonly DeviceLogs = this.domain + 'device/logs/';
}
