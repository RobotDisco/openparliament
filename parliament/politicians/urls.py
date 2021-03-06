from django.conf.urls import *
from parliament.politicians.views import *

urlpatterns = patterns('parliament.politicians.views',
    url(r'^(?P<pol_id>\d+)/rss/statements/$', 'politician_statement_feed', name="politician_statement_feed"),
    url(r'^(?P<pol_id>\d+)/rss/activity/$', PoliticianActivityFeed(), name="politician_activity_feed"),
    url(r'^$', 'current_mps', name='politicians'),
    (r'^former/$', 'former_mps'),
    (r'^autocomplete/$', 'politician_autocomplete'),
    url(r'^memberships/$', PoliticianMembershipListView.as_view(), name='politician_membership_list'),
    url(r'^memberships/(?P<member_id>\d+)/$', PoliticianMembershipView.as_view(), name='politician_membership'),
    (r'^(?P<pol_slug>[a-z-]+)/$', 'politician'),
    (r'^(?P<pol_id>\d+)/$', 'politician'),
    (r'^(?P<pol_slug>[a-z-]+)/contact/$', 'contact'),
    (r'^(?P<pol_id>\d+)/contact/$', 'contact'),
    (r'^(?P<pol_slug>[a-z-]+)/text-analysis/$', 'analysis'),
    (r'^(?P<pol_id>\d+)/text-analysis/$', 'analysis'),
    (r'^internal/hide_activity/$', 'hide_activity'),
)