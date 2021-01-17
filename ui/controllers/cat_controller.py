from typing import Dict

from flask import jsonify, request

from domain.entities.cat import Cat
from domain.usecases.cat_usecases import CatUseCase

from marshmallow import Schema, fields, ValidationError


class CreateCatSchema(Schema):
    name = fields.Str(required=True)


class CatController:

    def __init__(self, cat_use_cases: CatUseCase):
        self.cat_use_cases = cat_use_cases

    def find_all_cats(self):
        return jsonify(self.cat_use_cases.find_all_cats())

    def create_cat(self):
        data = CreateCatSchema().load(request.get_json())
        cat: Cat = Cat(**data)
        return jsonify(self.cat_use_cases.create_cat(cat=cat))
