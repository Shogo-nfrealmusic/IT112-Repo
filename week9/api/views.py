from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json

def get_all_items(request):
    if request.method == 'GET':
        items = list(Item.objects.values())
        return JsonResponse(items, safe=False, content_type='application/json')


def get_single_item(request):
    if request.method == 'GET':
        item_id = request.GET.get('id')
        try:
            item = Item.objects.get(id=item_id)
            return JsonResponse({
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'created_at': item.created_at,
            }, content_type='application/json')
        except Item.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, content_type='application/json')


@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            if not name or not description:
                raise ValueError('Missing name or description')

            item = Item.objects.create(name=name, description=description)
            return JsonResponse({'success': True, 'id': item.id}, content_type='application/json')
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, content_type='application/json')
