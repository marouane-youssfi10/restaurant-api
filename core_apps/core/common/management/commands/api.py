from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
import os


class Command(TemplateCommand):
    help: str = "creates the api folder templates for an app"

    def handle(self, **options):
        parent = "./core_apps/apis"
        app_name = options.pop("name")
        fullpath = os.path.join(parent, app_name)
        os.makedirs(fullpath)
        target = fullpath
        super().handle("app", app_name, target, **options)

    def handle_template(self, template, subdir):
        """
        Determine where the app or project templates are.
        Use django.__path__[0] as the default because the Django install
        directory isn't known.
        """
        path = "./core_apps/core/common/api_folder_template"
        if template is None:
            return os.path.join(path, subdir)

        raise CommandError(
            "couldn't handle %s template %s." % (self.app_or_project, template)
        )

    def validate_name(self, name, name_or_dir="name"):
        if name is None:
            raise CommandError(
                "you must provide {an} {app} name".format(
                    an=self.a_or_an,
                    app=self.app_or_project,
                )
            )
        # Check it's a valid directory name.
        if not name.isidentifier():
            raise CommandError(
                "'{name}' is not a valid {app} {type}. Please make sure the "
                "{type} is a valid identifier.".format(
                    name=name,
                    app=self.app_or_project,
                    type=name_or_dir,
                )
            )
