from django.shortcuts import render

# Create your views here.

# Input Page
def input_page(request):
    return render(request, 'input.html')

# Output Page
def output_page(request):
    number = int(request.GET.get('number', 0))
    primes = [n for n in range(2, number + 1) if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))]
    return render(request, 'output.html', {'number': number, 'primes': primes})
