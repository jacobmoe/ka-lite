from django.conf.urls.defaults import include, patterns, url

import api_urls


urlpatterns = patterns('securesync.users.views',
    url(r'^addteacher/$', 'add_facility_teacher', {}, 'add_facility_teacher'),
    url(r'^addstudent/$', 'add_facility_student', {}, 'add_facility_student'),
    url(r'^facility/$', 'facility_admin', {}, 'facility_admin'),
    url(r'^facility/new/$', 'facility_edit', {"id": "new"}, 'add_facility'),
    url(r'^facility/(?P<id>\w+)/$', 'facility_edit', {}, 'facility_edit'),
    url(r'^addgroup/$', 'add_group', {}, 'add_group'),
    url(r'^login/$', 'login', {}, 'login'),
    url(r'^logout/$', 'logout', {}, 'logout'),
    url(r'^api/', include(api_urls)),
)
