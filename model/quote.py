class Quote:
    def __init__(self, data):
        self.quote_id = data['CART_ID']
        self.order_date = data['DATE_ORDERED']
        self.status = data['ORDER_STATUS']
        self.shipping_method = data['SHIPPING_METHOD']
        self.comment = data['CART_COMMENT']
        self.payment_method = data['PAYMENT_METHOD']
        self.payment_approved = data['PAYMENT_APROOVED']
        self.total_amount = data['TOTALAMOUNT']
        self.currency = data['DEF_CURRENCY']
        self.currency_quote=data['currency_quote']
        self.email_sent = data['send_email_bill']
        self.generated_from = data['Origin']
        self.ship_address = data['MY_SHIP_TO']
        self.bill_address = data['MY_BILL_TO']
        self.origin = data['Origin']
        self.shipping_cost = data['SHIPPING_COST']

    @property
    def formatted_quote_number(self):
        return f"{self.origin:0>6}{self.quote_id:0>6}"