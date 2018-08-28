from django.contrib import messages
from django.utils import timezone


class MovieActionMixin:

    fields = ['title']

    @property
    def action_past_tense(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(
            self.request,
            '{} successfully {}'.format(
                form.cleaned_data['title'],
                self.action_past_tense
            )
        )
        return super(MovieActionMixin, self).form_valid(form)


class LastVisitedSession:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_visited'] = self.request.session.get('last_visited')
        self.request.session['last_visited'] = timezone.now().isoformat()
        return context
