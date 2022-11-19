from django.contrib import admin
from django.contrib.admin.apps import AdminConfig


class ProductsModuleAdmin(admin.AdminSite):
    site_header = "Products Admin"
    site_title = "Products Admin"
    index_title = "Welcome to Catalog"


productAdmin = ProductsModuleAdmin(name="productAdmin")
