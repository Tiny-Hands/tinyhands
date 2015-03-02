var constants = require('./testConstants.json');

exports.config = {
    seleniumAddress: 'http://localhost:4444/wd/hub',
    /*specs:  ['accounts/loginPage.spec.js',
	        'irf/irfCRUD.spec.js',
            'accounts/loginPage.spec.js',
            'accounts/permissionsPage.spec.js',
            'vdcs/vdcAdminPage.spec.js'
    ]*/
    specs: ['accounts/permissionsPage.spec.js']
};
