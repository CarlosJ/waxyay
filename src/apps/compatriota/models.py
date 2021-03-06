# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode
from datetime import datetime
from ubigeo.models import Ubigeo
from base.models import Base
from ciudadano.models import Citizen
from carrera.models import Education,Occupation,Profession

TIPO = (
    (1, u'Público'),
    (2, u'Interno'),
)

ESTADO = (
    (1, u'Activo'),
    (2, u'Expulsado'),
    (2, u'Renunció'),
)

class Affiliate(models.Model):
    citizen         = models.OneToOneField(Citizen)
    base            = models.ForeignKey(Base)
    ubigeo          = models.ForeignKey(Ubigeo, blank = True, null = True)
    address         = models.TextField('Dirección', blank = True, null = True)
    address_home    = models.TextField('Dirección actual', blank = True, null = True)
    phone           = models.CharField('Teléfono', max_length = 8, blank = True, null = True)
    cellphone       = models.CharField('Celular', max_length = 12, blank = True, null = True)
    email           = models.EmailField('E-Mail', blank = True, null = True)
    affidavit       = models.BooleanField('Declaración Jurada', default = True)
    foto            = models.ImageField('Foto', upload_to = 'Foto/', blank = True, null = True)
    kind            = models.IntegerField('Tipo', choices = TIPO, default = 1)
    state           = models.IntegerField('Estado', choices = ESTADO, default = 1)
    date_record     = models.DateField('Fecha de registro', editable = False, default = datetime.today())
    date_enrollment = models.DateField('Fecha de afiliación', default = datetime.today())

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'

    #def __str__(self):
    #    return u'%s %s; %s' % (force_unicode(self.citizen.paternal_surname, encoding='utf-8', strings_only=False, errors='strict'), force_unicode(self.citizen.mother_surname, encoding='utf-8', strings_only=False, errors='strict'),force_unicode(self.citizen.name, encoding='utf-8', strings_only=False, errors='strict'))
     
