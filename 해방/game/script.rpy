# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("나")
define k = Character("경수")

default chance = 3


# The game starts here.
label start:

    #jump year_2014

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

    hide ks_normal
    show ks_dark
    "또 그 소리, 뭘 잘못 먹었는지 1년전부터 계속 이 얘기를 한다."

    hide ks_dark
    show ks_normal

    k "아니 집에 도둑이 들어와서 내 인감이랑 민증을 들고 나가는 걸 똑똑히 봤거든?"

    k "근데 다시 보니까 그게 그대로 있었다니까?"

    m "잘못 본 거겠지. 꿈이라도 꾼 거 아니야?"

    hide ks_normal
    show ks_dark

    "그냥 적당히 받아주고 넘어가자. 괜히 신경 거슬려서 좋을 게 없다."

    hide ks_dark
    show ks_normal

    k "하... 아니다. 됐고, 이거나 받아라."

    "경수가 서랍장에서 고급스럽게 생긴 상자를 꺼내서 준다."

    "열어보니 동전들이 굉장히 많다."

    k "내가 예전에 취미로 모았거든? 버리려고 했는데 그냥 너 가져라."

    hide ks_normal
    show ks_dark

    "콩고물이 떨어진다."

    "당장 눈에 띄는 것은 1950년도 외화부터, 몇 개 없다는 1998년 500원까지,"

    "다 팔면 꽤나 큰 돈이 될 것 같다."

    hide ks_dark

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

    "이리 치이고 저리 치이다 보니 어느새 방으로 돌아와 있었다."

    show ks_normal

    k "야 너 뭐냐? 갑자기 사라졌다가 또 갑자기 튀어나왔어."

    k "정체가 뭐야? 초능력자 뭐 그런 건가?"

    m "헉...헉... 잠시만 숨 좀 고르고..."

    hide ks_normal
    show ks_dark

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

    hide ks_normal
    show ks_dark   

    "내 손에는 없다. 튕겼으니까 바닥에 떨어졌겠지."

    "아니나 다를까 바닥에 있다."

    #줍는 사운드?
    "경수가 먼저 주워서, 동전을 살펴본다."

    hide ks_dark
    show ks_normal

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

    hide ks_normal
    show ks_dark

    "비교적 최근이 좋겠어. 그리고 이번엔 익숙한 장소가 나오면 좋겠다."

    "2017년이 적당하겠다."
    jump year_2017


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

    jump after_2017

label after_2017:

    scene room

    show ks_normal

    k "어! 왔다."

    hide ks_normal

    scene black
    with dissolve

    "경수에게 2017년에서 했던 일을 설명했다."

    "이동하는 장소는 동전을 튕기기 전 생각한 장소로 이동하는 것 같고,"

    "타이머는 초기화되어 있었지만 대략 10분정도 과거에 머무르는 것 같다."

    "공원에 갔더니 돌도 그 자리에 있었다."

    scene room
    with dissolve

    show ks_normal

    k "야 진짜 어떻게 이런 일이 있을 수 있냐."

    m "그러게. 이걸로 뭔가 할 수 있을 것 같은데?"

    m "복권을 산다던가, 아니면 코인을 한참 전에 사는 거지."

    m "비트 코인이 발행된 2009년에 매수하는거야."

    k "코인에 돈을 그렇게 잃어 놓고, 아직도 정신을 못 차렸네."

    m "이번에는 성공해야지."

    hide ks_normal

    scene black
    with dissolve

    jump plan

label plan:

    "나는 계획을 세웠다."

    "코인을 직접 매수하는 것은 불가능하다고 생각했다."

    "현재 사용되는 지폐를 과거로 들고가면 그건 위조 지폐가 되는거니까,"

    "사용자체가 불가능하겠지."

    "따라서 직접 코인을 채굴해야한다."

    "처음에 코인 거래소 계좌를 만들고, 남은 연도 동안 계속해서 채굴하면 어마어마한 양이 모이겠지?"

    "2010년에 코인 거래소가 처음 개설되었으니까, 2011년부터 시작해야 한다."

    "그리고 2021년 대폭락 전에 모든 코인을 팔아버리는거지."

    "2017년도는 이미 사용했기 때문에, 주어진 기회는 9번. 대략 90분이다."

    jump before_2011

