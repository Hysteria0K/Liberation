# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("나")
define k = Character("경수")


# The game starts here.
label start:

    scene black

    "동전을 던지면 경우의 수는 두가지이다."

    "한 면은 위로 가고, 다른 한 면은 바닥에 깔리겠지."

    show ks_normal
    with dissolve

    "경수는 위쪽 면이다. 재벌 2세, 다이아 수저, 무슨 사고를 쳐도 수습이 된다."

    "한 번은 사람을 죽도록 때려서 기절시켰는데, 그냥 조서만 쓰고 풀려났다."

    hide ks_normal
    with dissolve

    "반면에 나는 아래쪽 면이다. 우리 집은 그렇게 잘 사는 편이 아니다."

    "나를 책임져줄 사람도 없다. 주변의 권유로 시작한 코인 거래도 2년전 급폭락때 다 잃었다."

    scene room
    with dissolve

    "그나마 내가 내세울 게 있다면, 경수랑 친하다는 것이다."

    jump prologue

label prologue:

    scene room
    show ks_normal

    k "야, 다시 생각해봐도 말이 안 되지 않냐?"

    # 속 마음 얘기할 때 경수 약간 채도 낮춰서 하면 좋을 거 같음
    "또 그 소리, 뭘 잘못 먹었는지 1년전부터 계속 이 얘기를 한다."

    k "아니 집에 도둑이 들어와서 내 인감이랑 민증을 들고 나가는 걸 똑똑히 봤거든?"

    k "근데 다시 보니까 그게 그대로 있었다니까?"

    m "잘못 본 거겠지. 꿈이라도 꾼 거 아니야?"

    "그냥 적당히 받아주고 넘어가자. 괜히 신경 거슬려서 좋을 게 없다."

    k "하... 아니다. 됐고, 이거나 받아라."

    "경수가 서랍장에서 고급스럽게 생긴 상자를 꺼내서 준다."

    "열어보니 동전들이 굉장히 많다."

    k "내가 예전에 취미로 모았거든? 버리려고 했는데 그냥 너 가져라."

    "콩고물이 떨어진다. 당장 눈에 띄는 것은 1950년도 외화부터, 몇 개 없다는 1998년 500원까지,"

    "다 팔면 꽤나 큰 돈이 될 것 같다."

    m "아니 뭘 이런 걸 다 주냐."

    "나는 동전을 아무거나 하나 잡아서 튕겼다."

    play sound "coin.mp3"

    scene white
    with dissolve

    "그 순간, 눈 앞이 하얘졌다."



label finale: 
    play music "theme.mp3"
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

    play sound "coin.mp3"
    hide ks_normal
    with dissolve

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