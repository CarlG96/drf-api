from rest_framework import serializers
from .models import Post

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    profile_id = serializer.ReadOnlyField(source='owner.profile.id')
    profile_image = serializer.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta():
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'image', 'owmer', 'is_owner',
            'profile_id', 'profile_image'
        ]