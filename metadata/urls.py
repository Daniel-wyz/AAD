from django.urls import path
from . import views

app_name = "metadata"

urlpatterns = [
    path("", views.MetadataListView.as_view(), name="home"),
    path("metadata/<str:metadata_id>/", views.metadata_detail_view, name="detail"),
    path("create/<str:metadata_id>/", views.create_metadata, name="create"),
    path("pdf/<str:metadata_id>/", views.render_pdf_view, name="pdf"),
    path("xml/<str:metadata_id>/", views.download_xml, name="xml"),
    path("upload/", views.upload_documents, name="upload"),
    path("search_science_keywords/", views.search_science_keywords, name="keywords"),
]
