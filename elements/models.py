from django.db import models
from django.http import JsonResponse


# Create your models here.
class Element(models.Model):
    atomic_number = models.IntegerField(default=0, blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    atomic_mass = models.CharField(max_length=100, blank=True, default='')
    electronic_configuration = models.CharField(max_length=100, blank=True, default='')
    electronegativity = models.FloatField(default=0, blank=True, null=True)
    atomic_radius = models.IntegerField(default=0, blank=True, null=True)
    ion_radius = models.CharField(max_length=100, blank=True, default='')
    vanderwaalsradius = models.CharField(max_length=100, blank=True, default='')
    ionization_energy = models.IntegerField(default=0, blank=True, null=True)
    year_discovered = models.CharField(max_length=100, blank=True, default='')
    electron_affinity = models.IntegerField(default=0, blank=True, null=True)
    oxidation_states = models.CharField(max_length=100, blank=True, default='')
    standard_state = models.CharField(max_length=100, blank=True, default='')
    bonding_type = models.CharField(max_length=100, blank=True, default='')
    melting_point = models.IntegerField(default=0, blank=True, null=True)
    boiling_point = models.IntegerField(default=0, blank=True, null=True)
    density = models.FloatField(default=0, blank=True, null=True)
    group_block = models.CharField(max_length=100, blank=True, default='')
    block = models.CharField(max_length=100, blank=True, default='')
    cpx_hex_color = models.CharField(max_length=100, blank=True, default='')
    period = models.IntegerField(default=0, blank=True, null=True)
    group = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return '{} / {} / {}'.format(self.symbol, self.name, self.atomic_number)
