from django.db import models


# Create your models here.
class Todo(models.Model):
    fechaCreado = models.DateTimeField()
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto

    # Para que ponga bien en plural search, antes decia todos ahora todo-es
    class Meta:
        verbose_name_plural = 'todo-es'