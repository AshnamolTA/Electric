from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save






# Create your models here.


class BaseModel(models.Model):

    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


class UserProfile(BaseModel):

    bio=models.CharField(max_length=200,null=True)

    profile_picture=models.ImageField(upload_to="profile_picture",null=True,blank=True,default="profile_picture/default.png")

    phone=models.CharField(max_length=200,null=True)

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")


    def __str__(self):

        return self.owner.username


class Category(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Brand(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Shape(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Material(BaseModel):

    light_material=models.CharField(max_length=200)

    def __str__(self):
        return self.light_material


class LightBodyColour(BaseModel):

    bodycolour=models.CharField(max_length=200)

    def __str__(self):
        return self.bodycolour



class LightColour(BaseModel):

    colour=models.CharField(max_length=200)

    def __str__(self):
        return self.colour


class Wates(BaseModel):

    light_wates=models.CharField(max_length=200)

    def __str__(self):
        return self.light_wates






class Light(BaseModel):

    name=models.CharField(max_length=200)

    description=models.TextField()

    preview_image=models.ImageField(upload_to="previewimage",null=True,blank=True,default="preview_image/image.png"
                                    )

    price=models.PositiveIntegerField()

    category_object = models.ForeignKey(Category, on_delete=models.CASCADE)

    body_object=models.ManyToManyField(LightBodyColour)

    colour_object=models.ManyToManyField(LightColour)

    shape_object=models.ManyToManyField(Shape)

    material_object=models.ForeignKey(Material,on_delete=models.CASCADE)

    wates_object=models.ForeignKey(Wates,on_delete=models.CASCADE)

    distributer=models.ForeignKey(User,on_delete=models.CASCADE)

    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)





class WishList(BaseModel):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="basket")

    def __str__(self):

        return self.owner.username


class WishListItem(BaseModel):

    wishlist_object=models.ForeignKey(WishList,on_delete=models.CASCADE,related_name="basket_item")

    light_object=models.ForeignKey(Light,on_delete=models.CASCADE)

    body_object=models.ForeignKey(LightBodyColour,on_delete=models.CASCADE)

    colour_object=models.ForeignKey(LightColour,on_delete=models.CASCADE)

    shape_object=models.ForeignKey(Shape,on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    is_order_placed=models.BooleanField(default=False)

   


class Order(BaseModel):

    wishlistitem_objects=models.ManyToManyField(WishListItem)

    user_object = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myorders')

    delivery_address = models.CharField(max_length=250)

    phone = models.CharField(max_length=12)

    email = models.CharField(max_length=100)

    pay_options = (
        ('online', 'online'),
        ('cod', 'cod')
    )

    payment_mode = models.CharField(max_length=100, choices=pay_options, default='cod')

    order_id = models.CharField(max_length=200, null=True)

    is_paid = models.BooleanField(default=False)

    order_status = (
        ('order_confirmed', 'Order confirmed'),
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),

    )

    status = models.CharField(max_length=200, choices=order_status, default='order_confirmed')




#django.db.models.signals---post_save,pre_save,post_init


def create_user_profile(sender,instance,created,**kwargs):

    if created:

        UserProfile.objects.create(owner=instance)

post_save.connect(create_user_profile,User)


def create_wishlist(sender,instance,created,**kwargs):

    if created:

        WishList.objects.create(owner=instance)

post_save.connect(create_wishlist,sender=User)
