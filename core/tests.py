from django.test import TestCase
from .views import ARTICLES

class BlogViewsTests(TestCase):
	def setUp(self):
		self.article = ARTICLES[0]

	def test_blog_page_displays_articles(self):
		response = self.client.get('/blog/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Mes Articles')
		self.assertContains(response, self.article.titre)

	def test_blog_detail_page_displays_article(self):
		response = self.client.get(f'/blog/{self.article.slug}/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.article.titre)

	def test_unknown_article_returns_404(self):
		response = self.client.get('/blog/article-inexistant/')

		self.assertEqual(response.status_code, 404)
