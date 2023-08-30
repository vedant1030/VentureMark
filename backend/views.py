from django.shortcuts import render
from django.http import JsonResponse
from .webScraperBot import TrademarkScraper

def check_trademark(request):
    if request.method == 'POST':
        trademark = request.POST.get('trademark')

        # Replace this part with your code to interact with the external URL
        bot = TrademarkScraper()
        availability = bot.check_trademark_availability(trademark)
        bot.cleanup()

        return JsonResponse({'available': availability})
    return JsonResponse({'error': 'Invalid request method'})
