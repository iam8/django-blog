# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Code for the views for the polling app.
"""

from django.shortcuts import render
from django.http import Http404

from polling.models import Poll


class ListView():

    def as_view(self):

        return self.get

    def get(self, request):

        model_list_name = self.model.__name__.lower() + "_list"
        context = {model_list_name: self.model.objects.all()}
        return render(request, self.template_name, context)


class PollListView(ListView):

    model = Poll
    template_name = "polling/list.html"


#def list_view(request):
#
#    """
#    List view of polls for the polling app.
#    """
#
#    context = {"polls": Poll.objects.all()}
#
#    return render(request, "polling/list.html", context)
#
#
#def detail_view(request, poll_id):
#
#    """
#    Detail view of polls for the polling app.
#    """
#
#    try:
#        poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist as err:
#        raise Http404 from err
#
#    if request.method == "POST":
#        if request.POST.get("vote") == "Yes":
#            poll.score += 1
#        else:
#            poll.score -= 1
#
#        poll.save()
#
#    context = {"poll": poll}
#
#    return render(request, "polling/detail.html", context)
