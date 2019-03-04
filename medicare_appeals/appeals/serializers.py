from medicare_appeals.appeals import models
from rest_framework import serializers


class AppealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Appeal
        fields = '__all__'


class AppellantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Appellant
        fields = '__all__'


class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Claim
        fields = '__all__'


class HolisticAppealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HolisticAppeal
        fields = '__all__'


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Level
        fields = '__all__'


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Provider
        fields = '__all__'


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'
