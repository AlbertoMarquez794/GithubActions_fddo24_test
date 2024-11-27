Clase Calculadora
=================

La clase **Calculadora** está diseñada para realizar cálculos matemáticos básicos como suma, resta, multiplicación y división, además de métodos extendidos que agregan valores predefinidos al resultado. Esta clase es ideal para aplicaciones que requieran cálculos rápidos y eficientes.

Características
===================================================

- **Operaciones básicas**: suma, resta, multiplicación y división.
- **Manejo de excepciones**: la división por cero genera un error manejable.
- **Operaciones extendidas**: métodos para sumar y agregar valores adicionales (2, 3 y 4).

Instalación
===================================================

Para usar esta clase, copia el archivo `Calculadora.py` a tu proyecto o instálalo desde tu repositorio local:

.. code-block:: bash

   pip install calculadora

Uso Rápido
==========

Ejemplo básico:

.. code-block:: python

   from Calculadora import Calculadora

   resultado = Calculadora.sumar(5, 3)
   print(f"La suma es: {resultado}")

Referencia API
==============

A continuación, se documentan todos los métodos disponibles en la clase **Calculadora**:

.. automodule:: Calculadora
    :members:
    :undoc-members:
    :special-members: __init__
    :show-inheritance:
    :no-index:

Notas Adicionales
=================

.. note::
   La clase `Calculadora` está diseñada para ser utilizada como una colección de métodos estáticos, lo que significa que no necesitas instanciarla para usarla.

.. warning::
   Asegúrate de manejar la excepción `ValueError` al utilizar el método `dividir` para evitar errores en caso de división por cero.
