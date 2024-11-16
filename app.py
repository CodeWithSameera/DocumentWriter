## developed by sameera

from util import DatabaseManager,QuoteDocumentGenerator

from util.logger_config import setup_logger

def main(cart_id: int, db_path: str, template_path: str, output_dir: str):
    db_manager = DatabaseManager(db_path)
    generator = QuoteDocumentGenerator(template_path, output_dir)
    logger = setup_logger()

    try:

        customer, quote, items = db_manager.fetch_quote_data(cart_id)

        if not customer or not quote or not items:
            logger.error("No data found for the provided cart ID.")
            return

        generator.generate_document(quote, customer, items)
        logger.info("Document generation completed successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")

def console_app(db_path: str, template_path: str, output_dir: str):

    logger = setup_logger()
    db_manager = DatabaseManager(db_path)
    generator = QuoteDocumentGenerator(template_path, output_dir)

    print("Choose an option:")
    print("1. Generate a document for a specific quote number")
    print("2. Generate documents for all available quotes in the database")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        quote_number = input("Enter the quote number: ").strip()
        try:
            customer, quote, items = db_manager.fetch_quote_data(quote_number)
            generator.generate_document( quote, customer, items)
            logger.info(f"Document generated for quote number: {quote_number}")
        except ValueError as e:
            logger.error(f"Error: {e}")

    elif choice == "2":
        try:
            all_cart_ids = db_manager.get_all_cart_ids()
            for cart_id in all_cart_ids:
                customer, quote, items = db_manager.fetch_quote_data(cart_id)
                generator.generate_document(quote, customer, items)
                logger.info(f"Document generated for cart_id: {cart_id}")
            print(f"Documents generated for all quotes. Check the output directory.")
        except Exception as e:
            logger.error(f"Error: {e}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    cart_id = 1
    db_path = 'db/quotes.db'
    template_path = 'template/Output_template.docx'
    output_dir = 'output'

    #main(cart_id, db_path, template_path, output_dir)
    console_app(db_path, template_path, output_dir)
