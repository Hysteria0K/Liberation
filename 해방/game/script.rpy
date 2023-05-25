# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("나")
define k = Character("경수")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "경수의 방으로 돌아왔다. 이젠 정말 마지막이다."

    show ks_normal

    m "경수야. 제발. 이번에는 절대로 실수하면 안 돼."

    m "시간도 촉박하고, 마지막 기회야."

    hide ks_normal
    show ks_angry

    k "하...진짜 알겠다니까 왜 이렇게 보채? 이게 그렇게 중요해?"

    "그렇게 중요하냐고? 아. 안 된다. 절대로 경수를 보내면 안 된다."

    "하지만 어떻게?"

    menu:

        "나는 경수에게..."

        "1950년도 미국 1센트를 준다.":
            jump liberation
        
        "2021년도 이순신이 그려진 100원을 준다.":
            jump slave

label liberation:
    
    scene room

    show ks_normal

    "나는 웃으며 말했다."

    m "이러는 편이 긴장감 있고 재밌잖아."

    k "어?"

    "경수는 당황한 것처럼 보였는데, 이내 웃음을 터뜨리고 말았다."

    k "그래, 재밌게 하자고."

    "나는 경수에게 백악관이 그려진 면이 위쪽으로 가게 동전을 손에 쥐여주었다."

    m "잘 하고 와."

    #동전소리 넣어야댐

    hide ks_normal
    "그렇게 경수가 동전을 튕겼다."

    "10분이 지나도 경수는 돌아오지 않았다."

    "나는 바닥에 떨어진 동전을 보았다."

    "1950년 미국 1센트. 링컨이 그려진 면이 위쪽으로 되어 있었다."

    scene black
    with dissolve

    "{b}해방{/b}."
    return

label slave:

    scene room

    show ks_normal

    m "아니야. 잘하고 와."

    "나는 경수에게 2021년도 100원을 주고 말았다."

    scene black
    with dissolve

    "역시나 경수는 실패했다. 아니 일부러 그런건가?"

    "고의였든 아니었든, 아무것도 달라진 게 없다."

    "나는 경수에게 화를 낼 수도 없다."

    "애초에 경수가 동전을 주지 않았다면 없었던 일이었다."

    "라고 정신승리라도 해야겠다."

    "{b}노예{/b}."
    return