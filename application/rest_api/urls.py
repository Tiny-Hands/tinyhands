from django.conf.urls import url

from rest_framework.authtoken import views

from portal.views import get_interception_records
from dataentry.views import Address2ViewSet, Address1ViewSet, GeoCodeAddress1APIView, GeoCodeAddress2APIView, InterceptionRecordViewSet, VictimInterviewViewSet, BatchView, IntercepteeViewSet, VictimInterviewDetailViewSet
from budget.views import BudgetViewSet, OtherItemsViewSet, OldBudgetViewSet, OldOtherItemsViewSet, MoneyDistribution, MoneyDistributionFormPDFView, money_distribution_view, retrieve_latest_budget_sheet_for_border_station, previous_data, StaffSalaryViewSet
from accounts.views import AccountViewSet, DefaultPermissionsSetViewSet, CurrentUserView, ResendActivationEmailView, AccountActivateView, AccountActivateClient
from static_border_stations.views import BorderStationViewSet, StaffViewSet, CommitteeMemberViewSet, LocationViewSet
from events.views import EventViewSet


list = {'get': 'list', 'post': 'create'}
detail = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    # Accounts App
        url(r'^login/', views.obtain_auth_token),
        url(r'^me/$', CurrentUserView.as_view(), name="CurrentUser"),

        url(r'^account/$', AccountViewSet.as_view(list), name="AccountList"),
        url(r'^account/all/$', AccountViewSet.as_view({'get': 'list_all'}), name="AccountListAll"),
        url(r'^account/(?P<pk>\d+)/$', AccountViewSet.as_view(detail), name='Account'),
        url(r'^account/activate/(?P<activation_key>[a-zA-Z0-9]+)/$', AccountActivateClient.as_view(), name='account_activate'),
        url(r'^account/resend-activation-email/(?P<pk>\d+)/$', ResendActivationEmailView.as_view(), name='ResendActivationEmail'),

        url(r'^defaultPermissionsSet/$', DefaultPermissionsSetViewSet.as_view(list), name="DefaultPermissionsSets"),
        url(r'^defaultPermissionsSet/(?P<pk>\d+)/$', DefaultPermissionsSetViewSet.as_view(detail), name="DefaultPermissionsSet"),


    # Data Entry App
        # Addresses
        url(r'^address1/$', Address1ViewSet.as_view(list), name='Address1'),
        url(r'^address1/all/$', Address1ViewSet.as_view({'get': 'list_all'}), name='Address1all'),
        url(r'^address1/(?P<pk>\d+)/$', Address1ViewSet.as_view(detail), name='Address1detail'),

        url(r'^address2/$', Address2ViewSet.as_view(list), name='Address2'),
        url(r'^address2/(?P<pk>\d+)/$', Address2ViewSet.as_view(detail), name='Address2detail'),

        url(r'^address1/fuzzy/$', GeoCodeAddress1APIView.as_view(), name="Address1FuzzySearch"),
        url(r'^address2/fuzzy/$', GeoCodeAddress2APIView.as_view(), name="Address2FuzzySearch"),

        # IRFs
        url(r'^irf/$', InterceptionRecordViewSet.as_view(list), name="InterceptionRecord"),
        url(r'^irf/(?P<pk>\d+)/$', InterceptionRecordViewSet.as_view(detail), name="InterceptionRecordDetail"),

        # Interceptee
        url(r'^interceptee/$', IntercepteeViewSet.as_view(list), name="Interceptee"),
        url(r'^interceptee/(?P<pk>\d+)/$', IntercepteeViewSet.as_view(detail), name="IntercepteeDetail"),

        # VIFs
        url(r'^vif/$', VictimInterviewViewSet.as_view(list), name="VictimInterview"),
        url(r'^vif/(?P<pk>\d+)/$', VictimInterviewDetailViewSet.as_view(detail), name="VictimInterviewDetail"),

    # Budget URLs
        url(r'^budget/$', BudgetViewSet.as_view(list), name='BudgetCalculation'),
        url(r'^budget/(?P<pk>\d+)/$', BudgetViewSet.as_view(detail), name='BudgetCalculationWithId'),

        url(r'^budget/(?P<parent_pk>\d+)/item/$', OtherItemsViewSet.as_view(list), name='BudgetCalculationWithId'),
        url(r'^budget/(?P<parent_pk>\d+)/item/(?P<pk>\d+)/$', OtherItemsViewSet.as_view(detail), name='BudgetCalculationWithId'),

        url(r'^budget/most_recent_form/(?P<pk>\d+)/$', retrieve_latest_budget_sheet_for_border_station, name="rest_api_budget_new_api"),
        url(r'^budget/previous_data/(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/$', previous_data, name="rest_api_previous_data"),

        url(r'^budget/staff_salary/$', StaffSalaryViewSet.as_view(list), name="rest_api_staff_salary_list_api"),
        url(r'^budget/(?P<parent_pk>\d+)/staff_salary/$', StaffSalaryViewSet.as_view({'get': 'budget_calc_retrieve'}), name="rest_api_staff_salary_detail_api"),
        url(r'^budget/(?P<parent_pk>\d+)/staff_salary/(?P<pk>\d+)/$', StaffSalaryViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name="rest_api_staff_salary_detail_api"),

        url(r'^budget/money_distribution/(?P<pk>\d+)/$', MoneyDistribution.as_view({'get': 'get_people_needing_form', 'post': 'send_emails'}), name="rest_api_money_distribution_api"),
        url(r'^budget/money_distribution_pdf/(?P<pk>\d+)/$', MoneyDistributionFormPDFView.as_view(), name="rest_api_money_distribution_pdf"),
        url(r'^budget/money_distribution/view/(?P<pk>\d+)/$', money_distribution_view, name="rest_api_money_distribution_view"),

        # Old Budget viewsets for the old django site. needs to change eventually - ask ben duggan about it
            # Budget URLs
            url(r'^Oldbudget/$', OldBudgetViewSet.as_view({'get': 'list', 'post': 'create'}), name='OldBudgetCalculation'),
            url(r'^Oldbudget/(?P<pk>\d+)/$', OldBudgetViewSet.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}), name='OldBudgetCalculationWithId'),

            # Other items
            url(r'^Oldbudget/(?P<parent_pk>\d+)/item/$', OldOtherItemsViewSet.as_view({'get': 'list_by_budget_sheet', 'post': 'create'}), name='OldBudgetCalculationWithId'),
            url(r'^Oldbudget/(?P<parent_pk>\d+)/item/(?P<pk>\d+)/$', OldOtherItemsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='OldBudgetCalculationWithId'),


    # Portal App
        url(r'^get_interception_records/$', get_interception_records, name='get_interception_records'),


    # Static Border Station App
        # Border Stations
        url(r'^border-station/$', BorderStationViewSet.as_view({'get':'list_all', 'post':'create'}), name="BorderStations"), # Detail
        url(r'^border-station/(?P<pk>\d+)/$', BorderStationViewSet.as_view(detail), name="BorderStation"),

        # Committee Members
        url(r'^committee-member/$', CommitteeMemberViewSet.as_view(list), name="CommitteeMembers"),
        url(r'^committee-member/(?P<pk>\d+)/$', CommitteeMemberViewSet.as_view(detail), name="CommitteeMember"),

        # Locations
        url(r'^location/$', LocationViewSet.as_view(list), name="Locations"),
        url(r'^location/(?P<pk>\d+)/$', LocationViewSet.as_view(detail), name="Location"),

        # Staff
        url(r'^staff/$', StaffViewSet.as_view(list), name="AllStaff"),
        url(r'^staff/(?P<pk>\d+)/$', StaffViewSet.as_view(detail), name="Staff"),

        # Events
            url(r'^event/$', EventViewSet.as_view({'get': 'list', 'post':'create'}), name="EventList"),
            url(r'^event/all/$', EventViewSet.as_view({'get': 'list_all'}), name="EventListAll"),
            url(r'^event/(?P<pk>\d+)/$', EventViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='Event'),
            url(r'^event/feed/calendar/$', EventViewSet.as_view({'get': 'calendar_feed'}), name='EventCalendarFeed'),
            url(r'^event/feed/dashboard/$', EventViewSet.as_view({'get': 'dashboard_feed'}), name='EventDashboardFeed'),
        #IRFBatch
        url(r'^batch/(?P<startDate>(\d{2}|\d{1})-(\d{2}|\d{1})-\d{4})/(?P<endDate>\d{2}-\d{2}-\d{4})', BatchView.as_view(), name="BatchView")
]