label before_2011:

    scene room

    show ks_normal

    k "그럼 이번에는 내가 한다?"

    m "갑자기 경수 니가 한다고?"

    k "안돼?"

    hide ks_normal
    show ks_dark

    "아. 안된다. 경수를 거스를 수는 없다."

    "경수는 윗면이고, 내가 아랫면이니까."

    "경수가 날 쳐내려고 하면 항상 쳐낼 수 있다."

    "하지만 그 반대는?"

    "상상조차 할 수 없다."

    show ks_normal
    hide ks_dark

    k "아니 나도 시간 여행은 해봐야지. 너만 좋은 거 하냐?"

    m "그래. 그럼 그렇게 해."

    show ks_dark
    hide ks_normal

    "나는 경수에게 계획을 설명해줬다."

    "2011년에 계좌 생성."

    "2012년부터 2020년까지 최대한 코인을 채굴한다."

    "...마지막으로 2021년에 전량 매도."

    hide ks_dark

    scene black
    with dissolve

    scene room
    with dissolve

    "실수를 하면 안 되니까 예행 연습도 했다."

    "2011년에 우리는 미성년자니까, 우리 명의로는 계좌를 만들 수 없다."

    "따라서 계좌 생성을 위한 명의는 경수의 부모님 것으로 하기로 했다."

    show ks_normal

    "난 경수에게 2011년도 100원을 줬다."

    m "잘해."

    k "...알아서 할게."

    play sound "coin.mp3"

    scene white
    with dissolve

    "경수가 동전을 튕겼다."

    scene room
    with dissolve

    "...그리고 사라졌다."

    "솔직히 말해서 좀 걱정이다."

    "경수는 별로 계획에 관심이 없는 것 같다."

    "애초에 돈도 많은 애가 굳이 내 계획을 따라줄 필요가 있을까?"

    scene black
    with dissolve

    "10분이 지나고 경수가 돌아왔다."

    jump after_2011

label after_2011:
    scene room
    with dissolve

    show ks_normal

    k "실패했어."

    m "왜?"

    k "주변에 컴퓨터가 없었어. 그리고 폰도 인터넷 접속이 안돼."

    hide ks_normal
    show ks_dark

    "맞다. 깜빡하고 있었다. 당연히 폰은 못쓰지."

    show ks_normal
    hide ks_dark

    m "계획을 좀 바꿔야겠어."

    hide ks_normal

    scene black
    with dissolve

    scene room
    with dissolve

    show ks_normal

    m "노트북을 2007년으로 가서 숨겨놓는 건 어때?"

    k "우리 집 창고에다가 숨겨놓자. 거기 아무도 안 써."

    m "그러면 일단 창고로 가보자."

    k "그래. 동전 챙겨라."

    #move sound

    scene black
    with dissolve

    scene storage
    with dissolve

    m "콘센트도 있고, 인터넷 선도 있네?"

    show ks_normal

    k "옛날부터 있었을거야."

    m "그러면 노트북을 2007년에 여기다 숨기고, 인터넷이 되나 확인해보자."

    m "그리고 2012년에 거래소 계좌를 만들면 될 것 같아."

    k "좋아, 해보자고."

    play sound "coin.mp3"

    scene white
    with dissolve

    "경수가 2007년도 동전을 튕겼다."

    scene storage
    with dissolve

    "걱정이 된다..."

    "그래도 노트북만 두고 오면 되는거니까 이번엔 잘하겠지?"

    scene black
    with dissolve

    "10분이 지나고 경수가 돌아왔다."

    jump after_2007

