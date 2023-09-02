from typing import Any
from django.db import models
from datetime import datetime
from rest_framework.serializers import *


class ForwardRelationSerializer(ModelSerializer):
    def create(self, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many={}

        others = {}
        for field_name, field_value in validated_data.items():
            if field_value:
                if field_name in info.forward_relations:
                    field_info = info.forward_relations[field_name]
                    if field_info.to_many:

                        try:
                            serializer = serializer = self.fields[field_name].child

                            serializer = self.fields[field_name].child.__class__(data=field_value, many=True)
                            if serializer.is_valid():
                                field_instance = serializer.save()
                                many_to_many[field_name] = field_instance
                            else:
                                raise ValidationError(serializer.errors)
                        except:
                            
                            others[field_name] = field_value
                    else:
                        try:
                            serializer = self.fields[field_name].__class__(data=field_value)
                            if serializer.is_valid():
                                field_instance = serializer.save()
                                others[field_name] = field_instance
                            else:
                                raise ValidationError(serializer.errors)   
                        except:
                            others[field_name] = field_value 
                else:
                    others[field_name] = field_value  

        
        instance = super().create(others)

        for field_name, field_value in many_to_many.items():
            field = getattr(instance, field_name)
            field.set(field_value)

        print(f"{instance} is saved successfully!")
        return instance
    

    def update(self, instance, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many={}
        others = {}
        for field_name, field_value in validated_data.items():
            if field_name in info.forward_relations:
                field_info = info.forward_relations[field_name]
                if field_info.to_many:
                    
                    try:
                        serializer = self.fields[field_name].child.__class__(data=field_value, many=True)
                        if serializer.is_valid():
                            
                            getattr(instance, field_name).all().delete()
                            field_instance = serializer.save()
                            field = getattr(instance, field_name)
                            field.set(field_instance)
                        else:
                            raise ValidationError(serializer.errors)
                        
                    except:
                        # if the field was non (saving instance of None field)
                        field = getattr(instance, field_name)
                        field.set(field_value)
                else:
                    try:
                        serializer = self.fields[field_name].__class__(getattr(instance, field_name), data=field_value)
                        if serializer.is_valid():
                            field_instance = serializer.save()
                            others[field_name] = field_instance
                        else:
                            raise ValidationError(serializer.errors)  
                    except:
                        others[field_name] = field_value
                     
            else:
                others[field_name] = field_value  

        instance = super().update(instance, others)
        print(f"{instance} is updated successfully!")
        return instance
    
class ComplexSerializer(ForwardRelationSerializer):
    def __init__(self, *args, **kwargs):
        self.forign_key = kwargs.pop('forign_key', None)
        self.exclude_fields = kwargs.pop("exclude", [])

        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        data= super().to_representation(instance)
        for field_name in self.exclude_fields:
            if field_name in data:
                del data[field_name]

        return data
    
    def create(self, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        one_to_many={}
        many_to_many={}
        for field_name, relation_info in info.relations.items():
            if field_name in validated_data and not validated_data.get(field_name, None) and self.fields[field_name].allow_null:
                validated_data.pop(field_name)
            if relation_info.reverse:
                if validated_data.get(field_name, None):
                    if relation_info.to_many:
                        print(field_name)
                        many_to_many[field_name] = validated_data.pop(field_name)
                    else:
                        one_to_many[field_name]=validated_data.pop(field_name)
        instance = super().create(validated_data=validated_data)
        for field_name, value in one_to_many.items():
            serializer = self.fields[field_name]
            value[serializer.forign_key] = instance.pk
            serializer = serializer.__class__(data=value)
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValidationError(serializer.errors)  
        for field_name, value in many_to_many.items():
            try:
                serializer = self.fields[field_name].child
                for data in value:
                    data[serializer.forign_key] = instance.pk
                serializer = serializer.__class__(data=value, many=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise ValidationError(serializer.errors)
            except:
                serializer = self.fields[field_name]
                value[serializer.forign_key] = instance.pk
                serializer = serializer.__class__(data=value)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise ValidationError(serializer.errors)  

        return instance
    
    def update(self, instance, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        fields = {}
        one_to_many={}
        many_to_many={}
        for field_name, field_value in validated_data.items():
            if field_name in info.reverse_relations:
                if field_value or not self.fields[field_name].allow_null:
                    field_info = info.relations[field_name]
                    if field_info.reverse:
                        serializer = self.fields[field_name]
                        if field_info.to_many:
                            getattr(instance, field_name).all().delete()
                            try:
                                serializer = serializer.child.__class__(data=field_value, many=True)
                                if serializer.is_valid():

                                    objs = serializer.save()
                                    getattr(instance, field_name).set(objs)
                                else:
                                    raise ValidationError(serializer.errors)
                            except:
                                serializer = serializer.__class__(data=field_value, many=False)
                                if serializer.is_valid():
                                    obj = serializer.save()
                                    fields[field_name] = obj
                                else:
                                    raise ValidationError(serializer.errors)
                        else:                    
                            try:
                                serializer = serializer.__class__(getattr(instance, field_name), data=field_value)
                                if serializer.is_valid():

                                    obj = serializer.save()
                                    fields[field_name] = obj
                                else:
                                    raise ValidationError(serializer.errors)
                            except:
                                # if reverse relation is not yet constructed
                                field_value[serializer.forign_key] = instance.pk
                                serializer = serializer.__class__(data=field_value)
                                if serializer.is_valid():
                                    obj = serializer.save()
                                    fields[field_name] = obj
                                else:
                                    raise ValidationError(serializer.errors)
            else:
                fields[field_name] = field_value
        
        instance = super().update(instance, fields)
        return instance


def get_current_quarter():
    month = datetime.now().month
    if month in [1, 2, 3]:
        return "Winter"
    elif month in [4, 5, 6]:
        return "Spring"
    elif month in [7, 8, 9]:
        return "Summer"
    else:
        return "Fall"