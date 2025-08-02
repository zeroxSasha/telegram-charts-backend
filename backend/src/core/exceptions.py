class TelegramWebViewError(Exception):
    """Raised when Telegram WebView cannot be obtained."""

class PalaceAuthError(Exception):
    """Raised when palace auth URL is invalid or cannot be parsed."""

class PalaceClientError(Exception):
    """Raised when PalaceNFTClient fails to fetch collections or offers."""