from django.shortcuts import render
from django.http import JsonResponse
import tracemalloc
import time
import sys
import json
from django.views.decorators.csrf import csrf_exempt

from .scripts.sequential import find_min_distance as sequential_compute
from .scripts.list_comprehension import compute as comprehension_compute
from .scripts.generators import compute as generator_compute
from .scripts.mprocessing import compute as mprocessing_compute

# Create your views here.
@csrf_exempt
def sequential_search(request):
    data = json.loads(request.body)
    n = int(data['n']) 
    m = int(data['m'])
    points = data['points']

    tracemalloc.start()
    start_time = time.process_time()

    result = sequential_compute(n, m, points)

    end_time = time.process_time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_time - start_time
    peak_in_MB = peak / 10**6

    return JsonResponse({'result': result, 'time_in_s': time_in_s, 'max_memory_in_MB': peak_in_MB}, safe=False, status=200)

@csrf_exempt
def comprehension_search(request):
    data = json.loads(request.body)
    n = int(data['n']) 
    m = int(data['m'])
    points = data['points']

    tracemalloc.start()
    start_time = time.process_time()

    result = comprehension_compute(n, m, points)

    end_time = time.process_time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_time - start_time
    peak_in_MB = peak / 10**6

    return JsonResponse({'result': result, 'time_in_s': time_in_s, 'max_memory_in_MB': peak_in_MB}, safe=False, status=200)

@csrf_exempt
def generator_search(request):
    data = json.loads(request.body)
    n = int(data['n']) 
    m = int(data['m'])
    points = data['points']

    tracemalloc.start()
    start_time = time.process_time()

    result_generator = generator_compute(n, m, points)

    end_time = time.process_time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_time - start_time
    peak_in_MB = peak / 10**6

    result = []
    for index in result_generator:
        result.append(index)

    return JsonResponse({'result': result, 'time_in_s': time_in_s, 'max_memory_in_MB': peak_in_MB}, safe=False, status=200)

@csrf_exempt
def mprocessing_search(request):
    data = json.loads(request.body)
    n = int(data['n']) 
    m = int(data['m'])
    points = data['points']

    tracemalloc.start()
    start_time = time.process_time()

    result = mprocessing_compute(n, m, points)

    end_time = time.process_time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_time - start_time
    peak_in_MB = peak / 10**6

    return JsonResponse({'result': result, 'time_in_s': time_in_s, 'max_memory_in_MB': peak_in_MB}, safe=False, status=200)