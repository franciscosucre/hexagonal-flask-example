from typing import Dict

from ui.controllers.cat_controller import CatController


class CatRouter:
    def __init__(self, cat_controller: CatController):
        self.cat_controller = cat_controller

    def get_routes(self) -> Dict:
        return {
            '/cats': {'view_func': self.cat_controller.find_all_cats, 'methods': ['GET']},
            '/cats/add': {'view_func': self.cat_controller.create_cat, 'methods': ['POST']}
        }
