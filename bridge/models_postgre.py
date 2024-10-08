# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allcol2023(models.Model):
    divi_name = models.CharField(db_column='DIVI_NAME', max_length=72, blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='DIST_NAME', max_length=90, blank=True, null=True)  # Field name made lowercase.
    thana_name = models.CharField(db_column='THANA_NAME', max_length=90, blank=True, null=True)  # Field name made lowercase.
    col_code = models.CharField(db_column='COL_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    college = models.CharField(db_column='COLLEGE', max_length=240, blank=True, null=True)  # Field name made lowercase.
    govt_stat = models.CharField(db_column='GOVT_STAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    eiin = models.CharField(db_column='EIIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    establish = models.CharField(db_column='ESTABLISH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=105, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=90, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    deg1 = models.CharField(db_column='DEG1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hon1 = models.CharField(db_column='HON1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mf1 = models.CharField(db_column='MF1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mp1 = models.CharField(db_column='MP1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    h_prof1 = models.CharField(db_column='H_PROF1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_prof1 = models.CharField(db_column='M_PROF1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aff_date = models.CharField(db_column='AFF_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allcol2023'


class Degcen22Y1(models.Model):
    c_code = models.CharField(max_length=3, blank=True, null=True)
    c_colcode = models.CharField(max_length=4, blank=True, null=True)
    centre = models.CharField(max_length=80, blank=True, null=True)
    col_code = models.CharField(max_length=4, blank=True, null=True)
    college = models.CharField(max_length=80, blank=True, null=True)
    course = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degcen22Y1'


class DegreeSubjectNew(models.Model):
    sl_no = models.CharField(max_length=254, blank=True, null=True)
    sub_code1 = models.CharField(max_length=254, blank=True, null=True)
    sub_code = models.CharField(max_length=254, blank=True, null=True)
    pap_code = models.CharField(max_length=254, blank=True, null=True)
    pap_name = models.CharField(max_length=254, blank=True, null=True)
    sub_name = models.CharField(max_length=254, blank=True, null=True)
    sub_title = models.CharField(max_length=254, blank=True, null=True)
    course = models.CharField(max_length=254, blank=True, null=True)
    sub_all = models.CharField(max_length=254, blank=True, null=True)
    sub_1st = models.CharField(max_length=254, blank=True, null=True)
    sub_2nd = models.CharField(max_length=254, blank=True, null=True)
    sub_3rd = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    opt_all = models.CharField(max_length=60, blank=True, null=True)
    dis_head = models.CharField(max_length=10, blank=True, null=True)
    packet = models.CharField(max_length=10, blank=True, null=True)
    serial = models.CharField(db_column='Serial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    question_s = models.CharField(db_column='Question_s', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pap_order = models.CharField(db_column='Pap_order', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degree_Subject_New'


class DegreeData(models.Model):
    uid = models.CharField(blank=True, null=True)
    mid = models.CharField(blank=True, null=True)
    reg_no = models.CharField(blank=True, null=True)
    roll_no = models.CharField(blank=True, null=True)
    std_name = models.CharField(blank=True, null=True)
    fname = models.CharField(blank=True, null=True)
    mname = models.CharField(blank=True, null=True)
    c_code = models.CharField(blank=True, null=True)
    centre = models.CharField(blank=True, null=True)
    issu_date = models.CharField(blank=True, null=True)
    old_col = models.CharField(blank=True, null=True)
    col_code = models.CharField(blank=True, null=True)
    college = models.CharField(blank=True, null=True)
    sub_code = models.CharField(blank=True, null=True)
    sess = models.CharField(blank=True, null=True)
    sif = models.CharField(blank=True, null=True)
    opt_all = models.CharField(blank=True, null=True)
    opt_all_ne = models.CharField(blank=True, null=True)
    opt_all_ol = models.CharField(blank=True, null=True)
    session = models.CharField(blank=True, null=True)
    std_type = models.CharField(blank=True, null=True)
    course = models.CharField(blank=True, null=True)
    course_nam = models.CharField(blank=True, null=True)
    adm_roll = models.CharField(blank=True, null=True)
    abs_sub = models.CharField(blank=True, null=True)
    exm_fee = models.CharField(blank=True, null=True)
    year = models.CharField(blank=True, null=True)
    sdate = models.CharField(blank=True, null=True)
    confirm_da = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    complete = models.CharField(blank=True, null=True)
    std_status = models.CharField(blank=True, null=True)
    imp_all = models.CharField(blank=True, null=True)
    syll = models.CharField(blank=True, null=True)
    syll_yr = models.CharField(blank=True, null=True)
    confirm_d1 = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree_data'


class FormfillupSubmitDataDegree(models.Model):
    uid = models.BigIntegerField(blank=True, null=True)
    reg_no = models.CharField(max_length=33, blank=True, null=True)
    issu_date = models.CharField(max_length=45, blank=True, null=True)
    old_col = models.CharField(max_length=12, blank=True, null=True)
    col_code = models.CharField(max_length=12, blank=True, null=True)
    sub_code = models.CharField(max_length=12, blank=True, null=True)
    mobile = models.CharField(max_length=33, blank=True, null=True)
    sif = models.CharField(max_length=240, blank=True, null=True)
    imp_all = models.CharField(max_length=240, blank=True, null=True)
    incourse_m = models.CharField(max_length=240, blank=True, null=True)
    exm_fee = models.CharField(max_length=12, blank=True, null=True)
    sdate = models.CharField(max_length=36, blank=True, null=True)
    confirm_da = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    complete = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formfillup_submit_data_degree'
