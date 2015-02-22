from django.conf.urls import patterns, url
from main.views import *

urlpatterns = patterns('',
		# url(r'^offers/$', show_offers, name='show all offers'),
  #       url(r'^firewallz/$', firewallzo_gl, name='firewallz outer booth home'),
  #       url(r'^firewallz/edit/(?P<participant_id>\d+)/$',firewallzo_edit_participant,name='editing individual participants'),
		# url(r'^firewallz/add/(?P<gl_id>\d+)/$',firewallzo_add_participant,name='add participant'),
		# url(r'^firewallz/newgl/(?P<gl_id>\d+)/$',firewallzo_gl_reassign,name='firewallzo_gl_reassign'),
		# url(r'^firewallz/remove/(?P<gl_id>\d+)/$',firewallzo_remove_people,name='remove participant'),
		# #url(r'^firewallzi/$',firewallz_fid,name='Firewallz Inner Booth'),
		# url(r'^recnacc/$', reconec_home, name='recnacc home'),
		# url(r'^recnnac/allot/(?P<gl_id>\d+)/$',acco_list,name='provides accomodation'),
		# url(r'^recnacc/deallocate/(?P<gl_id>\d+)/$',reconec_deallocate,name='provides accomodation'),
		# url(r'^recnacc/phonedetails/(?P<gl_id>\d+)/$',phonedetails,name='phone numbers'),
		url(r'^offers/(?P<category>trunks|electronics)/$',show_offers,name='checkout people'),
		url(r'^electronics/search/$', search_offers_e, name='search electronic stuff'),
		url(r'^makeoffer/$', makeoffer, name='search electronic stuff'),
		url(r'^makeoffere/$', make_offere, name='search electronic stuff'),
		url(r'^makeoffert/$', make_offert, name='search electronic stuff'),
		url(r'^about/$', about, name='search electronic stuff'),
		# url(r'^recnacc/roomdetails/$', room_details, name='all bhavans'),
		# url(r'^recnacc/bhavanwise/$',college_in_bhavan,name='bhavan college mapping'),
		# url(r'^controlz/receipt/$', receipt, name='controlzhome'),
		# url(r'^controlz/eventdetails/$', controlz_event_details, name='event participants details'),
  #       url(r'^controlz/edit/(?P<participant_id>\d+)/$',controlz_edit_participant,name='editing individual participants for controlz'),
  #       url(r'^controlz/bill/(?P<gl_id>\d+)/$',generate_receipt,name='print bill')
  )
