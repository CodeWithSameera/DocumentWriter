## developed by sameera

import sqlite3

from model import QuoteItem,Quote,Customer
from .logger_config import setup_logger

class DatabaseManager:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.logger = setup_logger()

    def fetch_quote_data(self, cart_id,limit=10,offset=0):

        query = """
        SELECT 
            ci.CUSTOMER_FIRST_NAME, 
            ci.CUSTOMER_LAST_NAME, 
            ci.CUSTOMER_E_MAIL_ADDR,
            ci.CUSTOMER_TITLE, 
            ci.CUSTOMER_COMPANY,
            ci.CUSTOMER_ADDR1, 
            ci.CUSTOMER_ADDR2, 
            ci.CUSTOMER_CITY, 
            ci.CUSTOMER_STATE, 
            ci.CUSTOMER_PROVINCE,
            ci.CUSTOMER_ZIP_CODE, 
            ci.CUSTOMER_COUNTRY, 
            ci.CUSTOMER_BUSINESS_PHONE,
            ci.customer_code,

            c.DATE_ORDERED, 
            c.ORDER_STATUS, 
            c.TOTALAMOUNT, 
            c.DEF_CURRENCY,
            c.currency_quote, 
            c.CART_ID,
            c.SHIPPING_METHOD, 
            c.send_email_bill, 
            c.SHIPPING_COST,
            c.PAYMENT_METHOD, 
            c.PAYMENT_APROOVED, 
            c.CART_COMMENT,
            c.MY_BILL_TO, 
            c.MY_SHIP_TO, 
            c.Origin,

            ci.CATALOGCODE, 
            ci.DESCRIPTION, 
            ci.QUANTITY, 
            ci.USER_DESCRIPTION, 
            ci.RecurringPrice, 
            ci.UnitOfMeasure, 
            ci.ITEM_DELIVERY_STATUS, 
            ci.ITEM_DELIVERY_METHOD, 
            ci.NETPRICE, 
            ci.CURRENCY, 
            ci.PRODUCT_WEIGHT
        FROM CART c
        LEFT JOIN CUSTOMER_INFO ci ON c.CUSTOMER_ID = ci.CUSTOMER_ID
        LEFT JOIN CART_ITEM ci ON c.CART_ID = ci.CART_ID
        WHERE c.CART_ID = ?
        LIMIT ? OFFSET ?;
        """

        with self.connection as conn:
            results = conn.execute(query, (cart_id,limit,offset)).fetchall()

        if not results:
            self.logger.error(f"No data found for cart_id {cart_id} with limit {limit} and offset {offset}")
            raise ValueError(f"No data found for cart_id {cart_id}")

        first_row = dict(results[0])
        customer = Customer(first_row)
        quote = Quote(first_row)

        items = [QuoteItem(dict(row)) for row in results]

        return customer, quote, items

    def get_all_cart_ids(self):
        query = "SELECT CART_ID FROM CART"
        with self.connection as conn:
            results = conn.execute(query).fetchall()

        if not results:
            self.logger.error("No cart IDs found in the database.")
            raise ValueError("No cart IDs available in the database.")

        return [row["CART_ID"] for row in results]

