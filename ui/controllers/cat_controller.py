from flask import jsonify

from domain.usecases.cat_usecases import CatUseCase


class CatController:

    def __init__(self, cat_use_cases: CatUseCase):
        self.cat_use_cases = cat_use_cases

    def find_all_cats(self):
        return jsonify(self.cat_use_cases.find_all_cats())
