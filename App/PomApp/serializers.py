from rest_framework import serializers
from models import ToDoItem

# class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = ToDoItem
# 		fields = ('description','done', 'pomodoros')

class ToDoItemSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	description = serializers.CharField(required=True, max_length=256)
	done = serializers.BooleanField(required=False)
	pomodoros = serializers.IntegerField(required=True)
	created_time = serializers.TimeField(required=False)

	def create(self, validated_data):
		return ToDoItem.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.description = validated_data.get('description', instance.description)
		instance.done = validated_data.get('done', instance.done)
		instance.pomodoros = validated_data.get('pomodoros', instance.pomodoros)
		instance.save()
		return instance


# class ToDoItemSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ToDoItem
# 		fields = ('id','description','done', 'pomodoros')