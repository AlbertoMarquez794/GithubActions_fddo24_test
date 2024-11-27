Clase GestorDeMatrices
=======================

La clase **GestorDeMatrices** está diseñada para realizar operaciones avanzadas con matrices como suma, multiplicación, transposición y cálculo del determinante. Es ideal para proyectos que involucren álgebra matricial y análisis matemático.

Características
===============

- **Operaciones básicas**: suma y multiplicación de matrices.
- **Operaciones avanzadas**: cálculo de determinantes y transposición.
- **Manejo de excepciones**: se gestionan errores como matrices de dimensiones incompatibles o no cuadradas.

Instalación
===========

Para usar esta clase, copia el archivo `GestorDeMatrices.py` a tu proyecto o instálalo desde tu repositorio local:

.. code-block:: bash

   pip install gestordematrices

Uso Rápido
==========

Ejemplo básico:

.. code-block:: python

   from GestorDeMatrices import GestorDeMatrices

   matriz1 = [[1, 2], [3, 4]]
   matriz2 = [[5, 6], [7, 8]]

   gestor = GestorDeMatrices(matriz1)

   suma = gestor.sumar(matriz2)
   print(f"La suma de matrices es: {suma}")

Referencia API
==============

A continuación, se documentan todos los métodos disponibles en la clase **GestorDeMatrices**:

.. automodule:: GestorDeMatrices
    :members:
    :undoc-members:
    :special-members: __init__
    :show-inheritance:
    :no-index:

Notas Adicionales
=================

.. note::
   La clase `GestorDeMatrices` utiliza NumPy internamente para operaciones matriciales, asegurando alta eficiencia y compatibilidad con proyectos matemáticos avanzados.

.. warning::
   Asegúrate de que las matrices tengan dimensiones compatibles antes de realizar operaciones como suma o multiplicación.
