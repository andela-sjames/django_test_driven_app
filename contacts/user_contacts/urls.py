from django.conf.urls import patterns, url

from user_contacts.views import *

urlpatterns = patterns('',
      url(r'^$', 'user_contacts.views',name = home),
      url(r'^all/$','user_contacts.views',name = all_contacts),
      url(r'^add/$', 'user_contacts.views',name =add),

)

#url(r'^$', 'contacts.views.home', name='home'),