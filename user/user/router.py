from api.viewsets import PermissionViewset,RoleViewset,UserViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register('permission',PermissionViewset)
router.register('role',RoleViewset)
router.register('user',UserViewset)