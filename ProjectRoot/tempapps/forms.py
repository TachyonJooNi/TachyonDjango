# 장고에서 form을 사용하기 위한 임포트
from multiprocessing.sharedctypes import Value
from django import forms

'''
장고에서 제공하는 Form기능을 사용하려면 우선 forms.Form 클래스를 상속한다.
각 변수명은 해당 input태그의 name속성값으로 사용된다.
태그 생성시 required 속성이 포함되어 기본적인 빈값에 대한 검증을 하게된다.
'''
class QuestionForm(forms.Form):
    # <input type=text >를 생성한다. label은 타이틀로 사용한다. max_length=제한글자수
    user_id = forms.CharField(label='아이디', max_length=10)
    # 가장 기본적인 input태그를 생성한다. label이 없으므로 변수명을 타이틀로 사용한다.
    title = forms.CharField()
    # 여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성한다.
    content = forms.CharField(widget=forms.Textarea)
    # 기본적인 input 태그를 생성하되 type=email로 지정된다.
    email = forms.EmailField()
    # <input type=checkbox> 를 생성한다. required=False이므로 유효성 검증을 하지 않는다.
    my_check = forms.BooleanField(required=False)
    
    #######################################################################################
    # 교안 이외의 코드 추가
    # <input type="text" name="form01" required="" id="id_form01">
    form01 = forms.CharField(widget=forms.TextInput)
    
    # <input type="number" name="form02" required="" id="id_form02">
    form02 = forms.CharField(widget=forms.NumberInput)
    
    # 추가적인 속성을 부여할때는 위젯에 attrs를 추가하면 된다.
    # 속성을 추가할때는 ,(콤마)로 구분하면 된다.
    # <input type="password" name="form03" size="30" value="1234" required="" id="id_form03">
    form03 = forms.CharField(widget=forms.PasswordInput(attrs={'size':30, 'value':1234}))

    # <textarea name="form04" cols="40" rows="10" required="" id="id_form04"></textarea>
    form04 = forms.CharField(widget=forms.Textarea)
    
    
    '''
    select태그를 표현한다.(1개선택)
        choices : <select>의 <option>태그를 구성하는 데이터를 사용한다.
            순서대로 value, text로 사용된다.
        initial : 해당 태그의 default값으로 사용한다. 주로 수정에서 활용할 수 있다.
        
        <select name="form05" id="id_form05">
            <option value="red">빨강</option>
            <option value="green">녹색</option>
            <option value="blue" selected="">파랑</option>
            <option value="black">검정</option>
        </select>
    '''
    data01 = [
        ('red', '빨강'), ('green', '녹색'), ('blue', '파랑'), ('black', '검정')
    ]
    form05 = forms.ChoiceField(
        widget=forms.Select,
        choices=data01,
        initial='blue'
    )
    
    '''
    위와같은 <select>태그이지만 multiple속성이 부여된 항목으로 2개이상의
    항목을 선택할 수 있다.
    또한 default값을 표현하기 위해 2개 이상의 항목을 표현할 수 있어야 하므로
    리스트를 사용한다.
    
    <select name="form06" required="" id="id_form06" multiple="">
        <option value="red">빨강</option>
        <option value="green">녹색</option>
        <option value="blue" selected="">파랑</option>
        <option value="black" selected="">검정</option>
    </select>
    '''
    form06 = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=data01,
        initial=['blue', 'black']
    )
    
    
    # <input type="radio" name="form07" value="green" required="" id="id_form07_1" checked="">
    form07 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=data01,
        initial='green',
    )
    
    # <input type="checkbox" name="form08" value="red" id="id_form08_0" checked="">
    form08 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=data01,
        initial=['red', 'green']
    )
    
    # 파일 속성
    form09 = forms.FileField(
        widget=forms.FileInput,
        label="첨부파일"
    )
    
    
    
# 게시판 글쓰기 페이지 UI구현하기
class WriteForm(forms.Form):
    # <input type=text> 로 출력
    name = forms.CharField(
        label='작성자',
        widget=forms.TextInput(attrs={'class':'form-control w100'})
    )
    # <input type=password> 로 출력
    passwd = forms.CharField(
        label='패스워드', 
        widget=forms.PasswordInput(attrs={'class':'form-control w150'})
    )
    title = forms.CharField(
        label='제목', 
        widget=forms.TextInput(attrs={'class':'form-control w200'})
    )
    # <textarea> 로 출력
    content = forms.CharField(
        label='내용', 
        widget=forms.Textarea(attrs={'class':'form-control'})
    )
    # <input type=file> 로 출력
    chumfile = forms.FileField(
        label='첨부파일', 
        widget=forms.FileInput(attrs={'class':'form-control'})
    )
    
    
''' 
내가한거
class WriteForm(forms.Form):
    user_id = forms.CharField(label='작성자', max_length=15)
    password = forms.CharField(label='패스워드', max_length=15)
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)
    my_check = forms.FileField(label='첨부파일', required=False)
'''    
    
    
    
    
    
    
    
    