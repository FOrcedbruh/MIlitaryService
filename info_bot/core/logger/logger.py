import logging
from colorama import Fore, Style

logger = logging.getLogger("Bot main logger")
logger.setLevel(level=logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.INFO: Fore.GREEN,
        logging.ERROR: Fore.RED
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        record.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"
        record.msg = f"{color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)
    
color_formatter = ColorFormatter()

console_handler.setFormatter(color_formatter)
logger.addHandler(console_handler)
logger.propagate = False


__all__ = (
    "logger",
)