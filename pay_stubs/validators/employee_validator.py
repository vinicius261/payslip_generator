"""Esse Script contém os códigos usados nas validações do serializer de
funcionários."""

from rest_framework import serializers


def name_(self, name):
    if len(name.split()) < 2:
        raise serializers.ValidationError('Por favor, insira o nome completo.')
    
    return name

def cpf_(self, cpf):
    if len(cpf) != 11:
        raise serializers.ValidationError('Por favor, insira o CPF corretamente.')
    
    return cpf