export class AppConfig {
    public readonly domain = 'http://track.skalenow.com/api/';
    public readonly domain1 = '';
    public readonly xapikey = 'dABlAHMAdAA=';
    public readonly support = '';
    public readonly Authorization = JSON.parse(localStorage.getItem('Authorization'));

    public readonly Track = this.domain + 'Track';
}
