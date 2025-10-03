from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import (
    Service, Project, TeamMember, CompanyInfo, 
    Testimonial, ContactMessage, PageContent
)

def home(request):
    """Home page view"""
    context = {
        'services': Service.objects.filter(is_active=True)[:3],
        'featured_projects': Project.objects.filter(is_featured=True, is_active=True)[:3],
        'testimonials': Testimonial.objects.filter(is_active=True)[:3],
        'company_info': CompanyInfo.objects.first(),
        'page_content': PageContent.objects.filter(page='home').first(),
    }
    return render(request, 'index.html', context)

def about(request):
    """About page view"""
    context = {
        'team_members': TeamMember.objects.filter(is_active=True),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'company_info': CompanyInfo.objects.first(),
        'page_content': PageContent.objects.filter(page='about').first(),
    }
    return render(request, 'about.html', context)

def services(request):
    """Services page view"""
    services_list = Service.objects.filter(is_active=True)
    context = {
        'services': services_list,
        'page_content': PageContent.objects.filter(page='services').first(),
    }
    return render(request, 'services.html', context)

def portfolio(request):
    """Portfolio page view"""
    projects = Project.objects.filter(is_active=True)
    
    # Filter by category if requested
    category = request.GET.get('category')
    if category:
        projects = projects.filter(category=category)
    
    # Pagination
    paginator = Paginator(projects, 9)  # Show 9 projects per page
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    context = {
        'projects': projects_page,
        'categories': Project.CATEGORY_CHOICES,
        'current_category': category,
        'page_content': PageContent.objects.filter(page='portfolio').first(),
    }
    return render(request, 'portfolio.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle contact form submission
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('projectType')
        budget = request.POST.get('budget')
        message = request.POST.get('message')
        
        # Create contact message
        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            project_type=project_type,
            budget=budget,
            message=message
        )
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    
        context = {
            'company_info': CompanyInfo.objects.first(),
            'page_content': PageContent.objects.filter(page='contact').first(),
        }
        return render(request, 'contact.html', context)

def sitemap_xml(request):
    """Generate XML sitemap"""
    base_url = request.build_absolute_uri('/')
    
    # Static pages
    static_pages = [
        {'url': '', 'priority': '1.0', 'changefreq': 'daily'},
        {'url': 'about/', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': 'services/', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': 'portfolio/', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': 'contact/', 'priority': '0.7', 'changefreq': 'monthly'},
    ]
    
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''
    
    for page in static_pages:
        xml_content += f'''
    <url>
        <loc>{base_url}{page['url']}</loc>
        <lastmod>{timezone.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
    </url>'''
    
    # Add dynamic project pages
    projects = Project.objects.filter(is_active=True)
    for project in projects:
        xml_content += f'''
    <url>
        <loc>{base_url}portfolio/?project={project.id}</loc>
        <lastmod>{project.updated_at.strftime('%Y-%m-%d')}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>'''
    
    xml_content += '''
</urlset>'''
    
    response = HttpResponse(xml_content, content_type='application/xml')
    return response

def robots_txt(request):
    """Serve robots.txt"""
    robots_content = '''User-agent: *
Allow: /

# Sitemap
Sitemap: {}/sitemap.xml

# Disallow admin and private areas
Disallow: /admin/
Disallow: /static/admin/
Disallow: /media/
Disallow: /api/

# Allow important pages
Allow: /
Allow: /about/
Allow: /services/
Allow: /portfolio/
Allow: /contact/

# Crawl delay (optional)
Crawl-delay: 1'''.format(request.build_absolute_uri('/'))
    
    response = HttpResponse(robots_content, content_type='text/plain')
    return response
