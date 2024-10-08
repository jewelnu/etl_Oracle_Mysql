# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Over300(models.Model):
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disbang = models.CharField(db_column='DisBang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    upozilla = models.CharField(db_column='Upozilla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    distance = models.CharField(db_column='Distance', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Over300'


class Upazilladis(models.Model):
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disbang = models.CharField(db_column='DisBang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    upozilla = models.CharField(db_column='Upozilla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    distance = models.CharField(db_column='Distance', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UpazillaDis'


class Bellow150(models.Model):
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disbang = models.CharField(db_column='DisBang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    upozilla = models.CharField(db_column='Upozilla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    distance = models.CharField(db_column='Distance', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bellow150'


class DegreeData(models.Model):
    uid = models.TextField(blank=True, null=True)
    mid = models.TextField(blank=True, null=True)
    reg_no = models.TextField(blank=True, null=True)
    roll_no = models.TextField(blank=True, null=True)
    std_name = models.TextField(blank=True, null=True)
    fname = models.TextField(blank=True, null=True)
    mname = models.TextField(blank=True, null=True)
    c_code = models.TextField(blank=True, null=True)
    centre = models.TextField(blank=True, null=True)
    issu_date = models.TextField(blank=True, null=True)
    old_col = models.TextField(blank=True, null=True)
    col_code = models.TextField(blank=True, null=True)
    college = models.TextField(blank=True, null=True)
    sub_code = models.TextField(blank=True, null=True)
    sess = models.TextField(blank=True, null=True)
    sif = models.TextField(blank=True, null=True)
    opt_all = models.TextField(blank=True, null=True)
    opt_all_ne = models.TextField(blank=True, null=True)
    opt_all_ol = models.TextField(blank=True, null=True)
    session = models.TextField(blank=True, null=True)
    std_type = models.TextField(blank=True, null=True)
    course = models.TextField(blank=True, null=True)
    course_nam = models.TextField(blank=True, null=True)
    adm_roll = models.TextField(blank=True, null=True)
    abs_sub = models.TextField(blank=True, null=True)
    exm_fee = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    sdate = models.TextField(blank=True, null=True)
    confirm_da = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    complete = models.TextField(blank=True, null=True)
    std_status = models.TextField(blank=True, null=True)
    imp_all = models.TextField(blank=True, null=True)
    syll = models.TextField(blank=True, null=True)
    syll_yr = models.TextField(blank=True, null=True)
    confirm_d1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree_data'
