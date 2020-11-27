from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JoobleIndia, JoobleAustralia, JoobleCanada, JoobleIreland, JoobleMalaysia, JoobleNewZealand,\
    JoobleNigeria, JooblePakistan, JooblePhilippines, JoobleSingapore, JoobleSouthAfrica, JoobleUnitedKingdom,\
    JoobleUSA
from .serializers import IndiaSerializer, USASerializer, UnitedKingdomSerializer, SouthAfricaSerializer, \
    SingaporeSerializer, PakistanSerializer, NigeriaSerializer, NewZealandSerializer, MalaysiaSerializer, \
    IrelandSerializer, CanadaSerializer, AustraliaSerializer, PhilippinesSerializer


class JoobleIndiaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleIndia.objects.all()
        serializer = IndiaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = IndiaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleIndia.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = IndiaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleIndia.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JooblePhilippinesView(APIView):
    @staticmethod
    def get(request):
        articles = JooblePhilippines.objects.all()
        serializer = PhilippinesSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = PhilippinesSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JooblePhilippines.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = PhilippinesSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JooblePhilippines.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleMalaysiaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleMalaysia.objects.all()
        serializer = MalaysiaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = MalaysiaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleMalaysia.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = MalaysiaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleMalaysia.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleCanadaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleCanada.objects.all()
        serializer = CanadaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = CanadaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleCanada.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = CanadaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleCanada.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleNewZealandView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleNewZealand.objects.all()
        serializer = NewZealandSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = NewZealandSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleNewZealand.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = NewZealandSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleNewZealand.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleAustraliaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleAustralia.objects.all()
        serializer = AustraliaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = AustraliaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleAustralia.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = AustraliaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleAustralia.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleNigeriaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleNigeria.objects.all()
        serializer = NigeriaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = NigeriaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleNigeria.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = NigeriaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleNigeria.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleSouthAfricaView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleSouthAfrica.objects.all()
        serializer = SouthAfricaSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = SouthAfricaSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleSouthAfrica.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = SouthAfricaSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleSouthAfrica.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleUnitedKingdomView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleUnitedKingdom.objects.all()
        serializer = UnitedKingdomSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = UnitedKingdomSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleUnitedKingdom.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = UnitedKingdomSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleUnitedKingdom.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleIrelandView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleIreland.objects.all()
        serializer = IrelandSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = IrelandSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleIreland.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = IrelandSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleIreland.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleSingaporeView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleSingapore.objects.all()
        serializer = SingaporeSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = SingaporeSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleSingapore.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = SingaporeSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleSingapore.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JooblePakistanView(APIView):
    @staticmethod
    def get(request):
        articles = JooblePakistan.objects.all()
        serializer = PakistanSerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = PakistanSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JooblePakistan.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = PakistanSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JooblePakistan.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)


class JoobleUSAView(APIView):
    @staticmethod
    def get(request):
        articles = JoobleUSA.objects.all()
        serializer = USASerializer(articles, many=True)
        return Response({"Vacancy": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("Vacancy")
        # Create an article from the above data
        serializer = USASerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Vacancy '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(JoobleUSA.objects.all(), pk=pk)
        data = request.data.get('Vacancy')
        serializer = USASerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Vacancy '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(pk):
        # Get object with this pk
        article = get_object_or_404(JoobleUSA.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vacancy with id `{}` has been deleted.".format(pk)
        }, status=204)