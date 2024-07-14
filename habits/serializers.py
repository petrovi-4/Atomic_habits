from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id',
            'place',
            'time',
            'periodicity',
            'action',
            'is_pleasurable',
            'associated_habit',
            'reward',
            'lead_time',
            'is_public'
        )


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'action',
            'time',
            'periodicity',
            'place',
            'is_pleasurable',
            'associated_habit',
            'reward',
            'lead_time',
        )