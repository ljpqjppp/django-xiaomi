from django.test import TestCase

# Create your tests here.
a = 'http://127.0.0.1:8001/index1/3'
b = a.split('/',-1)[-1]
print(b)