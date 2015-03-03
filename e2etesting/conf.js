var constants = require('./testConstants.json');

exports.config = {

  seleniumAddress: 'http://localhost:4444/wd/hub',

  //allScriptsTimeout: 10000,

  //SITE_DOMAIN: '0.0.0.0:8000',

  specs:  ['accounts/loginPage.spec.js',
	        'irf/irfCRUD.spec.js',
            'accounts/loginPage.spec.js',
            'vdcs/vdcAdminPage.spec.js',
            'borderStations/borderStationCRUD.spec.js',
            'accounts/permissionsPage.spec.js'
          ]

};
