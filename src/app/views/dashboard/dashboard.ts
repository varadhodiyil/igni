export class Dashboard {
    id: number;
    name: string;
    date_joined: Date;
    driver_name: string;
    owner: number;
    updated_at?: Date;
    status: string;
    latitude?: number;
    longitude?: number;
    speed?: number;
    altitude?: number;
    odometer?: number;
    address: string;
    fuel_level?: number;
    temperature?: number;
    ac_status  = '';
    fuel_diff?: number;
    device?: number;
    ignition_status: string;
}
