from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ctrl.paggination import CustomIndexPagination
from page.home.models import Blog, Testimonial, Clients
from .serializers import *
from page.home.serializers import (BlogSerializer,
                                   TestimonialSerializer,
                                   ClientsSerializer,)


# Create your views here.
class DeviceView(generics.ListAPIView):

    pagination_class = CustomIndexPagination

    def get(self, request, slug=None, pk=None, *args, **kwargs):
        product = Product.objects.all()
        prod_img = ProductFooterImages.objects.all()
        testimonial = Testimonial.objects.all()
        clients = Clients.objects.all()
        blog = Blog.objects.all()

        product_page = self.paginate_queryset(product)
        prod_img_page = self.paginate_queryset(prod_img)
        test_page = self.paginate_queryset(testimonial)
        clients_page = self.paginate_queryset(clients)
        blog_page = self.paginate_queryset(blog)

        serializer1 = ProductSerializer(
            product_page, context={'request': request}, many=True
        )
        serializer1_images = ProductImageSerializer(
            prod_img_page, context={'request': request}, many=True
        )
        main_images = PaSerializer(
            prod_img_page, context={'request': request}, many=True
        )

        serializer2 = TestimonialSerializer(
            test_page, context={'request': request}, many=True
        )
        serializer3 = ClientsSerializer(
            clients_page, context={"request": request}, many=True
        )
        serializer4 = BlogSerializer(
            blog_page, context={'request': request}, many=True
        )
        ls = []
        for i in main_images.data:
            for j in i.values():
                ls.append(j)

        for z, k in zip(serializer1.data, ls):
            z['img'] = k

        custom_data = {
            "devices": {
                "product": serializer1.data,
                "testimonial": serializer2.data,
                "clients": serializer3.data,
                "blog": serializer4.data
            }
        }
        a = serializer1_images.data.copy()
        for dicts in a:
            if None in dicts.values():
                pass

        image_data = {
            "device": {
                "product": a
            }
        }

        len_image_data = 0
        for i in serializer1_images.data:
            len_image_data += 1

        if slug == "custom_data" and pk is None:
            return Response(
                custom_data, status=status.HTTP_200_OK
            )

        elif slug == "images" and pk is None:

            return Response(
                image_data, status=status.HTTP_200_OK
            )

        elif slug == "images" and 1 <= pk <= len_image_data:
            filtered_data = []
            for dicts in serializer1_images.data:
                if dicts['id'] == pk:
                    filtered_data.append(dicts)
                    break

            filtered_image_data = {
                    "device": {
                        "images": filtered_data,
                    }
                }

            return Response(
                filtered_image_data, status=status.HTTP_200_OK
            )

        # elif slug == "images" and pk <= 3:
        #     key = f"footer_img{pk}"
        #     filtered_data = []
        #
        #     for dicts in serializer1_images.data:
        #         filtered_dict = {key: dicts[key]}
        #         filtered_data.append(filtered_dict)
        #
        #     filtered_image_data = {
        #         "device": {
        #             "images": filtered_data
        #         }
        #     }
        #     return Response(filtered_image_data,
        #                     status=status.HTTP_200_OK)

        else:
            return Response("Out of Range",
                            status=status.HTTP_400_BAD_REQUEST)
