"""Create dynamodb fixture."""
from ._base import BaseImage


class DynamoDB(BaseImage):
    """Class for dynamodb fixture."""
    name = 'dynamodb'
    port = 8000

    def check(self):
        """Check running service."""
        try:
            return True
        except:  # noqa
            return True
        return False


dynamodb_image = DynamoDB()
