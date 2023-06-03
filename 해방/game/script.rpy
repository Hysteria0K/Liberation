# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("나")
define k = Character("경수")


# The game starts here.
label start:

    jump year_2017

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

    "콩고물이 떨어진다."

    "당장 눈에 띄는 것은 1950년도 외화부터, 몇 개 없다는 1998년 500원까지,"

    "다 팔면 꽤나 큰 돈이 될 것 같다."

    m "아니 뭘 이런 걸 다 주냐."

    "나는 동전을 아무거나 하나 잡아서 튕겼다."

    play sound "coin.mp3"

    scene white
    with dissolve

    "그 순간, 눈 앞이 하얘졌다."

    jump year_2002

label year_2002:

    scene black
    with dissolve

    "무심코 눈을 감았다가, 다시 떴을 때 나는 놀라지 않을 수 없었다."

    scene year_2002_bg
    with dissolve

    "대~한민국!! 둥둥둥둥둥 대~한민국!!! 둥둥둥둥둥"

    scene year_2002_bg_dark

    "힘들다. 숨이 잘 안 쉬어진다. 속이 울렁거린다."

    "너무 시끄럽고, 사람이 너무 많다. 정신을 차릴 수가 없다."

    scene white
    with dissolve

    scene room
    with dissolve

    "이리 치이고 저리 치이다 보니 어느새 경수의 방으로 돌아와 있었다."

    show ks_normal

    k "야 너 뭐냐? 갑자기 사라졌다가 또 갑자기 튀어나왔어."

    k "정체가 뭐야? 초능력자 뭐 그런 건가?"

    m "헉...헉... 잠시만 숨 좀 고르고..."

    "너무 힘들다. 잠깐만 쉬어야겠다."
    scene black
    with dissolve

    jump main

label main:
    
    scene room
    with dissolve

    show ks_normal

    k "그래서 방금 그건 뭐였는데?"

    m "그니까 동전을 튕겼는데... 갑자기 눈 앞이 하얘지더니 웬 도로 한복판인거야."

    m "그리고 주변에 사람이 엄청 많았고, 다들 소리를 질러 댔어."

    k "그 동전 어딨냐?"

    "내 손에는 없다. 튕겼으니까 바닥에 떨어졌겠지."

    "아니나 다를까 바닥에 있다."

    #줍는 사운드?
    "경수가 먼저 주워서, 동전을 살펴본다."

    k "너 혹시 아까 사라졌을 때 사람들이 다 빨간 옷 입고 있었냐?"

    hide ks_normal

    scene year_2002_bg_dark
    with dissolve


    m "그런 것 같기도 하고, 어렴풋이 기억나는 건 응원가가 들렸던 것 같은데... 잘 모르겠다."

    k "그럼 맞네!"

    scene room
    with dissolve

    show ks_normal

    "경수가 이쪽으로 동전을 보여준다. 별거 아닌 10원인데, 제조연도는 2002년이다."

    k "이거 동전을 튕기면 제조연도로 시간여행 하는거 같은데?"

    m "그래?"

    play sound "coin.mp3"

    m "아무 일도 안 일어나는데?"

    k "다른 동전으로 해봐. 이미 쓴 거는 안 되나 보지."

    menu:

        "비교적 최근 걸로 하자. 그리고 이번엔 익숙한 장소가 나오면 좋겠다."

        "2017년도 동전":
            jump year_2017

        "2022년도 동전":
            #여기서 분기점 - 경수 인감, 민증 털기(나중에 담구기 힌트)
            jump another

label year_2017:

    play sound "coin.mp3"

    scene white
    with dissolve

    "다시 눈 앞이 하얘졌다."

    scene street
    with dissolve

    "눈을 떴을 때, 익숙한 풍경이 눈 앞에 보였다."

    m "우리 집 근처잖아?"

    "익숙한 장소를 생각해서 그런가?"

    "아 맞다, 타이머 맞춰야지."

    "나는 손목시계의 타이머를 맞췄다. 타이머를 맞춰두면 얼마동안 과거로 가 있는지 알 수 있겠지."

    "어? 잠깐만."
    
    "순간 나는 당연하지만 잊고 있던 사실을 하나 떠올렸다."

    "과거를 바꾸면 미래도 바뀌지 않을까?"

    "이걸 어떻게 확인해보지?"

    scene black
    with dissolve

    scene street
    with dissolve

    "음, 좋은 생각이 났다."

    "근처 공원으로 가야겠다."

    scene park

    "여기 큰 나무 밑에 돌을 하나 뭍어둬야겠다."

    "원래 시간으로 돌아갔을 때 돌이 그대로 있다면, 과거를 통해 미래를 바꿀 수 있는 거 겠지?"

    m "제발 됐으면 좋겠다..."

    "시간은 얼마나 됐지?"

    "9분 30초?"

    "생각보다 꽤 기네?"

    scene white
    with dissolve

    scene room
    with dissolve

    "라고 생각했는데 어느샌가 방으로 돌아왔다."

label another:
    "아직 안만들었음"

    jump year_2017
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