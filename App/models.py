from django.db import models


class Pet(models.Model):
    nome = models.CharField(max_length=250, verbose_name="Nome do Pet", blank=False, null=False)
    raca = models.CharField(max_length=250, verbose_name="Raça do Pet", blank=False, null=False)
    idade = models.PositiveIntegerField(verbose_name="Idade do Pet")
    peso = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}"


# Nome, e-mail, telefone e endereço do dono.

class Dono(models.Model):
    animal_dono = models.ForeignKey(Pet, on_delete=models.CASCADE)
    nome = models.CharField(max_length=250, verbose_name="Nome do Dono")
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, verbose_name="Telefone do Dono")
    endereco = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Dono'
        verbose_name_plural = 'Donos'

    def __str__(self):
        return f"Nome {self.nome}, Pet: {self.animal_dono}"
    
