from rest_framework.views import APIView
from rest_framework.response import Response
from db.models.user_model import User
from rest_framework import status 
from rest_framework.generics import get_object_or_404


class Verify_otp_API(APIView):

    def post(self,request):
        #putting your request.data which is a dictionary in the serializer 
        otp_code = request.data.get("otp_code")
        
            # getting and instance of the user using the generated unique otp_code
            # or returning a status code "404"
        user = get_object_or_404(User, otp_code=otp_code)
        user.email_verified = True
        user.save()
        return Response({'msg':'User has been verified successfully'}, status=status.HTTP_202_ACCEPTED)

                