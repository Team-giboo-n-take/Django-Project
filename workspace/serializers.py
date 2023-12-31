from django.conf import settings
from django.db.models import Sum, Count
from rest_framework import serializers

from customer_center.models import Inquery, Alarm
from member.models import Member

from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangReply, ReplyLike

from neulhaerang.models import Neulhaerang, NeulhaerangDonation
from neulhaerang_review.models import NeulhaerangReview, NeulhaerangReviewReply, ReviewReplyLike
from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, AuthenticationFeedLike
from notice.models import Notice


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class NeulhaerangSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    donation_amount_sum = serializers.SerializerMethodField(method_name='get_donation_amount_sum',read_only=True)

    def get_donation_amount_sum(self, neulhaerang):
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang).aggregate(Sum('donation_amount'))
        return amount_sum['donation_amount__sum']

    class Meta:
        model = Neulhaerang
        fields = '__all__'

class NeulhaerangDonationSerializer(serializers.ModelSerializer):
    neulhaerang_title = serializers.CharField(source='neulhaerang.neulhaerang_title',read_only=True)
    class Meta:
        model = NeulhaerangDonation
        fields = '__all__'


class NeulhaerangReplySerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    reply_member_thumbnail = serializers.CharField(source='member.profile_image', read_only=True)
    donation_amount = serializers.IntegerField(source='donation.donation_amount', read_only=True)
    check_anonymous = serializers.CharField(source='donation.donation_anonymous', read_only=True)
    member_profile_choice = serializers.CharField(source='member.profile_image_choice', read_only=True)
    member_kakao_profile = serializers.CharField(source='member.kakao_profile_image', read_only=True)
    reply_like_count = serializers.SerializerMethodField(method_name='get_reply_like_count',read_only=True)
    check_my_comment = serializers.SerializerMethodField(method_name='check_is_my_comment', read_only=True)
    my_like = serializers.SerializerMethodField(method_name='check_my_like', read_only=True)
    best_reply = serializers.BooleanField(read_only=True)
    def get_reply_like_count(self, neulhaerang_reply):
        reply_count = ReplyLike.objects.filter(neulhaerang_reply=neulhaerang_reply).aggregate(Count('id'))
        return reply_count['id__count']
    def check_is_my_comment(self, neulhaerang_reply):
        request = self.context.get('request')
        my_email = request.session.get('member_email', None)
        if (neulhaerang_reply.member.member_email == my_email):
            return True
        return False
    def check_my_like(self, neulhaerang_reply):
        request = self.context.get('request')
        my_email = request.session.get('member_email', None)
        my_reply_like = ReplyLike.objects.filter(member__member_email=my_email, neulhaerang_reply=neulhaerang_reply)
        if (my_reply_like):
            return True
        return False

    class Meta:
        model = NeulhaerangReply
        fields = '__all__'


class NeulhaerangReviewSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='neulhaerang.member.member_nickname', read_only=True)
    donation_amount_sum = serializers.SerializerMethodField(method_name='get_donation_amount_sum',read_only=True)
    target_amount = serializers.IntegerField(source='neulhaerang.target_amount',read_only=True)
    def get_donation_amount_sum(self, neulhaerangreview):
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerangreview.neulhaerang_id).aggregate(Sum('donation_amount'))
        return amount_sum['donation_amount__sum']

    class Meta:
        model = NeulhaerangReview
        fields = '__all__'

class NeulhaerangReviewReplySerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    reply_member_thumbnail = serializers.CharField(source='member.profile_image', read_only=True)
    member_profile_choice = serializers.CharField(source='member.profile_image_choice', read_only=True)
    reply_like_count = serializers.SerializerMethodField(method_name='get_reply_like_count', read_only=True)
    check_my_comment = serializers.SerializerMethodField(method_name='check_is_my_comment', read_only=True)
    my_like = serializers.SerializerMethodField(method_name='check_my_like', read_only=True)
    best_reply = serializers.BooleanField(read_only=True)

    def get_reply_like_count(self, neulhaerang_review_reply):
        reply_count = ReviewReplyLike.objects.filter(review_reply=neulhaerang_review_reply).aggregate(Count('id'))
        return reply_count['id__count']

    def check_is_my_comment(self, neulhaerang_review_reply):
        request = self.context.get('request')
        my_email = request.session.get('member_email', None)
        if (neulhaerang_review_reply.member.member_email == my_email):
            return True
        return False

    def check_my_like(self, neulhaerang_review_reply):
        request = self.context.get('request')
        my_email = request.session.get('member_email', None)
        my_reply_like = ReviewReplyLike.objects.filter(member__member_email=my_email, review_reply=neulhaerang_review_reply)
        if (my_reply_like):
            return True
        return False

    class Meta:
        model = NeulhaerangReviewReply
        fields = '__all__'

class NeulhajangSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    member_profile_image = serializers.CharField(source='member.profile_image', read_only=True)
    member_profile_choice = serializers.CharField(source='member.profile_image_choice', read_only=True)
    member_kakao_image = serializers.CharField(source='member.kakao_profile_image', read_only=True)
    authentication_count = serializers.SerializerMethodField(method_name='get_authentication_feed_sum',read_only=True)
    def get_authentication_feed_sum(self, neulhajang):
        authentication_feed_count = NeulhajangAuthenticationFeed.objects.filter(neulhajang=neulhajang.id).aggregate(Count('id'))
        return format(authentication_feed_count['id__count'],",")

    class Meta:
        model = Neulhajang
        fields = '__all__'

class AuthenticationFeedSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    feed_like_count = serializers.SerializerMethodField(method_name='action_feed_like_count',read_only=True)
    my_like = serializers.SerializerMethodField(method_name='check_my_like',read_only=True)
    image_url = serializers.SerializerMethodField()
    def action_feed_like_count(self, authenticationfeed):
        authentication_feed_like_count = AuthenticationFeedLike.objects.filter(authentication_feed=authenticationfeed).aggregate(Count('id'))
        return format(authentication_feed_like_count['id__count'],",")
    def check_my_like(self, authenticationfeed):
        request = self.context.get('request')
        my_email = request.session.get('member_email', None)
        my_feed_like = AuthenticationFeedLike.objects.filter(member__member_email=my_email, authentication_feed=authenticationfeed)
        if (my_feed_like):
            return True
        return False
    class Meta:
        model = NeulhajangAuthenticationFeed
        fields = '__all__'

    def get_image_url(self, obj):
        # 이미지 필드에 대한 경로 생성 시, MEDIA_URL 제외
        return obj.feedPhoto.url[len(settings.MEDIA_URL):]



class ReviewSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='neulhaerang.member.member_nickname', read_only=True)
    neulhaerang_title = serializers.CharField(source='neulhaerang.neulhaerang_title', read_only=True)
    neulhaerang_id = serializers.IntegerField(source='neulhaerang.id', read_only=True)
    class Meta:
        model = NeulhaerangReview
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='admin.member_nickname', read_only=True)
    class Meta:
        model = Notice
        fields = '__all__'

class InquerySerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    class Meta:
        model = Inquery
        fields = '__all__'

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'



class PagenatorSerializer(serializers.Serializer):

    has_next = serializers.BooleanField()
    has_next_data = serializers.BooleanField()
    has_prev = serializers.BooleanField()
    total = serializers.IntegerField()
    start_page = serializers.IntegerField()
    end_page = serializers.IntegerField()
    page_count =serializers.IntegerField()
    # "has_next":pagenator.has_next,
    # "has_prev":pagenator.has_prev,
    #  "total":pagenator.total,
    #  "start_page":pagenator.start_page,
    #  "end_page":pagenator.end_page


