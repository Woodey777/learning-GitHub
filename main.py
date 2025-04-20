import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Программа запущена")
    print("Hello world!!!")
    logger.info("Программа уже завершила работу")
    print("feature1")

if __name__ == "__main__":
    main()