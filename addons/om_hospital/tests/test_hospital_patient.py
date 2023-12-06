import unittest

from odoo.tests.common import TransactionCase
from odoo.tests.common import tagged
@tagged('unit')


class TestHospitalPatient(TransactionCase):
     
        
     def test_on_change(self):
        # Créer un nouveau patient
        patient = self.env["hospital.patient"].create({'name': "Ulrich"})
        
        # Vérifier que l'attribut is_child est initialisé à False
        self.assertFalse(patient.is_child)
        
        # Modifier l'âge du patient à 8 et appeler la méthode onchange_age
        patient.age = 8
        patient.onchange_age()
        
        # Vérifier que l'attribut is_child est mis à True
        self.assertTrue(patient.is_child)
       

  