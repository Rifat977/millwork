from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from millwork_site.models import *
import os

class Command(BaseCommand):
    help = 'Populate database with dummy data'

    def handle(self, *args, **options):
        # Company Info
        company, created = CompanyInfo.objects.get_or_create(
            defaults={
                'name': 'Royal Aluminium and UPVC Qatar',
                'name_arabic': 'رويال الألمنيوم واليو بي في سي قطر',
                'description': 'Leading provider of premium aluminium and UPVC solutions in Qatar. We specialize in windows, doors, facades, and architectural solutions with unmatched quality and craftsmanship.',
                'description_arabic': 'المزود الرائد لحلول الألمنيوم واليو بي في سي المتميزة في قطر. نتخصص في النوافذ والأبواب والواجهات والحلول المعمارية بجودة وحرفية لا مثيل لها.',
                'address': 'West Bay, Doha, Qatar',
                'address_arabic': 'الغرب، الدوحة، قطر',
                'phone': '+974 1234 5678',
                'email': 'info@royalaluminium.qa',
                'whatsapp': '97412345678'
            }
        )

        # Services
        services_data = [
            {
                'name': 'Aluminium Windows',
                'name_arabic': 'نوافذ الألمنيوم',
                'description': 'Energy-efficient aluminium windows designed for Qatar\'s climate. Available in various styles including casement, sliding, and tilt-and-turn.',
                'description_arabic': 'نوافذ ألمنيوم موفرة للطاقة مصممة لمناخ قطر. متوفرة بأنماط مختلفة تشمل المفتوحة والمنزلقة والمائلة والدوارة.',
                'icon': 'fas fa-window-maximize',
                'order': 1
            },
            {
                'name': 'UPVC Doors',
                'name_arabic': 'أبواب اليو بي في سي',
                'description': 'Premium UPVC doors offering excellent thermal insulation, security, and durability. Perfect for residential and commercial applications.',
                'description_arabic': 'أبواب يو بي في سي متميزة توفر عزل حراري ممتاز وأمان ومتانة. مثالية للتطبيقات السكنية والتجارية.',
                'icon': 'fas fa-door-open',
                'order': 2
            },
            {
                'name': 'Aluminium Facades',
                'name_arabic': 'واجهات الألمنيوم',
                'description': 'Modern aluminium facade systems for commercial and residential buildings. Custom designs to enhance architectural aesthetics.',
                'description_arabic': 'أنظمة الواجهات الألمنيومية الحديثة للمباني التجارية والسكنية. تصاميم مخصصة لتعزيز الجماليات المعمارية.',
                'icon': 'fas fa-building',
                'order': 3
            }
        ]

        for service_data in services_data:
            Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )

        # Projects
        projects_data = [
            {
                'title': 'Luxury Villa Windows',
                'title_arabic': 'نوافذ الفيلا الفاخرة',
                'description': 'Custom aluminium windows for a luxury villa in West Bay. Features energy-efficient glass and modern design.',
                'description_arabic': 'نوافذ ألمنيوم مخصصة لفيلا فاخرة في الغرب. تتميز بزجاج موفر للطاقة وتصميم عصري.',
                'category': 'windows',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Commercial Building Facade',
                'title_arabic': 'واجهة المبنى التجاري',
                'description': 'Complete aluminium facade system for a commercial building in Doha. Modern design with excellent thermal performance.',
                'description_arabic': 'نظام الواجهة الألمنيومية الكامل لمبنى تجاري في الدوحة. تصميم عصري بأداء حراري ممتاز.',
                'category': 'facades',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Residential UPVC Doors',
                'title_arabic': 'أبواب يو بي في سي سكنية',
                'description': 'Premium UPVC doors for residential complex. Features advanced security and thermal insulation.',
                'description_arabic': 'أبواب يو بي في سي متميزة للمجمع السكني. تتميز بأمان متقدم وعزل حراري.',
                'category': 'doors',
                'is_featured': True,
                'order': 3
            }
        ]

        for project_data in projects_data:
            Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )

        # Team Members
        team_data = [
            {
                'name': 'Ahmed Al-Mansouri',
                'name_arabic': 'أحمد المنصوري',
                'position': 'General Manager',
                'position_arabic': 'المدير العام',
                'bio': 'Over 15 years of experience in aluminium and UPVC industry. Expert in project management and quality control.',
                'bio_arabic': 'أكثر من 15 عاماً من الخبرة في صناعة الألمنيوم واليو بي في سي. خبير في إدارة المشاريع ومراقبة الجودة.',
                'order': 1
            },
            {
                'name': 'Sarah Johnson',
                'name_arabic': 'سارة جونسون',
                'position': 'Design Consultant',
                'position_arabic': 'استشارية التصميم',
                'bio': 'Architectural designer specializing in modern facade systems and energy-efficient solutions.',
                'bio_arabic': 'مصممة معمارية متخصصة في أنظمة الواجهات الحديثة والحلول الموفرة للطاقة.',
                'order': 2
            }
        ]

        for member_data in team_data:
            TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )

        # Testimonials
        testimonials_data = [
            {
                'customer_name': 'Mohammed Al-Thani',
                'customer_name_arabic': 'محمد آل ثاني',
                'company': 'Al-Thani Group',
                'company_arabic': 'مجموعة آل ثاني',
                'testimonial': 'Excellent service and quality. The aluminium windows exceeded our expectations. Highly recommended for any project.',
                'testimonial_arabic': 'خدمة ممتازة وجودة عالية. النوافذ الألمنيومية تجاوزت توقعاتنا. موصى به بشدة لأي مشروع.',
                'rating': 5,
                'order': 1
            },
            {
                'customer_name': 'Jennifer Smith',
                'customer_name_arabic': 'جينيفر سميث',
                'company': 'Doha Properties',
                'company_arabic': 'عقارات الدوحة',
                'testimonial': 'Professional team with attention to detail. The UPVC doors are perfect for our climate. Great value for money.',
                'testimonial_arabic': 'فريق مهني مع الاهتمام بالتفاصيل. أبواب اليو بي في سي مثالية لمناخنا. قيمة ممتازة مقابل المال.',
                'rating': 5,
                'order': 2
            }
        ]

        for testimonial_data in testimonials_data:
            Testimonial.objects.get_or_create(
                customer_name=testimonial_data['customer_name'],
                defaults=testimonial_data
            )

        # Page Content
        page_content_data = [
            {
                'page': 'home',
                'title': 'Premium Aluminium & UPVC Solutions',
                'title_arabic': 'حلول الألمنيوم واليو بي في سي المتميزة',
                'subtitle': 'Transform your space with our premium aluminium and UPVC solutions. From energy-efficient windows to stunning facades.',
                'subtitle_arabic': 'حوّل مساحتك مع حلولنا المتميزة من الألمنيوم واليو بي في سي. من النوافذ الموفرة للطاقة إلى الواجهات المذهلة.',
                'content': 'Royal Aluminium and UPVC Qatar is your trusted partner for premium aluminium and UPVC solutions. We specialize in creating energy-efficient, durable, and aesthetically pleasing windows, doors, and facades that enhance the beauty and functionality of your space.',
                'content_arabic': 'رويال الألمنيوم واليو بي في سي قطر هو شريكك الموثوق لحلول الألمنيوم واليو بي في سي المتميزة. نتخصص في إنشاء نوافذ وأبواب وواجهات موفرة للطاقة ومتينة وجميلة تعزز جمال ووظائف مساحتك.'
            }
        ]

        for content_data in page_content_data:
            PageContent.objects.get_or_create(
                page=content_data['page'],
                defaults=content_data
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with dummy data!')
        )
