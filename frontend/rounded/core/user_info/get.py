from rounded.core.user_info import accounts
from rounded.core import redis
from flask import current_app as app

API_KEY = "5843532b7d4678ebf648c08c09c61d81"
NAME = app.config.get("CUSTOMER")

CUSTOMERS = accounts.get_customers(API_KEY)
CUSTOMER_ID = accounts.get_customers_id(CUSTOMERS, NAME)
CLIENT = accounts.make_client(API_KEY, CUSTOMER_ID)
ACCOUNTS = accounts.get_customers_accounts(API_KEY, CLIENT)