label after_2007:

    scene storage

    show ks_normal

    k "잘 숨겨놓고 왔어."

    m "인터넷은 잘 돼?"

    k "어. 콘센트 전원도 들어오더라."

    m "좋아. 그럼 바로 2012년으로 가자."

    m "가서 계좌만 만들면 돼."

    hide ks_normal
    show ks_dark

    "나는 경수에게 2012년도 동전을 건넸다."

    show ks_normal
    hide ks_dark

    k "조금만 쉬었다가 할까?"

    show ks_dark
    hide ks_normal

    "아. 제발. 대체 왜 그러는 거야."

    show ks_normal
    hide ks_dark

    m "힘들면 그냥 내가 할게."

    k "왜 그렇게 재촉하냐?"

    k "누가 훔쳐 가기라도 할 거 같애?"

    m "그냥 마음이 급해서 그래."

    k "천천히 해. 느긋하게."

    show black
    with dissolve

    "그래. 넌 느긋하겠지."

    "어차피 돈은 썩을대로 넘쳐나니까."

    "하지만 난 아냐."

    "이번 기회를 놓치면 난 평생 후회하겠지."

    "절대로 실패하면 안되는 일이라고."

    play sound "coin.mp3"

    scene white
    with dissolve

    scene storage
    with dissolve

    "뭐야?"

    "지금 말도 안하고 간거야?"

    "하... 이젠 완전히 제멋대로잖아?"

    "하긴 나한테 굳이 말해야 된다고 생각하지도 않겠지."

    "슬슬 화가 난다. 아무리봐도 이대로 가면 계획은 실패한다."

    "뭔가 대책을 세워야겠어."

    scene white
    with dissolve
    
    "경수가 돌아왔다. 꽤 피곤해보인다."

    scene storage
    with dissolve

    show ks_normal

    k "계좌 만들었어. 이거 생각보다 쉽네?"

    m "연습도 했으니까. 다음 꺼가 제일 중요해."

    m "이건 내가 할게."

    k "그러시던가."

    show ks_dark
    hide ks_normal

    "코인 채굴."

    "2023년 최신형 게이밍 노트북이기 때문에,"

    "10년도의 데스크탑보다 성능이 월등히 좋다."

    "그리고 과거의 코인 채굴 알고리즘은 현재보다 훨씬 단순하다."

    "따라서 1년간 가동하더라도 과부하가 안 걸릴 거야."

    "가서 10분 안에 노트북을 켜서 코인 채굴 프로그램을 설치하고,"

    "거래소 계좌를 연결한 다음에,"

    "프로그램 작동 버튼만 누르면 된다."

    "그러면 1년동안 알아서 코인이 채굴되겠지?"

    "좋아. 가보자."

    scene storage

    "그런데 2013년도 동전이... 안 보인다."

    m "2013년도가 없는데?"

    show ks_normal
    hide ks_dark

    k "없으면 없는 거야. 항상 모으진 않았으니까."

    show ks_dark
    hide ks_normal

    "아. 이런 젠장. 기회가 또 한 번 줄었다."

    show ks_normal
    hide ks_dark

    k "야, 표정이 왜 그렇냐?"

    m "아니야."

    show ks_dark
    hide ks_normal

    "다행히 14년부터는 동전이 다 있다."

    "남은 기회는 6번."

    "솔직히 이제 경수는 믿을 수 없다."

    "애가 생각이 없다. 이게 어떤 기회인지도 모르는 것 같다."

    "후.. 일단 집중하자."

    "2014년도 동전을 튕겼다."

    play sound "coin.mp3"

    scene white
    with dissolve

    "진짜 엄청 눈부시네."

    jump year_2014

label year_2014:

    scene storage_past
    with dissolve

    "일단 타이머부터 맞추자."

    "타이머를 10분으로 설정했다."

    "빨리 해야겠다."

    #꺼내는 사운드

    "노트북에 인터넷 선을 연결하고, 전원 선도 연결했다."

    "전원을 키고... 이제부터가 중요하다."

    jump year_2014_choice_1

label year_2014_choice_1:

    if chance < 0:
        jump year_2014_fail

    menu:

        "우선..."

        "채굴 프로그램을 설치한다.":
            "좋아, 설치 완료."
            jump year_2014_choice_2

        "거래소 계좌를 생성한다.":
            "계좌는 이미 만들었잖아? 이게 아니지."

            if chance == 1:
                "시간 상 다음 번이 마지막 기회일 것 같다."
                "한 번만 더 실수하면 끝이야."
            elif chance != 0:
                "후... 다시 집중하자. 기회는 많지 않다."

            $ chance -= 1
            jump year_2014_choice_1


label year_2014_choice_2:

    if chance < 0:
        jump year_2014_fail

    menu:

        "그 다음은..."

        "프로그램을 작동 버튼을 누른다.":
            "- 오류가 발생했습니다 : 계좌가 연결 돼 있지 않음. -"
            "아. 실수했다."

            if chance == 1:
                "시간 상 다음 번이 마지막 기회일 것 같다."
                "한 번만 더 실수하면 끝이야."
            elif chance != 0:
                "후... 다시 집중하자. 기회는 많지 않다."
    
            $ chance -= 1
            jump year_2014_choice_2

        "프로그램에 거래소 계좌를 연결한다.":
            "좋았어. 이제 마지막이다."
            jump year_2014_choice_3

label year_2014_choice_3:

    if chance < 0:
        jump year_2014_fail

    menu:

        "마지막으로..."

        "프로그램을 작동 버튼을 누른다.":
            "좋았어. 다 끝났다."
    
            jump year_2014_complete

        "거래소를 켠다.":

            "아, 거래소를 켜버렸네."
            "한창 매매할 때는 컴퓨터 키면 무조건 거래소부터 켰었지..."

            if chance == 1:
                "시간 상 다음 번이 마지막 기회일 것 같다."
                "한 번만 더 실수하면 끝이야."
            elif chance != 0:
                "후... 다시 집중하자. 기회는 많지 않다."
            $ chance -= 1

            jump year_2014_choice_3

