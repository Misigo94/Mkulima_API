from mkulimapp.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('merchandise', MerchandiseViewset)
router.register('feeds', FeedsViewset)
router.register('category', CategoryViewset)
router.register('comment', CommentViewset)
# router.register('user', UserViewset)
