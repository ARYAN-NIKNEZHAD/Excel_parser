from rest_framework_nested.routers import DefaultRouter
from core.api.views.excel_files import ExcelFileViewSet


router = DefaultRouter()

router.register("excel_files", ExcelFileViewSet, basename="excel_files")

urlpatterns = router.urls