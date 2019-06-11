# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.shortcuts import render,get_object_or_404,redirect
from TestModel.models import Entry
from .models import Comment
from .forms import CommentForm

from django.shortcuts import render

# Create your views here.

def post_comment(request,post_id):
    post=get_object_or_404(Entry,pk=post_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)
        else:
            comment_list=post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list

            }
            return render(request,'blog/detail.html',context)
    return redirect(post)