label year_2014_fail:

    scene white
    with dissolve
    
    scene storage
    with dissolve

    "아!!!"

    show ks_normal

    k "성공했어?"

    m "아니."

    k "뭐야, 못 했어?"

    m "실수를 좀 많이 했어."

    m "다음 번에는 꼭 성공해야지."

    k "또 니가 가게?"

    k "이번에는 내 차례지."

    m "뭐? 이젠 기회가 몇 번 안 남았어."

    m "절대로 실수하면 안 된다고. 니가 가면 안 돼."

    show ks_angry

    k "내가 무조건 실수할 것처럼 말을 하네?"

    "아차."

    k "그렇게 중요한 일이었으면 니가 처음부터 성공했어야지."

    k "그리고 니가 못 했으면 나도 못 할 수도 있는거 아니냐?"

    k "하... 됐다."

    k "야, 나가."

    m "...어?"

    k "못 들었어? 꺼지라고."

    m "알겠어."

    hide ks_angry

    scene black
    with dissolve

    "급하게 나오느라 아무 것도 챙기지 못했다."

    "동전을 챙겨나왔어야 했는데."

    "지금이라도 가서 동전이라도 달라고 할까?"

    "..."

    "생각해보니 더 이상 경수 밑에 못 붙어있겠네."

    "...하."

    "거기서 실수만 안 했으면 됐을텐데."

    scene white
    with dissolve

    "일주일 뒤"

    scene black
    with dissolve

    "몇 일이 지나도 경수는 전화를 받지 않는다."

    "직접 찾아가도 반응도 없다."

    "아무래도 난 버림받은 것 같다."

    "한 순간의 실수로 인생 역전의 기회를 놓쳐버렸다."

    "경수도 이젠 나와 아무 관계도 아니다."

    "이젠 나한테 남은 게 없다."

    "{b}버려짐{/b}."

    return

label year_2014_complete:

    "휴, 잘 되네."

    "채굴 프로그램이 정상적으로 작동하고 있다."

    "이제 계속 확인만 하면 되겠다."

    "시간도 거의 다 됐네."

    "휴..."

    "마음이 조금 놓인다. 역시 직접하는게 훨씬 안심이 된다."

    scene white
    with dissolve

    jump year_2014_after

label year_2014_after:

    scene storage
    with dissolve

    show ks_normal

    m "제대로 설치했고, 이제 확인만 하면 돼."

    k "그러면 1년 동안 코인을 채굴하는 거야?"

    m "어. 이제 잘 돌아가고 있는지 확인만 하면 돼."

    scene black
    with dissolve

    "생각보다 시간 여행은 너무 피곤해서 나는 잠시 쉬기로 했다."

    "내가 쉬는 동안 경수는 2015년, 2016년에 다녀왔다."

    "아무 일도 없었고 노트북도 잘 작동하고 있다고 했다."

    "다행이다..."

    "그리고 쉬는 동안 인터넷에서 중요한 사실을 하나 알아냈다."

    "지금 쓰고 있는 채굴 프로그램은 2017년까지만 사용이 가능하다고 한다."

    "그러면 2018년으로 가서 프로그램을 다른 걸로 업데이트 해야 한다."

    scene storage
    with dissolve

    m "2018년부터는 내가 갈게."

    show ks_normal

    k "그래. 난 좀 쉬어야겠다."

    show ks_dark
    hide ks_normal

    "다행이다. 중요한 일은 너한테 못 맡기겠거든."

    "나는 2018년도 평창 동계 올림픽 기념 주화를 튕겼다."

    play sound "coin.mp3"

    scene white
    with dissolve

    jump year_2018

label year_2018:

    scene storage_past
    with dissolve

    "역시나."

    "노트북은 켜져 있었지만 프로그램은 작동하고 있지 않았다."

    "미리 조사하고 오길 잘했다."

    "바로 새로운 프로그램을 설치하고, 실행시켰다."

    "여태까지 채굴한 코인을 보니 143개였다."

    "가장 높을 때 기준인 7400만원에 전량 매도를 한다면..."

    "상상만 해도 행복하다."

    "다만 약간 걱정이 되는 점이 있다."

    "노트북이 확실히 느려졌다."

    "아무리 오버 스펙이라지만 3년 동안이나 계속 코인을 채굴했는데,"

    "고장이 안 난 것이 신기하다."

    scene white
    with dissolve

    "시간이 다 됐나 보다."

    jump after_2018

