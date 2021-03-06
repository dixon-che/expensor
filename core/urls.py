from __future__ import absolute_import

from django.conf.urls import patterns, url
from core.views.people import (PeopleView, PersonDetailView, PersonEdit,
                               SalaryAddView)
from core.views.settings import (DashboardView, SettingsView, AccountCreateView,
                                 ExpenseCategoryAddView, CurrencyAddView)
from core.views.transactions import (TransactionListView, IncomeAddView,
                                     ExpenseAddView, TransferAddView,
                                     CommissionAddView, PaymentAddView)


urlpatterns = patterns('core.views',
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^settings/$', SettingsView.as_view(), name='settings'),

    url(r'^people/$', PeopleView.as_view(), name='people'),
    url(r'^people/(?P<pk>\d+)$', PersonDetailView.as_view(), name='person'),
    url(r'^people/add/$', PersonEdit.as_view(), name='add_person'),
    url(r'^people/edit/(?P<pk>\d+)$', PersonEdit.as_view(), name='edit_person'),

    url(r'^salaries/add/$', SalaryAddView.as_view(), name='add_salary'),

    url(r'^accounts/add/$', AccountCreateView.as_view(), name='add_account'),

    url(r'^expense_categories/add/$', ExpenseCategoryAddView.as_view(),
        name='add_expense_category'),

    url(r'^currencies/add/$', CurrencyAddView.as_view(), name='add_currency'),

    url(r'^transactions/$', TransactionListView.as_view(), name='transactions'),
    url(r'^income/add/$', IncomeAddView.as_view(), name='add_income'),
    url(r'^expense/add/$', ExpenseAddView.as_view(), name='add_expense'),
    url(r'^transfer/add/$', TransferAddView.as_view(), name='add_transfer'),
    url(r'^comission/add/(?P<pk>\d+)$', CommissionAddView.as_view(),
        name='add_comission'),
    url(r'^payment/add/(?P<pk>\d+)$', PaymentAddView.as_view(),
        name='add_payment'),
)
