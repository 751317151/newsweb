'''
@Author: 华豪
@Date: 2019-11-25 17:37:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-25 18:36:56
'''
<div class="imagearea-top">
    <div class="image-mask-item">
        {% if hot_enter_pic_news %}
            <a href="{{ hot_enter_pic_news.0.urls }}" target="_blank" class="item-image" title="{{ hot_enter_pic_news.0.titles }}"><img referrer-policy="no-referrer" src="{{ hot_enter_pic_news.0.imgurls }}"></a>
            <a href="{{ hot_enter_pic_news.0.urls }}" target="_blank" class="item-title" title="{{ hot_enter_pic_news.0.titles }}">{{ hot_enter_pic_news.0.titles }}</a>
        {% endif %}
    </div>
</div>
<div class="imagearea-bottom">
    <div class="image-list-item">
        {% if hot_enter_pic_news %}
            <a href="{{ hot_enter_pic_news.1.urls }}" target="_blank" title="{{ hot_enter_pic_news.1.titles }}"><img referrer-policy="no-referrer" src="{{ hot_enter_pic_news.1.imgurls }}"></a>
            <a href="{{ hot_enter_pic_news.1.urls }}" target="_blank" class="txt" title="{{ hot_enter_pic_news.1.titles }}">{{ hot_enter_pic_news.1.titles }}</a>
        {% endif %}
    </div>
    <div class="image-list-item">
        {% if hot_enter_pic_news %}
            <a href="{{ hot_enter_pic_news.2.urls }}" target="_blank" title="{{ hot_enter_pic_news.2.titles }}"><img referrer-policy="no-referrer" src="{{ hot_enter_pic_news.2.imgurls }}"></a>
            <a href="{{ hot_enter_pic_news.2.urls }}" target="_blank" class="txt" title="{{ hot_enter_pic_news.2.titles }}">{{ hot_enter_pic_news.2.titles }}</a>
        {% endif %}
    </div>
</div>