label after_2018:
    
    scene storage
    with dissolve

    "나는 돌아오자마자 2019년도 동전을 찾아서 상자를 뒤졌다."

    show ks_normal

    k "느긋하게 하라니까, 성질 급하기는."

    show ks_dark
    hide ks_normal

    "하... 왜 시비지?"

    "도움도 안 될거면 가만히라도 있던가."

    show ks_normal
    hide ks_dark

    m "재밌어서 그래."

    show ks_dark
    hide ks_normal

    "절대로 화내면 안된다."

    "참아야한다. 계획만 성공하면 된다."

    "동전은... 여기있었네."

    "나는 바로 2019년도 동전을 튕겼다."

    play sound "coin.mp3"

    scene white
    with dissolve

    jump year_2019

label year_2019:

    scene storage_past
    with dissolve

    "역시... 그럼 그렇지."

    "아니나 다를까 노트북이 꺼져있다."

    "전원 버튼을 눌러봤지만 노트북은 켜지지 않는다."

    "드디어 고장이 나버렸다."

    "다음 계획을 세워야겠다."

    scene black
    with dissolve

    "2020년에 스마트폰 용 코인 거래소 어플이 출시됐으니까,"

    "2020년으로 가서 공유기를 설치하면 인터넷이 되겠지?"

    "그리고 2021년으로 가서 어플을 설치하고 코인을 싹 다 팔면 될 것 같다."

    "다만 어플을 설치하고, 계좌를 연결하고, 코인을 파는 것까지."

    "전부 다 하려면 시간이 너무 촉박할 것 같다."

    scene white
    with dissolve

    "실수를 하면 안 될 것 같다."

    jump after_2019

label after_2019:

    scene storage
    with dissolve

    "나는 창고로 돌아와서 계획을 경수에게 설명했다."

    show ks_normal

    k "그러면 공유기 설치는 너가 하고, 코인을 내가 팔게."

    show ks_dark
    hide ks_normal

    "뭐라고? 안돼. 절대 안돼."

    "이번에는 실수하면 기회가 없다고."

    "라는 말이 입에 맴돌지만 절대로 밖으로 나오지 않는다."

    "한심하다."

    "나는 이런 상황에서도 경수의 눈치를 볼 수밖에 없는 것이다."

    m "알았어."

    "결국 알겠다고 해버렸다."

    show ks_normal
    hide ks_dark

    k "공유기는 창고에 있는 거 저거 쓰면 될거야."

    show ks_dark
    hide ks_normal

    "흠..."

    "솔직히 경수에게 맡기면 실패할 것 같다."

    "아니, 무조건 실패한다."

    "어떻게 해야하지?"

    "모르겠다. 일단 공유기부터 설치하고 생각해야겠다."

    play sound "coin.mp3"

    scene white
    with dissolve

    "공유기를 챙겨서 2020년도 동전을 튕겼다."

    jump year_2020

label year_2020:

    scene storage_past
    with dissolve

    "우선 공유기부터 설치하자."

    scene black
    with dissolve

    "계획대로 공유기를 설치했다."

    "남는 시간동안 웃긴 사실이 떠올랐다."

    "결국 2021년에 140개 이상의 코인을 팔아버렸으니까,"

    "그런 대폭락이 발생한게 아닐까?"

    "내 티끌만한 돈도 앗아간 대폭락이,"

    "결국 내가 계획한 일이라는 거잖아?"

    "나는 혼자 한참을 웃었다."

    jump finale

label finale: 
    play music "theme.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene white
    with dissolve

    scene storage
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "창고로 돌아왔다. 이젠 정말 마지막이다."

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
    
    scene storage

    show ks_dark

    "나는 웃으며 말했다."

    m "이러는 편이 긴장감 있고 재밌잖아."

    show ks_normal
    hide ks_dark

    k "어?"

    "경수는 당황한 것처럼 보였는데, 이내 웃음을 터뜨리고 말았다."

    k "그래, 재밌게 하자고."

    show ks_dark
    hide ks_normal

    "나는 경수에게 백악관이 그려진 면이 위쪽으로 가게 동전을 손에 쥐여주었다."

    show ks_normal
    hide ks_dark

    m "잘 하고 와."

    play sound "coin.mp3"

    scene white
    with dissolve

    scene storage
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

    scene storage

    show ks_normal

    m "아니야. 잘하고 와."

    show ks_dark
    hide ks_normal

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