__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework.routers import DefaultRouter
from larave_appl import views
router=DefaultRouter()
router.register(r'state',views.Stat_views,basename='state')
router.register(r'search',views.search_emp,basename='search')
router.register(r'create',views.Employee_view,basename='create')

urlpatterns=router.urls
