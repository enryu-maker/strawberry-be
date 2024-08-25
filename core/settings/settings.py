from .settings import *
import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv('DJANGO_ENV') == 'production':
    print(os.getenv('DJANGO_ENV'))
    from .production import *
else:
    from .development import *
