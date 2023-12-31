from django.db import models

from member.models import Member
from neulhaerang.models import Neulhaerang
from workspace.models import Period


class NeulhaerangReview(Period):
    review_title = models.TextField(null=False, blank=False)
    thumbnail_image = models.ImageField(null=False, blank=False, upload_to='neulhaerang_review/thumbnail/%Y/%m/%d')
    byeoljji_receiver_openchat_link = models.TextField(null=False, blank=False)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_review'
        ordering = ["-id"]

class NeulhaerangReviewLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_neulhaerang_review_like'
        ordering = ["-id"]

class NeulhaerangReviewReply(Period):
    reply_content = models.TextField(null=False, blank=False)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_review_reply'
        ordering = ["-id"]

class ReviewReplyLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    review_reply = models.ForeignKey(NeulhaerangReviewReply, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_review_reply_like'
        ordering = ["-id"]

class FundUsageHistory(Period):
    history_name = models.TextField(null=False, blank=False)
    history_amount = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_fund_usage_history'
        ordering = ["-id"]

class NeulhaerangReviewTag(Period):
    tag_name = models.CharField(max_length=50,null=False, blank=False)
    tag_type = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_review_tag'
        ordering = ["-id"]


class ReviewInnerTitle(Period):
    inner_title_text = models.TextField(null=False, blank=False)
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_review_inner_title'
        ordering = ["-id"]

class ReviewInnerContent(Period):
    inner_content_text = models.TextField(null=False, blank=False)
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_review_inner_content'
        ordering = ["-id"]

class ReviewInnerPhotos(Period):
    inner_photo = models.ImageField(null=False, blank=False, upload_to='neulhaerang_review/innerphoto/%Y/%m/%d')
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    photo_order = models.IntegerField(null=False, blank=False, default=0)
    photo_explanation = models.TextField(null=False, blank=False)
    neulhaerang_review = models.ForeignKey(NeulhaerangReview, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_review_inner_photos'
        ordering = ["-id"]