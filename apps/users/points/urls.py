from django.urls import path

from .api.views import (GetAccountStatus, GetTransactionStatus,
                        AccountTransactionView, GetTransactionSource, GetTransactionType, GetAccount)

urlpatterns = [
    path('status/', GetAccountStatus.as_view(), name='account_status'),
    path('', GetAccount.as_view(), name='account'),
    path('transaction/status/', GetTransactionStatus.as_view(),
         name='transaction_status'),
    path('transaction/source/', GetTransactionSource.as_view(),
         name='transaction_source'),
    path('transaction/type/', GetTransactionType.as_view(), name='transaction_type'),
    path('transaction/', AccountTransactionView.as_view(),
         name="get_account_transaction"),
]
