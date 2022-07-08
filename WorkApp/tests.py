from django.test import TestCase
from WorkApp.views import MainPage
from WorkApp.models import Personal

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		resp=self.client.get('/')
		self.assertTemplateUsed(resp,'mainpage.html')

	def test_save_POST_request(self):
		resp = self.client.post('/', data={'FullName':'FullName_v',
			'Email':'Email_v','PhoneNumber':'PhoneNumber_v','Gender':'Gender_v','Age':'Age_v'})

		self.assertEqual(Personal.objects.count(),1)
		newPersonal = Personal.objects.first()
		self.assertEqual(newPersonal.Aname,'FullName_v')

	def test_redirecting_post(self):
		resp = self.client.post('/', data={'FullName':'FullName_v',
			'Email':'Email_v','PhoneNumber':'PhoneNumber_v','Gender':'Gender_v','Age':'Age_v'})
		self.assertEqual(resp.status_code, 302)
		self.assertEqual(resp['location'],'/')

	def test_save_request(self):
		self.client.get('/')
		self.assertEqual(Personal.objects.count(),0)

class ORMTest(TestCase):
	def test_saving_list(self):
		Personal1 = Personal()
		Personal1.Aname = 'JohnCarlo'
		Personal1.Aemail = 'johncarlo@rocketmail.com'
		Personal1.Aphonenumber = '14356782804'
		Personal1.Agender = 'Male'
		Personal1.Aage = '23'
		Personal1.save()
		Personal2 = Personal()
		Personal2.Aname = 'LucasMarcus'
		Personal2.Aemail = 'marcusl@hotmail.com'
		Personal2.Aphonenumber = '19860452390'
		Personal2.Agender = 'Male'
		Personal2.Aage = '28'
		Personal2.save()
		pers = Personal.objects.all()
		self.assertEqual(pers.count(),2)
		Personal1 = pers[0]
		Personal2 = pers[1]
		self.assertEqual(Personal1.Aname, 'JohnCarlo')
		self.assertEqual(Personal2.Aname, 'LucasMarcus')

	def test_template_create(self):
		Personal.objects.create(Aname='App1')
		Personal.objects.create(Aname='App2')
		response = self.client.get('/')
		self.assertIn('App1', response.content.decode())
		self.assertIn('App2', response.content.decode())
	
	"""def test_responding_post_request(self):
					resp = self.client.post('/', data={'inpDets' :'FullName'})
					self.assertIn('FullName', resp.content.decode())
					self.assertTemplateUsed(resp, 'mainpage.html')
					
					resp = self.client.post('/', data={'inpDets1' :'Email'})
					self.assertIn('Email', resp.content.decode())
					self.assertTemplateUsed(resp, 'mainpage.html')
					
					resp = self.client.post('/', data={'inpDets2' :'PhoneNumber'})
					self.assertIn('PhoneNumber', resp.content.decode())
					self.assertTemplateUsed(resp, 'mainpage.html')
					
					resp = self.client.post('/', data={'inpDets3' :'Gender'})
					self.assertIn('Gender', resp.content.decode())
					self.assertTemplateUsed(resp, 'mainpage.html')
			
					resp = self.client.post('/', data={'inpDets4' :'Age'})
					self.assertIn('Age', resp.content.decode())
					self.assertTemplateUsed(resp, 'mainpage.html')"""

