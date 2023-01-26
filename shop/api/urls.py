from django.urls import re_path, path
from .views import CategoriesListView, ProducerListView, ProductListView, PromocodeListView, DiscountsListView, \
    CategoryProductView, ProducerProductView, DiscountProductView, RegistrationView, ActivateAccountView, LoginView,\
    BasketView, CreateOrderView, SingleProductView


urlpatterns = [
    re_path(r'^categories-all/',CategoriesListView.as_view(), name='categories-all'),
    re_path(r'^discounts-all/',DiscountsListView.as_view(), name='discounts-all'),
    re_path(r'^producers-all/',ProducerListView.as_view(), name='producers-all'),
    re_path(r'^products-all/',ProductListView.as_view(), name='products-all'),
    re_path(r'^promocodes-all/',PromocodeListView.as_view(), name='promocodes-all'),
    path('category/<int:cat_id>/', CategoryProductView.as_view()),
    path('producer/<int:producer_id>/', ProducerProductView.as_view()),
    path('discount/<int:discount_id>/', DiscountProductView.as_view()),
    re_path(r'^register/', RegistrationView.as_view()),
    path('activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate'),
    re_path(r'^login/', LoginView.as_view()),
    re_path(r'^basket/', BasketView.as_view()),
    re_path(r'^create-order/', CreateOrderView.as_view()),
    path('product/<int:product_id>/', SingleProductView.as_view()),

]