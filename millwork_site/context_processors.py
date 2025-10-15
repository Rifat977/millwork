"""
Context processors to make data available to all templates
"""
from .models import CompanyInfo


def company_info(request):
    """
    Add company information to all template contexts
    This makes company_info available in every template automatically
    """
    return {
        'company_info': CompanyInfo.objects.first()
    }

