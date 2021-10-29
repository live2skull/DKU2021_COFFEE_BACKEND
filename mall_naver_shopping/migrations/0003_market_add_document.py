# Generated by Django 3.2.8 on 2021-10-29 04:36
from random import randrange

from django.db import migrations

from mall_naver_shopping.models import Product
from market.models import Product as MallProduct

names = [
    '위더스 데코선반 335',
    '이고진 멀티 홈짐 EX006A 레그프레스 68kg 블럭포함',
    '이고진 좌식 실내자전거 704R 온가족 헬스자전거',
    '보솜이 베이비케어(푸에디션) 물티슈 캡형 74매 x 10팩',
    '[동원] 인기구성 개성 만두 6종 x 4봉 골라담기 (왕교자 / 왕새우 / 주꾸미 / 얇은피고기 / 얇은피김치 / 물만두 택1) [브랜드DAY]',
    '30% [벤튼] 스네일비 하이콘텐트 에센스 60m (~8.29)',
    '30% [벤튼] 알로에 바하 스킨토너 200ml (~8.29)',
    '이고진 워킹머신 6200 가정용 워킹패드 런닝머신'
    '이고진 스텝퍼 트위스트 7120 계단오르기 스탭퍼 스테퍼 유산소 가정용 운동 기구 헬스',
    '신박한 정리 PVC 튼튼한 논슬립 슬림 니트 코트 정장 양복 세탁소 옷가게 옷걸이 20P',
    '신박한 정리 논슬립 고급 스텐 집게 정장 청 바지걸이 행거 세트 외 바지 옷걸이',
    '고급의류용 중성세제 울터치 프리미엄 1.3Lx3개',
    '소프시스 파체어 PP',
]
display_image = "https://picsum.photos/200/300"


def generate_product(apps, schema_editor):
    for product in MallProduct.objects.all():
        Product.objects.create(
            name=f'네이버상품정보_{product.name}', display_image=display_image,
            product_id=randrange(1, 100000),
            original_product_extension=product.extended_info
        )


class Migration(migrations.Migration):

    initial = True
    dependencies = [
        ('mall_naver_shopping', '0002_product_display_image'),
        ('market', '0004_market_add_document')
    ]
    operations = [
        migrations.RunPython(generate_product, reverse_code=migrations.RunPython.noop)
    ]
