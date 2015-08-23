from django.conf.urls import patterns, url

from user_contacts import views

urlpatterns = patterns('',
      url(r'^$', views.home,name = 'home'),
      url(r'^all/$',views.all_contacts,name = 'all_contacts'),
      url(r'^add/$', views.add,name = 'add'),

)

#url(r'^$', 'contacts.views.home', name='home'),

'''
from django.conf.urls import url
from myapp import views

urlpatterns = [
    url('^$', views.myview),
    url('^other/$', views.otherview),
]
'''