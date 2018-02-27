# import ModelSerializer and SerializerMethodField from rest_framework.serializers
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

#import all of the models
from ..models import Question, Choice

#Model Serializer of Question
class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It should also include a field "choices" that will serialize all the
        choices for a question
    You well need a SerializerMethodField for choices,
        http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    Reference this stack overflow for the choices:
        https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field
    """

#Declare class attribute from child model/table to be serialized
    choices = SerializerMethodField()#serialize choices for given question

#Declare metaclass and specify meta behavior
    class Meta:
        model = Question
        fields = ('id','text', 'pub_date', 'choices')   #list of fields in the Question Model
                                                        #with reference to foreign entity 'choices'

#Declare attribute functions for getting out serializable data from child table/model
    def get_choices(self, obj):
        choices = obj.choice_set.all()
        return ChoiceSerializer(choices, many=True).data

#Model Serializer of Choice
class ChoiceSerializer(ModelSerializer):
    '''
    This serializes the Choice model
    '''
    class Meta:
        model = Choice
        fields = ('choice_text','votes')
