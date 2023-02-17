# -- coding: utf-8 --


from odoo import models, fields, api


class Subject(models.Model):
    _name = 'instituto.subject'
    _description = 'Asignaturas del instituto'


    codAsignatura = fields.Integer("Codigo Asignatura", required=True)
    name = fields.Text("Nombre", required=True)
    numHoras = fields.Integer("Numero de horas")
    optativa = fields.Boolean("Es optativa?", required=True)


    student_ids = fields.Many2many("instituto.student",string="Estudiantes registrados en la asignatura")