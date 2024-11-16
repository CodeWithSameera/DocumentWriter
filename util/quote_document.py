## developed by sameera

from typing import List

from docxtpl import DocxTemplate

from model import Quote, Customer, QuoteItem

from .logger_config import setup_logger


class QuoteDocumentGenerator:
    def __init__(self, template_path: str, output_dir: str):
        self.template_path = template_path
        self.output_dir = output_dir
        self.logger= setup_logger()

    def generate_document(self, quote: Quote, customer: Customer, items: List[QuoteItem]):
        doc = DocxTemplate(self.template_path)

        context = {
            # Quote details
            "quote_number": quote.formatted_quote_number,
            "quote_date": quote.order_date,
            "quote_status": quote.status,
            "total_amount": f"{quote.total_amount:.2f}",
            "currency": quote.currency,
            "payment_method": quote.payment_method,
            "payment_approved": quote.payment_approved,
            "comment": quote.comment,
            "currency_quoted": quote.currency_quote,
            "delivery_method": quote.shipping_method,
            "shipping_cost":quote.shipping_cost,
            "email_status":quote.email_sent,
            "quote_generated_from":quote.generated_from,
            "ship_to": quote.ship_address,
            "bill_to": quote.bill_address,

            # Customer details
            "customer_name": f"{customer.first_name} {customer.last_name}",
            "customer_company": customer.company,
            "customer_email": customer.email,
            "customer_address1": customer.address_1,
            "customer_address2": customer.address_2,
            "customer_city": customer.city,
            "customer_state": customer.state,
            "customer_province": customer.province,
            "customer_country": customer.country,
            "customer_postal_code": customer.postal_code,
            "customer_phone": customer.business_phone,
            "customer_code": customer.system_code,
            "customer_title": customer.title,
            

            # list of items
            "items": [
                {
                    "catalog_code": item.catalog_code,
                    "description": item.description,
                    "user_description":item.user_description,
                    "long_description": item.description,
                    "quantity": item.quantity,
                    "net_price": f"{item.net_price:.2f}",
                    "rec_price": f"{item.recurring_price:.2f}",
                    "currency": item.currency,
                    "weight":item.product_weight,
                    "unit":item.unit_of_measure,
                    "delivery_status":item.delivery_status,
                    "delivery_method":item.item_delivery_method
                }
                for item in items
            ],
        }

        # Render the document by objects
        doc.render(context)

        # Save the generated documents
        output_path = f"{self.output_dir}/Output_doc_for_{quote.formatted_quote_number}.docx"
        doc.save(output_path)
        self.logger.info(f"Document saved at: {output_path}")
