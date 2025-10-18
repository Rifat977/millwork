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
        ('aluminium_kitchen', 'Aluminium Kitchen Cabinet Luxurious Design'),
        ('upvc_door_window', 'UPVC Door & Window'),
        ('glass_door_partition', 'Glass Door & Partition'),
        ('aluminum_door_window', 'Aluminum Door & Window'),
    ]
    
    title = models.CharField(max_length=200)
    title_arabic = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    description_arabic = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', help_text="Main display image")
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

class ProjectImage(models.Model):
    """Model for additional project images (for slider)"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    caption_arabic = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"

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
    
    # Business Hours
    weekday_hours = models.CharField(max_length=100, default="8:00 AM - 6:00 PM", help_text="Monday to Friday hours")
    weekday_hours_arabic = models.CharField(max_length=100, blank=True, help_text="Monday to Friday hours in Arabic")
    saturday_hours = models.CharField(max_length=100, default="9:00 AM - 4:00 PM", help_text="Saturday hours")
    saturday_hours_arabic = models.CharField(max_length=100, blank=True, help_text="Saturday hours in Arabic")
    sunday_hours = models.CharField(max_length=100, default="Closed", help_text="Sunday hours (e.g., 'Closed' or time)")
    sunday_hours_arabic = models.CharField(max_length=100, default="مغلق", help_text="Sunday hours in Arabic")
    
    # Service Areas
    service_areas = models.TextField(blank=True, help_text="Comma-separated list of areas served (e.g., Doha, Lusail, West Bay)")
    service_areas_arabic = models.TextField(blank=True, help_text="Comma-separated list of areas in Arabic")
    showroom_address = models.CharField(max_length=500, blank=True, help_text="Physical showroom/office address")
    showroom_address_arabic = models.CharField(max_length=500, blank=True)
    
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

class CompanyStatistics(models.Model):
    """Model for company statistics displayed on home page"""
    years_in_business = models.PositiveIntegerField(default=8, help_text="Years in business")
    projects_completed = models.PositiveIntegerField(default=500, help_text="Total projects completed")
    happy_clients = models.PositiveIntegerField(default=350, help_text="Number of satisfied clients")
    team_members = models.PositiveIntegerField(default=15, help_text="Number of team members")
    
    # Labels (customizable)
    years_label = models.CharField(max_length=100, default="Years of Excellence")
    years_label_arabic = models.CharField(max_length=100, default="سنوات من التميز")
    projects_label = models.CharField(max_length=100, default="Projects Completed")
    projects_label_arabic = models.CharField(max_length=100, default="مشاريع مكتملة")
    clients_label = models.CharField(max_length=100, default="Happy Clients")
    clients_label_arabic = models.CharField(max_length=100, default="عملاء سعداء")
    team_label = models.CharField(max_length=100, default="Expert Team")
    team_label_arabic = models.CharField(max_length=100, default="فريق خبراء")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Statistics"
        verbose_name_plural = "Company Statistics"

    def __str__(self):
        return "Company Statistics"

class WhyChooseUsItem(models.Model):
    """Model for 'Why Choose Us' section items"""
    title = models.CharField(max_length=200)
    title_arabic = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    description_arabic = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class or SVG identifier")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Why Choose Us Item"
        verbose_name_plural = "Why Choose Us Items"

    def __str__(self):
        return self.title

class Certification(models.Model):
    """Model for certifications and trust badges"""
    name = models.CharField(max_length=200)
    name_arabic = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    description_arabic = models.TextField(blank=True)
    logo = models.ImageField(upload_to='certifications/', blank=True, null=True, help_text="Certification logo or badge")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.name

class FAQ(models.Model):
    """Model for Frequently Asked Questions - SEO Optimized"""
    question = models.CharField(max_length=300, help_text="Question (keyword-rich)")
    question_arabic = models.CharField(max_length=300, blank=True)
    answer = models.TextField(help_text="Detailed answer with keywords")
    answer_arabic = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=[
        ('general', 'General'),
        ('products', 'Products'),
        ('installation', 'Installation'),
        ('pricing', 'Pricing'),
        ('warranty', 'Warranty'),
    ], default='general')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question