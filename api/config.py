from urllib.parse import urlparse
import os
# Assuming POSTGRES_URL is something like:
# "postgres://user:password@host:port/database"
uri = os.getenv("POSTGRES_URL")
parsed_uri = urlparse(uri)

# Extract components
host = parsed_uri.hostname
database = parsed_uri.path[1:]  # Remove the leading slash
user = parsed_uri.username
password = parsed_uri.password
port = parsed_uri.port  # This will be None if not specified in the URI

# If port is not specified, you might need to set a default PostgreSQL port
if port is None:
    port = 5432  # Default PostgreSQL port

# Fill in the DATABASE_CONFIG dictionary
DATABASE_CONFIG = {
    'host': host,
    'database': database,
    'user': user,
    'password': password,
    'port': port
}
