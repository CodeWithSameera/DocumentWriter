class QuoteItem:
    def __init__(self, data):
        self.catalog_code = data['CATALOGCODE']
        self.description = data['DESCRIPTION']
        self.user_description = data['USER_DESCRIPTION']
        self.quantity = data['QUANTITY']
        self.net_price = data['NETPRICE']
        self.recurring_price = data['RecurringPrice']
        self.currency = data['CURRENCY']
        self.product_weight = data['PRODUCT_WEIGHT']
        self.unit_of_measure = data['UnitOfMeasure']
        self.delivery_status = data['ITEM_DELIVERY_STATUS']
        self.item_delivery_method = data['ITEM_DELIVERY_METHOD']