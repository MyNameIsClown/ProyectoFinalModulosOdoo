# -- coding: utf-8 --


from odoo import models, fields, api


class Student(models.Model):
    _name = 'instituto.student'
    _description = 'Estudiantes del instituto'


    nif = fields.Char(string="Identificacion",required=True, help="Identificacion del alumno")
    name =fields.Text("Nombre", required=True)
    fsurname=fields.Text("Apellido 1", required=True)
    ssurname=fields.Text("Apellido 2")


    subjects_ids = fields.Many2many("instituto.subject",string="Asignaturas en la que se ha matriculado el alumno")
    class_id = fields.Many2one('instituto.classes',string="Clase en la que esta matriculado el alumno")