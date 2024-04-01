import sys
import re
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/google_ui.ui")[0]
# 디자인한 외부 ui파일 불러와서 저장

class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출
        self.setupUi(self)  # 불러온 ui파일을 연결

        self.setWindowTitle("구글 한줄 번역기")  # 윈도우 타이틀
        self.setWindowIcon(QIcon("icon/google.png"))  # 윈도우 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 Made By Gyojincompany")  # 윈도우 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action)  # signal
        self.init_btn1.clicked.connect(self.init1_action)
        self.init_btn2.clicked.connect(self.init2_action)


    def trans_action(self):  # 번역 실행 함수 -> slot 함수
        korText = self.kor_input.text()  # kor_input에 입력된 한글 텍스트 가져오기
        reg = re.compile('[가-힣]')  # 한글만 찾는 정규표현식

        if korText == "":
            print("공백입력!!")
            QMessageBox.warning(self, "입력오류!","한글입력란에 번역할 문장을 넣어주세요.")
        elif korText != reg:  # 한글인지 아닌 여부 확인(숫자 또는 영어로만 입력시 경고창 출력)
            print("한글아닌 문자 입력!!")
            QMessageBox.warning(self, "입력오류!", "한글입력란에는 한글만 넣어주세요.")
        else:
            print("정상번역결과 출력!!")
            trans = googletrans.Translator()  # 구글트랜스 모듈의 객체 선언
            # print(googletrans.LANGUAGES) -> 번역 언어의 dest 약자 찾기

            engText = trans.translate(korText, dest="en")  # 영어 번역 결과
            japText = trans.translate(korText, dest="ja")  # 일본어 번역 결과
            chnText = trans.translate(korText, dest="zh-cn")  # 중국어 번역 결과

            self.eng_input.append(engText.text)
            # 번역된 영어 텍스트를 eng_input에 출력
            self.jap_input.append(japText.text)
            self.chn_input.append(chnText.text)

    def init2_action(self):  # 전체초기화 버튼 함수
        self.kor_input.clear()  # 입력 내용 지우기
        self.eng_input.clear()
        self.jap_input.clear()
        self.chn_input.clear()

    def init1_action(self):  # 입력초기화 버튼 함수
        self.kor_input.clear()  # 입력 내용 지우기


if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())
        







