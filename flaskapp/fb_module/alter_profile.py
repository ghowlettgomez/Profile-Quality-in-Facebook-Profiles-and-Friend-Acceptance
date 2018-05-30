# coding: utf8
import random;
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

""" Given a body html in the form of a string, edits the html in certain ways..
"""
class HTML_Editor(object):


    defaultPic = '<img class="_11kf img" src="https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c94.0.320.320/p320x320/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&amp;oh=63eaf30685976e364570705952740b4f&amp;oe=5B9BDFDE"'
    requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">Sadflj Segilua</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'

    def getStartAndEnd(self, s, start, end):
        indices = []
        try:
            indices.append(s.index(start))
            indices.append(s.index(end, indices[0]))
        except ValueError:
            return [0, 0]
        return indices
    
    def getFriends(self, s):
        startAndEnd=self.getStartAndEnd(s, 'data-tab-key="friends"', 'href="')
        href=s[startAndEnd[1]+5:len(s)]
        startAndEndHref=self.getStartAndEnd(href, '"', '">')
        return href[(startAndEndHref[0]+1):startAndEndHref[1]]

    def getName(self, s):
        nameStart = self.getStartAndEnd(s, "_2nlw _2nlv", '>')[1]
        nameEnd = self.getStartAndEnd(s, "_2nlw _2nlv", '</a>')[1]
        return s[nameStart+1:nameEnd]

    def replaceProfilePic(self, s):
        try:
            startAndEnd = self.getStartAndEnd(s, '<img class="_11kf', '>')
        except ValueError:
            startAndEnd = self.getStartAndEnd(s, '<img class="silhouette _11kf', '>')
        return s[0:startAndEnd[0]] + self.defaultPic + s[startAndEnd[1]:len(s)]

    def saveProfilePic(self, s):
        try:
            startAndEnd = self.getStartAndEnd(s, '<img class="_11kf', '>')
        except ValueError:
            startAndEnd = self.getStartAndEnd(s, '<img class="silhouette _11kf', '>')
        picElement = s[startAndEnd[0]:startAndEnd[1]]
        startAndEndPic = self.getStartAndEnd(picElement, 'https', '"')
        return picElement[startAndEndPic[0]:startAndEndPic[1]].replace('amp;', '')

    def replaceBackground(self, s):
        name = self.getName(s)
        defaultBackground = '<div class="cover" id="u_jsonp_7_0"><div class="coverEmptyWrap _37fg coverImage coverNoImage" id="fbCoverImageContainer" data-cropped="1"><img class="coverChangeThrobber img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/RozqvGf0LV-.gif" alt="" width="16" height="16"></div><div class="_2nlj _3x7_ _2xc6"><h1 class="_2nlv"><span class="_2t_q" id="fb-timeline-cover-name" data-testid="profile_name_in_profile_page"><a class="_2nlw _2nlv" href="https://www.facebook.com/profile.php?id=100008426081012">' + name + '</a></span><span class="_2nly"></span></h1></div></div>'
        startAndEnd = self.getStartAndEnd(s, '<div class="cover"', '</span></h1></div></div>')
        return s[0:startAndEnd[0]] + defaultBackground + s[startAndEnd[1]:len(s)]

    def removeHistory(self, s):
        startAndEnd = self.getStartAndEnd(s, '<ol class="_2t4u clearfix', '</ol>')
        name = self.getName(s)
        first_name = name.split(' ')[0]
        placeholder_history = '<ol class="_2t4u clearfix" data-referrer="pagelet_timeline_recent_ocm" id="u_0_1j_story"><div class="_5pcb _4b0l"></div><div class="mbm _5kxd"><div class="_70l"><div class="_57fp" data-ft="{&quot;tn&quot;:&quot;C&quot;}"><div class="fsm fwn fcg"><h3 class="_71u _70n _5r0_">No recent posts</h3></div></div></div><div class="_5kxe">To see posts on <span class="blueName">' + first_name + "</span>'s timeline, accept their friend request.</div></div></ol>"
        return s[0:startAndEnd[0]] + placeholder_history + s[startAndEnd[1]:len(s)]

    def createRequestHeader(self, s):
        name = self.getName(s)
        self.requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">' + name + '</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'
        startAndEnd = self.getStartAndEnd(s, '<div class="_5h60" id="pagelet_above_header_timeline"', '</div>')
        return s[0:startAndEnd[0]] + self.requestHeader + s[startAndEnd[1]:len(s)]

    def fixButton(self, s):
        requestButton = '<button value="1" class="_42ft _4jy0 FriendRequestIncoming _52nf _4jy4 _517h _9c6" type="submit" id="u_ps_fetchstream_17_1_7" aria-controls="js_2dz" aria-haspopup="true" aria-describedby="js_2e0"><i class="_3-8_ img sp_9qsyMvYUWch_2x sx_10eb3e"></i>Respond to Friend Request</button>'
        startAndEnd = self.getStartAndEnd(s, '<button class="_42ft _4jy0 FriendRequestAdd addButton _4jy4 _517h _9c6', '</button>')
        return s[0:startAndEnd[0]] + requestButton + s[startAndEnd[1]:len(s)]

    def removeAddFriendBanner (self, s):
        startAndEnd = self.getStartAndEnd(s, '<div class="escapeHatchMinimal', '<div id="fbSuggestionsHatchPlaceHolder">')
        return s[0:startAndEnd[0]] + s[startAndEnd[1]:len(s)]

    def removeSidebar(self,s):
        startAndEnd = self.getStartAndEnd(s,'<ol class="_2t4v clearfix','</ol>')
        siderbar_placeholder = '<ol class="_2t4v clearfix" data-referrer="pagelet_timeline_recent_ocm" id="u_0_1j_report" style="min-height: 100px;"><div class="_5h60" id="u_0_1q" data-referrer="u_0_1q"><div><div class="_5h60" id="profile_timeline_tiles_unit_pagelets_photos" data-referrer="profile_timeline_tiles_unit_pagelets_photos"><li class="fbTimelineTwoColumn fbTimelineUnit clearfix" data-type="r"><div class="_4-u2 _4-u8"><div role="article"><div id="u_0_1t"><div class="clearfix _3-8t _2pi4"><a href="https://www.facebook.com/sadflj.segilua.7/photos" class="_8o _8r lfloat _ohe" tabindex="-1" aria-hidden="true"><i class="img sp_eapY7va1Ect_2x sx_e10df9"></i></a><div class="clearfix _8u _42ef"><span class="_65tx rfloat _ohf"></span><div class="_6a _3-99"><div class="_6a _6b" style="height:24px"></div><div class="_6a _6b"><a href="https://www.facebook.com/sadflj.segilua.7/photos" data-gt="{&quot;type&quot;:&quot;xtracking&quot;,&quot;xt&quot;:&quot;56.{\&quot;element_type\&quot;:\&quot;section_header_link\&quot;,\&quot;profile_id\&quot;:100025753903858,\&quot;section_type\&quot;:\&quot;photos\&quot;,\&quot;view_style\&quot;:null,\&quot;view_type\&quot;:null,\&quot;vpp_type\&quot;:3}&quot;}" data-xt-vimp="{&quot;pixel_in_percentage&quot;:30,&quot;duration_in_ms&quot;:500,&quot;subsequent_gap_in_ms&quot;:-1,&quot;log_initial_nonviewable&quot;:false,&quot;should_batch&quot;:true,&quot;require_horizontally_onscreen&quot;:true}" class="_39g6" id="u_0_1u"><span role="heading" aria-level="3" class="_2iel _5kx5">Photos</span><iframe src="/xti.php?xt=56.%7B%22element_type%22%3A%22section_header_link%22%2C%22profile_id%22%3A100025753903858%2C%22section_type%22%3A%22photos%22%2C%22view_style%22%3Anull%2C%22view_type%22%3Anull%2C%22vpp_type%22%3A3%7D&amp;isv=1&amp;cts=1526938018&amp;csp" scrolling="no" class="fbEmuTracking" aria-hidden="true" width="0" height="0" frameborder="0"></iframe></a></div></div></div></div></div></div></div></li></div><div class="_5h60" id="profile_timeline_tiles_pager_0" data-referrer="profile_timeline_tiles_pager_0"></div></div></div><div><div class="_5h60" id="profile_timeline_tiles_unit_pagelets_friends" data-referrer="profile_timeline_tiles_unit_pagelets_friends"><li class="fbTimelineTwoColumn fbTimelineUnit clearfix" data-type="r"><div class="_4-u2 _4-u8"><div role="article"><div id="u_jsonp_2_0"><div class="clearfix _3-8t _2pi4"><a href="https://www.facebook.com/sadflj.segilua.7/friends" class="_8o _8r lfloat _ohe" tabindex="-1" aria-hidden="true"><img class="img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/Wa3_mLE4WJJ.png?_nc_eui2=AeHt0W_SpWZ-PKnS9zJxkfH_cpnq5pPJsLxZ-palblmTQY4jOMArwpG8GAX5flRPoq_B_yt-m5q-3-_gFS9OelqgHDzJrAy0mYlvibM5xu9ibA" alt="" width="24" height="24"></a><div class="clearfix _8u _42ef"><span class="_65tx rfloat _ohf"></span><div class="_6a _3-99"><div class="_6a _6b" style="height:24px"></div><div class="_6a _6b"><a href="https://www.facebook.com/sadflj.segilua.7/friends" data-gt="{&quot;type&quot;:&quot;xtracking&quot;,&quot;xt&quot;:&quot;56.{\&quot;element_type\&quot;:\&quot;section_header_link\&quot;,\&quot;profile_id\&quot;:100025753903858,\&quot;section_type\&quot;:\&quot;friends\&quot;,\&quot;view_style\&quot;:null,\&quot;view_type\&quot;:null,\&quot;vpp_type\&quot;:3}&quot;}" data-xt-vimp="{&quot;pixel_in_percentage&quot;:30,&quot;duration_in_ms&quot;:500,&quot;subsequent_gap_in_ms&quot;:-1,&quot;log_initial_nonviewable&quot;:false,&quot;should_batch&quot;:true,&quot;require_horizontally_onscreen&quot;:true}" class="_39g6" id="u_jsonp_2_1"><span role="heading" aria-level="3" class="_2iel _5kx5">Friends</span><iframe src="/xti.php?xt=56.%7B%22element_type%22%3A%22section_header_link%22%2C%22profile_id%22%3A100025753903858%2C%22section_type%22%3A%22friends%22%2C%22view_style%22%3Anull%2C%22view_type%22%3Anull%2C%22vpp_type%22%3A3%7D&amp;isv=1&amp;cts=1526938019&amp;csp" scrolling="no" class="fbEmuTracking" aria-hidden="true" width="0" height="0" frameborder="0"></iframe></a></div></div></div></div></div></div></div></li></div><div class="_5h60" id="profile_timeline_tiles_pager_1" data-referrer="profile_timeline_tiles_pager_1"></div></div><div><div class="_5h60" id="profile_timeline_tiles_unit_pagelets_fun_fact_answers" data-referrer="profile_timeline_tiles_unit_pagelets_fun_fact_answers"><div></div></div><div class="_5h60" id="profile_timeline_rhs_footer_pagelet" data-referrer="profile_timeline_rhs_footer_pagelet"><div class="_4gt0"><div id="pagelet_rhc_footer" data-referrer="pagelet_rhc_footer"><div class="_45mq"><div class="uiContextualLayerParent"><div class="_4-u2 _19ah _2ph_ _4-u8"><div class="_5aj7"><div class="_4bl9"><div class="fsm fwn fcg"><span lang="en_US">English (US)</span><span role="presentation" aria-hidden="true"> · </span><a dir="ltr" href="/intl/save_locale/dialog/?loc=es_LA&amp;href=https%3A%2F%2Fwww.facebook.com%2Fajax%2Fpagelet%2Fgeneric.php%2FProfileTimelineProtilesPaginationPagelet%3Fdata%3D%257B%2522profile_id%2522%253A%2522100025753903858%2522%252C%2522fref%2522%253A%2522%252Freqs.php%2522%252C%2522vanity%2522%253A%2522sadflj.segilua.7%2522%252C%2522sk%2522%253A%2522timeline%2522%252C%2522tab_key%2522%253A%2522timeline%2522%252C%2522start%2522%253A%25220%2522%252C%2522end%2522%253A%25221527836399%2522%252C%2522query_type%2522%253A%252236%2522%252C%2522lst%2522%253A%2522100008426081012%253A100025753903858%253A1526938016%2522%252C%2522section_pagelet_id%2522%253A%2522pagelet_timeline_recent%2522%252C%2522load_immediately%2522%253A%25221%2522%252C%2522pagelet_token%2522%253A%2522AWuUzGrwOX5dQlWXiX5jhU_Svao6px_WD-_lFLnJgLQoCH3NjkxGIhwlRmHUTSFbBr8%2522%252C%2522target_id%2522%253A%2522u_0_1j_report%2522%252C%2522count%2522%253A%25221%2522%252C%2522page_index%2522%253A%25222%2522%252C%2522profile_has_parallel_pagelets%2522%253A%2522%2522%252C%2522section_types%2522%253A%255B%2522fun_fact_answers%2522%255D%252C%2522buffer%2522%253A%2522100%2522%257D&amp;ls_ref=www_card_selector" rel="dialog" title="Spanish" class="_5f4c" role="button" lang="es_LA">Español</a><span role="presentation" aria-hidden="true"> · </span><a dir="ltr" href="/intl/save_locale/dialog/?loc=pt_BR&amp;href=https%3A%2F%2Fwww.facebook.com%2Fajax%2Fpagelet%2Fgeneric.php%2FProfileTimelineProtilesPaginationPagelet%3Fdata%3D%257B%2522profile_id%2522%253A%2522100025753903858%2522%252C%2522fref%2522%253A%2522%252Freqs.php%2522%252C%2522vanity%2522%253A%2522sadflj.segilua.7%2522%252C%2522sk%2522%253A%2522timeline%2522%252C%2522tab_key%2522%253A%2522timeline%2522%252C%2522start%2522%253A%25220%2522%252C%2522end%2522%253A%25221527836399%2522%252C%2522query_type%2522%253A%252236%2522%252C%2522lst%2522%253A%2522100008426081012%253A100025753903858%253A1526938016%2522%252C%2522section_pagelet_id%2522%253A%2522pagelet_timeline_recent%2522%252C%2522load_immediately%2522%253A%25221%2522%252C%2522pagelet_token%2522%253A%2522AWuUzGrwOX5dQlWXiX5jhU_Svao6px_WD-_lFLnJgLQoCH3NjkxGIhwlRmHUTSFbBr8%2522%252C%2522target_id%2522%253A%2522u_0_1j_report%2522%252C%2522count%2522%253A%25221%2522%252C%2522page_index%2522%253A%25222%2522%252C%2522profile_has_parallel_pagelets%2522%253A%2522%2522%252C%2522section_types%2522%253A%255B%2522fun_fact_answers%2522%255D%252C%2522buffer%2522%253A%2522100%2522%257D&amp;ls_ref=www_card_selector" rel="dialog" title="Portuguese (Brazil)" class="_5f4c" role="button" lang="pt_BR">Português (Brasil)</a><span role="presentation" aria-hidden="true"> · </span><a dir="ltr" href="/intl/save_locale/dialog/?loc=fr_FR&amp;href=https%3A%2F%2Fwww.facebook.com%2Fajax%2Fpagelet%2Fgeneric.php%2FProfileTimelineProtilesPaginationPagelet%3Fdata%3D%257B%2522profile_id%2522%253A%2522100025753903858%2522%252C%2522fref%2522%253A%2522%252Freqs.php%2522%252C%2522vanity%2522%253A%2522sadflj.segilua.7%2522%252C%2522sk%2522%253A%2522timeline%2522%252C%2522tab_key%2522%253A%2522timeline%2522%252C%2522start%2522%253A%25220%2522%252C%2522end%2522%253A%25221527836399%2522%252C%2522query_type%2522%253A%252236%2522%252C%2522lst%2522%253A%2522100008426081012%253A100025753903858%253A1526938016%2522%252C%2522section_pagelet_id%2522%253A%2522pagelet_timeline_recent%2522%252C%2522load_immediately%2522%253A%25221%2522%252C%2522pagelet_token%2522%253A%2522AWuUzGrwOX5dQlWXiX5jhU_Svao6px_WD-_lFLnJgLQoCH3NjkxGIhwlRmHUTSFbBr8%2522%252C%2522target_id%2522%253A%2522u_0_1j_report%2522%252C%2522count%2522%253A%25221%2522%252C%2522page_index%2522%253A%25222%2522%252C%2522profile_has_parallel_pagelets%2522%253A%2522%2522%252C%2522section_types%2522%253A%255B%2522fun_fact_answers%2522%255D%252C%2522buffer%2522%253A%2522100%2522%257D&amp;ls_ref=www_card_selector" rel="dialog" title="French (France)" class="_5f4c" role="button" lang="fr_FR">Français (France)</a><span role="presentation" aria-hidden="true"> · </span><a dir="ltr" href="/intl/save_locale/dialog/?loc=de_DE&amp;href=https%3A%2F%2Fwww.facebook.com%2Fajax%2Fpagelet%2Fgeneric.php%2FProfileTimelineProtilesPaginationPagelet%3Fdata%3D%257B%2522profile_id%2522%253A%2522100025753903858%2522%252C%2522fref%2522%253A%2522%252Freqs.php%2522%252C%2522vanity%2522%253A%2522sadflj.segilua.7%2522%252C%2522sk%2522%253A%2522timeline%2522%252C%2522tab_key%2522%253A%2522timeline%2522%252C%2522start%2522%253A%25220%2522%252C%2522end%2522%253A%25221527836399%2522%252C%2522query_type%2522%253A%252236%2522%252C%2522lst%2522%253A%2522100008426081012%253A100025753903858%253A1526938016%2522%252C%2522section_pagelet_id%2522%253A%2522pagelet_timeline_recent%2522%252C%2522load_immediately%2522%253A%25221%2522%252C%2522pagelet_token%2522%253A%2522AWuUzGrwOX5dQlWXiX5jhU_Svao6px_WD-_lFLnJgLQoCH3NjkxGIhwlRmHUTSFbBr8%2522%252C%2522target_id%2522%253A%2522u_0_1j_report%2522%252C%2522count%2522%253A%25221%2522%252C%2522page_index%2522%253A%25222%2522%252C%2522profile_has_parallel_pagelets%2522%253A%2522%2522%252C%2522section_types%2522%253A%255B%2522fun_fact_answers%2522%255D%252C%2522buffer%2522%253A%2522100%2522%257D&amp;ls_ref=www_card_selector" rel="dialog" title="German" class="_5f4c" role="button" lang="de_DE">Deutsch</a></div></div><div class="_4bl7 _2pit"><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" ajaxify="/settings/language/language/?uri=https%3A%2F%2Fwww.facebook.com%2Fajax%2Fpagelet%2Fgeneric.php%2FProfileTimelineProtilesPaginationPagelet%3Fdata%3D%257B%2522profile_id%2522%253A%2522100025753903858%2522%252C%2522fref%2522%253A%2522%252Freqs.php%2522%252C%2522vanity%2522%253A%2522sadflj.segilua.7%2522%252C%2522sk%2522%253A%2522timeline%2522%252C%2522tab_key%2522%253A%2522timeline%2522%252C%2522start%2522%253A%25220%2522%252C%2522end%2522%253A%25221527836399%2522%252C%2522query_type%2522%253A%252236%2522%252C%2522lst%2522%253A%2522100008426081012%253A100025753903858%253A1526938016%2522%252C%2522section_pagelet_id%2522%253A%2522pagelet_timeline_recent%2522%252C%2522load_immediately%2522%253A%25221%2522%252C%2522pagelet_token%2522%253A%2522AWuUzGrwOX5dQlWXiX5jhU_Svao6px_WD-_lFLnJgLQoCH3NjkxGIhwlRmHUTSFbBr8%2522%252C%2522target_id%2522%253A%2522u_0_1j_report%2522%252C%2522count%2522%253A%25221%2522%252C%2522page_index%2522%253A%25222%2522%252C%2522profile_has_parallel_pagelets%2522%253A%2522%2522%252C%2522section_types%2522%253A%255B%2522fun_fact_answers%2522%255D%252C%2522buffer%2522%253A%2522100%2522%257D&amp;source=www_card_selector_more" rel="dialog" href="#" aria-label="Use Facebook in another language."><i class="img sp_-5UQgJ79515_2x sx_f78fd3"></i></a></div></div></div></div><div aria-label="Facebook" class="_26z1" role="contentinfo"><div class="fsm fwn fcg"><a href="https://www.facebook.com/privacy/explanation" title="Learn about your privacy and Facebook.">Privacy</a><span role="presentation" aria-hidden="true"> · </span><a accesskey="9" href="https://www.facebook.com/policies?ref=pf" title="Review our terms and policies.">Terms</a><span role="presentation" aria-hidden="true"> · </span><a href="https://www.facebook.com/ad_campaign/landing.php?placement=pf_rhc&amp;campaign_id=242449722530626&amp;extra_1=auto" title="Advertise on Facebook.">Advertising</a><span role="presentation" aria-hidden="true"> · </span><a class="_41uf" href="https://www.facebook.com/help/568137493302217" title="Learn about Ad Choices.">Ad Choices<i class="img sp_-5UQgJ79515_2x sx_6c6c3a"></i></a><span role="presentation" aria-hidden="true"> · </span><a href="https://www.facebook.com/help/cookies?ref_type=sitefooter" title="Cookies">Cookies</a><span role="presentation" aria-hidden="true"> · </span><div class="_6a uiPopover" id="u_jsonp_4_1"><a class="_45mr _p" aria-haspopup="true" aria-expanded="false" rel="toggle" href="#" role="button" id="u_jsonp_4_2">More<i class="img sp_-5UQgJ79515_2x sx_9593ca"></i></a></div></div><div><span> Facebook © 2018</span></div></div></div></div></div></div></div>'
        return s[0:startAndEnd[0]] + siderbar_placeholder +s[startAndEnd[1]:len(s)]

    def nameInMenu(self, s, name):
        friend_name = self.getName(s)
        startAndEnd = self.getStartAndEnd(s, '<span class="_1vp5"', '</span>')
        person = s[0:startAndEnd[0]] + '<span class="_1vp5">' + name + '</span>' + s[startAndEnd[1]:len(s)]
        startAndEndSearchFull = self.getStartAndEnd(person, '<div class="_5861', '</div></div></div></div>')
        fullSearch = person[startAndEndSearchFull[0]:startAndEndSearchFull[1]]
        startAndEndName = self.getStartAndEnd(fullSearch, 'value="', '"')
        return person[0:startAndEndSearchFull[0]] + fullSearch[0:startAndEndName[0]] + 'value="' + friend_name + fullSearch[startAndEndName[1]:len(fullSearch)] + person[startAndEndSearchFull[1]:len(person)]

    def alterSmallRequest (self, name, friends, url):
        if friends <= 0:
            mutual = ''
        else:
            mutual = str(friends) + ' mutual friends'
        request = '<li class="objectListItem" id="01392847102938471209587012398471029384701_1_req"><div class="clearfix" data-ft="{&quot;tn&quot;:&quot;-Z&quot;}"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel" tabindex="-1" data-ft="{&quot;tn&quot;:&quot;-^&quot;}" class="_8o _8s lfloat _ohe" id="u_14_3"><img class="_s0 _4ooo _rw img" src="' + url + '" alt="" aria-label="Aditya Shekhar" role="img"></a><div class="_42ef"><div id="100002392517786_1_req_status" class="requestStatus"><div class="clearfix"><div class="rfloat _ohf"><div class="accessible_elem" data-ft="{&quot;tn&quot;:&quot;-]&quot;}"><span class="title fsl fwb fcb"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel">' + name + '</a></span> </div><div class="_6a"><div class="_6a _6b" style="height:50px"></div><div class="_6a _6b"><div class="auxiliary" id="100002392517786_1_req_aux"><form rel="async" action="/ajax/reqs.php" method="post" onsubmit="return window.Event &amp;&amp; Event.__inlineSubmit &amp;&amp; Event.__inlineSubmit(this,event)" id="u_14_4"><input type="hidden" name="fb_dtsg" value="AQEty0AqyR4i:AQGWLGET-qZp" autocomplete="off"><input type="hidden" autocomplete="off" id="confirm_100002392517786_1_req" value="100002392517786" name="confirm"><input type="hidden" autocomplete="off" value="friend_connect" name="type"><input type="hidden" autocomplete="off" value="100002392517786" name="request_id"><input type="hidden" autocomplete="off" value="100002392517786_1_req" name="list_item_id"><input type="hidden" autocomplete="off" value="100002392517786_1_req_status" name="status_div_id"><input type="hidden" autocomplete="off" value="1" name="inline"><input type="hidden" autocomplete="off" value="jewel" name="ref"><input type="hidden" autocomplete="off" name="ego_log"><div class="actions"><img class="loadingIndicator img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/0_KqJAcnl8J.gif" alt="" width="16" height="11"><button value="1" class="_42ft _4jy0 _4jy3 _4jy1 selected _51sy" name="actions[accept]" type="submit">Confirm</button><button value="1" class="_42ft _4jy0 _4jy3 _517h _51sy" name="actions[reject]" type="submit">Delete Request</button></div></form></div></div></div></div><div class="_6a requestStatusBlock _42ef" aria-hidden="true"><div class="_6a _6b" style="height:50px"></div><div class="_6a _6b"><div data-ft="{&quot;tn&quot;:&quot;-]&quot;}" id="u_14_5"><span class="title fsl fwb fcb"><a href="https://www.facebook.com/aditya.shekhar.14?fref=jewel">' + name + '</a></span> </div><span class="_1nd3"><a ajaxify="/ajax/browser/dialog/mutual_friends/?uid=100002392517786" href="/browse/mutual_friends/?uid=100002392517786" rel="dialog" style="" role="button" class="_39g5" data-hover="tooltip" id="js_g9">' + mutual + '</a></span></div></div></div></div></div></div></li>'
        return request

    def replaceRequests (self, s, type, friends):
        name = self.getName(s)
        if type == 0:
            url = 'https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c94.0.320.320/p320x320/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&amp;oh=63eaf30685976e364570705952740b4f&amp;oe=5B9BDFDE'
        else:
            url = self.saveProfilePic(s)
        newReqs = self.alterSmallRequest(name, friends, url)
        startAndEnd = self.getStartAndEnd(s,'<ul class="uiList _4kg _4ks">','<li class')
        return s[0:startAndEnd[0]] + '<ul class="uiList _4kg _4ks">' + newReqs +  s[startAndEnd[1]:len(s)]
    
    def deleteRequestDropdown (self, s):
        startAndEnd = self.getStartAndEnd(s, '<div class="__tw _3nzk', '<button class="hideToggler')
        return s[0:startAndEnd[0]] + s[startAndEnd[1]:len(s)]

    def replaceTL (self, s):
        return s.replace('<a class="_6-6 _6-7"','<a class="_6-6"')
    
    def removeChat (self, s):
        startAndEnd = self.getStartAndEnd(s, '<a class="fbNubButton"', '<div class="fbNubFlyout')
        return s[0:startAndEnd[0]] + s[startAndEnd[1]:len(s)]

    def addMutualFriends (self, s, friends):
        if friends <= 0:
            return s
        startAndEnd = self.getStartAndEnd(s, 'Friends<span class="_513x', '>')
        mutual = '<span class="_gs6"><span id="u_0_v">' + str(friends) + ' Mutual</span></span>'
        return s[0:startAndEnd[0]+7] + mutual + s[startAndEnd[0]+7:len(s)]

    def doAlways (self, s, name, friends):
        return self.addMutualFriends(self.removeChat(self.fixButton(self.removeAddFriendBanner(self.nameInMenu(s, name)))), friends)


    def returnToDefault(self, s, name, friends):
        return self.replaceTL(self.removeSidebar(self.removeHistory(self.replaceBackground(self.replaceProfilePic(self.doAlways(s, name, friends))))))

    def returnUnchanged(self, s, name, friends):
        return self.doAlways(s, name, friends)

    def onlySidebar(self, s, name, friends):
        return self.removeHistory(self.doAlways(s, name, friends))

    def onlyPosts (self, s, name, friends):
        return self.removeSidebar(self.doAlways(s, name, friends))

    def removeAllHistory (self, s, name, friends):
        return self.removeSidebar(self.removeHistory(self.doAlways(s, name, friends)))
