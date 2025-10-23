from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Medicine
from .serializers import MedicineSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Custom search endpoint
        Usage: /api/medicines/search/?q=search_term
        """
        query = request.query_params.get('q', '')
        if query:
            medicines = Medicine.objects.filter(name__icontains=query) | Medicine.objects.filter(description__icontains=query)
        else:
            medicines = Medicine.objects.all()
        
        serializer = self.get_serializer(medicines, many=True)
        return Response(serializer.data)
