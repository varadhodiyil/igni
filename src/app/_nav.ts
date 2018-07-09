export const navItems = [
  {
    name: 'Dashboard',
    url: '/dashboard',
    icon: 'icon-speedometer',
    // badge: {
    //   variant: 'info',
    //   text: 'NEW'
    // }
  },
  // {
  //   title: true,
  //   name: 'Components'
  // },
  {
    name: 'Mapping',
    url: '/maps',
    icon: 'icon-map',
    children: [
      {
        name: 'Vehicle',
        url: '/maps/vehicle',
        icon: 'icon-puzzle'
      },
      {
        name: 'Device',
        url: '/maps/device',
        icon: 'icon-puzzle'
      }
    ]
  },
  {
    name: 'Reports',
    url: '/report',
    icon: 'icon-docs',
    children: [
      {
        name: 'Vehice Summary',
        url: '/report/vehicle',
        icon: 'icon-cursor'
      },
      {
        name: 'Device Group Summary',
        url: '/report/device',
        icon: 'icon-cursor'
      },
      {
        name: 'Distance Reports',
        url: '/report/distance',
        icon: 'icon-cursor'
      },
      {
        name: 'Ignition Reports',
        url: '/report/ignition',
        icon: 'icon-cursor'
      }
    ]
  },
  {
    name: 'Charts',
    url: '/charts',
    icon: 'icon-pie-chart',
    children: [
      {
        name: 'Speed Chart',
        url: '/charts/speed',
        icon: 'icon-cursor'
      },
      {
        name: 'Temperature Chart',
        url: '/charts/temperature',
        icon: 'icon-cursor'
      }
    ]
  },
  {
    name: 'Administration',
    url: '/admin',
    icon: 'icon-people',
  },
];
