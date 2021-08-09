from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLES_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLES_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        주어진 validated_data를 사용해 새 `Snippet` 인스턴스를 생성 및 반환함
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance: Snippet, validated_data):
        """
        주어진 validated_data를 사용해 이미 존재하는 `Snippet` 인스턴스를 수정 및 반환함
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
