## developed by sameera

from util import DatabaseManager,QuoteDocumentGenerator

from util.logger_config import setup_logger

def main(cart_id: int, db_path: str, template_path: str, output_dir: str, limit: int = 10):
    db_manager = DatabaseManager(db_path)
    generator = QuoteDocumentGenerator(template_path, output_dir)
    logger = setup_logger()
    offset = 0
    try:
        while True:
            try:
                # Fetch data with pagination
                customer, quote, items = db_manager.fetch_quote_data(cart_id, limit=limit, offset=offset)

                if not customer or not quote or not items:
                    logger.info(f"No more data found for cart_id: {cart_id}. Ending pagination.")
                    break

                # Generate the document for the current page
                generator.generate_document(quote, customer, items)
                logger.info(f"Document generated for cart_id: {cart_id}, page: {(offset // limit) + 1}")

                # Move to the next page
                offset += limit

            except ValueError as ve:
                # Handle case when no more data is available for this cart_id
                logger.info(f"Pagination complete for cart_id {cart_id}: {ve}")
                break

    except Exception as e:
        # Log any unexpected errors during the document generation process
        logger.error(f"An error occurred while processing cart_id {cart_id}: {e}")

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
            limit = 10  # Number of items per page
            offset = 0

            while True:
                try:
                    # Fetch data for the current page
                    customer, quote, items = db_manager.fetch_quote_data(quote_number, limit=limit, offset=offset)

                    # Generate the document for the current page
                    generator.generate_document(quote, customer, items)

                    logger.info(f"Document generated for quote number: {quote_number}, page: {offset // limit + 1}")

                    # Increment offset
                    offset += limit
                except ValueError:
                    logger.info("No more data to fetch for this quote.")
                    break

        except Exception as e:
            logger.error(f"Error: {e}")

    elif choice == "2":
        try:
            all_cart_ids = db_manager.get_all_cart_ids()  # Retrieve all cart IDs from the database

            for cart_id in all_cart_ids:
                limit = 10  # Number of items per page
                offset = 0

                while True:
                    try:
                        customer, quote, items = db_manager.fetch_quote_data(cart_id, limit=limit, offset=offset)

                        generator.generate_document(quote, customer, items)

                        logger.info(f"Document generated for cart_id: {cart_id}, page: {offset // limit + 1}")

                        offset += limit
                    except ValueError:
                        logger.info(f"No more data to fetch for cart_id: {cart_id}.")
                        break

            print("Documents generated for all quotes. Check the output directory.")

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
