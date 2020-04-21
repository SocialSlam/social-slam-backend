from rest_framework import serializers


class SlamSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['audience', 'slammers']

    slammers = serializers.SerializerMethodField()

    def get_slammers(self, obj):
        for slammer in obj.slammers:
            pass

