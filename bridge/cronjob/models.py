from django.db import models

# MySQL Models
class MySQLTable(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mysql_table'
        managed = False  # This table already exists in the MySQL server

# Oracle Model
class OracleTable(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'oracle_table'
        managed = False  # This table already exists in the Oracle server
