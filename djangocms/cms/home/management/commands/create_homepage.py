from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import HomePage
from articles.models import ArticlePage
from django.utils import timezone
from wagtail.images import get_image_model

class Command(BaseCommand):
    help = 'Create a default homepage and articles if they do not exist'

    def handle(self, *args, **options):
        root_page = Page.objects.get(pk=1)
        homepage = HomePage.objects.first()

        if not homepage:
            homepage = HomePage(
                title="Home",
                body=[{'type': 'paragraph', 'value': 'Welcome to our site'}]
            )
            root_page.add_child(instance=homepage)
            homepage.save_revision().publish()
            self.stdout.write(self.style.SUCCESS('Successfully created homepage'))
        else:
            self.stdout.write(self.style.WARNING('Homepage already exists'))

        if not ArticlePage.objects.exists():
            articles = [
                {
                    "title": "The Power of Docker in Modern Development",
                    "custom_title": "Docker: Revolutionizing Development",
                    "slug": "docker-power",
                    "date": timezone.now().date(),
                    "intro": "Learn how Docker has transformed development processes.",
                    "body": "<p>Docker has become essential in modern software development, providing lightweight and portable environments. It allows developers to work consistently across multiple machines and setups, improving collaboration and productivity. From microservices to continuous integration, Docker's versatility is unparalleled.</p><p>For more on Docker, visit <a href='https://www.docker.com'>Docker's official site</a>.</p>",
                    "featured_image": self.get_image('docker.webp')
                },
                {
                    "title": "Implementing CI/CD with GitHub Actions",
                    "custom_title": "GitHub Actions: Streamlining CI/CD",
                    "slug": "github-actions-cicd",
                    "date": timezone.now().date(),
                    "intro": "Explore how GitHub Actions facilitates continuous integration and deployment.",
                    "body": "<p>GitHub Actions offers a robust platform for automating CI/CD pipelines directly within your GitHub repositories. With customizable workflows, developers can automate tests, builds, and deployments, enhancing the efficiency of their development cycle. This tool not only supports multiple languages and platforms but also integrates seamlessly with other services.</p><p>Read more about <a href='https://docs.github.com/en/actions'>GitHub Actions</a>.</p>",
                    "featured_image": self.get_image('github-actions.png')
                },
                {
                    "title": "Building Scalable Web Applications with Django",
                    "custom_title": "Django: A Framework for Perfectionists",
                    "slug": "django-web-applications",
                    "date": timezone.now().date(),
                    "intro": "Django is the go-to framework for scalable web applications.",
                    "body": "<p>Django, known for its 'batteries-included' philosophy, simplifies the development of complex, database-driven websites. It emphasizes reusability, rapid development, and the principle of DRY (Don't Repeat Yourself). With a strong community and extensive documentation, Django is perfect for both newcomers and seasoned developers.</p><p>Discover more on <a href='https://www.djangoproject.com'>Django's official site</a>.</p>",
                    "featured_image": self.get_image('django.webp')
                },
                {
                    "title": "The Importance of DevOps in Software Development",
                    "custom_title": "DevOps: Bridging Development and Operations",
                    "slug": "devops-importance",
                    "date": timezone.now().date(),
                    "intro": "DevOps practices enhance collaboration between development and operations.",
                    "body": "<p>DevOps is more than just a buzzword; it's a culture that fosters collaboration between developers and IT operations. By implementing DevOps practices, organizations can deploy software more frequently, with fewer failures and faster recovery times. The integration of tools and processes accelerates development and deployment cycles.</p><p>Learn more about <a href='https://www.devops.com'>DevOps</a>.</p>",
                    "featured_image": self.get_image('github.png')
                },
                {
                    "title": "Container Orchestration with Kubernetes",
                    "custom_title": "Kubernetes: Orchestrating Containers at Scale",
                    "slug": "kubernetes-orchestration",
                    "date": timezone.now().date(),
                    "intro": "Kubernetes automates deployment, scaling, and management of containerized applications.",
                    "body": "<p>Kubernetes, often referred to as K8s, is a powerful system for managing containerized applications across a cluster of machines. It automates deployment, scaling, and operations of application containers. As organizations move towards microservices, Kubernetes provides the necessary infrastructure to scale and manage these services efficiently.</p><p>Find out more at <a href='https://kubernetes.io'>Kubernetes' official site</a>.</p>",
                    "featured_image": self.get_image('kubernetes.png')
                },
            ]

            for article_data in articles:
                article = ArticlePage(
                    title=article_data["title"],
                    custom_title=article_data["custom_title"],
                    slug=article_data["slug"],
                    date=article_data["date"],
                    intro=article_data["intro"],
                    body=article_data["body"],
                    live=True,
                    first_published_at=timezone.now(),
                    featured_image=article_data["featured_image"]
                )
                homepage.add_child(instance=article)
                article.save_revision().publish()
                
            self.stdout.write(self.style.SUCCESS('Successfully created articles under the homepage'))
        else:
            self.stdout.write(self.style.WARNING('Articles already exist'))

    def get_image(self, filename):
        Image = get_image_model()
        image, created = Image.objects.get_or_create(
            title=filename,
            defaults={'file': f'original_images/{filename}'}
        )
        return image if created else None
