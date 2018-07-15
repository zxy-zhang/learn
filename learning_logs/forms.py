from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
	class Meta:
		#包含一个内嵌类Meta，告诉django根据那个模型创建表单，以及在表单中包含哪些字段
		#根据模型创建一个表单
		model=Topic
		#该表单只包含字段text
		fields=['text']
		#让django不要为字段text生成标签
		labels={'text': ''}


class EntryForm(forms.ModelForm):
	class Meta:
		model =Entry
		fields =['text']
		labels ={'text':''}
		#定义了属性widghts（小部件）是一个HTML表单元素，如单行文本框，下拉列表
		#通过设置widghts属性，可以覆盖django选择的默认小部件
		#文本区域宽度设置为80列，而不是默认的40列
		widgets ={'text':forms.Textarea(attrs={'cols':80})}