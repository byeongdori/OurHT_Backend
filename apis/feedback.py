# 피드백 함수들 로직 구현 중

def feedback_squrt():

    # check_head() - 목 & 머리 체크 함수
    '''
    허리 - 등 - 목으로 이어지는 직선 체크
    측면에서 귀의 좌표가 찍히는지?
    '''
    # check_back() - 등 체크 함수
    '''
    배경 제거 이미지와 응용하여 등의 굽음 측정
    '''
    # check_waist() - 허리 체크 함수
    '''
    무릎과 골반 좌표 활용해, 너무 앉거나 일어서지는 
    않았는지 체크
    '''
    # check_knee() - 무릎 체크 함수
    '''
    발목과의 좌표 비교, 굳이 발 끝이 아니여도 된다
    '''
    # check_dynamic() - 동적 정보 체크 함수
    '''
    어깨가 위 아래로만 왔다갔다 하는지
    즉, 일정하게 몸이 위아래로 움직이는지
    '''
    pass

def feedback_pushup():

    # check_head() - 목 & 머리 체크 함수
    '''
    스쿼트에서 쓰는 목 & 머리 체크 방식과 동일할 듯
    '''
    # check_back() - 등 체크 함수
    '''
    스쿼트에서 쓰는 등 체크 방식과 동일할 듯
    '''
    # check_elbow() - 팔꿈치 체크 함수
    '''
    팔꿈치의 위치가 몸통 위에서 1/3 지점(정확히 체크)
    어깨&골반&팔꿈치 좌표 활용하여 판단
    '''
    # check_lower_body() - 하반신 체크 함수
    '''
    골반 - 무릎 - 발목이 잘 이어지나 체크
    '''
    # check_dynamic() - 동적 정보 체크 함수
    '''
    좌표변화가 가장 큰 어깨 기준으로 가동범위 판단
    온 몸이 균일하게 잘 내려가고 올라오는지!
    '''
    pass

def feedback_plank():

    # check_head() - 목 & 머리 체크 함수
    '''
    스쿼트에서 쓰는 목 & 머리 체크 방식과 동일할 듯
    '''
    # check_shoulder() - 어깨 체크 함수 -> 필요한가?
    # check_elbow() - 팔꿈치 체크 함수
    '''
    푸쉬업에서 쓰는 팔꿈치 체크 방식과 동일할 듯
    '''
    # check_dynamic() - 동적 정보 체크 함수
    '''
    초기 자세를 기준으로, 
    몸의 자세가 흐트러지지 않는지 판단
    '''
    pass
