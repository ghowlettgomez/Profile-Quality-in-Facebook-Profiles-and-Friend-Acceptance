""" Given a body html in the form of a string, edits the html in certain ways.
"""
class HTML_Editor(object):

    defaultPic = '<img class="_11kf img" src="https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c94.0.320.320/p320x320/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&amp;oh=63eaf30685976e364570705952740b4f&amp;oe=5B9BDFDE"'
    requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">Sadflj Segilua</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'

    def getStartAndEnd(self, s, start, end):
        indices = []
        indices.append(s.index(start))
        indices.append(s.index(end, indices[0]))
        return indices

    def getName(self, s):
        nameStart = self.getStartAndEnd(s, '<a class="_2nlw _2nlv"', '>')[1]
        nameEnd = self.getStartAndEnd(s, '<a class="_2nlw _2nlv"', '</a>')[1]
        return s[nameStart+1:nameEnd]

    def replaceProfilePic(self, s):
        startAndEnd = self.getStartAndEnd(s, '<img class="_11kf', '>')
        return s[0:startAndEnd[0]] + self.defaultPic + s[startAndEnd[1]:len(s)]

    def saveProfilePic(self, s):
        startAndEnd = self.getStartAndEnd(s, '<img class="_11kf', '>')
        picElement = s[startAndEnd[0]:startAndEnd[1]]
        startAndEndPic = self.getStartAndEnd(picElement, 'src="', ' /')
        return picElement[startAndEndPic[0]+5:startAndEndPic[1]-1]

    def replaceBackground(self, s):
        name = self.getName(s)
        defaultBackground = '<div class="cover" id="u_fetchstream_4_0"><div class="coverEmptyWrap _37fg coverImage coverNoImage" id="fbCoverImageContainer" data-cropped="1"><img class="coverChangeThrobber img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/RozqvGf0LV-.gif" alt="" width="16" height="16"></div><div class="_2nlj _3x7_ _2xc6"><h1 class="_2nlv"><span class="_2t_q" id="fb-timeline-cover-name" data-testid="profile_name_in_profile_page"><a class="_2nlw _2nlv" href="https://www.facebook.com/sadflj.segilua.7">' + name + '</a></span><span class="_2nly"></span>'
        startAndEnd = self.getStartAndEnd(s, '<div class="cover"', '</h1>')
        return s[0:startAndEnd[0]] + defaultBackground + s[startAndEnd[1]:len(s)]

    def removeHistory(self, s):
        startAndEnd = self.getStartAndEnd(s, '<div class="_5nb8"', '<div class="_1vc-"')
        return s[0:startAndEnd[0]] + s[startAndEnd[1]:len(s)]

    def createRequestHeader(self, s):
        name = getName(s)
        print(name)
        self.requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">' + name + '</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'
        startAndEnd = self.getStartAndEnd(s, '<div class="_5h60" id="pagelet_above_header_timeline"', '</div>')
        print(startAndEnd)
        return s[0:startAndEnd[0]] + self.requestHeader + s[startAndEnd[1]:len(s)]

    def fixButton(self, s):
        requestButton = '<button value="1" class="_42ft _4jy0 FriendRequestIncoming _52nf _4jy4 _517h _9c6" type="submit" id="u_ps_fetchstream_17_1_7" aria-controls="js_2dz" aria-haspopup="true" aria-describedby="js_2e0"><i class="_3-8_ img sp_9qsyMvYUWch_2x sx_10eb3e"></i>Respond to Friend Request</button>'
        startAndEnd = self.getStartAndEnd(s, '<button class="_42ft _4jy0 FriendRequestAdd addButton _4jy4 _517h _9c6', '</button>')
        return s[0:startAndEnd[0]] + requestButton + s[startAndEnd[1]:len(s)]

    def nameInMenu(self, s, name):
        startAndEnd = self.getStartAndEnd(s, '<span class="_1vp5"', '</span>')
        return s[0:startAndEnd[0]] + '<span class="_1vp5">' + name + '</span>' + s[startAndEnd[1]:len(s)]

    def alterSmallRequest (self, name, friends):
        if friends <= 0:
            mutual = ''
        else:
            mutual = str(friends) + ' mutual friends'
        request = '<li class="objectListItem" id="100002392517786_1_req"><div class="clearfix" data-ft="{&quot;tn&quot;:&quot;-Z&quot;}"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel" tabindex="-1" data-ft="{&quot;tn&quot;:&quot;-^&quot;}" class="_8o _8s lfloat _ohe" id="u_14_3"><img class="_s0 _4ooo _rw img" src="https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c29.0.100.100/p100x100/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&amp;oh=215b9060cca16dedf781d5c0a3f2733a&amp;oe=5B8E4A77" alt="" aria-label="Aditya Shekhar" role="img"></a><div class="_42ef"><div id="100002392517786_1_req_status" class="requestStatus"><div class="clearfix"><div class="rfloat _ohf"><div class="accessible_elem" data-ft="{&quot;tn&quot;:&quot;-]&quot;}"><span class="title fsl fwb fcb"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel">' + name + '</a></span> </div><div class="_6a"><div class="_6a _6b" style="height:50px"></div><div class="_6a _6b"><div class="auxiliary" id="100002392517786_1_req_aux"><form rel="async" action="/ajax/reqs.php" method="post" onsubmit="return window.Event &amp;&amp; Event.__inlineSubmit &amp;&amp; Event.__inlineSubmit(this,event)" id="u_14_4"><input type="hidden" name="fb_dtsg" value="AQEty0AqyR4i:AQGWLGET-qZp" autocomplete="off"><input type="hidden" autocomplete="off" id="confirm_100002392517786_1_req" value="100002392517786" name="confirm"><input type="hidden" autocomplete="off" value="friend_connect" name="type"><input type="hidden" autocomplete="off" value="100002392517786" name="request_id"><input type="hidden" autocomplete="off" value="100002392517786_1_req" name="list_item_id"><input type="hidden" autocomplete="off" value="100002392517786_1_req_status" name="status_div_id"><input type="hidden" autocomplete="off" value="1" name="inline"><input type="hidden" autocomplete="off" value="jewel" name="ref"><input type="hidden" autocomplete="off" name="ego_log"><div class="actions"><img class="loadingIndicator img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/0_KqJAcnl8J.gif" alt="" width="16" height="11"><button value="1" class="_42ft _4jy0 _4jy3 _4jy1 selected _51sy" name="actions[accept]" type="submit">Confirm</button><button value="1" class="_42ft _4jy0 _4jy3 _517h _51sy" name="actions[reject]" type="submit">Delete Request</button></div></form></div></div></div></div><div class="_6a requestStatusBlock _42ef" aria-hidden="true"><div class="_6a _6b" style="height:50px"></div><div class="_6a _6b"><div data-ft="{&quot;tn&quot;:&quot;-]&quot;}" id="u_14_5"><span class="title fsl fwb fcb"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel">' + name + '</a></span> </div><span class="_1nd3"><a ajaxify="/ajax/browser/dialog/mutual_friends/?uid=100002392517786" href="/browse/mutual_friends/?uid=100002392517786" rel="dialog" style="" role="button" class="_39g5" data-hover="tooltip" id="js_g9">' + mutual + '</a></span></div></div></div></div></div></div></li>'
        return request
