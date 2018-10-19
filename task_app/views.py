from django.shortcuts import render

from task_app.StatePatern_task import *
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
import json
# Create your views here.


@csrf_exempt
@require_http_methods(["POST"])

def get_state(request):
    data = json.loads(request.body.decode('utf-8'))

    state = data['state']
    id = data['id']
    title = data['title']
    desc = data['des']
    # print(state, id, title, desc)
    st = Context(eval(state))
    print(st.In_New(id, title, desc))
    print(st.In_Progress())
    print(st.In_Done())
    results = Task.objects.filter(id=id).values('id', 'title', 'description')
    return JsonResponse({'results': list(results)})
    # return HttpResponse(data, content_type='application/json')

    # return JsonResponse({"subtotal": subtotal, "payable_now": payable_now,
        #                      "grand_total": grand_total, "remainder": remainder,
        #                      "host_comm": host_comm, "guest_comm": guest_comm,
        #                      "additional_amount": additional_amount
        #                      })
