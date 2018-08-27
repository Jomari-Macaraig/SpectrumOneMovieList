from django.contrib import messages


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
