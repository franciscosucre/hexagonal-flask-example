from flask import jsonify, request

from domain.entities.cat import Cat
from domain.usecases.cat_usecases import CatUseCase


class CatController:

    def __init__(self, cat_use_cases: CatUseCase):
        self.cat_use_cases = cat_use_cases

    def find_all_cats(self):
        return jsonify(self.cat_use_cases.find_all_cats())

    def create_cat(self):
        cat: Cat = Cat(**request.get_json())
        return jsonify(self.cat_use_cases.create_cat(cat=cat))

