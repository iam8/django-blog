# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Code for the views for the polling app.
"""

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from polling.models import Poll


# CLASS BASED VIEWS USING DJANGO -------------------------------------------------------------------

class PollListView(ListView):

    """
    List view class for polls.
    """

    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):

    """
    Detail view class for polls.
    """

    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):

        """
        POST method for poll detail view. A poll can be voted up or down by the user on that poll's
        detail page.
        """

        poll = self.get_object()
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1

        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)

#---------------------------------------------------------------------------------------------------


# LIST VIEW CLASSES FROM SCRATCH -------------------------------------------------------------------

#class ListView():
#
#    def as_view(self):
#
#        return self.get
#
#    def get(self, request):
#
#        model_list_name = self.model.__name__.lower() + "_list"
#        context = {model_list_name: self.model.objects.all()}
#        return render(request, self.template_name, context)
#
#
#class PollListView(ListView):
#
#    model = Poll
#    template_name = "polling/list.html"

#---------------------------------------------------------------------------------------------------


# FUNCTION-BASED VIEWS -----------------------------------------------------------------------------

#def list_view(request):
#
#    """
#    List view of polls for the polling app.
#    """
#
#    context = {"polls": Poll.objects.all()}
#
#    return render(request, "polling/list.html", context)


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

#---------------------------------------------------------------------------------------------------
