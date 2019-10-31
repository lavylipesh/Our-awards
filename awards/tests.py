from django.test import TestCase
from .models import Profile

class ProfileTestClass(Testcase):
    self.lilibeth = Profile(user = 'Lilibeth', bio ='I love being myself')

    def test_instance(self):
    self.assertTrue(isinstance(self.lilibeth,Profile))

    def test_save_method(self):
    self.lilibeth.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)
    
    def test_delete_method(self):
    self.lilibeth.delete_profile()

class ProjectTestClass(TestCase):
    def test_instance(self):
    self.assertTrue(isinstance(self.Intsgram,Project))
    
    def test_create_method(self):
    self.project.create_project()

    def test_save_method(self):
    self.Instagram.save_project()
    projects = Projects.objects.all()
    self.assertTrue(len(projects>0))

    def test_delete_method(self)
    self.intagram.delete_project()


 
