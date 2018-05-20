with open('full_profile.txt', 'r') as full:
    profile = full.read()

defaultPic = '<img class="_11kf img" src="https://scontent-ort2-2.xx.fbcdn.net/v/t1.0-1/c94.0.320.320/p320x320/10354686_10150004552801856_220367501106153455_n.jpg?_nc_cat=0&amp;oh=63eaf30685976e364570705952740b4f&amp;oe=5B9BDFDE"'

requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">Sadflj Segilua</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'

def getStartAndEnd (s, start, end):
    indices = []
    indices.append(s.index(start))
    indices.append(s.index(end, indices[0]))
    return indices

def getName (s):
    nameStart = getStartAndEnd(s, '<a class="_2nlw _2nlv"', '>')[1]
    nameEnd = getStartAndEnd(s, '<a class="_2nlw _2nlv"', '</a>')[1]
    return s[nameStart+1:nameEnd]

def replaceProfilePic (s):
    startAndEnd = getStartAndEnd(s, '<img class="_11kf', '>')
    return s[0:startAndEnd[0]] + defaultPic + s[startAndEnd[1]:len(s)]

def replaceBackground (s):
    name = getName(s)
    defaultBackground = '<div class="cover" id="u_fetchstream_4_0"><div class="coverEmptyWrap _37fg coverImage coverNoImage" id="fbCoverImageContainer" data-cropped="1"><img class="coverChangeThrobber img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/RozqvGf0LV-.gif" alt="" width="16" height="16"></div><div class="_2nlj _3x7_ _2xc6"><h1 class="_2nlv"><span class="_2t_q" id="fb-timeline-cover-name" data-testid="profile_name_in_profile_page"><a class="_2nlw _2nlv" href="https://www.facebook.com/sadflj.segilua.7">' + name + '</a></span><span class="_2nly"></span>'
    startAndEnd = getStartAndEnd(s, '<div class="cover"', '</h1>')
    return s[0:startAndEnd[0]] + defaultBackground + s[startAndEnd[1]:len(s)]

def removeHistory (s):
    startAndEnd = getStartAndEnd(s, '<div class="_5nb8"', '<div class="_1vc-"')
    return s[0:startAndEnd[0]] + s[startAndEnd[1]:len(s)]

def createRequestHeader (s):
    name = getName(s)
    print(name)
    requestHeader = '<div class="_5h60" id="pagelet_above_header_timeline" data-referrer="pagelet_above_header_timeline" style="top: 0px;"><div class="_2pi6 _52jv" id="u_fetchstream_3_5"><span class="_2iem"><span class="_35ow"><span class="_50f7">' + name + '</span> sent you a friend request</span><a role="button" class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy" href="/ajax/add_friend/action.php?to_friend=100025753903858&amp;action=confirm&amp;ref_param=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" data-hover="tooltip" data-tooltip-content="Confirm Request" id="js_i2"><img class="_2vhe hidden_elem _3-8_ img" alt="Confirm Request" src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/9X_pFYHCHN4.png" width="23" height="23"><span class="_2vhc">Confirm Request</span></a><a role="button" class="_42ft _4jy0 _4jy4 _517h _51sy" href="/ajax/profile/connect/reject.php?profile_id=100025753903858&amp;ref=%2Fprofile.php&amp;floc=profile_box&amp;frefs%5B0%5D=jewel" rel="async-post" id="u_fetchstream_3_4" data-hover="tooltip" data-tooltip-content="Delete Request"><i class="_2vhf hidden_elem _3-8_ img sp_xfcCes0Za9Q_2x sx_83b7a3"><u>Delete Request</u></i><span class="_2vhd">Delete Request</span></a></span></div></div>'
    startAndEnd = getStartAndEnd (s, '<div class="_5h60" id="pagelet_above_header_timeline"', '</div>')
    print (startAndEnd)
    return s[0:startAndEnd[0]] + requestHeader + s[startAndEnd[1]:len(s)]

def fixButton (s):
    requestButton = '<button value="1" class="_42ft _4jy0 FriendRequestIncoming _52nf _4jy4 _517h _9c6" type="submit" id="u_ps_fetchstream_17_1_7" aria-controls="js_2dz" aria-haspopup="true" aria-describedby="js_2e0"><i class="_3-8_ img sp_9qsyMvYUWch_2x sx_10eb3e"></i>Respond to Friend Request</button>'
    startAndEnd = getStartAndEnd (s, '<button class="_42ft _4jy0 FriendRequestAdd addButton _4jy4 _517h _9c6', '</button>')
    return s[0:startAndEnd[0]] + requestButton + s[startAndEnd[1]:len(s)]

def nameInMenu (s, name):
    startAndEnd = getStartAndEnd(s, '<span class="_1vp5"', '</span>')
    return s[0:startAndEnd[0]] + '<span class="_1vp5">' + name + '</span>' + s[startAndEnd[1]:len(s)]

with open('full_profile_edited.txt', 'w') as edited:
    edited.write(removeHistory(replaceBackground(replaceProfilePic(fixButton(nameInMenu(profile, 'Test'))))))
