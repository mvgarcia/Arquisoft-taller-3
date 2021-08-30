from ..models import Variable

def get_all_variables():
    variables = Variable.objects.all()
    return variables