from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Sprint, Task
from rest_framework.reverse import reverse, reverse_lazy

User = get_user_model()


class SprintSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')

    def get_links(self, obj):
        request = self.context['request']
        return {
                'self': reverse('sprint-detail',
                                kwargs={'pk': obj.pk},
                                request=request),
        }

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'links')


class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False, read_only=True)
    status_display = serializers.SerializerMethodField('get_status_display')
    links = serializers.SerializerMethodField('get_links')

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('task-detail',
                            kwargs={'pk': obj.pk},
                            request=request),
            'sprint': None,
            'assigned': None
        }
        if obj.sprint_id:
            links['sprint'] = reverse('sprint-detail', wargs={'pk': obj.sprint_id}, request=request)
        if obj.assigned:
            links['assigned'] = reverse('user-detail', wargs={User.USERNAME_FIELD: obj.assigned}, request=request)
        return links

    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint',
                  'status', 'status_display', 'order',
                  'assigned', 'started', 'due', 'completed', 'links')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField('get_links')

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
                            kwargs={User.USERNAME_FIELD: username},
                            request=request),
        }

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')
