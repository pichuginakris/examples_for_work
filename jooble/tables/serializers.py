from rest_framework import serializers
from .models import JoobleIndia, JoobleAustralia, JoobleCanada, JoobleIreland, JoobleMalaysia, JoobleNewZealand,\
    JoobleNigeria, JooblePakistan, JooblePhilippines, JoobleSingapore, JoobleSouthAfrica, JoobleUnitedKingdom, \
    JoobleUSA


class VacancySerializer(serializers.Serializer):
    vacancy = serializers.CharField(max_length=20000)
    link_to_a_vacancy = serializers.CharField(max_length=20000)
    salary = serializers.CharField(max_length=20000)
    company = serializers.CharField(max_length=20000)
    short_description = serializers.CharField(max_length=20000)
    location = serializers.CharField(max_length=20000)
    date_from_creation = serializers.CharField(max_length=20000)
    full_description = serializers.CharField(max_length=20000)
    link_to_a_company = serializers.CharField(max_length=20000)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.vacancy = validated_data.get('vacancy', instance.title)
        instance.link_to_a_vacancy = validated_data.get('link_to_a_vacancy', instance.title)
        instance.salary = validated_data.get('salary', instance.title)
        instance.company = validated_data.get('company', instance.title)
        instance.short_description = validated_data.get('short_description', instance.title)
        instance.location = validated_data.get('location', instance.title)
        instance.date_from_creation = validated_data.get('date_from_creation', instance.title)
        instance.full_description = validated_data.get('full_description', instance.title)
        instance.link_to_a_company = validated_data.get('link_to_a_company', instance.title)
        instance.save()
        return instance


class IndiaSerializer (VacancySerializer):
    title = 'India'

    def create(self, validated_data):
        return JoobleIndia.objects.create(**validated_data)


class AustraliaSerializer(VacancySerializer):
    title = 'Australia'

    def create(self, validated_data):
        return JoobleAustralia.objects.create(**validated_data)


class PhilippinesSerializer(VacancySerializer):
    title = 'Philippines'

    def create(self, validated_data):
        return JooblePhilippines.objects.create(**validated_data)


class CanadaSerializer(VacancySerializer):
    title = 'Canada'

    def create(self, validated_data):
        return JoobleCanada.objects.create(**validated_data)


class IrelandSerializer(VacancySerializer):
    title = 'Ireland'

    def create(self, validated_data):
        return JoobleIreland.objects.create(**validated_data)


class MalaysiaSerializer(VacancySerializer):
    title = 'Malaysia'

    def create(self, validated_data):
        return JoobleMalaysia.objects.create(**validated_data)


class NewZealandSerializer(VacancySerializer):
    title = 'New_Zealand'

    def create(self, validated_data):
        return JoobleNewZealand.objects.create(**validated_data)


class NigeriaSerializer(VacancySerializer):
    title = 'Nigeria'

    def create(self, validated_data):
        return JoobleNigeria.objects.create(**validated_data)


class PakistanSerializer(VacancySerializer):
    title = 'Pakistan'

    def create(self, validated_data):
        return JooblePakistan.objects.create(**validated_data)


class SingaporeSerializer(VacancySerializer):
    title = 'India'

    def create(self, validated_data):
        return JoobleSingapore.objects.create(**validated_data)


class SouthAfricaSerializer(VacancySerializer):
    title = 'South_Africa'

    def create(self, validated_data):
        return JoobleSouthAfrica.objects.create(**validated_data)


class UnitedKingdomSerializer(VacancySerializer):
    title = 'United_Kingdom'

    def create(self, validated_data):
        return JoobleUnitedKingdom.objects.create(**validated_data)


class USASerializer(VacancySerializer):
    title = 'USA'

    def create(self, validated_data):
        return JoobleUSA.objects.create(**validated_data)
