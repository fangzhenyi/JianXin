from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    res_data = common_data()
    return render_to_response("index.html", res_data)


def commu(request):
    res_data = common_data()
    return render_to_response("commu.html", res_data)


def intro(request):
    res_data = common_data()
    return render_to_response("intro.html", res_data)


def news(request):
    page = int(request.GET.get("page", 1))
    pageNum = 1
    res_data = common_data()
    object = ArticleNews.object
    objects = object.order_by("pub_date")
    num = len(objects)
    if page >= num:
        page = num
    mPageinator = Paginator(objects, pageNum)
    res_data["objNum"] = num
    res_data["article"] = mPageinator.page(page)

    print page
    if page <= 3:
        res_data["page"] = mPageinator.page_range[0:5]
    elif (mPageinator.num_pages - page) < 3:
        res_data["page"] = mPageinator.page_range[mPageinator.num_pages - 5:mPageinator.num_pages]
    else:
        res_data["page"] = mPageinator.page_range[page - 3:page + 2]
    res_data["currentPage"] = page
    if len(str(page)) == 2:
        res_data["isDouble"] = True
    else:
        res_data["isDouble"] = False
    pageObj = mPageinator.page(page)
    res_data["isHasNext"] = pageObj.has_next()
    res_data["isHasPre"] = pageObj.has_previous()
    res_data["nextPage"] = page + 1
    res_data["prePage"] = page - 1
    return render_to_response('news.html', res_data)


def product(request):
    res_data = common_data()
    return render_to_response('product.html', res_data)


def sight(request):
    res_data = common_data()
    return render_to_response("sight.html", res_data)


def common_data():
    res_data = {
        'static_url': '/static/'
    }
    return res_data
