from mkulimapp.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('farmer',FarmerViewset)
router.register('vendor',VendorViewset)
router.register('merchandise',MerchandiseViewset)
router.register('feeds',FeedsViewset)
router.register('category',CategoryViewset)
router.register('comment',CommentViewset)
