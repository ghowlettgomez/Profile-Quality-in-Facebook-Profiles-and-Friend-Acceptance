from html.parser import HTMLParser
import sys

requesthtml = '''<div class="clearfix ruUserBox _3-z friendRequestItem" data-id="100009833611894" data-ft="{&quot;tn&quot;:&quot;-Z&quot;}" id="u_fetchstream_2_1l"><a href="https://www.facebook.com/profile.php?id=100009833611894&amp;fref=%2Freqs.php" class="_8o _8t lfloat _ohe" tabindex="-1" aria-hidden="true"><div class="uiScaledImageContainer ruProfilePicXLarge"><img class="scaledImageFitWidth img" src="https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/p160x160/11011577_102006226803831_6677917841080541820_n.jpg?_nc_cat=0&amp;oh=75fd99f4635cda1f32c00538bf0ab2a1&amp;oe=5B65C76F" alt="" width="75" height="75" data-ft="{&quot;tn&quot;:&quot;-^&quot;}" itemprop="image"></div></a><div class="clearfix _42ef"><div class="_6a mlm ruResponseSectionContainer rfloat _ohf"><div class="_6a _6b" style="height:50px"></div><div class="_6a _6b"><div class="ruResponse ruResponseSimple"><div class="ruResponseButtons"><button value="1" class="_42ft _4jy0 _4jy3 _4jy1 selected _51sy" aria-describedby="u_fetchstream_2_2e" type="submit" id="u_fetchstream_2_2p">Confirm</button><button value="1" class="_42ft _4jy0 _4jy3 _517h _51sy" aria-describedby="u_fetchstream_2_2e" type="submit" id="u_fetchstream_2_2q">Delete Request</button></div><img class="ruResponseLoading hidden_elem img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/RozqvGf0LV-.gif" alt="" width="16" height="16"><span class="ruTransportErrorMsg hidden_elem">Connection error. Please check your Internet connection.</span></div></div></div><div class="fcg"><div id="u_fetchstream_2_2e" class="_6-_"><a href="https://www.facebook.com/profile.php?id=100009833611894&amp;fref=%2Freqs.php" data-hovercard="/ajax/hovercard/user.php?id=100009833611894" data-hovercard-prefer-more-content-show="1">Rachel Simmons</a></div><div class="hidden_elem followUpQuestion _1byw fcg" id="u_fetchstream_2_2r"><div class="clearfix _5hb1 _2dzh"><a role="button" class="_42ft _4jy0 _5hb3 rfloat _ohf _4jy3 _517h _51sy mls" href="#" data-hover="tooltip" data-tooltip-content="If you click \'Mark as Spam\', this person will not be able to send you any more friend requests.">Mark as Spam</a><div class="_2dze _1byw">Request removed.</div></div><img class="_9- hidden_elem img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/RozqvGf0LV-.gif" alt="" width="16" height="16"><div class="clearfix _5hb2 hidden_elem _2dzh"><a role="button" class="_42ft _4jy0 _2qk_ rfloat _ohf _4jy3 _517h _51sy mls" href="#">Undo</a><div class="_2dze _1byw">Thanks. This person won\'t be able to send you any more friend requests.</div></div><div class="mrs _a2 hidden_elem _2dze _1byw">Unblocked. This person can send you friend requests again.</div><div class="_9z hidden_elem _2dze _1byw">Facebook experienced an error while modifying this friend request. Try again later.</div></div><div class="requestInfoContainer"><div><table class="uiGrid _51mz" cellspacing="0" cellpadding="0" role="presentation"><tbody><tr class="_51mx"><td class="_51m- vTop hLeft prs"><i class="img sp_wjfmCmBScjF_2x sx_ea4805"></i></td><td class="_51m- vTop hLeft _51mw">Purnell School</td></tr></tbody></table></div><div><span class="_1nd3"><a style="" href="https://www.facebook.com/scott.carvalho.35" data-hovercard="/ajax/hovercard/user.php?id=100001583772503" data-hovercard-prefer-more-content-show="1">Scott Carvalho</a> and <a ajaxify="/ajax/browser/dialog/mutual_friends/?uid=100009833611894" href="/browse/mutual_friends/?uid=100009833611894" rel="dialog" style="" role="button" data-hover="tooltip" data-tooltip-uri="/ajax/mutual_friends/tooltip.php?friend_id=100009833611894&amp;exclude_id=100001583772503">7 other mutual friends</a></span></div></div></div></div></div>'''

defaultpic = 'https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c94.0.320.320/p320x320/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&oh=63eaf30685976e364570705952740b4f&oe=5B9BDFDE'

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

imgurl = find_between(requesthtml, '<img class="scaledImageFitWidth img" src="', '" alt=')

a, b = requesthtml.split(imgurl)

finalhtml = a + defaultpic + b

print(finalhtml)
