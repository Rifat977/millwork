from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from millwork_site.models import *
import os
import shutil
from pathlib import Path

class Command(BaseCommand):
    help = 'Populate database with realistic SEO-friendly dummy data'

    def copy_static_to_media(self, static_image_name, media_subfolder):
        """Copy image from static/images to media folder"""
        static_dir = Path('static/images')
        media_dir = Path('media') / media_subfolder
        media_dir.mkdir(parents=True, exist_ok=True)
        
        source = static_dir / static_image_name
        destination = media_dir / static_image_name
        
        if source.exists() and not destination.exists():
            shutil.copy(source, destination)
            return f'{media_subfolder}/{static_image_name}'
        elif destination.exists():
            return f'{media_subfolder}/{static_image_name}'
        return None

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Starting to populate database...'))

        # Company Info
        company, created = CompanyInfo.objects.get_or_create(
            defaults={
                'name': 'Royal Aluminium and UPVC Qatar',
                'name_arabic': 'رويال الألمنيوم واليو بي في سي قطر',
                'description': 'Leading provider of premium aluminium and UPVC solutions in Qatar. We specialize in energy-efficient windows, doors, facades, and architectural solutions with unmatched quality and craftsmanship. Serving Doha and all of Qatar since 2015.',
                'description_arabic': 'المزود الرائد لحلول الألمنيوم واليو بي في سي المتميزة في قطر. نتخصص في النوافذ الموفرة للطاقة والأبواب والواجهات والحلول المعمارية بجودة وحرفية لا مثيل لها. نخدم الدوحة وجميع أنحاء قطر منذ عام 2015.',
                'address': 'Industrial Area, Street 38, Doha, Qatar',
                'address_arabic': 'المنطقة الصناعية، شارع 38، الدوحة، قطر',
                'phone': '+974 7790 4281',
                'email': 'info@royalaluminium.qa',
                'whatsapp': '97477904281',
                'weekday_hours': '8:00 AM - 6:00 PM',
                'weekday_hours_arabic': '8:00 ص - 6:00 م',
                'saturday_hours': '9:00 AM - 4:00 PM',
                'saturday_hours_arabic': '9:00 ص - 4:00 م',
                'sunday_hours': 'Closed',
                'sunday_hours_arabic': 'مغلق'
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Company Info {"created" if created else "already exists"}'))

        # Services - SEO optimized
        services_data = [
            {
                'name': 'Aluminium Windows Qatar',
                'name_arabic': 'نوافذ الألمنيوم قطر',
                'description': 'Premium energy-efficient aluminium windows designed for Qatar\'s extreme climate. Our double-glazed windows provide excellent thermal insulation, reducing cooling costs by up to 40%. Available in casement, sliding, tilt-and-turn, and fixed window styles. Certified for Qatar Construction Specifications.',
                'description_arabic': 'نوافذ ألمنيوم متميزة موفرة للطاقة مصممة لمناخ قطر القاسي. نوافذنا ذات الزجاج المزدوج توفر عزل حراري ممتاز، مما يقلل تكاليف التبريد بنسبة تصل إلى 40٪. متوفرة بأنماط النوافذ المفتوحة والمنزلقة والمائلة والدوارة والثابتة. معتمدة لمواصفات البناء القطرية.',
                'icon': 'fas fa-window-maximize',
                'order': 1
            },
            {
                'name': 'UPVC Doors Doha',
                'name_arabic': 'أبواب يو بي في سي الدوحة',
                'description': 'High-security UPVC doors with multi-point locking systems. Resistant to Qatar\'s humidity, salt air, and extreme temperatures. Perfect for villas, apartments, and commercial buildings. Available in various colors and finishes with German quality hardware.',
                'description_arabic': 'أبواب يو بي في سي عالية الأمان مع أنظمة قفل متعددة النقاط. مقاومة للرطوبة في قطر والهواء المالح ودرجات الحرارة القصوى. مثالية للفلل والشقق والمباني التجارية. متوفرة بألوان وتشطيبات مختلفة مع أجهزة ألمانية الجودة.',
                'icon': 'fas fa-door-open',
                'order': 2
            },
            {
                'name': 'Aluminium Facades',
                'name_arabic': 'واجهات الألمنيوم',
                'description': 'Modern aluminium curtain wall and facade systems for commercial and residential towers. Unitized and stick systems available. Enhanced solar control with Low-E glass. Full structural calculations and wind load analysis included. Compliant with Qatar Civil Defence regulations.',
                'description_arabic': 'أنظمة جدران ستارية وواجهات ألمنيوم حديثة للأبراج التجارية والسكنية. أنظمة موحدة وعصا متاحة. تحكم شمسي محسّن مع زجاج Low-E. حسابات هيكلية كاملة وتحليل حمل الرياح متضمنة. متوافقة مع لوائح الدفاع المدني القطري.',
                'icon': 'fas fa-building',
                'order': 3
            },
            {
                'name': 'Sliding Systems',
                'name_arabic': 'أنظمة منزلقة',
                'description': 'Premium sliding door and window systems for modern Qatar homes. Space-saving designs with smooth operation. Available in aluminium and UPVC. Excellent air-tightness and water resistance. Perfect for balconies, patios, and terraces.',
                'description_arabic': 'أنظمة أبواب ونوافذ منزلقة متميزة للمنازل القطرية الحديثة. تصاميم موفرة للمساحة مع تشغيل سلس. متوفرة بالألمنيوم واليو بي في سي. إحكام هواء ومقاومة ماء ممتازة. مثالية للشرفات والباحات والتراسات.',
                'icon': 'fas fa-arrows-alt-h',
                'order': 4
            },
            {
                'name': 'Shower Enclosures',
                'name_arabic': 'حاويات الدش',
                'description': 'Elegant frameless and framed glass shower enclosures. Tempered safety glass with water-repellent coating. Custom sizes available. Durable aluminium frames resistant to moisture. Professional installation included.',
                'description_arabic': 'حاويات دش زجاجية أنيقة بدون إطار وبإطار. زجاج أمان مقسى مع طلاء طارد للماء. أحجام مخصصة متاحة. إطارات ألمنيوم متينة مقاومة للرطوبة. تركيب احترافي متضمن.',
                'icon': 'fas fa-shower',
                'order': 5
            },
            {
                'name': 'Partitions & Cladding',
                'name_arabic': 'التقسيمات والكسوة',
                'description': 'Office partitions, ACP cladding, and interior aluminium solutions. Fire-rated partitions available. Modern aesthetics with functional design. Perfect for commercial fit-outs and office renovations in Doha.',
                'description_arabic': 'فواصل المكاتب وكسوة ACP وحلول الألمنيوم الداخلية. متوفرة فواصل مقاومة للحريق. جماليات حديثة مع تصميم وظيفي. مثالية لتجهيزات تجارية وتجديدات المكاتب في الدوحة.',
                'icon': 'fas fa-th-large',
                'order': 6
            }
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Service: {service.name} {"created" if created else "updated"}'))

        # Projects - Using actual images with SEO-optimized content
        projects_data = [
            {
                'title': 'West Bay Luxury Villa - Aluminium Windows Installation',
                'title_arabic': 'فيلا فاخرة في الغرب - تركيب نوافذ ألمنيوم',
                'description': 'Complete aluminium window installation for a 5-bedroom luxury villa in West Bay. Features energy-efficient double-glazed windows with Low-E coating, reducing AC costs by 35%. Project completed in 3 weeks with minimal disruption to residents.',
                'description_arabic': 'تركيب نوافذ ألمنيوم كامل لفيلا فاخرة من 5 غرف نوم في الغرب. تتميز بنوافذ زجاج مزدوج موفرة للطاقة مع طلاء Low-E، مما يقلل تكاليف التكييف بنسبة 35٪. اكتمل المشروع في 3 أسابيع بأقل قدر من الإزعاج للسكان.',
                'category': 'windows',
                'is_featured': True,
                'order': 1,
                'image': 'demo1.jpeg'
            },
            {
                'title': 'Pearl Qatar Tower - Commercial Facade System',
                'title_arabic': 'برج اللؤلؤة قطر - نظام واجهة تجارية',
                'description': 'Modern aluminium curtain wall facade for a 30-story commercial tower at The Pearl Qatar. Unitized system with superior thermal performance. Includes solar control glass and structural silicone glazing. Completed on schedule with QCD approval.',
                'description_arabic': 'واجهة جدار ستاري ألمنيوم حديث لبرج تجاري من 30 طابق في اللؤلؤة قطر. نظام موحد بأداء حراري فائق. يشمل زجاج تحكم شمسي وزجاج سيليكون هيكلي. اكتمل في الموعد المحدد مع موافقة الدفاع المدني القطري.',
                'category': 'facades',
                'is_featured': True,
                'order': 2,
                'image': 'demo2.jpeg'
            },
            {
                'title': 'Al Rayyan Compound - UPVC Doors Project',
                'title_arabic': 'مجمع الريان - مشروع أبواب يو بي في سي',
                'description': 'Supply and installation of 150+ UPVC doors for residential compound in Al Rayyan. Multi-point locking system with weather seals. Completed for 40 villas with 2-year warranty. Excellent thermal and acoustic insulation.',
                'description_arabic': 'توريد وتركيب أكثر من 150 باب يو بي في سي لمجمع سكني في الريان. نظام قفل متعدد النقاط مع أختام الطقس. اكتمل ل 40 فيلا مع ضمان لمدة عامين. عزل حراري وصوتي ممتاز.',
                'category': 'doors',
                'is_featured': True,
                'order': 3,
                'image': 'demo3.jpeg'
            },
            {
                'title': 'Lusail Modern Villa - Complete Aluminium Package',
                'title_arabic': 'فيلا لوسيل الحديثة - حزمة ألمنيوم كاملة',
                'description': 'Full aluminium works including windows, doors, and sliding systems for modern villa in Lusail City. Black powder-coated frames with tinted glass. Custom-made sliding doors for living areas. Project value: QAR 450,000.',
                'description_arabic': 'أعمال ألمنيوم كاملة تشمل النوافذ والأبواب والأنظمة المنزلقة لفيلا حديثة في مدينة لوسيل. إطارات سوداء مطلية بالمسحوق مع زجاج ملون. أبواب منزلقة مصنوعة حسب الطلب لمناطق المعيشة. قيمة المشروع: 450,000 ريال قطري.',
                'category': 'windows',
                'is_featured': False,
                'order': 4,
                'image': 'demo4.jpeg'
            },
            {
                'title': 'Doha Office Building - Glass Partitions',
                'title_arabic': 'مبنى مكاتب الدوحة - فواصل زجاجية',
                'description': 'Modern office partitions with aluminium framing for 8-floor office building. Fire-rated glass partitions with soundproofing. Frameless glass doors and frosted glass panels. Completed fit-out in 6 weeks.',
                'description_arabic': 'فواصل مكاتب حديثة بإطارات ألمنيوم لمبنى مكاتب من 8 طوابق. فواصل زجاجية مقاومة للحريق مع عزل صوتي. أبواب زجاجية بدون إطار وألواح زجاج مصنفر. اكتمل التجهيز في 6 أسابيع.',
                'category': 'other',
                'is_featured': False,
                'order': 5,
                'image': 'demo5.jpeg'
            },
            {
                'title': 'Al Wakrah Villa - Sliding Door Systems',
                'title_arabic': 'فيلا الوكرة - أنظمة أبواب منزلقة',
                'description': 'Premium sliding door installation connecting indoor and outdoor spaces. Heavy-duty aluminium track system. Thermally broken profiles for energy efficiency. Large glass panels for maximum natural light.',
                'description_arabic': 'تركيب أبواب منزلقة متميزة تربط المساحات الداخلية والخارجية. نظام مسار ألمنيوم للخدمة الشاقة. ملفات تعريف مكسورة حرارياً لكفاءة الطاقة. ألواح زجاج كبيرة لأقصى إضاءة طبيعية.',
                'category': 'doors',
                'is_featured': False,
                'order': 6,
                'image': 'demo6.jpeg'
            }
        ]

        for project_data in projects_data:
            image_name = project_data.pop('image')
            image_path = self.copy_static_to_media(image_name, 'projects')
            
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={**project_data, 'image': image_path if image_path else ''}
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Project: {project.title} {"created" if created else "updated"}'))

        # Team Members - More realistic
        team_data = [
            {
                'name': 'Ahmed Al-Mansouri',
                'name_arabic': 'أحمد المنصوري',
                'position': 'General Manager & Founder',
                'position_arabic': 'المدير العام والمؤسس',
                'bio': 'Over 18 years of experience in aluminium and UPVC industry across Qatar and UAE. Expert in project management, quality control, and Qatar Construction Specifications. Led 500+ successful projects in Qatar.',
                'bio_arabic': 'أكثر من 18 عاماً من الخبرة في صناعة الألمنيوم واليو بي في سي في قطر والإمارات. خبير في إدارة المشاريع ومراقبة الجودة ومواصفات البناء القطرية. قاد أكثر من 500 مشروع ناجح في قطر.',
                'order': 1
            },
            {
                'name': 'Mohammad Al-Kuwari',
                'name_arabic': 'محمد الكواري',
                'position': 'Technical Manager',
                'position_arabic': 'المدير الفني',
                'bio': 'Certified aluminium systems engineer with 12+ years experience. Specialist in facade design and thermal calculations. Trained by leading European manufacturers.',
                'bio_arabic': 'مهندس أنظمة ألمنيوم معتمد بخبرة تزيد عن 12 عاماً. متخصص في تصميم الواجهات والحسابات الحرارية. مدرب من قبل كبار المصنعين الأوروبيين.',
                'order': 2
            },
            {
                'name': 'Sarah Al-Naimi',
                'name_arabic': 'سارة النعيمي',
                'position': 'Design Consultant',
                'position_arabic': 'استشارية التصميم',
                'bio': 'Architectural designer specializing in modern facade systems and energy-efficient solutions. Expertise in custom window designs for Qatar villas and towers.',
                'bio_arabic': 'مصممة معمارية متخصصة في أنظمة الواجهات الحديثة والحلول الموفرة للطاقة. خبرة في تصاميم نوافذ مخصصة لفلل وأبراج قطر.',
                'order': 3
            },
            {
                'name': 'Rajesh Kumar',
                'name_arabic': 'راجيش كومار',
                'position': 'Installation Supervisor',
                'position_arabic': 'مشرف التركيب',
                'bio': '15+ years of hands-on experience in aluminium installation. Expert in high-rise facade installation and quality assurance. Safety-certified with excellent track record.',
                'bio_arabic': 'أكثر من 15 عاماً من الخبرة العملية في تركيب الألمنيوم. خبير في تركيب واجهات المباني الشاهقة وضمان الجودة. معتمد في السلامة مع سجل حافل ممتاز.',
                'order': 4
            }
        ]

        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Team Member: {member.name} {"created" if created else "updated"}'))

        # Testimonials - More detailed and realistic
        testimonials_data = [
            {
                'customer_name': 'Mohammed Al-Thani',
                'customer_name_arabic': 'محمد آل ثاني',
                'position': 'Property Owner',
                'position_arabic': 'مالك العقار',
                'company': 'West Bay Villa',
                'company_arabic': 'فيلا الخليج الغربي',
                'testimonial': 'Royal Aluminium installed windows for my villa in West Bay. The quality is outstanding and my AC bills dropped by 30%! The team was professional, on time, and cleaned up after themselves. Highly recommend for anyone building or renovating in Qatar.',
                'testimonial_arabic': 'قامت رويال الألمنيوم بتركيب نوافذ لفيلتي في الخليج الغربي. الجودة ممتازة وانخفضت فواتير التكييف بنسبة 30٪! كان الفريق محترفاً وفي الوقت المحدد ونظف بعد نفسه. أوصي به بشدة لأي شخص يبني أو يجدد في قطر.',
                'rating': 5,
                'order': 1
            },
            {
                'customer_name': 'Fatima Al-Ansari',
                'customer_name_arabic': 'فاطمة الأنصاري',
                'position': 'Homeowner',
                'position_arabic': 'مالكة منزل',
                'company': 'Al Rayyan Residence',
                'company_arabic': 'إقامة الريان',
                'testimonial': 'We needed UPVC doors for our entire compound. Royal Aluminium gave us the best price without compromising quality. The doors are beautiful, secure, and block out the heat perfectly. Installation was smooth and completed ahead of schedule!',
                'testimonial_arabic': 'احتجنا إلى أبواب يو بي في سي للمجمع بأكمله. أعطتنا رويال الألمنيوم أفضل سعر دون المساس بالجودة. الأبواب جميلة وآمنة وتحجب الحرارة تماماً. كان التركيب سلساً واكتمل قبل الموعد المحدد!',
                'rating': 5,
                'order': 2
            },
            {
                'customer_name': 'David Richardson',
                'customer_name_arabic': 'ديفيد ريتشاردسون',
                'position': 'Project Manager',
                'position_arabic': 'مدير المشروع',
                'company': 'Pearl Tower Development',
                'company_arabic': 'تطوير برج اللؤلؤة',
                'testimonial': 'We contracted Royal Aluminium for the facade of our 30-story tower. They delivered exceptional quality with proper engineering and QCD compliance. Their technical team knows Qatar regulations inside out. Would definitely work with them again.',
                'testimonial_arabic': 'تعاقدنا مع رويال الألمنيوم لواجهة برجنا المكون من 30 طابقاً. قدموا جودة استثنائية مع هندسة مناسبة والامتثال للدفاع المدني القطري. فريقهم الفني يعرف لوائح قطر من الداخل إلى الخارج. بالتأكيد سنعمل معهم مرة أخرى.',
                'rating': 5,
                'order': 3
            },
            {
                'customer_name': 'Khalid Al-Marri',
                'customer_name_arabic': 'خالد المري',
                'position': 'Villa Owner',
                'position_arabic': 'مالك الفيلا',
                'company': 'Lusail City Villa',
                'company_arabic': 'فيلا مدينة لوسيل',
                'testimonial': 'From consultation to installation, Royal Aluminium exceeded expectations. They helped me choose the right windows for Qatar weather and the result is amazing. My home stays cool even in summer heat. Great value for money!',
                'testimonial_arabic': 'من الاستشارة إلى التركيب، تجاوزت رويال الألمنيوم التوقعات. ساعدوني في اختيار النوافذ المناسبة لطقس قطر والنتيجة مذهلة. منزلي يبقى بارداً حتى في حرارة الصيف. قيمة ممتازة مقابل المال!',
                'rating': 5,
                'order': 4
            },
            {
                'customer_name': 'Jennifer Williams',
                'customer_name_arabic': 'جينيفر ويليامز',
                'position': 'Interior Designer',
                'position_arabic': 'مصممة داخلية',
                'company': 'Doha Design Studio',
                'company_arabic': 'استوديو تصميم الدوحة',
                'testimonial': 'I recommend Royal Aluminium to all my clients. Their sliding door systems are sleek and modern, perfect for contemporary Qatar homes. The black frames with glass look absolutely stunning. Professional service from start to finish.',
                'testimonial_arabic': 'أوصي بـ رويال الألمنيوم لجميع عملائي. أنظمة الأبواب المنزلقة أنيقة وحديثة، مثالية للمنازل القطرية المعاصرة. الإطارات السوداء مع الزجاج تبدو مذهلة تماماً. خدمة احترافية من البداية إلى النهاية.',
                'rating': 5,
                'order': 5
            }
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                customer_name=testimonial_data['customer_name'],
                defaults=testimonial_data
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Testimonial: {testimonial.customer_name} {"created" if created else "updated"}'))

        # Page Content - SEO optimized for all pages
        page_content_data = [
            {
                'page': 'home',
                'title': 'Premium Aluminium & UPVC Windows, Doors & Facades in Qatar',
                'title_arabic': 'نوافذ وأبواب وواجهات الألمنيوم واليو بي في سي المتميزة في قطر',
                'subtitle': 'Leading supplier and installer of energy-efficient aluminium and UPVC solutions in Doha, Qatar. Save up to 40% on AC costs with our certified windows and doors.',
                'subtitle_arabic': 'المورد والمثبت الرائد لحلول الألمنيوم واليو بي في سي الموفرة للطاقة في الدوحة، قطر. وفر حتى 40٪ على تكاليف التكييف مع نوافذنا وأبوابنا المعتمدة.',
                'content': 'Royal Aluminium and UPVC Qatar is your trusted partner for premium aluminium and UPVC solutions across Doha and Qatar. Since 2015, we have specialized in creating energy-efficient, durable, and aesthetically pleasing windows, doors, facades, and architectural solutions that enhance the beauty and functionality of your residential or commercial space. Our products are specifically designed for Qatar\'s extreme climate, offering superior thermal insulation and long-lasting performance.',
                'content_arabic': 'رويال الألمنيوم واليو بي في سي قطر هو شريكك الموثوق لحلول الألمنيوم واليو بي في سي المتميزة في جميع أنحاء الدوحة وقطر. منذ عام 2015، تخصصنا في إنشاء نوافذ وأبواب وواجهات وحلول معمارية موفرة للطاقة ومتينة وجميلة تعزز جمال ووظائف مساحتك السكنية أو التجارية. منتجاتنا مصممة خصيصاً لمناخ قطر القاسي، وتوفر عزل حراري فائق وأداء طويل الأمد.',
                'meta_description': 'Best aluminium and UPVC windows, doors, and facades in Qatar. Energy-efficient solutions for villas, apartments, and commercial buildings. Qatar Civil Defence approved. Free consultation.',
                'meta_description_arabic': 'أفضل نوافذ وأبواب وواجهات الألمنيوم واليو بي في سي في قطر. حلول موفرة للطاقة للفلل والشقق والمباني التجارية. معتمد من الدفاع المدني القطري. استشارة مجانية.'
            },
            {
                'page': 'about',
                'title': 'About Royal Aluminium Qatar - 8+ Years of Excellence',
                'title_arabic': 'عن رويال الألمنيوم قطر - أكثر من 8 سنوات من التميز',
                'subtitle': 'Qatar\'s trusted aluminium and UPVC specialist serving homeowners and businesses since 2015.',
                'subtitle_arabic': 'متخصص الألمنيوم واليو بي في سي الموثوق في قطر يخدم أصحاب المنازل والشركات منذ عام 2015.',
                'content': 'Founded in 2015, Royal Aluminium and UPVC Qatar has grown to become one of the most trusted names in the aluminium and UPVC industry in Qatar. We have successfully completed over 500 projects across Doha, Lusail, Al Rayyan, and other areas of Qatar. Our commitment to quality, customer satisfaction, and technical expertise sets us apart in the market.',
                'content_arabic': 'تأسست رويال الألمنيوم واليو بي في سي قطر في عام 2015، ونمت لتصبح واحدة من أكثر الأسماء الموثوقة في صناعة الألمنيوم واليو بي في سي في قطر. أكملنا بنجاح أكثر من 500 مشروع في الدوحة ولوسيل والريان ومناطق أخرى من قطر. التزامنا بالجودة ورضا العملاء والخبرة الفنية يميزنا في السوق.',
                'meta_description': 'Learn about Royal Aluminium Qatar - leading aluminium and UPVC company with 500+ completed projects. Expert team, QCD certified, serving all of Qatar since 2015.',
                'meta_description_arabic': 'تعرف على رويال الألمنيوم قطر - شركة ألمنيوم ويو بي في سي رائدة مع أكثر من 500 مشروع مكتمل. فريق خبراء، معتمد من الدفاع المدني القطري، يخدم جميع أنحاء قطر منذ عام 2015.'
            },
            {
                'page': 'services',
                'title': 'Aluminium & UPVC Services Qatar - Windows, Doors, Facades',
                'title_arabic': 'خدمات الألمنيوم واليو بي في سي قطر - نوافذ، أبواب، واجهات',
                'subtitle': 'Comprehensive aluminium and UPVC solutions for residential and commercial properties in Qatar.',
                'subtitle_arabic': 'حلول الألمنيوم واليو بي في سي الشاملة للعقارات السكنية والتجارية في قطر.',
                'content': 'We offer a complete range of aluminium and UPVC services including energy-efficient windows, secure doors, modern facades, sliding systems, shower enclosures, and partitions. All our products comply with Qatar Civil Defence regulations and are backed by comprehensive warranties.',
                'content_arabic': 'نقدم مجموعة كاملة من خدمات الألمنيوم واليو بي في سي بما في ذلك النوافذ الموفرة للطاقة والأبواب الآمنة والواجهات الحديثة والأنظمة المنزلقة وحاويات الدش والفواصل. جميع منتجاتنا تتوافق مع لوائح الدفاع المدني القطري ومدعومة بضمانات شاملة.',
                'meta_description': 'Complete aluminium and UPVC services in Qatar: Windows, Doors, Facades, Sliding Systems, Shower Enclosures. QCD approved. Free quotes. Professional installation.',
                'meta_description_arabic': 'خدمات الألمنيوم واليو بي في سي الكاملة في قطر: النوافذ، الأبواب، الواجهات، الأنظمة المنزلقة، حاويات الدش. معتمد من الدفاع المدني القطري. عروض أسعار مجانية. تركيب احترافي.'
            },
            {
                'page': 'portfolio',
                'title': 'Our Projects - Aluminium & UPVC Work in Qatar',
                'title_arabic': 'مشاريعنا - أعمال الألمنيوم واليو بي في سي في قطر',
                'subtitle': 'Browse our completed aluminium and UPVC projects across Doha, Lusail, West Bay, and Qatar.',
                'subtitle_arabic': 'تصفح مشاريعنا المكتملة من الألمنيوم واليو بي في سي في الدوحة ولوسيل والخليج الغربي وقطر.',
                'content': 'Explore our portfolio of successfully completed projects including luxury villas, residential compounds, commercial towers, and office buildings across Qatar. Each project showcases our commitment to quality and customer satisfaction.',
                'content_arabic': 'استكشف محفظتنا من المشاريع المكتملة بنجاح بما في ذلك الفلل الفاخرة والمجمعات السكنية والأبراج التجارية والمباني المكتبية في جميع أنحاء قطر. كل مشروع يعرض التزامنا بالجودة ورضا العملاء.',
                'meta_description': 'View our aluminium and UPVC project portfolio in Qatar. Completed projects in West Bay, Lusail, Pearl Qatar, Al Rayyan. Villas, towers, and commercial buildings.',
                'meta_description_arabic': 'عرض محفظة مشاريع الألمنيوم واليو بي في سي في قطر. مشاريع مكتملة في الخليج الغربي ولوسيل واللؤلؤة قطر والريان. الفلل والأبراج والمباني التجارية.'
            },
            {
                'page': 'contact',
                'title': 'Contact Royal Aluminium Qatar - Get Free Quote',
                'title_arabic': 'اتصل برويال الألمنيوم قطر - احصل على عرض سعر مجاني',
                'subtitle': 'Get in touch for free consultation and quotation. Visit our showroom in Doha or call +974 7790 4281',
                'subtitle_arabic': 'تواصل للحصول على استشارة وعرض سعر مجاني. قم بزيارة معرضنا في الدوحة أو اتصل على +974 7790 4281',
                'content': 'Contact Royal Aluminium and UPVC Qatar today for a free consultation and quotation. Our expert team is ready to help you with your aluminium and UPVC needs. We serve all areas of Qatar including Doha, Lusail, West Bay, Al Rayyan, and Al Wakrah.',
                'content_arabic': 'اتصل برويال الألمنيوم واليو بي في سي قطر اليوم للحصول على استشارة وعرض سعر مجاني. فريق الخبراء لدينا جاهز لمساعدتك في احتياجات الألمنيوم واليو بي في سي الخاصة بك. نخدم جميع مناطق قطر بما في ذلك الدوحة ولوسيل والخليج الغربي والريان والوكرة.',
                'meta_description': 'Contact Royal Aluminium Qatar for free quotation. Phone: +974 7790 4281, WhatsApp: +974 7790 4281. Office in Industrial Area, Doha. Serving all Qatar.',
                'meta_description_arabic': 'اتصل برويال الألمنيوم قطر للحصول على عرض سعر مجاني. الهاتف: +974 7790 4281، واتساب: +974 7790 4281. مكتب في المنطقة الصناعية، الدوحة. نخدم جميع أنحاء قطر.'
            }
        ]

        for content_data in page_content_data:
            content, created = PageContent.objects.get_or_create(
                page=content_data['page'],
                defaults=content_data
            )
            if not created:
                for key, value in content_data.items():
                    setattr(content, key, value)
                content.save()
            self.stdout.write(self.style.SUCCESS(f'✓ Page Content: {content.page} {"created" if created else "updated"}'))

        # Company Statistics
        stats, created = CompanyStatistics.objects.get_or_create(
            defaults={
                'years_in_business': 8,
                'projects_completed': 500,
                'happy_clients': 350,
                'team_members': 15,
                'years_label': 'Years of Excellence',
                'years_label_arabic': 'سنوات من التميز',
                'projects_label': 'Projects Completed',
                'projects_label_arabic': 'مشاريع مكتملة',
                'clients_label': 'Happy Clients',
                'clients_label_arabic': 'عملاء سعداء',
                'team_label': 'Expert Team',
                'team_label_arabic': 'فريق خبراء'
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Company Statistics {"created" if created else "updated"}'))

        # Why Choose Us Items
        why_choose_data = [
            {
                'title': 'Qatar Climate Expertise',
                'title_arabic': 'خبرة مناخ قطر',
                'description': 'Specialized solutions designed for Qatar\'s extreme heat and humidity. Our products reduce AC costs by up to 40%.',
                'description_arabic': 'حلول متخصصة مصممة للحرارة الشديدة والرطوبة في قطر. منتجاتنا تقلل تكاليف التكييف بنسبة تصل إلى 40٪.',
                'icon': 'sun',
                'order': 1
            },
            {
                'title': 'QCD Certified',
                'title_arabic': 'معتمد من الدفاع المدني القطري',
                'description': 'All our installations comply with Qatar Civil Defence regulations and building codes.',
                'description_arabic': 'جميع تركيباتنا تتوافق مع لوائح الدفاع المدني القطري وقوانين البناء.',
                'icon': 'shield',
                'order': 2
            },
            {
                'title': 'European Quality Standards',
                'title_arabic': 'معايير الجودة الأوروبية',
                'description': 'Premium materials from leading European manufacturers with international quality certifications.',
                'description_arabic': 'مواد متميزة من كبار المصنعين الأوروبيين مع شهادات جودة دولية.',
                'icon': 'star',
                'order': 3
            },
            {
                'title': 'Free Consultation & Quote',
                'title_arabic': 'استشارة وعرض سعر مجاني',
                'description': 'Expert consultation at no cost. We visit your site, measure, and provide detailed quotation.',
                'description_arabic': 'استشارة خبراء بدون تكلفة. نزور موقعك، نقيس، ونقدم عرض سعر مفصل.',
                'icon': 'calculator',
                'order': 4
            },
            {
                'title': 'Fast Installation',
                'title_arabic': 'تركيب سريع',
                'description': 'Professional installation teams complete most projects within 2-4 weeks with minimal disruption.',
                'description_arabic': 'فرق التركيب المحترفة تكمل معظم المشاريع في غضون 2-4 أسابيع بأقل قدر من الإزعاج.',
                'icon': 'clock',
                'order': 5
            },
            {
                'title': '2-Year Warranty',
                'title_arabic': 'ضمان لمدة عامين',
                'description': 'Comprehensive warranty on all products and installations. After-sales support included.',
                'description_arabic': 'ضمان شامل على جميع المنتجات والتركيبات. دعم ما بعد البيع متضمن.',
                'icon': 'check-circle',
                'order': 6
            }
        ]

        for item_data in why_choose_data:
            item, created = WhyChooseUsItem.objects.get_or_create(
                title=item_data['title'],
                defaults=item_data
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Why Choose Us: {item.title} {"created" if created else "updated"}'))

        # Certifications
        certifications_data = [
            {
                'name': 'Qatar Civil Defence Approved',
                'name_arabic': 'معتمد من الدفاع المدني القطري',
                'description': 'All our products and installations meet Qatar Civil Defence safety and quality standards.',
                'description_arabic': 'جميع منتجاتنا وتركيباتنا تلبي معايير السلامة والجودة للدفاع المدني القطري.',
                'order': 1
            },
            {
                'name': 'ISO 9001:2015 Certified',
                'name_arabic': 'معتمد ISO 9001:2015',
                'description': 'Quality management system certification ensuring consistent service excellence.',
                'description_arabic': 'شهادة نظام إدارة الجودة التي تضمن التميز المستمر في الخدمة.',
                'order': 2
            },
            {
                'name': 'European Standards',
                'name_arabic': 'المعايير الأوروبية',
                'description': 'Materials and systems from certified European manufacturers (Germany, Italy, UK).',
                'description_arabic': 'مواد وأنظمة من مصنعين أوروبيين معتمدين (ألمانيا، إيطاليا، المملكة المتحدة).',
                'order': 3
            },
            {
                'name': 'Energy Efficiency Certified',
                'name_arabic': 'معتمد لكفاءة الطاقة',
                'description': 'Our windows and doors meet international energy efficiency standards for hot climates.',
                'description_arabic': 'نوافذنا وأبوابنا تلبي المعايير الدولية لكفاءة الطاقة للمناخات الحارة.',
                'order': 4
            }
        ]

        for cert_data in certifications_data:
            cert, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                defaults=cert_data
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Certification: {cert.name} {"created" if created else "updated"}'))

        # Update Company Info with service areas
        if company:
            company.service_areas = 'Doha, Lusail, West Bay, Al Rayyan, Al Wakrah, The Pearl Qatar, Al Khor, Mesaieed'
            company.service_areas_arabic = 'الدوحة، لوسيل، الخليج الغربي، الريان، الوكرة، اللؤلؤة قطر، الخور، مسيعيد'
            company.showroom_address = 'Industrial Area, Street 38, Gate 15, Doha, Qatar'
            company.showroom_address_arabic = 'المنطقة الصناعية، شارع 38، بوابة 15، الدوحة، قطر'
            company.save()
            self.stdout.write(self.style.SUCCESS('✓ Updated Company Info with service areas'))

        # FAQ Section - SEO Optimized
        faq_data = [
            {
                'question': 'What are the best aluminium windows for Qatar climate?',
                'question_arabic': 'ما هي أفضل نوافذ الألمنيوم لمناخ قطر؟',
                'answer': 'The best aluminium windows for Qatar are thermally broken, double-glazed windows with Low-E coating. These windows reduce heat transfer by up to 40%, significantly lowering AC costs in Qatar\'s extreme heat. We recommend powder-coated frames for durability against humidity and salt air. All our windows are QCD certified and designed specifically for Gulf climates.',
                'answer_arabic': 'أفضل نوافذ الألمنيوم لقطر هي النوافذ المكسورة حرارياً ذات الزجاج المزدوج مع طلاء Low-E. هذه النوافذ تقلل نقل الحرارة بنسبة تصل إلى 40٪، مما يقلل بشكل كبير تكاليف التكييف في حرارة قطر الشديدة. نوصي بإطارات مطلية بالمسحوق للمتانة ضد الرطوبة والهواء المالح. جميع نوافذنا معتمدة من الدفاع المدني القطري ومصممة خصيصاً لمناخ الخليج.',
                'category': 'products',
                'order': 1
            },
            {
                'question': 'How much do aluminium windows cost in Qatar?',
                'question_arabic': 'كم تكلفة نوافذ الألمنيوم في قطر؟',
                'answer': 'Aluminium window prices in Qatar vary based on size, type, and specifications. Standard casement windows start from QAR 800-1,200 per square meter. Sliding systems range from QAR 900-1,500 per sqm. Premium thermally broken systems with Low-E glass cost QAR 1,200-2,000 per sqm. Prices include materials, fabrication, and installation. We offer free site visits and detailed quotations for accurate pricing.',
                'answer_arabic': 'تختلف أسعار نوافذ الألمنيوم في قطر بناءً على الحجم والنوع والمواصفات. النوافذ المفتوحة القياسية تبدأ من 800-1,200 ريال قطري لكل متر مربع. أنظمة المنزلقة تتراوح من 900-1,500 ريال قطري لكل متر مربع. أنظمة المكسورة حرارياً المتميزة مع زجاج Low-E تكلف 1,200-2,000 ريال قطري لكل متر مربع. الأسعار تشمل المواد والتصنيع والتركيب. نقدم زيارات موقع مجانية وعروض أسعار مفصلة.',
                'category': 'pricing',
                'order': 2
            },
            {
                'question': 'Are your aluminium and UPVC products QCD approved in Qatar?',
                'question_arabic': 'هل منتجات الألمنيوم واليو بي في سي معتمدة من الدفاع المدني القطري؟',
                'answer': 'Yes, all our aluminium windows, UPVC doors, and facade systems are Qatar Civil Defence (QCD) approved and comply with Qatar Construction Specifications (QCS). We provide QCD certificates for all installations. Our products meet fire safety, structural, and quality standards required for residential and commercial buildings in Qatar.',
                'answer_arabic': 'نعم، جميع نوافذ الألمنيوم وأبواب اليو بي في سي وأنظمة الواجهات معتمدة من الدفاع المدني القطري (QCD) وتتوافق مع مواصفات البناء القطرية (QCS). نقدم شهادات QCD لجميع التركيبات. منتجاتنا تلبي معايير السلامة من الحريق والهيكلية والجودة المطلوبة للمباني السكنية والتجارية في قطر.',
                'category': 'general',
                'order': 3
            },
            {
                'question': 'How long does aluminium window installation take in Qatar?',
                'question_arabic': 'كم من الوقت يستغرق تركيب نوافذ الألمنيوم في قطر؟',
                'answer': 'Aluminium window installation in Qatar typically takes 2-4 weeks from measurement to completion. This includes: 1-2 days for site measurement, 1-2 weeks for fabrication, and 3-7 days for installation depending on project size. For villas, we usually complete within 2 weeks. Large commercial projects may take 3-4 weeks. We provide detailed timelines during quotation.',
                'answer_arabic': 'تركيب نوافذ الألمنيوم في قطر يستغرق عادة 2-4 أسابيع من القياس حتى الإكمال. يشمل ذلك: 1-2 أيام للقياس الموقعي، 1-2 أسابيع للتصنيع، و3-7 أيام للتركيب حسب حجم المشروع. للفلل، نكمل عادة في غضون أسبوعين. المشاريع التجارية الكبيرة قد تستغرق 3-4 أسابيع. نقدم جداول زمنية مفصلة أثناء التسعير.',
                'category': 'installation',
                'order': 4
            },
            {
                'question': 'What warranty do you provide on aluminium windows and UPVC doors?',
                'question_arabic': 'ما الضمان الذي تقدمونه على نوافذ الألمنيوم وأبواب اليو بي في سي؟',
                'answer': 'We provide a comprehensive 2-year warranty on all aluminium windows and UPVC doors in Qatar. This covers manufacturing defects, hardware failures, and installation issues. Powder coating on frames has a 5-year warranty against peeling or fading. Glass units have a 2-year seal warranty. We also offer extended warranty options and lifetime after-sales support.',
                'answer_arabic': 'نقدم ضمان شامل لمدة عامين على جميع نوافذ الألمنيوم وأبواب اليو بي في سي في قطر. يغطي هذا عيوب التصنيع وفشل الأجهزة ومشاكل التركيب. الطلاء بالمسحوق على الإطارات له ضمان 5 سنوات ضد التقشير أو التلاشي. وحدات الزجاج لها ضمان ختم لمدة عامين. نقدم أيضاً خيارات ضمان ممتدة ودعم ما بعد البيع مدى الحياة.',
                'category': 'warranty',
                'order': 5
            },
            {
                'question': 'Do you serve Lusail and West Bay in Qatar?',
                'question_arabic': 'هل تخدمون لوسيل والخليج الغربي في قطر؟',
                'answer': 'Yes, we serve all areas of Qatar including Lusail, West Bay, Doha, Al Rayyan, Al Wakrah, The Pearl Qatar, Al Khor, and Mesaieed. We have completed numerous projects in Lusail City and West Bay luxury villas. Our installation teams are experienced with high-rise towers and residential compounds across Qatar. We provide free site visits throughout Qatar.',
                'answer_arabic': 'نعم، نخدم جميع مناطق قطر بما في ذلك لوسيل والخليج الغربي والدوحة والريان والوكرة واللؤلؤة قطر والخور ومسيعيد. أكملنا العديد من المشاريع في مدينة لوسيل وفلل الخليج الغربي الفاخرة. فرق التركيب لدينا ذات خبرة في الأبراج العالية والمجمعات السكنية في جميع أنحاء قطر. نقدم زيارات موقع مجانية في جميع أنحاء قطر.',
                'category': 'general',
                'order': 6
            },
            {
                'question': 'How much can I save on AC costs with energy-efficient windows?',
                'question_arabic': 'كم يمكنني توفيره على تكاليف التكييف مع النوافذ الموفرة للطاقة؟',
                'answer': 'Energy-efficient aluminium windows in Qatar can reduce AC costs by 30-40%. Our thermally broken windows with Low-E glass significantly reduce heat gain. Typical Qatar villa can save QAR 2,000-4,000 annually on electricity bills. The investment pays back within 3-5 years. Our windows have U-values as low as 1.6 W/m²K, perfect for Qatar\'s climate.',
                'answer_arabic': 'نوافذ الألمنيوم الموفرة للطاقة في قطر يمكن أن تقلل تكاليف التكييف بنسبة 30-40٪. نوافذنا المكسورة حرارياً مع زجاج Low-E تقلل بشكل كبير كسب الحرارة. فيلا قطر النموذجية يمكن أن توفر 2,000-4,000 ريال قطري سنوياً على فواتير الكهرباء. الاستثمار يؤتي ثماره في غضون 3-5 سنوات. نوافذنا لها قيم U منخفضة تصل إلى 1.6 W/m²K، مثالية لمناخ قطر.',
                'category': 'products',
                'order': 7
            },
            {
                'question': 'What is the difference between UPVC and aluminium doors in Qatar?',
                'question_arabic': 'ما الفرق بين أبواب اليو بي في سي والألمنيوم في قطر؟',
                'answer': 'UPVC doors offer better thermal insulation and are more affordable (QAR 1,500-3,000 per door). They require less maintenance and resist Qatar\'s humidity well. Aluminium doors are stronger, slimmer, and better for larger openings (QAR 2,500-5,000). They\'re ideal for commercial use and modern aesthetics. Both are QCD approved. We recommend UPVC for residential main doors and aluminium for sliding patio doors in Qatar.',
                'answer_arabic': 'أبواب اليو بي في سي توفر عزل حراري أفضل وأكثر تكلفة معقولة (1,500-3,000 ريال قطري لكل باب). تتطلب صيانة أقل وتقاوم رطوبة قطر جيداً. أبواب الألمنيوم أقوى وأنحف وأفضل للفتحات الأكبر (2,500-5,000 ريال قطري). إنها مثالية للاستخدام التجاري والجماليات الحديثة. كلاهما معتمد من QCD. نوصي باليو بي في سي للأبواب الرئيسية السكنية والألمنيوم للأبواب المنزلقة للفناء في قطر.',
                'category': 'products',
                'order': 8
            },
            {
                'question': 'Do you provide free quotations and site visits in Qatar?',
                'question_arabic': 'هل تقدمون عروض أسعار وزيارات موقع مجانية في قطر؟',
                'answer': 'Yes, we provide completely FREE quotations and site visits anywhere in Qatar. Our expert team will visit your location in Doha, Lusail, or any Qatar area to take precise measurements and discuss your requirements. We provide detailed quotations within 24-48 hours including material specifications, timeline, and pricing. No obligation. Call +974 7790 4281 or WhatsApp us to schedule.',
                'answer_arabic': 'نعم، نقدم عروض أسعار وزيارات موقع مجانية تماماً في أي مكان في قطر. فريق الخبراء لدينا سيزور موقعك في الدوحة أو لوسيل أو أي منطقة في قطر لأخذ قياسات دقيقة ومناقشة متطلباتك. نقدم عروض أسعار مفصلة في غضون 24-48 ساعة بما في ذلك مواصفات المواد والجدول الزمني والتسعير. بدون التزام. اتصل على +974 7790 4281 أو واتساب لتحديد موعد.',
                'category': 'general',
                'order': 9
            },
            {
                'question': 'Which areas in Qatar do you provide aluminium and UPVC services?',
                'question_arabic': 'ما هي المناطق في قطر التي تقدمون فيها خدمات الألمنيوم واليو بي في سي؟',
                'answer': 'We provide aluminium windows and UPVC door services throughout Qatar including: Doha (all districts), Lusail City, West Bay, The Pearl Qatar, Al Rayyan, Al Wakrah, Al Khor, Mesaieed, and surrounding areas. We have completed 500+ projects across Qatar with installation teams ready to serve any location. Contact us for service in your area.',
                'answer_arabic': 'نقدم خدمات نوافذ الألمنيوم وأبواب اليو بي في سي في جميع أنحاء قطر بما في ذلك: الدوحة (جميع المناطق)، مدينة لوسيل، الخليج الغربي، اللؤلؤة قطر، الريان، الوكرة، الخور، مسيعيد، والمناطق المحيطة. أكملنا أكثر من 500 مشروع في جميع أنحاء قطر مع فرق تركيب جاهزة لخدمة أي موقع. اتصل بنا للحصول على الخدمة في منطقتك.',
                'category': 'general',
                'order': 10
            }
        ]

        for faq_item in faq_data:
            faq, created = FAQ.objects.get_or_create(
                question=faq_item['question'],
                defaults=faq_item
            )
            self.stdout.write(self.style.SUCCESS(f'✓ FAQ: {faq.question[:50]}... {"created" if created else "updated"}'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('✓ Successfully populated database with SEO-friendly data!'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(self.style.WARNING('\nSummary:'))
        self.stdout.write(f'  • Company Info: 1')
        self.stdout.write(f'  • Services: {Service.objects.count()}')
        self.stdout.write(f'  • Projects: {Project.objects.count()}')
        self.stdout.write(f'  • Team Members: {TeamMember.objects.count()}')
        self.stdout.write(f'  • Testimonials: {Testimonial.objects.count()}')
        self.stdout.write(f'  • Page Contents: {PageContent.objects.count()}')
        self.stdout.write(f'  • Statistics: {CompanyStatistics.objects.count()}')
        self.stdout.write(f'  • Why Choose Us: {WhyChooseUsItem.objects.count()}')
        self.stdout.write(f'  • Certifications: {Certification.objects.count()}')
        self.stdout.write(f'  • FAQs: {FAQ.objects.count()}')
