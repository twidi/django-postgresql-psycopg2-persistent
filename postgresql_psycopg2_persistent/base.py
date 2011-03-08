# http://stackoverflow.com/questions/1125504/django-persistent-database-connection

# Custom DB backend postgresql_psycopg2 based
# implements persistent database connection using thread local storage
from threading import local

from django.db.backends.postgresql_psycopg2.base import DatabaseError, \
    DatabaseWrapper as BaseDatabaseWrapper, IntegrityError
from psycopg2 import OperationalError

threadlocal = local()

class DatabaseWrapper(BaseDatabaseWrapper):
    def _cursor(self, *args, **kwargs):
        if hasattr(threadlocal, 'connection') and threadlocal.connection is \
            not None and self.connection is None:
            try: # Check if connection is alive
                threadlocal.connection.cursor().execute('SELECT 1')
            except OperationalError: # The connection is not working, need reconnect
                threadlocal.connection = None
            else:
                self.connection = threadlocal.connection
        cursor = super(DatabaseWrapper, self)._cursor(*args, **kwargs)
        if (not hasattr(threadlocal, 'connection') or threadlocal.connection \
             is None) and self.connection is not None:
            threadlocal.connection = self.connection
        return cursor

    def close(self):
        if self.connection is not None:
            self.connection.commit()
            self.connection = None

