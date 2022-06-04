from django.views.generic import TemplateView

from todoprj.settings_local import SERVER_VERSION


class AboutView(TemplateView):
    template_name = "About.html"

    def get_context_data(self, **kwargs):
        request = self.request
        context = super().get_context_data(**kwargs)
        context["server_version"] = SERVER_VERSION
        username = request.user.username
        if username:
            context["logged_user"] = username
        else:
            context["logged_user"] = "Anonymous"
        return context
