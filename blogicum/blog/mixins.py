from django.shortcuts import redirect
from django.urls import reverse

from blog.models import Post


class PostMixin:
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'blog/create.html'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().dispatch(request, *args, **kwargs)
        return redirect(
            reverse(
                'blog:post_detail',
                kwargs={'post_id': self.kwargs['post_id']}
            )
        )
