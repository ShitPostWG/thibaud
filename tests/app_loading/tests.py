import os

from thibaud.apps import apps
from thibaud.test import SimpleTestCase
from thibaud.test.utils import extend_sys_path


class GetModelsTest(SimpleTestCase):
    def setUp(self):
        from .not_installed import models

        self.not_installed_module = models

    def test_get_model_only_returns_installed_models(self):
        with self.assertRaises(LookupError):
            apps.get_model("not_installed", "NotInstalledModel")

    def test_get_models_only_returns_installed_models(self):
        self.assertNotIn("NotInstalledModel", [m.__name__ for m in apps.get_models()])
