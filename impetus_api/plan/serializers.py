from rest_framework import serializers


class PlanSerializer(serializers.Serializer):  # noqa: D101
    # class Meta:
    #     model = Plan
    #     fields = ('id', 'name', 'summary')
    name = serializers.CharField(max_length=72)
    summary = serializers.CharField(max_length=300)

    def create(self, validated_data):  # noqa: D102
        print('creating data')
        print(validated_data)
