import os
import os.path
import logging

_logger = logging.getLogger(__name__)

FILENAME_PEM_PRIVATE_KEY = 'ca_private.pem'
FILENAME_PEM_PUBLIC_KEY = 'ca_public.pem'
FILENAME_PEM_CERTIFICATE = 'ca_cert.pem'

REQUIRED_DN_FIELDS = set(('C', 'ST', 'L', 'O', 'CN', 'emailAddress'))
BITS = 2048

CA_PATH = os.environ.get('SAPI_CA_PATH', '/var/lib/ca')

DEFAULT_VALIDITY_Y = 10

_logger.debug("Importing custom API hooks (CA, optional).")

try:
    from sapi_custom_ca.ca import *
except ImportError:
    _logger.debug("Custom functionality not found (CA).")
else:
    _logger.debug("Custom functionality found (CA).")

_logger.info("CA PATH: %s", CA_PATH)

if os.path.exists(CA_PATH) is False:
    os.makedirs(CA_PATH)
