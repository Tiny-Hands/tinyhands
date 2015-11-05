var constants = require('./testConstants.json');

exports.config = {

    onPrepare: function() {
        browser.driver.manage().window().setSize(2000,1800);
    },

    seleniumAddress: 'http://localhost:4444/wd/hub',

    //The order is very important. Ex. budgetForm.spec.js is dependant on borderStationCRUD.spec.js
    specs:  [
        'borderStations/closeABorderStation.spec.js',
      ],
    ////The order is very important. Ex. budgetForm.spec.js is dependant on borderStationCRUD.spec.js
    //specs:  [
    //    // First logically
    //    'accounts/loginPage.spec.js',
    //
    //    'dataentry/irfList.spec.js',
    //    'dataentry/vifList.spec.js',
    //    'dataentry/irfCRUD.spec.js',
    //    'dataentry/vifCrud.spec.js',
    //    'dataentry/search.spec.js', //dependent on vifCrud.spec.js and irfCRUD.spec.js
    //    //
    //
    //    //These three are dependent on each other
    //    'borderStations/borderStationCRUD.spec.js',
    //    'budget/budgetForm.spec.js',
    //    'budget/moneyDistributionForm.spec.js',
    //
    //    'DynStationWindow/dynStation.spec.js',
    //
    //    'addresses/vdcAdminPage.spec.js',
    //    'addresses/address1Page.spec.js',
    //    'accounts/accessDefaults.spec.js',
    //
    //    'accounts/permissionsPage.spec.js' // Has to run last
    //  ],

    framework: 'jasmine2',

    capabilities: {
        "browserName":"chrome"
    }
};
