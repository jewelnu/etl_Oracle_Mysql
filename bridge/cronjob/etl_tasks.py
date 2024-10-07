from .models import MySQLTable, OracleTable
from django.db import transaction

def run_etl():
    # Extract data from MySQL
    mysql_data = MySQLTable.objects.using('default').all()

    for mysql_record in mysql_data:
        try:
            # Check if the record already exists in Oracle
            oracle_record, created = OracleTable.objects.using('oracle').get_or_create(
                name=mysql_record.name,
                defaults={
                    'value': mysql_record.value,
                    'updated_at': mysql_record.updated_at,
                }
            )
            if not created:
                # Update existing record if there's a change
                oracle_record.value = mysql_record.value
                oracle_record.updated_at = mysql_record.updated_at
                oracle_record.save(using='oracle')
        except Exception as e:
            print(f"Error syncing record {mysql_record.name}: {str(e)}")
