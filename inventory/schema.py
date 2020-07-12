import graphene
from graphene import Argument
from graphene_django.types import DjangoObjectType
from inventory.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(object):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.ID())

    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.ID())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
    
    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)
    
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_category(self, info, id):
        return Category.objects.get(pk=id)


class CreateProduct(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        price = graphene.Float()
        category = graphene.List(graphene.ID)
        in_stock = graphene.Boolean()
        date_created = graphene.types.datetime.DateTime()
    
    product = graphene.Field(ProductType)

    def mutate(self, info, name, price=None, category=None, in_stock=True, date_created=None):
        product = Product.objects.create(
            name=name,
            price=price,
            in_stock=in_stock,
            date_created=date_created
        )

        if category is not None:
            category_set = []
            for category_id in category:
                category_object = Category.objects.get(pk=category_id)
                category_set.append(category_object)
            product.category.set(category_set)
        
        product.save()
        return CreateProduct(
            product=product
        )


class UpdateProduct(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        price = graphene.Float()
        category = graphene.List(graphene.ID)
        in_stock = graphene.Boolean()
        date_created = graphene.types.datetime.DateTime()
    
    product = graphene.Field(ProductType)
