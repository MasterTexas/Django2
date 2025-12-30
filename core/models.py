from django.db import models
from stdimage import StdImageField

class Base(models.Model):
    criado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    modelo = models.CharField('Modelo', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem_capa',
                           upload_to='produtos',
                           variations={'thumb':{'width':100,'height':100,'crop':True}},
                           delete_orphans=True
                           )
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

