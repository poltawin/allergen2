# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allergens(models.Model):
    code = models.TextField(primary_key=True, blank=True)
    product_name = models.TextField(blank=True, null=True)
    aller1 = models.FloatField(blank=True, null=True)
    aller2 = models.FloatField(blank=True, null=True)
    aller3 = models.FloatField(blank=True, null=True)
    aller4 = models.FloatField(blank=True, null=True)
    aller5 = models.FloatField(blank=True, null=True)
    aller6 = models.FloatField(blank=True, null=True)
    aller7 = models.FloatField(blank=True, null=True)
    aller8 = models.FloatField(blank=True, null=True)
    aller9 = models.FloatField(blank=True, null=True)
    aller10 = models.FloatField(blank=True, null=True)
    aller11 = models.FloatField(blank=True, null=True)
    aller12 = models.FloatField(blank=True, null=True)
    aller13 = models.FloatField(blank=True, null=True)
    aller14 = models.FloatField(blank=True, null=True)
    aller15 = models.FloatField(blank=True, null=True)
    aller16 = models.FloatField(blank=True, null=True)
    aller17 = models.FloatField(blank=True, null=True)
    aller18 = models.FloatField(blank=True, null=True)
    aller19 = models.FloatField(blank=True, null=True)
    aller20 = models.FloatField(blank=True, null=True)
    aller21 = models.FloatField(blank=True, null=True)
    aller22 = models.FloatField(blank=True, null=True)
    aller23 = models.FloatField(blank=True, null=True)
    aller24 = models.FloatField(blank=True, null=True)
    aller25 = models.FloatField(blank=True, null=True)
    aller26 = models.FloatField(blank=True, null=True)
    aller27 = models.FloatField(blank=True, null=True)
    aller28 = models.FloatField(blank=True, null=True)
    aller29 = models.FloatField(blank=True, null=True)
    aller30 = models.FloatField(blank=True, null=True)
    aller31 = models.FloatField(blank=True, null=True)
    aller32 = models.FloatField(blank=True, null=True)
    aller33 = models.FloatField(blank=True, null=True)
    aller34 = models.FloatField(blank=True, null=True)
    aller35 = models.FloatField(blank=True, null=True)
    aller36 = models.FloatField(blank=True, null=True)
    aller37 = models.FloatField(blank=True, null=True)
    aller38 = models.FloatField(blank=True, null=True)
    aller39 = models.FloatField(blank=True, null=True)
    aller40 = models.FloatField(blank=True, null=True)
    aller41 = models.FloatField(blank=True, null=True)
    aller42 = models.FloatField(blank=True, null=True)
    aller43 = models.FloatField(blank=True, null=True)
    aller44 = models.FloatField(blank=True, null=True)
    aller45 = models.FloatField(blank=True, null=True)
    aller46 = models.FloatField(blank=True, null=True)
    aller47 = models.FloatField(blank=True, null=True)
    aller48 = models.FloatField(blank=True, null=True)
    aller49 = models.FloatField(blank=True, null=True)
    aller50 = models.FloatField(blank=True, null=True)
    aller51 = models.FloatField(blank=True, null=True)
    aller52 = models.FloatField(blank=True, null=True)
    aller53 = models.FloatField(blank=True, null=True)
    aller54 = models.FloatField(blank=True, null=True)
    aller55 = models.FloatField(blank=True, null=True)
    aller56 = models.FloatField(blank=True, null=True)
    aller57 = models.FloatField(blank=True, null=True)
    aller58 = models.FloatField(blank=True, null=True)
    aller59 = models.FloatField(blank=True, null=True)
    aller60 = models.FloatField(blank=True, null=True)
    aller61 = models.FloatField(blank=True, null=True)
    aller62 = models.FloatField(blank=True, null=True)
    aller63 = models.FloatField(blank=True, null=True)
    aller64 = models.FloatField(blank=True, null=True)
    aller65 = models.FloatField(blank=True, null=True)
    aller66 = models.FloatField(blank=True, null=True)
    aller67 = models.FloatField(blank=True, null=True)
    aller68 = models.FloatField(blank=True, null=True)
    aller69 = models.FloatField(blank=True, null=True)
    aller70 = models.FloatField(blank=True, null=True)
    aller71 = models.FloatField(blank=True, null=True)
    aller72 = models.FloatField(blank=True, null=True)
    aller73 = models.FloatField(blank=True, null=True)
    aller74 = models.FloatField(blank=True, null=True)
    aller75 = models.FloatField(blank=True, null=True)
    aller76 = models.FloatField(blank=True, null=True)
    aller77 = models.FloatField(blank=True, null=True)
    aller78 = models.FloatField(blank=True, null=True)
    aller79 = models.FloatField(blank=True, null=True)
    aller80 = models.FloatField(blank=True, null=True)
    aller81 = models.FloatField(blank=True, null=True)
    aller82 = models.FloatField(blank=True, null=True)
    aller83 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allergens'


class Main(models.Model):
    code = models.TextField(db_column='Code', blank=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    ref1 = models.TextField(db_column='Ref1', blank=True, null=True)  # Field name made lowercase.
    name1 = models.TextField(db_column='Name1', blank=True, null=True)  # Field name made lowercase.
    ratio1 = models.FloatField(db_column='Ratio1', blank=True, null=True)  # Field name made lowercase.
    ref2 = models.TextField(db_column='Ref2', blank=True, null=True)  # Field name made lowercase.
    name2 = models.TextField(db_column='Name2', blank=True, null=True)  # Field name made lowercase.
    ratio2 = models.FloatField(db_column='Ratio2', blank=True, null=True)  # Field name made lowercase.
    ref3 = models.TextField(db_column='Ref3', blank=True, null=True)  # Field name made lowercase.
    name3 = models.TextField(db_column='Name3', blank=True, null=True)  # Field name made lowercase.
    ratio3 = models.FloatField(db_column='Ratio3', blank=True, null=True)  # Field name made lowercase.
    ref4 = models.TextField(db_column='Ref4', blank=True, null=True)  # Field name made lowercase.
    name4 = models.TextField(db_column='Name4', blank=True, null=True)  # Field name made lowercase.
    ratio4 = models.FloatField(db_column='Ratio4', blank=True, null=True)  # Field name made lowercase.
    ref5 = models.TextField(db_column='Ref5', blank=True, null=True)  # Field name made lowercase.
    name5 = models.TextField(db_column='Name5', blank=True, null=True)  # Field name made lowercase.
    ratio5 = models.FloatField(db_column='Ratio5', blank=True, null=True)  # Field name made lowercase.
    ref6 = models.TextField(db_column='Ref6', blank=True, null=True)  # Field name made lowercase.
    name6 = models.TextField(db_column='Name6', blank=True, null=True)  # Field name made lowercase.
    ratio6 = models.FloatField(db_column='Ratio6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main'


class Spec(models.Model):
    productcode = models.TextField(primary_key=True)
    productname = models.TextField(blank=True, null=True)
    sgavg = models.IntegerField(blank=True, null=True)
    sglow = models.IntegerField(blank=True, null=True)
    sghigh = models.IntegerField(blank=True, null=True)
    riavg = models.IntegerField(blank=True, null=True)
    rilow = models.IntegerField(blank=True, null=True)
    rihigh = models.IntegerField(blank=True, null=True)
    flashpoint = models.IntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    exp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec'
