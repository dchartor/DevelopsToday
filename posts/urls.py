from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet


router = SimpleRouter()
router.register(r'comments', CommentViewSet, basename='comments')
# router.register('update', UpdateViewSet, basename='update')
router.register(r'', PostViewSet, basename='posts')

urlpatterns = router.urls
