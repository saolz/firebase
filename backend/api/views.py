from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import json
import razorpay
from django.conf import settings

@api_view(['POST'])
def register_user(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        # Check if user exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=400)

        # Create new user
        hashed_password = make_password(password)
        user = User.objects.create(
            email=email,
            password=hashed_password,
            name=name
        )

        return Response({
            'message': 'User registered successfully',
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name
            }
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def login_user(request):
    try:
        data = request.data
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            # Direct password comparison since we're not using hashing
            if password == user.password:
                return Response({
                    'message': 'Login successful',
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'name': user.name
                    }
                })
            else:
                return Response({'error': 'Invalid password'}, status=401)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
            
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def create_order(request):
    try:
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        
        payment_data = {
            "amount": 50000,  # amount in paise (500 INR)
            "currency": "INR",
            "receipt": "order_rcptid_11"
        }
        
        order = client.order.create(data=payment_data)
        return Response({
            'id': order['id'],
            'amount': order['amount'],
            'currency': order['currency']
        })
    except Exception as e:
        print("Error:", str(e))
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def signup_user(request):
    try:
        data = request.data
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        # Check if user exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=400)

        # Create new user
        user = User.objects.create(
            email=email,
            password=password,  # Plain password
            name=name
        )

        return Response({
            'message': 'User registered successfully',
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name
            }
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)
