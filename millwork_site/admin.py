from django.contrib import admin
from .models import (
    Service, Project, TeamMember, CompanyInfo, 
    Testimonial, ContactMessage, PageContent
)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'name_arabic', 'description']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'name_arabic', 'description', 'description_arabic')
        }),
        ('Media & Settings', {
            'fields': ('image', 'icon', 'is_active', 'order')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'title_arabic', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'title_arabic', 'description', 'description_arabic')
        }),
        ('Media & Category', {
            'fields': ('image', 'category')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'name_arabic', 'position']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'name_arabic', 'position', 'position_arabic')
        }),
        ('Bio & Media', {
            'fields': ('bio', 'bio_arabic', 'image')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'name_arabic', 'address', 'address_arabic')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'whatsapp')
        }),
        ('About Content', {
            'fields': ('description', 'description_arabic')
        }),
        ('Media', {
            'fields': ('logo', 'hero_image')
        }),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'company', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['customer_name', 'company', 'testimonial']
    list_editable = ['is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'customer_name_arabic', 'company', 'company_arabic', 'rating')
        }),
        ('Testimonial Content', {
            'fields': ('testimonial', 'testimonial_arabic', 'image')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'project_type', 'status', 'created_at']
    list_filter = ['status', 'project_type', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'message']
    list_editable = ['status']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Project Details', {
            'fields': ('project_type', 'budget', 'message')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'created_at')
        }),
    )

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page', 'title', 'updated_at']
    search_fields = ['page', 'title', 'title_arabic', 'content']
    
    fieldsets = (
        ('Page Information', {
            'fields': ('page',)
        }),
        ('Title Section (English)', {
            'fields': ('title', 'subtitle')
        }),
        ('Title Section (Arabic)', {
            'fields': ('title_arabic', 'subtitle_arabic')
        }),
        ('Page Content (English)', {
            'fields': ('content', 'meta_description')
        }),
        ('Page Content (Arabic)', {
            'fields': ('content_arabic', 'meta_description_arabic')
        }),
    )

# Django Jazzmin handles admin site customization