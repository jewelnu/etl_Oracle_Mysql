from .models import MSsqldata, Postgresdata
from django.db import transaction

def run_etl():
    # Extract data from MySQL
    mysql_data = Postgresdata.objects.using('default').all()

    for mysql_record in mysql_data:
        try:
            # Check if the record already exists in Oracle
            oracle_record, created = MSsqldata.objects.using('sqlserver').get_or_create(
                reg_no=mysql_record.reg_no,
                defaults={
                    'std_name': mysql_record.std_name,
                    'fname': mysql_record.fname,
                }
            )
            if not created:
                # Update existing record if there's a change
                oracle_record.std_name = mysql_record.std_name
                oracle_record.fname = mysql_record.fname
                oracle_record.save(using='sqlserver')
        except Exception as e:
            print(f"Error syncing record {mysql_record.name}: {str(e)}")
