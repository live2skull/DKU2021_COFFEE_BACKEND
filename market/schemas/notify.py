from typing import List

from drf_yasg import openapi
from drf_yasg.openapi import Schema, Parameter

from utils.schema_utils import build_list_object_schema


SET_NOTIFY_PRODUCT_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'product_id': openapi.Schema(type=openapi.TYPE_NUMBER)
    }
)

READ_NOTIFY_PRODUCT_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'notification_id': openapi.Schema(type=openapi.TYPE_NUMBER)
    }
)


GET_NOTIFY_RESPONSE_BODY = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림설정 고유아이디'),
            'product_id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림 지정 제품아이디'),
            'created_at': openapi.Schema(type=openapi.FORMAT_DATE, description="생성 시각")
        }
    )
)

GENERIC_RESULT_RESPONSE_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'result': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'error_message': openapi.Schema(
            type=['null', openapi.TYPE_STRING],
            description='요청 실패시 해당 오류 메시지를 반환합니다'
        )
    }
)

GET_NOTIFY_PRODUCT_RESPONSE_BODY = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림 고유아이디, 알림 읽음처리 시 사용'),
            'product_id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림이 발생한 상품의 고유아이디'),
            'mall_name': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='해당 고유 상품에서의 알림이 발생한 쇼핑몰 이름 (naver_shopping_products, auction_products) 등 위 API 참조 소스'
            ),
            'created_at': openapi.Schema(type=openapi.FORMAT_DATE, description="생성 시각")
        }
    )
)

