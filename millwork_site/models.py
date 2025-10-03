from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Service(models.Model):
    """Model for services offered by the company"""
    name = models.CharField(max_length=100)
    name_arabic = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    description_arabic = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class name (e.g., 'fas fa-window')")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order for display")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Project(models.Model):
    """Model for portfolio projects"""
    CATEGORY_CHOICES = [
        ('windows', 'Windows'),
        ('doors', 'Doors'),
        ('facades', 'Facades'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    title_arabic = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    description_arabic = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    """Model for team members"""
    name = models.CharField(max_length=100)
    name_arabic = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100)
    position_arabic = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    bio_arabic = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class CompanyInfo(models.Model):
    """Model for company information"""
    name = models.CharField(max_length=200, default="Royal Aluminium and UPVC Qatar")
    name_arabic = models.CharField(max_length=200, default="رويال الألمنيوم واليو بي في سي قطر")
    description = models.TextField()
    description_arabic = models.TextField(blank=True)
    address = models.CharField(max_length=500)
    address_arabic = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='company/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    """Model for customer testimonials"""
    customer_name = models.CharField(max_length=100)
    customer_name_arabic = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    position_arabic = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    company_arabic = models.CharField(max_length=100, blank=True)
    testimonial = models.TextField()
    testimonial_arabic = models.TextField(blank=True)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.company}"

class ContactMessage(models.Model):
    """Model for contact form messages"""
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    project_type = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.project_type}"

class PageContent(models.Model):
    """Model for dynamic page content"""
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('services', 'Services'),
        ('portfolio', 'Portfolio'),
        ('contact', 'Contact'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    title_arabic = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    subtitle_arabic = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    content_arabic = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_description_arabic = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page']

    def __str__(self):
        return f"{self.get_page_display()} Page Content"