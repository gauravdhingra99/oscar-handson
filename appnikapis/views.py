from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import *
from oscar.apps.address.models import *  # noqa isort:skip

# Create your views here.

class ProfileView(APIView):
	def get(self,request):
		userid=request.query_params.get("id",None)
		if userid:
			userobj=UserAddress.objects.filter(pk=userid)
			if userobj.exists():
				data=UserAddress.objects.filter(pk=userid).values("first_name","last_name","phone_number","line1","line2","postcode","state",)
				return Response({"data":data},status=200)
			else:
				return Response({"error":"User with that id does not exists"},status=400)
		else:
			data=UserAddress.objects.all().values("first_name","last_name","phone_number","line1","line2","postcode","state",)
			print(type(data))
			return Response({"data":data},status=200)

	def put(self,request,format=None):
		pk=request.query_params.get("id",None)
		phone_number=request.data.get("phone_number")
		name=request.data.get("name")
		print(name,phone_number)
		uaddress= UserAddress.objects.filter(pk=pk)
		if not uaddress.exists():
			return Response({"error":"User with that id does not exists"},status=400)
		if phone_number:
			UserAddress.objects.filter(pk=pk).update(phone_number=phone_number)
		if name:
			UserAddress.objects.filter(pk=pk).update(first_name=name)
		data=UserAddress.objects.filter(pk=pk).values()
		return Response({"data":data},status=200)






# "{
# ""full_name"": ""First Last Name"",
# ""phone_number"": ""+919876543210"",
# ""email"": ""test@test.com"",
# ""store_name"": ""ABC Store"",
# ""address_line1"": ""addreess line 1"",
# ""address_line2"": ""addreess line 2"",
# ""pin_code"": ""560102"",
# ""district"": ""Bengaluru"",
# ""state"": ""Karnataka"",
# ""pan_number"": ""DAZER9876S"",
# ""gst_number"": ""xvx1ewcs12""
# }"






