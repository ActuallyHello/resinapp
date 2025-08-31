from django.http import JsonResponse
from django.views import View

from apps.resinauth.models import User
from apps.resincore.validations.validator import is_valid_id


class UserRestController(View):

    def get(self, request, user_id):
        """Получить пользователя/ей"""

        if user_id is not None:
            try :
                is_valid_id(user_id)

            except Exception as e :
                return JsonResponse({'error': str(e)})


        try:
            if user_id:
                # Получить конкретного пользователя
                user = User.objects.get(id=user_id, is_active=True)
                user_data = self._user_to_dict(user)
                return JsonResponse({'success': True, 'user': user_data})
            else:
                # Получить всех пользователей
                users = User.objects.filter(is_active=True)
                users_data = [self._user_to_dict(user) for user in users]
                return JsonResponse({'success': True, 'users': users_data})

        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Пользователь не найден'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
