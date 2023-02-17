# -- coding: utf-8 --


from odoo import models, fields, api


class Classes(models.Model):
    _name = 'instituto.classes'
    _description = 'Clases del instituto'


    idclase = fields.Integer("Id Clase", required=True)
    name =fields.Text("Nombre", required=True)
    numEstudiantes = fields.Integer("Numero de estudiantes")
    students_ids = fields.One2many("instituto.student","class_id", string="Estudiantes")