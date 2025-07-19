from rest_framework import serializers


from store.models import Category, Product, Gallery,Specification, Size, Color, Cart, CartOrder, CartOrderItem, ProductFaq, Review, Wishlist, Notification, Coupon
from vendor.models import Vendor

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


# Define a serializer for the Gallery model
class GallerySerializer(serializers.ModelSerializer):
    # Serialize the related Product model

    class Meta:
        model = Gallery
        fields = '__all__'



# Define a serializer for the Specification model
class SpecificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specification
        fields = '__all__'


# Define a serializer for the Size model
class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'

# Define a serializer for the Color model
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'



################# PRODUCT ##################################
class ProductSerializer(serializers.ModelSerializer):
    # many images so True
    gallerys = GallerySerializer(many=True, read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    specification = SpecificationSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "image",
            "description",
            "category",
            "price",
            "old_price",
            "shipping_amount",
            "stock_qty",
            "in_stock",
            "status",
            "featured",
            "views",
            "rating",
            "vendor",
            "date",
            'product_rating',
            'rating_count',
            "gallerys",
            "specification",
            "size",
            "color",
        ]
        
    # we use this for depth like category is has own model.
    # so with this we can get all fields about Category like cat-titile, cat-image etc...
    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3

# Define a serializer for the CartOrderItem model
class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartSerializer, self).__init__(*args, **kwargs)

            request = self.context.get("request")
            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3
    

# Define a serializer for the CartOrder model
class CartOrderSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartOrder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CartOrderSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3


# Define a serializer for the CartOrder model
class CartOrderItemSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartOrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CartOrderItemSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3



# Define a serializer for the CartOrder model
class ProductFaqSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = ProductFaq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductFaqSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3


# Define a serializer for the CartOrder model
class VendorSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3





# Define a serializer for the CartOrder model
class ReviewSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReviewSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3



# Define a serializer for the CartOrder model
class WishlistSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WishlistSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3



# Define a serializer for the CartOrder model
class CouponSerializer(serializers.ModelSerializer):
    # Serialize related CartOrderItem models
    # orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CouponSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new cart order, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NotificationSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'POST':
            # When creating a new coupon user, set serialization depth to 0.
            self.Meta.depth = 0
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 3