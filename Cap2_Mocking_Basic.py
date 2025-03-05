# Python Beast Series
# Mastering Mocking in Python

from unittest.mock import Mock

Mock_0 = Mock()

# Retorno inteiro
Mock_0.return_value = 77
result = Mock_0()
print (result)

#adicionando o metodo_string
Mock_0.metodo_string.return_value = "Hello World"
result = Mock_0.metodo_string()
print (result)

#Imitando objetos especificos

from datetime import datetime

Mock_1 = Mock(spec=datetime)

result1 = Mock_1.now()
result2 = Mock_1.date()

print (result1)
print (result2)

#
# Using MagicMock

from unittest.mock import MagicMock

Mock_2 = MagicMock()

Mock_2 = 10

result1 = str(Mock_2);
result2 = float(Mock_2) * 3.1416
result3 = Mock_2 * 100

print (result1)
print (result2)
print (result3)


#
# multiplos atributos pre-definidos
Mock_3 = Mock(name="John", age=30, is_admin=False)

print (Mock_3.name);
print (Mock_3.age);
print (Mock_3.is_admin);

#
# Gerenciador de contexto com __enter__ e __exit__

Mock_4 = Mock()
Mock_4.__enter__ = Mock(return_value=Mock_4)
Mock_4.__exit__ = Mock(return_value=False)

with Mock_4 as f:
    Mock_4.write ("test")
    Mock_4.__enter__.assert_called_once()
    Mock_4.write.assert_called_once_with("test")
    Mock_4.__exit__()
    Mock_4.__exit__.assert_called_once()

#
# Iteracao por mock
from unittest.mock import MagicMock

Mock_5 = MagicMock()
Mock_5.__iter__.return_value = iter(["a", "b", "c", "d", "e"])

for item in Mock_5:
    print (item)

#
# Called e count called

print (Mock_0.called)
print (Mock_0.call_count)

print (Mock_1.called)
print (Mock_1.call_count)

#print (Mock_2.called)
#print (Mock_2.call_count)

print (Mock_3.called)
print (Mock_3.call_count)

print (Mock_4.called)
print (Mock_4.call_count)

print (Mock_5.called)
print (Mock_5.call_count)