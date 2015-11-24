var c = require('../testConstants.json');
var loginPage = require('../accounts/loginPage.js');
var irfPage = require('./irfCRUD.js');

describe('Interception Record Form -', function() {

    beforeEach(function () {
        return browser.ignoreSynchronization = true;
    });

    describe('A user', function () {
        it('Logs In', function () {
            loginPage.logout();
            loginPage.loginAsAdmin();
        });

        it('Can Create an IRF', function () {
            irfPage.getToIRF();
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/create/');
            irfPage.fillOutIRF(c.irfNumber);
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/');
        });

        it('Can Read an IRF', function () {
            irfPage.viewIRF();
            expect(browser.driver.getCurrentUrl()).toContain('/data-entry/irfs/');
            expect(element(by.id('id_irf_number')).getAttribute('value')).toEqual(c.irfNumber);
            expect(element(by.id('id_location')).getAttribute('value')).toEqual(c.irfLocation);
            expect(element(by.id('id_date_time_of_interception')).getAttribute('value')).toContain(c.irfInterceptTimeTest);
            expect(element(by.id('id_staff_name')).getAttribute('value')).toEqual(c.irfStaffName);
            expect(element(by.id('id_drugged_or_drowsy')).isSelected()).toBeTruthy();
            expect(element(by.id('id_contact_noticed')).isSelected()).toBeTruthy();
            expect(element(by.id('id_which_contact_hotel_owner')).isSelected()).toBeTruthy();
            expect(element(by.cssContainingText('option', 'Victim')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-full_name')).getAttribute('value')).toEqual(c.irfInterceptFname);
            expect(element(by.cssContainingText('option', 'F')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-district')).getAttribute('value')).toEqual(c.irfInterceptDistrict);
            expect(element(by.id('id_interceptees-0-vdc')).getAttribute('value')).toEqual(c.irfInterceptVdc);
            expect(element(by.cssContainingText('option', 'Absolutely sure'))).toBeTruthy();
            expect(element(by.id('id_interception_type_india_trafficking')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_subcommittee_chair')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_thn_to_cross_check')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_1')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_value')).getAttribute('value')).toEqual(c.irfNameCameUpBeforeValue);
            expect(element(by.id('id_scan_and_submit_same_day')).isSelected()).toBeTruthy();
            expect(element(by.id('id_has_signature')).isSelected()).toBeTruthy();
            browser.get(c.webAddress + '/data-entry/irfs/');
        });

        it('Can Edit an IRF', function () {
            irfPage.editIRF();
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/');
            irfPage.viewIRF();
            expect(element(by.id('id_irf_number')).getAttribute('value')).toEqual(c.irfEditNumber);
            expect(element(by.id('id_location')).getAttribute('value')).toEqual(c.irfLocation);
            expect(element(by.id('id_date_time_of_interception')).getAttribute('value')).toContain(c.irfInterceptTimeTest);
            expect(element(by.id('id_staff_name')).getAttribute('value')).toEqual(c.irfStaffName);
            expect(element(by.id('id_drugged_or_drowsy')).isSelected()).toBeTruthy();
            expect(element(by.id('id_contact_noticed')).isSelected()).toBeTruthy();
            expect(element(by.id('id_which_contact_hotel_owner')).isSelected()).toBeTruthy();
            expect(element(by.cssContainingText('option', 'Victim')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-full_name')).getAttribute('value')).toEqual(c.irfInterceptFname);
            expect(element(by.cssContainingText('option', 'F')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-district')).getAttribute('value')).toEqual(c.irfInterceptDistrict);
            expect(element(by.id('id_interceptees-0-vdc')).getAttribute('value')).toEqual(c.irfInterceptVdc);
            expect(element(by.cssContainingText('option', 'Absolutely sure'))).toBeTruthy();
            expect(element(by.id('id_interception_type_india_trafficking')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_subcommittee_chair')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_thn_to_cross_check')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_1')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_value')).getAttribute('value')).toEqual(c.irfNameCameUpBeforeValue);
            expect(element(by.id('id_scan_and_submit_same_day')).isSelected()).toBeTruthy();
            expect(element(by.id('id_has_signature')).isSelected()).toBeTruthy();
            browser.get(c.webAddress + '/data-entry/irfs/');
        });

        it('Cannot Edit while Viewing IRF', function() {
            irfPage.viewIRF();
            expect(element(by.id('id_irf_number')).getAttribute('disabled')).toEqual('true');
        });

        it ('Can Delete an IRF', function () {
            //irfPage.getToIRF();
            //irfPage.fillOutIRF();
            browser.get(c.webAddress + '/data-entry/irfs/');
            //var firstLink = element(by.xpath("//a[@class='btn btn-sm btn-primary']")).getAttribute('href');
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/');
            irfPage.deleteIRF();
            //var secondLink = element(by.xpath("//a[@class='btn btn-sm btn-primary']")).getAttribute('href');
            browser.sleep(500);
            expect(element(by.xpath("//a[@class='btn btn-sm btn-primary']")).isPresent()).toBe(false);
            //expect(firstLink != secondLink).toBeTruthy();

        });
        it('create save for later', function() {
            browser.sleep(2000);
            irfPage.getToIRF();
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/create/');
            browser.sleep(2000);
            irfPage.fillOutPartialIRF1('abc123');
            browser.sleep(2000);
            irfPage.getToIRF();
            expect(browser.driver.getCurrentUrl()).toContain('data-entry/irfs/create/');
            browser.sleep(2000);
            irfPage.fillOutPartialIRF2('abc456');
        });
        it('check save for later', function() {
            browser.sleep(2000);
            irfPage.getToIRF();
            element(by.xpath('//*[@id="saved-for-later-list"]/option[2]')).click();
            expect(element(by.id('id_irf_number')).getAttribute('value')).toEqual('abc123');
            expect(element(by.id('id_location')).getAttribute('value')).toEqual(c.irfLocation);
            expect(element(by.id('id_date_time_of_interception')).getAttribute('value')).toContain(c.irfInterceptTime);
            expect(element(by.id('id_staff_name')).getAttribute('value')).toEqual(c.irfStaffName);
            expect(element(by.id('id_drugged_or_drowsy')).isSelected()).toBeTruthy();
            expect(element(by.id('id_contact_noticed')).isSelected()).toBeTruthy();
            expect(element(by.id('id_which_contact_hotel_owner')).isSelected()).toBeTruthy();
            expect(element(by.cssContainingText('option', 'Victim')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-full_name')).getAttribute('value')).toEqual(c.irfInterceptFname);
            expect(element(by.cssContainingText('option', 'F')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-district')).getAttribute('value')).toEqual(c.irfInterceptDistrict);
            expect(element(by.id('id_interceptees-0-vdc')).getAttribute('value')).toEqual(c.irfInterceptVdc);
            expect(element(by.cssContainingText('option', 'Absolutely sure'))).toBeTruthy();
            expect(element(by.id('id_interception_type_india_trafficking')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_subcommittee_chair')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_thn_to_cross_check')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_1')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_value')).getAttribute('value')).toEqual(c.irfNameCameUpBeforeValue);
            expect(element(by.id('id_scan_and_submit_same_day')).isSelected()).toBeTruthy();
            expect(element(by.id('id_has_signature')).isSelected()).toBeTruthy();
            
            browser.sleep(2000);
            irfPage.getToIRF();
            element(by.xpath('//*[@id="saved-for-later-list"]/option[3]')).click();
            expect(element(by.id('id_irf_number')).getAttribute('value')).toEqual('abc456');
            expect(element(by.id('id_location')).getAttribute('value')).toEqual(c.irfLocation);
            expect(element(by.id('id_date_time_of_interception')).getAttribute('value')).toContain(c.irfInterceptTime);
            expect(element(by.id('id_staff_name')).getAttribute('value')).toEqual(c.irfStaffName);
            expect(element(by.id('id_drugged_or_drowsy')).isSelected()).toBeTruthy();
            expect(element(by.id('id_contact_noticed')).isSelected()).toBeTruthy();
            expect(element(by.id('id_which_contact_hotel_owner')).isSelected()).toBeTruthy();
            expect(element(by.cssContainingText('option', 'Victim')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-full_name')).getAttribute('value')).toEqual(c.irfInterceptFname);
            expect(element(by.cssContainingText('option', 'F')).isSelected()).toBeTruthy();
            expect(element(by.id('id_interceptees-0-district')).getAttribute('value')).toEqual(c.irfInterceptDistrict);
            expect(element(by.id('id_interceptees-0-vdc')).getAttribute('value')).toEqual(c.irfInterceptVdc);
            expect(element(by.cssContainingText('option', 'Absolutely sure'))).toBeTruthy();
            expect(element(by.id('id_interception_type_india_trafficking')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_subcommittee_chair')).isSelected()).toBeTruthy();
            expect(element(by.id('id_call_thn_to_cross_check')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_1')).isSelected()).toBeTruthy();
            expect(element(by.id('id_name_came_up_before_value')).getAttribute('value')).toEqual(c.irfNameCameUpBeforeValue);
            expect(element(by.id('id_scan_and_submit_same_day')).isSelected()).toBeTruthy();
            expect(element(by.id('id_has_signature')).isSelected()).toBeTruthy();

        });
    });
});


